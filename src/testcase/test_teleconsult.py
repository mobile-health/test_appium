import time

from common import BaseTestCase
from testcase.helper.test_login_helper import test_login


class TestProviderPool(BaseTestCase):

    def test_request_consult_successful(self):
        test_login("31231234", "123456")
    #Click button [Consult a doctor online]


        edt_reason = self.driver_helper.wait_and_find("edt_reason")
        edt_reason.click()
        edt_reason.set_text("Headache")

        btn_continue = self.driver_helper.wait_and_find("btn_continue")
        btn_continue.click()

    # click button request new consult of ongoing teleconsult popup.

        btn_request = self.driver_helper.wait_and_find("btn_request")
        btn_request.click()

        btn_agree = self.driver_helper.wait_and_find("btn_agree")
        btn_agree.click()

