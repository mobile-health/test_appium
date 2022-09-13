from driver_helper import global_driver_helper as driver_helper

def registerByPhone(phone_number, otp_code, first_name, last_name, email, referral_code):
    driver_helper.wait_for_el_by_id (el_id = "group_phone")

    btn_register_by_phone = driver_helper.find_el_by_id (el_id = "group_phone")
    btn_register_by_phone.click()

# input Phone number screen
    driver_helper.wait_for_el_by_id (el_id = "group_phone_country_code")

# Pick Phone country code
#    el = driver_helper.find_el_by_id (el_id = "group_phone_country_code")
#   el.click()

    edt_phone = driver_helper.find_el_by_id (el_id = "edt_phone_number")
    edt_phone.click()
    edt_phone.set_text(phone_number)

    btn_continue = driver_helper.find_el_by_id ("btn_continue")
    btn_continue.click()
# OTP screen    
    edt_code = driver_helper.wait_and_find("group_codes")
    edt_code.set_text(otp_code)

# Welcome screen
    btn_create_acc = driver_helper.wait_and_find("btn_create")
    btn_create_acc.click()
# Create New Acc screen
    edt_first_name = driver_helper.wait_and_find ("edt_first_name")
    edt_first_name.set_text (first_name)

    edt_last_name = driver_helper.wait_and_find ("edt_last_name")
    edt_last_name.set_text (last_name)

    edt_email = driver_helper.wait_and_find ("edt_email")
    edt_email.set_text (email)

    txt_phone_number = driver_helper.wait_and_find("tv_phone_number")
    if txt_phone_number == phone_number:
        print("-------get Phone OK")
    else :
        print ("Show phone number incorrectly")
    
    edt_ref_code = driver_helper.wait_and_find ("edt_ref_code")
    edt_ref_code.set_text (referral_code)

    btn_continue = driver_helper.wait_and_find ("btnContinue")
    btn_continue.click()

    