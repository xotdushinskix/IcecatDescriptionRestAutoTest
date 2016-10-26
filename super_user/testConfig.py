import unittest


import superUserData
from accessKeyGenerator import accesskey, getAccessKey
from delete import deleteRequest


accessKey = accesskey.AccessKeyGenerator()
accessKeyFile = getAccessKey.ReadAccessKeyFile()
deleteAction = deleteRequest.DeleteAction()

class TestConfig(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        key = accessKey.accessKey('ASfW9179vRL6U_G_EKPCBc9vBj2C2c1m', 'https://bo.icecat.biz/user/login')
        assert (key[1] == 200)




    def setUp(self):
        deleteAction.deleteRequestAction("https://bo-preprod.icecat.biz/restful/v2/descriptionblock/",
                                          superUserData.dictFullInfo.get("productId"),
                                          superUserData.dictFullInfo.get("langId"), accessKeyFile.fileReader())




    def tearDown(self):
        deleteAction.deleteRequestAction("https://bo-preprod.icecat.biz/restful/v2/descriptionblock/",
                                          superUserData.dictFullInfo.get("productId"),
                                          superUserData.dictFullInfo.get("langId"), accessKeyFile.fileReader())




    @classmethod
    def tearDownClass(cls):
        deleteAction.deleteRequestAction("https://bo-preprod.icecat.biz/restful/v2/descriptionblock/",
                                          superUserData.dictFullInfo.get("productId"),
                                          superUserData.dictFullInfo.get("langId"), accessKeyFile.fileReader())

