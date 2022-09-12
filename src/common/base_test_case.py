import unittest

from driver_helper import global_driver_helper


class BaseTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver_helper = global_driver_helper
        self.driver_helper.launch_app()

    def tearDown(self) -> None:
        self.driver_helper.close_app()

    
