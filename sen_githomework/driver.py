import time
from selenium import webdriver
class Driver:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    

