import requests

class AccessKeyGenerator():

    def accessKey(self, applicationKey, url):
        payload = '{"application_key":"'+applicationKey+'"}'
        headers = {
            'cache-control': "no-cache",
            'postman-token': "c3000588-eff0-2b23-be71-52dd123711e4"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        helpRequiredKey = response.text
        accessKeyStatus = response.status_code
        a = str(helpRequiredKey)
        requiredKey = a[15:-2]
        with open("accesskey.txt", "w") as myfile:
            myfile.write(requiredKey)
        myfile.close()
        return requiredKey, accessKeyStatus