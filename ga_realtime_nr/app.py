import httplib2
import requests
import json

from oauth2client.service_account import ServiceAccountCredentials

# Google Analytics View + Metrics & Dimensions to query
VIEW_ID = 000000000 # Can be obtained from here: https://ga-dev-tools.appspot.com/account-explorer/
METRICS = ['rt:activeUsers','rt:pageviews','rt:goalCompletionsAll']
DIMENSIONS = ['rt:country','rt:city']

# New Relic Insights Credentials
INSIGHTS_KEY = 'YOUR_INSIGHTS_KEY'
INSIGHTS_ACCOUNT_ID = 'YOUR_INSIGHTS_ACCOUNT_ID'

def lambda_handler(event, context):
    """
    Google Analytics to New Relic POC
    """

    with open('./credentials.json') as json_file:
        keyfile_dict = json.load(json_file)

    credentials = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict, scopes=['https://www.googleapis.com/auth/analytics.readonly'])

    # Create requests session object (avoids need to pass in headers with every request)
    session = requests.Session()
    session.headers= {'Authorization': 'Bearer ' + credentials.get_access_token().access_token}

    dimensions_url_string = ','.join(DIMENSIONS)

    events = []

    for metric in METRICS:
        url_kwargs = {
            'view_id': VIEW_ID,  
            'get_args': 'metrics={metric}&dimensions={dimensions}'.format(metric=metric, dimensions = dimensions_url_string)  # https://developers.google.com/analytics/devguides/reporting/realtime/v3/reference/data/realtime/get
        }

        response = session.get('https://www.googleapis.com/analytics/v3/data/realtime?ids=ga:{view_id}&{get_args}'.format(**url_kwargs))
        response.raise_for_status()
        result = response.json()



        columnHeaders = result.get('columnHeaders', {})

        rows = result.get('rows')

        eventDict = {'eventType':'GaEvent_{metric}'.format(metric=metric)}

        if rows:
            for row in rows:
                dimensions = []
                for i, column in enumerate(row):
                    dimensions.append(column)
                    dimensions.append(columnHeaders[i].get('name'))

                    if columnHeaders[i].get('columnType') == 'METRIC':
                        nrValue = column

                nrColumnName = '_'.join(dimensions)

                eventDict[nrColumnName] = float(nrValue)

            events.append(eventDict)   
    
    insights_headers = {'X-Insert-Key': INSIGHTS_KEY,'Content-Type': 'application/json'}
    insights_url = 'https://insights-collector.newrelic.com/v1/accounts/{account_id}/events'.format(account_id=INSIGHTS_ACCOUNT_ID)

    r = requests.post(insights_url,headers = insights_headers, data = json.dumps(events))

    return {
        "statusCode": 200,
        "body": json.dumps(events),
    }
