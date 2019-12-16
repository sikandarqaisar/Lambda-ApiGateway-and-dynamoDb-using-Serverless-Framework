# Serverless for lambda and ApiGateway

## [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#structure)Structure

This service has a separate directory for all the operations on dynamodb Table. For each operation exactly one file exists e.g.  `lambdFunctions/delete.py`. In each of these files there is exactly one function defined in lambdaFunctions directory.

- serverless.yml
-  .gitignore
- lambdaFunctions
	- create.py
	- get.py
	- delete.py
## [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#setup) Installation Prerequisites
- Pytnon3 
- nvm 

## [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#setup)Setup

`npm install -g serverless`

## [](https://github.com/serverless/examples/tree/master/aws-python-rest-api-with-dynamodb#deploy)Deploy

In order to deploy the code simply go to desired folder and run

```serverless deploy```

The expected result should be similar to:

![Image description](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework/blob/master/outputfile.png)

- endpoints:
  - POST - https://45wf34z5yf.execute-api.us-east-2.amazonaws.com/dev/lambdaFunction
  - GET - https://45wf34z5yf.execute-api.us-east-2.amazonaws.com/dev/lambdaFunction/{id}
  - DELETE - https://45wf34z5yf.execute-api.us-east-2.amazonaws.com/dev/lambdaFunction/{id}
- functions:
  - serverless-rest-api-with-dynamodb-dev-get
  - serverless-rest-api-with-dynamodb-dev-create
  - serverless-rest-api-with-dynamodb-dev-delete

## [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#usage)Usage

You can create, retrieve, or delete data with the following commands:

### [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#create-a-todo)Create an Entry

curl -X POST https://XXXXXXX.execute-api.us-east-2.amazonaws.com/dev/lambdaFunction --data 'Learn Serverless'

```{"text": "Learn Serverless ", "checked": false, "id": "e4b5c986-2054-11ea-992f-5ac6ea53ed15"}```


### [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#get-one-todo)Get one Entry

# Replace the <id> part with a real id from your Dynamodb table
curl https://XXXXXXX.execute-api.us-east-2.amazonaws.com/dev/lambdFunctions/<id>

Example Result:

```{"text": "Learn Serverless ", "checked": false, "id": "e4b5c986-2054-11ea-992f-5ac6ea53ed15"}```


### [](https://github.com/sikandarqaisar/Lambda-ApiGateway-and-dynamoDb-using-Serverless-Framework#delete-Entry)Delete an Entry

# Replace the <id> part with a real id from your dynamodb table
curl -X DELETE https://XXXXXXX.execute-api.us-east-2.amazonaws.com/dev/lambdFunctions/<id>

Result:
`No Output`
