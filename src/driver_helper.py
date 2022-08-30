import pathlib
import json
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

path = str(pathlib.Path(__file__).parent.resolve())

desired_cap_file = path + "/../desired_cap.json"

with open(desired_cap_file) as f:
    desired_cap = json.load(f)


class DriverHelper:

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    def wait_for_el_by_id(self, timeout=10, el_id: str = ""):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, el_id)))

    def find_el_by_id(self, el_id: str = ""):
        return self.driver.find_element(by=AppiumBy.ID, value='tv_next')

    def quit(self):
        self.driver.quit()
