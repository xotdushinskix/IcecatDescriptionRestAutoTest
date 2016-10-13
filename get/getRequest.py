import requests


def getRequest(url, productId, accessKey):
    reqURL = url + productId

    querystring = {"access_key":accessKey,"session_type":"rest"}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "5de1095e-6628-3952-45ab-6fc8155bc724"
        }

    response = requests.request("GET", reqURL, headers=headers, params=querystring)
    responseText = response.text
    status = response.status_code
    return status, responseText