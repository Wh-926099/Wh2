
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys('大道至简')