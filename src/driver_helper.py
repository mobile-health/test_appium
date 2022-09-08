import json
from lib2to3.pgen2 import driver
import pathlib

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

path = str(pathlib.Path(__file__).parent.resolve())

desired_cap_file = path + "/../desired_cap.json"

app_package_name = "com.mhealth.manadr.test"

with open(desired_cap_file) as f:
    desired_cap = json.load(f)

desired_cap['app'] = path + "/../app-sat-debug.apk"


class DriverHelper:

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    def wait_for_el_by_id(self, timeout=10, el_id: str = ""):
        WebDriverWait(self.driver, timeout)\
            .until(EC.presence_of_element_located((By.ID, el_id)))

    def wait_for_text(self, text: str = "", timeout=10):
        search_x_path = f"//*[contains(@text, \"{text}\")]"

        WebDriverWait(self.driver, timeout)\
            .until(EC.presence_of_element_located((By.XPATH, search_x_path)))

    def find_el_by_id(self, el_id: str = ""):
        return self.driver.find_element(by=AppiumBy.ID, value=el_id)

    def has_el_by_id(self, el_id: str = ""):
        try:
            self.driver.find_element(by=AppiumBy.ID, value=el_id)
            return True
        except:
            return False

    def wait_and_find(self, el_id: str = "", timeout=10):
        self.wait_for_el_by_id(timeout=timeout, el_id=el_id)
        return self.find_el_by_id(el_id)

    def keyevent(self, keycode: int):
        self.driver.keyevent(keycode)

    def quit(self):
        self.driver.quit()

    def close_app(self):
        self.driver.close_app()

    def launch_app(self):
        self.driver.launch_app()

    def has_text(self, text: str):
        search_x_path = f"//*[contains(@text, \"{text}\")]"

        try:
            self.driver.find_element(by=AppiumBy.XPATH, value=search_x_path)
            return True
        except:
            return False

    def scroll(self, full_el_id: str, max_retries: int = 1, percent: float = 0.5, until=None):

        for i in range(max_retries):
            self.driver.execute_script('mobile: scrollGesture', {
                'elementId': full_el_id,
                'direction': 'down',
                'percent': percent
            })

            if until:
                valid = until()
                if (valid):
                    return

        if until:
            raise Exception("Scroll is not success")

    def scroll_to_end(self, full_el_id: str, percent: float = 0.5):

        max = 20

        for i in range(max):

            last_page_source = self.driver.page_source

            self.driver.execute_script('mobile: scrollGesture', {
                'elementId': full_el_id,
                'direction': 'down',
                'percent': percent
            })

            now_page_source = self.driver.page_source

            if last_page_source == now_page_source:
                break


global_driver_helper = DriverHelper()
