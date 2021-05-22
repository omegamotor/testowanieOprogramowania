from selenium import webdriver
from django.test import TestCase
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Firefox(executable_path=r'C:\Users\Robert\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe')
#browser.get('http://localhost:8000')
#assert 'To-Do lists' in browser.title

class Test(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\Robert\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe')
        #assert 'Lista rzeczy do zrobienia' in self.browser.title

    def test_browser(self):
        self.browser.get('http://localhost:8000')
        self.header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('h1', self.header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys('Gotowanie')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Gotowanie' for row in rows))

    def tearDown(self):
        self.browser.close()