from typing import Text
import unittest
from selenium import webdriver
import time

class test_registration(unittest.TestCase):
    def test_registr1(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')
        first = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        first.click()
        first.send_keys('matthew')
        second = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        second.click()
        second.send_keys('chern')
        email = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        email.click()
        email.send_keys('email')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual((welcome_text), "Congratulations! You have successfully registered!")
    def test_registr2(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration2.html')
        first = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        first.click()
        first.send_keys('matthew')
        second = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        second.click()
        second.send_keys('chern')
        email = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        email.click()
        email.send_keys('email')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual((welcome_text), "Congratulations! You have successfully registered!")
if __name__ == "__main__":
    unittest.main()    
