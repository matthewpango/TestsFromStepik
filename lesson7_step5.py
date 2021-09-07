from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver =  webdriver.Chrome()
link = 'http://suninjuly.github.io/math.html'
try:
    driver.get(link)
    x_element = driver.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    
    field = driver.find_element_by_xpath('//*[@id="answer"]')
    field.click()
    field.send_keys(y)
    checkbox = driver.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
    radiobut = driver.find_element_by_xpath('//*[@id="robotsRule"]').click()
    sumbit = driver.find_element_by_xpath('/html/body/div/form/button').click()
    
finally:
    time.sleep(10)
    driver.quit()
