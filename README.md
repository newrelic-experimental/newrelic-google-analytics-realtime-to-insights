[![Experimental Project header](https://github.com/newrelic/opensource-website/raw/master/src/images/categories/Experimental.png)](https://opensource.newrelic.com/oss-category/#experimental)

# Google Analytics Realtime API to New Relic Insights [build badges go here when available]

>
This is a AWS Lambda serverless application that queries Google Analytics Realtime data and creates events in New Relic using the Insights insert api. It is built with the AWS Serverless Application Model (SAM). This is created as a proof of concept for sending GA realtime data to the New Relic Telemetry Data Platform (TDP).

## Installation

> 
The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modified IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

To delete the application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name newrelic-google-analytics-realtime-to-insights
```

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

## Getting Started
>
To query the google analytics real time api, currently it is required to do the following:
- Sign up for the realtime api beta linked on this page: https://developers.google.com/analytics/devguides/reporting/realtime/v3
- Create a service account on google cloud and create credentials.json for the account: https://cloud.google.com/docs/authentication/production#auth-cloud-explicit-python

Once you have the google cloud credentials, 
1. in the folder replace the contents of the `ga_realtime_nr/credentials.json` with the content of the json file you generated for your service accounts.

2. In `ga_realtime_nr/app.py` replace
- `VIEW_ID` with the view id of the google analytics account view. Can be found here: https://ga-dev-tools.appspot.com/account-explorer/
- `METRICS` with the metrics that you want to query from the realtime api. Examples can be found here: https://developers.google.com/analytics/devguides/reporting/realtime/dimsmets
- `DIMENSIONS` with the dimensions the metrics should be grouped by. Also found at the link above.
- `INSIGHTS_KEY` and `INSIGHTS_ACCOUNT_ID` with your New Relic credentials. Documentation on how to generate/obtain these: https://docs.newrelic.com/docs/insights/insights-api/get-data/query-insights-event-data-api#register

## Usage
>
This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- ga_realtime_nr - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an Schedule Expression. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

If you prefer to use an integrated development environment (IDE) to build and test your application, you can use the AWS Toolkit.  
The AWS Toolkit is an open source plug-in for popular IDEs that uses the SAM CLI to build and deploy serverless applications on AWS. The AWS Toolkit also adds a simplified step-through debugging experience for Lambda function code. See the following links to get started.

* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)


## Building

>
Build your application with the `sam build --use-container` command.

```bash
newrelic-google-analytics-realtime-to-insights$ sam build --use-container
```

The SAM CLI installs dependencies defined in `ga_realtime_nr/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
newrelic-google-analytics-realtime-to-insights$ sam local invoke GaRealtimeNrFunction --event events/event.json
```

## Testing

>
Tests are defined in the `tests` folder in this project. Use PIP to install the [pytest](https://docs.pytest.org/en/latest/) and run unit tests.

```bash
newrelic-google-analytics-realtime-to-insights$ pip install pytest pytest-mock --user
newrelic-google-analytics-realtime-to-insights$ python -m pytest tests/ -v
```

## Support

New Relic hosts and moderates an online forum where customers can interact with New Relic employees as well as other customers to get help and share best practices. Like all official New Relic open source projects, there's a related Community topic in the New Relic Explorers Hub. You can find this project's topic/threads here:

>Add the url for the support thread here

## Contributing
We encourage your contributions to improve [project name]! Keep in mind when you submit your pull request, you'll need to sign the CLA via the click-through using CLA-Assistant. You only have to sign the CLA one time per project.
If you have any questions, or to execute our corporate CLA, required if your contribution is on behalf of a company,  please drop us an email at opensource@newrelic.com.

## License
[Project Name] is licensed under the [Apache 2.0](http://apache.org/licenses/LICENSE-2.0.txt) License.
>[If applicable: The [project name] also uses source code from third-party libraries. You can find full details on which libraries are used and the terms under which they are licensed in the third-party notices document.]
