from selenium import webdriver
import math
import time

def calc(sunduk_atr):
  return str(math.log(abs(12*math.sin(int(sunduk_atr)))))

driver =  webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'

try:
    driver.get(link)
    sunduk  = driver.find_element_by_xpath('//*[@id="treasure"]')
    sunduk_atr = sunduk.get_attribute("valuex")
    valuex = sunduk
    y = calc(sunduk_atr)
    field = driver.find_element_by_xpath('//*[@id="answer"]')
    field.click()
    field.send_keys(y)
    checkbox = driver.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
    radiobut = driver.find_element_by_xpath('//*[@id="robotsRule"]').click()
    submit = driver.find_element_by_xpath('/html/body/div/form/div/div/button').click()

finally:
    time.sleep(5)
    driver.quit()