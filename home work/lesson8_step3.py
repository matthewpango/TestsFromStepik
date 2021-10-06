from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math 


driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'

try:
    driver.get(link)
    x = driver.find_element_by_xpath('//*[@id="num1"]').text
    y = driver.find_element_by_xpath('//*[@id="num2"]').text
    sum = str(int(x)+int(y))
    select = Select(driver.find_element_by_css_selector('#dropdown'))
    select.select_by_value(sum)
    submit = driver.find_elements_by_xpath('/html/body/div/form/button')
    submit.click()

finally:
    time.sleep(10)
    driver.close()

