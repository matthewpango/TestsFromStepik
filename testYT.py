
from selenium import webdriver

driver = webdriver.Chrome()

driver.get ("https://www.youtube.com/")
searchBox = driver.find_element_by_xpath('//*[@id="search"]')
searchBox.send_keys ('qa')
searchButon  = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
import time
time.sleep(5)
mainPage = driver.find_element_by_xpath('//*[@id="logo-icon"]').click()
import time
time.sleep(5)
driver.quit()