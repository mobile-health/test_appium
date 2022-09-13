import time

from common import BaseTestCase
from testcase.helper.register_helper import registerByPhone


class RegisterSuccessful(BaseTestCase):

    def testRegisterByPhone(self):
        registerByPhone("85552763", "123456", "Mia", "test", "email@mana.com", "referral_code")