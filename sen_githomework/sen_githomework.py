
import time
from sen_githomework.driver import Driver as dr
from sen_githomework.web_elements import Button, Dropdown, GenericText, TextField, WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



dr.driver.get("https://demoqa.com/automation-practice-form")

TextField(text="First Name").send_keys("Janssen")
TextField(text="Last Name").send_keys("Hayag")

TextField(text="userEmail").send_keys("janssen.hayag@anthesisgroup.com")

Button(text="Male").click()

TextField(text="Mobile Number").send_keys("0912345678")

TextField(text="dateOfBirthInput").click()

Dropdown(xpath=f"//select[@class='react-datepicker__month-select']").choose("January")
Dropdown(xpath=f"//select[@class='react-datepicker__year-select']").choose("2000")
day = 28
GenericText(xpath=f"//div[not(contains(@class, '--outside-month')) and normalize-space()='{day}']").click()

subject = TextField(text="subjectsInput")
subject.send_keys("English")
subject.enter()
# menu = WebDriverWait(dr.driver, 5).until(
#     EC.presence_of_element_located(('xpath', "//div[contains(@class, '-menu')]")))
# option = menu.find_element('xpath', ".//*[normalize-space()='English']")
# option.click()
subject = TextField(text="subjectsInput")
subject.send_keys("Chemistry")
subject.enter()

Button(text="Reading").check()
Button(text="Music").check()

Button(text="uploadPicture").upload(r"C:\Users\SenHayag\Downloads\sign.jpg")

TextField(text="Current Address").send_keys("Batangas City, Philippines")
state = Dropdown(text="state")
state.click()

menu = WebDriverWait(dr.driver, 5).until(
    EC.presence_of_element_located(('xpath', "//div[contains(@class, '-menu')]"))
)

option = menu.find_element('xpath', ".//div[contains(text(), 'NCR')]")
dr.driver.execute_script("arguments[0].click();", option)


Dropdown(text="city").click()
menu = WebDriverWait(dr.driver, 5).until(
    EC.presence_of_element_located(('xpath', "//div[contains(@class, '-menu')]"))
)

option = menu.find_element('xpath', ".//div[contains(text(), 'Delhi')]")
option.click()

Button(text="submit").click()


submitted = GenericText(xpath=f"//div[@class='modal-title h4']")

assert submitted.is_displayed(), "Form submission failed"
time.sleep(10)