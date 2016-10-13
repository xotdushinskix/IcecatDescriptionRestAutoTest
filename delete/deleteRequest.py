import requests


def deleteRequestAction(url, productId, langId, accessKey):
    reqURL = url + productId

    querystring = {"langid":langId,"access_key":accessKey, "session_type": "rest"}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "97d63581-64e5-a293-eab2-c0bf20c97909"
        }

    response = requests.request("DELETE", reqURL, headers=headers, params=querystring)
    responseStatus = response.status_code
    return response.text, responseStatus