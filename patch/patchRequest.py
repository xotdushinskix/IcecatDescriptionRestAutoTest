import json

import requests


class PatchAction():

    def patchRequest(self, url, dataDict, accessKey):

        productId = dataDict['productId']
        langId = dataDict['langId']
        shortDescrip = dataDict['shortDescrip']
        innerDict = dataDict['fullInfo']


        requiredURL = url + productId


        querystring = {"access_key":accessKey,"langid":langId,"short_desc":shortDescrip, "session_type":"rest"}

        payload = json.dumps(innerDict)

        headers = {
            'cache-control': "no-cache",
            'postman-token': "430f65c9-f2b8-815d-c025-387754d7a5c2"
            }


        response = requests.request("PATCH", requiredURL, data=payload, headers=headers, params=querystring)

        return response.text, response.status_code
