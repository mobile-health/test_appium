import unittest
import time

from driver_helper import DriverHelper


class SampleTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver_helper = DriverHelper()

    def tearDown(self) -> None:
        self.driver_helper.quit()

    def testSample(self):
        self.driver_helper.wait_for_el_by_id(el_id="tv_next")

        el = self.driver_helper.find_el_by_id("tv_next")
        el.click()
        el.click()
        el.click()

        btn_login_with_phone = self.driver_helper.wait_and_find("group_phone")
        btn_login_with_phone.click()

        edt_phone = self.driver_helper.wait_and_find("edt_phone_number")
        edt_phone.click()
        edt_phone.set_text("31231234")

        btn_contiue = self.driver_helper.wait_and_find("btn_continue")
        btn_contiue.click()

        edt_codes = self.driver_helper.wait_and_find("edt_codes")
        edt_codes.click()
        edt_codes.set_text("123456")

        time.sleep(10.0)


unittest.main()