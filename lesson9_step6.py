from typing import final
from selenium import webdriver
import time
import math
 
driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(link)
    btn = driver.find_element_by_xpath('/html/body/form/div/div/button')
    btn.click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    x = driver.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(x)
    field = driver.find_element_by_xpath('//*[@id="answer"]')
    field.click()
    field.send_keys(y)
    submit = driver.find_element_by_xpath('/html/body/form/div/div/button')
    submit.click()

finally:
    time.sleep(5)
    driver.quit()

