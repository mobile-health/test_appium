import imp
from pkgutil import ImpImporter
from driver_helper import global_driver_helper as driver_helper

def test_login(
    phone_number, password
):
    driver_helper.wait_for_el_by_id(el_id="tv_next")

    el = driver_helper.find_el_by_id("tv_next")
    el.click()
    el.click()
    el.click()

    btn_login_with_phone = driver_helper.wait_and_find("group_phone")
    btn_login_with_phone.click()

    edt_phone = driver_helper.wait_and_find("edt_phone_number")
    edt_phone.click()
    edt_phone.set_text(phone_number)

    btn_contiue = driver_helper.wait_and_find("btn_continue")
    btn_contiue.click()

    edt_codes = driver_helper.wait_and_find("edt_codes")
    edt_codes.click()
    edt_codes.set_text("123456")