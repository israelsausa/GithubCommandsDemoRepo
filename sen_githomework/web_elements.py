
import time
from sen_githomework.driver import Driver as dr
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class WebElement:

    def __init__(self, xpath):
        self.xpath = xpath
        self.element = dr.driver.find_element('xpath', xpath)
        time.sleep(.5)
    
    def scroll_into_view(self):
        dr.driver.execute_script("arguments[0].scrollIntoView();", self.element)

    def click(self):
        self.scroll_into_view()
        self.element.click()
    
    def select(self):
        self.scroll_into_view()
        self.element.click()

    def send_keys(self, text):
        self.scroll_into_view()
        self.element.send_keys(text)

    def enter(self):
        self.scroll_into_view()
        self.element.send_keys(Keys.ENTER)
    
    def upload(self, file_path):
        self.scroll_into_view()
        self.element.send_keys(file_path)

    def is_selected(self):
        self.scroll_into_view()
        return self.element.is_selected()
    
    def is_displayed(self): 
        self.scroll_into_view()
        return self.element.is_displayed()
    
    def is_enabled(self):
        self.scroll_into_view()
        return self.element.is_enabled()

    def is_disabled(self):
        self.scroll_into_view()
        return not self.is_enabled()

class GenericText(WebElement):
    def __init__(self, xpath=None, text=None):
        if not xpath:
            xpath = (f"//label[normalize-space()='{text}']|"
                     f"//input[@id='{text}']|"
                     f"//div[normalize-space()='{text}']|"
                     f"//*[normalize-space()='{text}']")
        super().__init__(xpath)

class TextField(WebElement):
    def __init__(self, xpath=None, text=None):
        if not xpath:
            xpath = (f"//input[@placeholder='{text}']|"
                     f"//input[@id='{text}']|"
                     f"//div[@id='{text}']|"
                     f"//*[@placeholder='{text}']")
        super().__init__(xpath)

    

class Button(WebElement):
    def __init__(self, xpath=None, text=None):
        if not xpath:
            xpath = (f"//label[normalize-space()='{text}']|"
                     f"//input[@id='{text}']|"
                     f"//input[@type='{text}']|"
                     f"//button[@id='{text}']|"
                     f"//button[normalize-space()='{text}']")
            
        super().__init__(xpath)

    def check(self):
        self.scroll_into_view()
        if not self.element.is_selected():
            self.click()
        
class Dropdown(WebElement):
    def __init__(self, xpath=None, text=None):
        if not xpath:
            xpath = (f"//div[@id='{text}']|"
                     f"//div[@id='{text}']")
    
        super().__init__(xpath)

    def choose(self, text=None, index=None):
        if text:
            Select(self.element).select_by_visible_text(text)
        elif index:
            Select(self.element).select_by_index(index)
