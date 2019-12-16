# Serverless for lambda and ApiGateway

## [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#structure)Structure

This service has a separate directory for all the todo operations. For each operation exactly one file exists e.g.  `lambdFunctions/delete.py`. In each of these files there is exactly one function defined.

The idea behind the  `lambdFunctions`  directory is that in case you want to create a service containing multiple resources e.g. users, notes, comments you could do so in the same service. While this is certainly possible you might consider creating a separate service for each resource. It depends on the use-case and your preference.


## [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#setup)Setup

`npm install -g serverless`

## [](https://github.com/serverless/examples/tree/master/aws-python-rest-api-with-dynamodb#deploy)Deploy

In order to deploy the code simply go to desired folder and run

```serverless deploy```

The expected result should be similar to:

Serverless: Packaging service…
Serverless: Uploading CloudFormation file to S3…
Serverless: Uploading service .zip file to S3…
Serverless: Updating Stack…
Serverless: Checking Stack update progress…
Serverless: Stack update finished…

Service Information
service: serverless-rest-api-with-dynamodb
stage: dev
region: us-east-2
api keys:
  None
endpoints:
  POST - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  PUT - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  DELETE - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
functions:
  serverless-rest-api-with-dynamodb-dev-get: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-get
  serverless-rest-api-with-dynamodb-dev-create: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-create
  serverless-rest-api-with-dynamodb-dev-delete: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-dynamodb-dev-delete

## [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#usage)Usage

You can create, retrieve, or delete data with the following commands:

### [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#create-a-todo)Create a Todo

curl -X POST https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos --data 'Learn Serverless'

No output

### [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#list-all-todos)List all Todos

curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos

Example output:

[{"text":"Deploy my first service","id":"ac90feaa11e6-9ede-afdfa051af86","checked":true,"updatedAt":1479139961304},{"text":"Learn Serverless","id":"206793aa11e6-9ede-afdfa051af86","createdAt":1479139943241,"checked":false,"updatedAt":1479139943241}]%

### [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#get-one-todo)Get one Todo

# Replace the <id> part with a real id from your Dynamodb table
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id>

Example Result:

{"text":"Learn Serverless","id":"ee6490d0-aa11e6-9ede-afdfa051af86","createdAt":1479138570824,"checked":false,"updatedAt":1479138570824}%

### [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#update-a-todo)Update a Todo

# Replace the <id> part with a real id from your Dynamodb table
curl -X PUT https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id> --data '{ "text": "Learn Serverless", "checked": true }'

Example Result:

{"text":"Learn Serverless","id":"ee6490d0-aa11e6-9ede-afdfa051af86","createdAt":1479138570824,"checked":true,"updatedAt":1479138570824}%

### [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#delete-Entry)Delete Entry

# Replace the <id> part with a real id from your dynamodb table
curl -X DELETE https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id>
