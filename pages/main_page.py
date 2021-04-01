from .base_page import BasePage
from .locators import MainPageLocators
from .inputs import MainPageInputs
from .locators import MailPageLocators
from .inputs import MailInputs
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):
 def __init__(self, *args, **kwargs):
  super(MainPage, self).__init__(*args, **kwargs)
 
 def login_user(self):
  login=(MainPageInputs.LOGIN)
  password=(MainPageInputs.PASS)
  self.enter_data(*MainPageLocators.LOGIN_FORM, login)
  button=self.browser.find_element(*MainPageLocators.PASS_BUTTON)
  button.click()
  checkbox=self.browser.find_element(*MainPageLocators.REMEMBER_ME)
  checkbox.click()
  self.enter_data(*MainPageLocators.PASS_FORM, password)
  button=self.browser.find_element(*MainPageLocators.ENTER_BUTTON)
  button.click()
