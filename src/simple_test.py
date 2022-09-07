import time

from driver_helper import DriverHelper

driver_helper = DriverHelper()


# class SimpleTest(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.driver = webdriver.Remote(
#             "http://localhost:4723/wd/hub", desired_cap)

#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.driver.quit()

#     def getResult(self)    :
#         el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='tv_next')
#         el.click()


# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)
#     unittest.TextTestRunner(verbosity=2).run(suite)

driver_helper.wait_for_el_by_id(el_id="tv_next")

el = driver_helper.find_el_by_id("tv_next")
el.click()
el.click()
el.click()

btn_login_with_phone = driver_helper.wait_and_find("group_phone")
btn_login_with_phone.click()

edt_phone = driver_helper.wait_and_find("edt_phone_number")
edt_phone.click()
edt_phone.set_text("31231234")

btn_contiue = driver_helper.wait_and_find("btn_continue")
btn_contiue.click()

edt_codes = driver_helper.wait_and_find("edt_codes")
edt_codes.click()
driver_helper.keyevent(8)
driver_helper.keyevent(9)
driver_helper.keyevent(10)
driver_helper.keyevent(11)
driver_helper.keyevent(12)
driver_helper.keyevent(13)

time.sleep(10.0)
driver_helper.quit()
