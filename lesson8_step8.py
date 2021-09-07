from selenium import webdriver
import os
import time
 
driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

try:
    driver.get(link)
    first = driver.find_element_by_xpath('/html/body/div/form/div/input[1]')
    first.click()
    first.send_keys('name')
    second = driver.find_element_by_xpath('/html/body/div/form/div/input[2]')
    second.click()
    second.send_keys('lastname')
    mail = driver.find_element_by_xpath('/html/body/div/form/div/input[3]')
    mail.click()
    mail.send_keys('milo')
    attach = driver.find_element_by_xpath('//*[@id="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test_file.txt"
    file_path = os.path.join(current_dir, file_name)
    attach = driver.find_element_by_xpath('//*[@id="file"]')
    attach.send_keys(file_path)
    sumbit = driver.find_element_by_xpath('/html/body/div/form/button').click()

finally:
    time.sleep(5)
    driver.quit()
    