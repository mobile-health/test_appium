import time

from common import BaseTestCase


class SampleTestCase(BaseTestCase):

    def abcSample_2(self):
        self.driver_helper.wait_for_el_by_id(el_id="tv_next")

        # raise Exception("Xiu is good")
        self.fail("Xiu fail")

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

        rv_main = self.driver_helper.wait_and_find("rv_main", timeout=20)

        self.driver_helper.wait_for_text("Clinic Visit")

        # self.driver_helper.scroll(
        #     rv_main.id, 5, lambda: self.driver_helper.has_text("Top Stories"))
        self.driver_helper.scroll_to_end(rv_main.id)

        time.sleep(2.0)
