from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
link  = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    driver.get(link)
    cena = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )
    btn = driver.find_element_by_xpath('//*[@id="book"]')
    btn.click()
    x = driver.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(x)
    field = driver.find_element_by_xpath('//*[@id="answer"]')
    field.click()
    field.send_keys(y)
    submit = driver.find_element_by_xpath('//*[@id="solve"]')
    submit.click()


finally:
    time.sleep(5)
    driver.quit()