from testcase import *
import unittest
from html_reporter import HTMLTestRunner
from driver_helper import global_driver_helper

if __name__ == "__main__":
    runner = HTMLTestRunner(
        report_filepath="sample_report.html",
        title="My unit test",
        description="This demonstrates the report output by HTMLTestRunner.",
        open_in_browser=False
    )

    unittest.main(testRunner=runner, exit=False)

    global_driver_helper.quit()

    print("ToanTK end of life")
