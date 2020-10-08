import os
SECRETS_DIR = "/var/openfaas/secrets/"

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    dir_contents = os.listdir(SECRETS_DIR)
    print(dir_contents)
    with open(SECRETS_DIR+"my-new-secret") as fptr:
        print(fptr.read())
    return dir_contents
