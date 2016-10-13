import unittest
from accessKeyGenerator import getAccessKey
import superUserData
from delete import deleteRequest
from accessKeyGenerator import accesskey


class TestConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        key = accesskey.accessKey('', 'https://bo.icecat.biz/user/login')
        assert (key[1] == 200)




    def setUp(self):
        deleteRequest.deleteRequestAction("https://bo-preprod.icecat.biz/restful/v2/descriptionblock/",
                                          superUserData.dictFullInfo.get("productId"),
                                          superUserData.dictFullInfo.get("langId"), getAccessKey.fileReader())




    def tearDown(self):
        deleteRequest.deleteRequestAction("https://bo-preprod.icecat.biz/restful/v2/descriptionblock/",
                                          superUserData.dictFullInfo.get("productId"),
                                          superUserData.dictFullInfo.get("langId"), getAccessKey.fileReader())




    @classmethod
    def tearDownClass(cls):
        deleteRequest.deleteRequestAction("https://bo-preprod.icecat.biz/restful/v2/descriptionblock/",
                                          superUserData.dictFullInfo.get("productId"),
                                          superUserData.dictFullInfo.get("langId"), getAccessKey.fileReader())

