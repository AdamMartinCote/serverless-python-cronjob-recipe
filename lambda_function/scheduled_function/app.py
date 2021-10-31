import requests


def lambda_handler(event, context):
    del event, context

    # Fetch a random fact about cats from a public api and print it to
    # the function logs using stdout
    response = requests.get("https://catfact.ninja/fact")
    print(response.json().get("fact"))

    return
