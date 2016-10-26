import ast
import unittest

import superUserData
from accessKeyGenerator import getAccessKey
from delete import deleteRequest
from get import getRequest
from post import postRequest
from testConfig import TestConfig
from patch import patchRequest
from put import putRequest


accessKeyFile = getAccessKey.ReadAccessKeyFile()
deleteAction = deleteRequest.DeleteAction()
getAction = getRequest.GetAction()
postAction = postRequest.PostAction()
patchAction = patchRequest.PatchAction()
putAction = putRequest.PutAction()

class SuperUserTest(TestConfig):



    def test_Post(self):
        request = postAction.postRequestAction(accessKeyFile.fileReader(), superUserData.dictFullInfo,
                                                "https://bo.icecat.biz/restful/v2/descriptionblock/")

        bodyDict = ast.literal_eval(request[1])

        self.assertEqual(request[0], 201)
        self.assertEqual(bodyDict["message"], "Created")
        self.assertEqual(bodyDict["product_id"], int(superUserData.dictFullInfo.get("productId")))
        self.assertEqual(bodyDict["langid"], int(superUserData.dictFullInfo.get("langId")))
        self.assertNotEqual(len(str(bodyDict["product_description_id"])), 0)





    def test_Get(self):
        postAction.postRequestAction(accessKeyFile.fileReader(), superUserData.dictFullInfo,
                                      "https://bo.icecat.biz/restful/v2/descriptionblock/")

        getBody = getAction.getRequest("https://bo.icecat.biz/restful/v2/descriptionblock/",
                                        superUserData.dictFullInfo.get("productId"), accessKeyFile.fileReader())

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
        postAction.postRequestAction(accessKeyFile.fileReader(), superUserData.dictFullInfo,
                                      "https://bo.icecat.biz/restful/v2/descriptionblock/")

        deleteBody = deleteAction.deleteRequestAction("https://bo-preprod.icecat.biz/restful/v2/descriptionblock/",
                                                       superUserData.dictFullInfo.get("productId"),
                                                       superUserData.dictFullInfo.get("langId"),
                                                      accessKeyFile.fileReader())

        deleteBodyDict = ast.literal_eval(deleteBody[0])
        self.assertEqual(deleteBodyDict["message"], "Deleted")
        self.assertEqual(deleteBodyDict["product_id"], int(superUserData.dictFullInfo.get("productId")))
        self.assertEqual(deleteBodyDict["langid"], int(superUserData.dictFullInfo.get("langId")))






    def test_Patch(self):
        postAction.postRequestAction(accessKeyFile.fileReader(), superUserData.dictFullInfo,
                                      "https://bo.icecat.biz/restful/v2/descriptionblock/")

        patchBody = patchAction.patchRequest("https://bo.icecat.biz/restful/v2/descriptionblock/",
                                             superUserData.dictFullInfoPatch, accessKeyFile.fileReader())

        patchBodyDict = ast.literal_eval(patchBody[0])

        self.assertEqual(patchBody[1], 200)
        self.assertEqual(patchBodyDict.get("message"), "Updated")
        self.assertEqual(patchBodyDict.get("product_id"), int(superUserData.dictFullInfoPatch.get("productId")))
        self.assertEqual(patchBodyDict.get("langid"), int(superUserData.dictFullInfoPatch.get("langId")))


        getBody = getAction.getRequest("https://bo.icecat.biz/restful/v2/descriptionblock/",
                                       superUserData.dictFullInfoPatch.get("productId"), accessKeyFile.fileReader())

        getBodyDict = ast.literal_eval(getBody[1])
        self.assertEqual(getBodyDict["data"][0]["langid"], superUserData.dictFullInfoPatch.get("langId"))
        self.assertEqual(getBodyDict["data"][0]["short_desc"], superUserData.dictFullInfoPatch.get("shortDescrip"))
        self.assertEqual(getBodyDict["data"][0]["long_desc"], superUserData.dictFullInfoPatch.get("fullInfo")["long_desc"])
        self.assertEqual(getBodyDict["data"][0]["official_url"], superUserData.dictFullInfoPatch.get("fullInfo")["official_url"])
        self.assertEqual(getBodyDict["data"][0]["warranty_info"], superUserData.dictFullInfoPatch.get("fullInfo")["warranty_info"])
        self.assertEqual(getBodyDict["data"][0]["seo_title"], superUserData.dictFullInfoPatch.get("fullInfo")["seo_title"])
        self.assertEqual(getBodyDict["data"][0]["seo_description"], superUserData.dictFullInfoPatch.get("fullInfo")["seo_description"])
        self.assertEqual(getBodyDict["data"][0]["seo_keywords"], superUserData.dictFullInfoPatch.get("fullInfo")["seo_keywords"])
        self.assertEqual(getBodyDict["data"][0]["disclaimer"], superUserData.dictFullInfoPatch.get("fullInfo")["disclaimer"])
        self.assertEqual(getBodyDict["data"][0]["middle_desc"], superUserData.dictFullInfoPatch.get("fullInfo")["middle_desc"])






    def test_Put_Like_Post(self):
        putRequest = putAction.putRequest("https://bo.icecat.biz/restful/v2/descriptionblock/", superUserData.dictFullInfoPutPost,
                                          accessKeyFile.fileReader())

        putBodyDict = ast.literal_eval(putRequest[0])

        self.assertEqual(putRequest[1], 200)
        self.assertEqual(putBodyDict['message'], 'Upserted')
        self.assertEqual(putBodyDict['product_id'], int(superUserData.dictFullInfoPutPost.get('productId')))
        self.assertEqual(putBodyDict['langid'], int(superUserData.dictFullInfoPutPost.get("langId")))
        self.assertIsNot(len(str(putBodyDict["product_description_id"])), 0)



        getBody = getAction.getRequest("https://bo.icecat.biz/restful/v2/descriptionblock/",
                                       superUserData.dictFullInfoPutPost.get("productId"), accessKeyFile.fileReader())

        getBodyDict = ast.literal_eval(getBody[1])
        self.assertEqual(getBodyDict["data"][0]["langid"], superUserData.dictFullInfoPutPost.get("langId"))
        self.assertEqual(getBodyDict["data"][0]["short_desc"], superUserData.dictFullInfoPutPost.get("shortDescrip"))
        self.assertEqual(getBodyDict["data"][0]["long_desc"], superUserData.dictFullInfoPutPost.get("fullInfo")["long_desc"])
        self.assertEqual(getBodyDict["data"][0]["official_url"],
                         superUserData.dictFullInfoPutPost.get("fullInfo")["official_url"])
        self.assertEqual(getBodyDict["data"][0]["warranty_info"],
                         superUserData.dictFullInfoPutPost.get("fullInfo")["warranty_info"])
        self.assertEqual(getBodyDict["data"][0]["seo_title"], superUserData.dictFullInfoPutPost.get("fullInfo")["seo_title"])
        self.assertEqual(getBodyDict["data"][0]["seo_description"],
                         superUserData.dictFullInfoPutPost.get("fullInfo")["seo_description"])
        self.assertEqual(getBodyDict["data"][0]["seo_keywords"],
                         superUserData.dictFullInfoPutPost.get("fullInfo")["seo_keywords"])
        self.assertEqual(getBodyDict["data"][0]["disclaimer"],
                         superUserData.dictFullInfoPutPost.get("fullInfo")["disclaimer"])
        self.assertEqual(getBodyDict["data"][0]["middle_desc"],
                         superUserData.dictFullInfoPutPost.get("fullInfo")["middle_desc"])





    def test_Put_Like_Patch(self):
        postAction.postRequestAction(accessKeyFile.fileReader(), superUserData.dictFullInfo,
                                     "https://bo.icecat.biz/restful/v2/descriptionblock/")

        putRequest = putAction.putRequest("https://bo.icecat.biz/restful/v2/descriptionblock/",
                                           superUserData.dictFullInfoPutPatch,
                                           accessKeyFile.fileReader())

        putBodyDict = ast.literal_eval(putRequest[0])
        self.assertEqual(putRequest[1], 200)
        self.assertEqual(putBodyDict['message'], 'Upserted')
        self.assertEqual(putBodyDict['product_id'], int(superUserData.dictFullInfoPutPatch.get('productId')))
        self.assertEqual(putBodyDict['langid'], int(superUserData.dictFullInfoPutPatch.get("langId")))
        self.assertIsNot(len(str(putBodyDict["product_description_id"])), 0)



        getBody = getAction.getRequest("https://bo.icecat.biz/restful/v2/descriptionblock/",
                                       superUserData.dictFullInfoPutPatch.get("productId"), accessKeyFile.fileReader())

        getBodyDict = ast.literal_eval(getBody[1])
        self.assertEqual(getBodyDict["data"][0]["langid"], superUserData.dictFullInfoPutPatch.get("langId"))
        self.assertEqual(getBodyDict["data"][0]["short_desc"], superUserData.dictFullInfoPutPatch.get("shortDescrip"))
        self.assertEqual(getBodyDict["data"][0]["long_desc"],
                         superUserData.dictFullInfoPutPatch.get("fullInfo")["long_desc"])
        self.assertEqual(getBodyDict["data"][0]["official_url"],
                         superUserData.dictFullInfoPutPatch.get("fullInfo")["official_url"])
        self.assertEqual(getBodyDict["data"][0]["warranty_info"],
                         superUserData.dictFullInfoPutPatch.get("fullInfo")["warranty_info"])
        self.assertEqual(getBodyDict["data"][0]["seo_title"],
                         superUserData.dictFullInfoPutPatch.get("fullInfo")["seo_title"])
        self.assertEqual(getBodyDict["data"][0]["seo_description"],
                         superUserData.dictFullInfoPutPatch.get("fullInfo")["seo_description"])
        self.assertEqual(getBodyDict["data"][0]["seo_keywords"],
                         superUserData.dictFullInfoPutPatch.get("fullInfo")["seo_keywords"])
        self.assertEqual(getBodyDict["data"][0]["disclaimer"],
                         superUserData.dictFullInfoPutPatch.get("fullInfo")["disclaimer"])
        self.assertEqual(getBodyDict["data"][0]["middle_desc"],
                         superUserData.dictFullInfoPutPatch.get("fullInfo")["middle_desc"])




if __name__ == '__main__':
    unittest.main()
