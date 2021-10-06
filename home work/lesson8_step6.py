from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'

try:
    driver.get(link)
    x = driver.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(x)
    answer = driver.find_element_by_xpath('//*[@id="answer"]')
    answer.click()
    answer.send_keys(y)
    button = driver.find_element_by_xpath('/html/body/div/form/button')
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = driver.find_element_by_xpath('//*[@id="robotCheckbox"]')
    checkbox.click()
    radiobutton = driver.find_element_by_xpath('//*[@id="robotsRule"]')
    radiobutton.click()
    button.click()

finally:
    time.sleep(10)
    driver.quit()