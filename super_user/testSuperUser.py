import unittest
from accessKeyGenerator import getAccessKey
import superUserData
import ast
from delete import deleteRequest
from get import getRequest
from post import postRequest
from testConfig import TestConfig



class SuperUserTest(TestConfig):


    def test_Post(self):
        request = postRequest.postRequestAction(getAccessKey.fileReader(), superUserData.dictFullInfo,
                                                "https://bo.icecat.biz/restful/v2/descriptionblock/")
        bodyDict = ast.literal_eval(request[1])

        self.assertEqual(request[0], 201)
        self.assertEqual(bodyDict["message"], "Created")
        self.assertEqual(bodyDict["product_id"], int(superUserData.dictFullInfo.get("productId")))
        self.assertEqual(bodyDict["langid"], int(superUserData.dictFullInfo.get("langId")))
        self.assertNotEqual(len(str(bodyDict["product_description_id"])), 0)

        deleteRequest.deleteRequestAction("https://bo-preprod.icecat.biz/restful/v2/descriptionblock/",
                                          superUserData.dictFullInfo.get("productId"),
                                          superUserData.dictFullInfo.get("langId"), getAccessKey.fileReader())




    def test_Get(self):
        postRequest.postRequestAction(getAccessKey.fileReader(), superUserData.dictFullInfo,
                                      "https://bo.icecat.biz/restful/v2/descriptionblock/")
        getBody = getRequest.getRequest("https://bo.icecat.biz/restful/v2/descriptionblock/",
                                        superUserData.dictFullInfo.get("productId"), getAccessKey.fileReader())

        getBodyDict = ast.literal_eval(getBody[1])
        self.assertEqual(getBody[0], 200)
        self.assertEqual(getBodyDict["data"][0]["langid"], superUserData.dictFullInfo.get("langId"))
        self.assertEqual(getBodyDict["data"][0]["short_desc"], superUserData.dictFullInfo.get("shortDescrip"))
        self.assertEqual(getBodyDict["data"][0]["long_desc"], superUserData.dictFullInfo.get("fullInfo")["long_desc"])
        self.assertEqual(getBodyDict["data"][0]["official_url"], superUserData.dictFullInfo.get("fullInfo")["official_url"])
        self.assertEqual(getBodyDict["data"][0]["warranty_info"], superUserData.dictFullInfo.get("fullInfo")["warranty_info"])
        self.assertEqual(getBodyDict["data"][0]["seo_title"], superUserData.dictFullInfo.get("fullInfo")["seo_title"])
        self.assertEqual(getBodyDict["data"][0]["seo_description"], superUserData.dictFullInfo.get("fullInfo")["seo_description"])
        self.assertEqual(getBodyDict["data"][0]["seo_keywords"], superUserData.dictFullInfo.get("fullInfo")["seo_keywords"])
        self.assertEqual(getBodyDict["data"][0]["disclaimer"], superUserData.dictFullInfo.get("fullInfo")["disclaimer"])
        self.assertEqual(getBodyDict["data"][0]["middle_desc"], superUserData.dictFullInfo.get("fullInfo")["middle_desc"])




    def test_Delete(self):
        postRequest.postRequestAction(getAccessKey.fileReader(), superUserData.dictFullInfo,
                                      "https://bo.icecat.biz/restful/v2/descriptionblock/")

        deleteBody = deleteRequest.deleteRequestAction("https://bo-preprod.icecat.biz/restful/v2/descriptionblock/",
                                          superUserData.dictFullInfo.get("productId"),
                                          superUserData.dictFullInfo.get("langId"), getAccessKey.fileReader())

        deleteBodyDict = ast.literal_eval(deleteBody[0])
        self.assertEqual(deleteBodyDict["message"], "Deleted")
        self.assertEqual(deleteBodyDict["product_id"], int(superUserData.dictFullInfo.get("productId")))
        self.assertEqual(deleteBodyDict["langid"], int(superUserData.dictFullInfo.get("langId")))



if __name__ == '__main__':
    unittest.main()
