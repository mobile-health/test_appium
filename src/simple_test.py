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

driver_helper.quit()
