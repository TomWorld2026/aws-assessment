import boto3
import os
import json

ecs = boto3.client("ecs")

def lambda_handler(event, context):

    region = os.environ["AWS_REGION"]
    
    ecs.run_task(
        cluster=os.environ["CLUSTER"],
        taskDefinition=os.environ["TASK"],
        launchType="FARGATE",

        networkConfiguration={
            "awsvpcConfiguration": {
                "subnets": [os.environ["SUBNET"]],
                "securityGroups": [os.environ["SECURITY_GROUP"]],
                "assignPublicIp": "ENABLED"
            }
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"region": region})
    }