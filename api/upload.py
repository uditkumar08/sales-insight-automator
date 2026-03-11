import pandas as pd
import json

def handler(request):

    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Method not allowed"
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "API working"})
    }