import time

from driver_helper import DriverHelper

driver_helper = DriverHelper()

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
edt_codes.set_text("123456")

time.sleep(10.0)
driver_helper.quit()
