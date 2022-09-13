from testcase.helper.login_helper import loginByPhone
from testcase.helper.book_appt_helper import book_an_appt
from common.base_test_case import BaseTestCase


class BookApptSuccessful (BaseTestCase):
    def testBookAppt (self):
        loginByPhone("312128080", "123456")
        book_an_appt(self)