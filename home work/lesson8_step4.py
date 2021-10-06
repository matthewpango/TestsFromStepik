from selenium import webdriver
driver = webdriver.Chrome()
driver.execute_script("document.title='Script executing';alert('Robots at work');")
