from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from get_chrome_driver import GetChromeDriver

# Automatically get the compatible ChromeDriver
get_driver = GetChromeDriver()
path = get_driver.install()

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add._argument("--headless")

service = Service(executable_path=path + "/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://test3.anthesis.network/users/accounts/login/?next=/")
time.sleep(10)

driver.close()
driver.quit()