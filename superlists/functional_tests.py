from selenium import webdriver
from selenium.common.exceptions import WebDriverException

import unittest


class NewVisitiorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # The software works, as quit the firefox:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Test if the home page works on Firefox:
        try:
            self.browser.get('http://localhost:8000')
        except WebDriverException:
            error_message = "\n"
            error_message += "Be sure the server is running.\n"
            error_message += "In an other terminal:\n"
            error_message += "python manage.py runserver\n"
            self.fail(error_message)

        # Test if page title is right:
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
