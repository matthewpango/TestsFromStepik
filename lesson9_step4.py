from selenium import webdriver
import math
import time
 
driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(link)
    btn = driver.find_element_by_xpath('/html/body/form/div/div/button').click()
    time.sleep(1)
    confirm = driver.switch_to.alert
    confirm.accept()
    x = driver.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(x)
    field  = driver.find_element_by_xpath('//*[@id="answer"]')
    field.click()
    field.send_keys(y)
    submit = driver.find_element_by_xpath('/html/body/form/div/div/button').click()

finally:
    time.sleep(5)
    driver.quit()