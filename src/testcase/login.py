import time

from common import BaseTestCase
from testcase.helper.login_helper import loginByPhone


class LoginSuccessful(BaseTestCase):

    def testSample_3(self):
        login("31231234", "123456")

        # raise Exception("Xiu is good")
        self.fail("Xiu fail")