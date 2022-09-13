from driver_helper import global_driver_helper as  driver_helper

def book_an_appt(self):
    el = driver_helper.find_el_by_xpath(el_xpath = "(//RecyclerView[@id = 'iv_icon'])[2]")
    el.click

    driver_helper.wait_for_el_by_id(el_id = 'btn_new_clinic_visit')
    #driver_helper.find_by_text("Teleconsult").find_parent_clickable().click()
    ss
    el = driver_helper.find_el_by_id(el_id = 'btn_new_clinic_visit')
    el.click
    