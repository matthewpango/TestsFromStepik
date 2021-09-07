from selenium import webdriver
import time
import math

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'

try:
    driver.get(link)
    driver.find_element_by_xpath('//*[@id="input_value"]')
    

    button = browser.find_element_by_tag_name("button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



finally:
    time.sleep(10)
    driver.quit()