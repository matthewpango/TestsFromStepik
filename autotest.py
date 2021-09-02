from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.google.ru/')
searchbox =  driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('papich')

