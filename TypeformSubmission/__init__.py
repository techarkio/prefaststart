from json import dumps
import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    a = json.loads(json.dumps(req.get_body().decode("utf-8")))
    logging.info(req.get_body().decode("utf-8"))
    logging.info(a)
    # logging.info(json.loads(req.get_body()))
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    from twilio.rest import Client

    # Your Account SID from twilio.com/console
    account_sid = "account"
    # Your Auth Token from twilio.com/console
    auth_token  = "token"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+0000", 
        from_="+0000",
        body="Hello from Python!")

    logging.info(message.sid)

    if name:
        logging.info(name)
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

    

