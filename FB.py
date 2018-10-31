from selenium import webdriver
import time
username='username'
password='password'

#  url for the Accouring sit
url='https://www.facebook.com'

driver=webdriver.Chrome('C:addres to driver /chromedriver.exe')


driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)

time.sleep(4)

driver.find_element_by_id('loginbutton').click()
