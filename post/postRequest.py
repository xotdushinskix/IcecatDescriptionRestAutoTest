import pprint
import json

import requests


def postRequestAction(accessKey, dataDict, url):

    productId = dataDict['productId']
    langId = dataDict['langId']
    shortDescrip = dataDict['shortDescrip']
    innerDict = dataDict['fullInfo']


    urlFinish = url + productId

    querystring = {"access_key": accessKey, "langid": langId, "short_desc": shortDescrip,  "session_type": "rest"}

    payload = json.dumps(innerDict)

    headers = {
        'cache-control': "no-cache",
        'postman-token': "4d7b0758-62c0-b91e-ae0a-672edd76be5b"
        }

    response = requests.request("POST", urlFinish, data=payload, headers=headers, params=querystring)
    postStatus = response.status_code
    return postStatus, response.text




