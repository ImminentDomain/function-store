import requests
import json


SECRETS_DIR = "/var/openfaas/secrets/"

def handle(req):
    """
    I should be updated to include description, params, and output

    """

    with open(SECRETS_DIR+"mailgun-api-key") as fptr:
        MAILGUN_API_KEY = fptr.read()

    with open(SECRETS_DIR+"mailgun-sandbox-url") as fptr:
        MAILGUN_SANDBOX_URL = fptr.read()

    with open(SECRETS_DIR+"from-email-address") as fptr:
        FROM_EMAIL_ADDRESS = fptr.read()

    json_req = json.loads(req)
    recipient = json_req["recipient"]
    subject = json_req["subject"]
    text = json_req["text"]
    print(json_req)

    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(MAILGUN_SANDBOX_URL)

    try:
        request = requests.post(request_url, auth=('api', MAILGUN_API_KEY), data={
            'from': FROM_EMAIL_ADDRESS,
            'to': recipient,
            'subject': subject,
            'text': text
        })

        print 'Status: {0}'.format(request.status_code)
        print 'Body:   {0}'.format(request.text)
    except Exception as e:
        return e.message

    return request.text



