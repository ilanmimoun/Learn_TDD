from selenium import webdriver
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
        self.browser.get('http://localhost:8000')
        # Test if page title is right:
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
