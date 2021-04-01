from .base_page import BasePage
from .locators import MailPageLocators
from .inputs import MailInputs
from selenium.webdriver.support.ui import WebDriverWait

 
class MailPage(BasePage): 
 def send_message(self):
  self.browser.implicitly_wait(10)
  try:
   button=self.browser.find_element(*MailPageLocators.MAIL_BUTTON)
   button=self.browser.find_element(*MailPageLocators.MAIL_BUTTON)
  except:
   button=self.browser.find_element(*MailPageLocators.MAIL_BUTTON_SMALLER)
   button=self.browser.find_element(*MailPageLocators.MAIL_BUTTON_SMALLER)
  button.click()
  mailto=(MailInputs.MAILTO)
  handler=(MailInputs.HANDLER)
  text=(MailInputs.TEXT)
  self.enter_data(*MailPageLocators.MAILTO, mailto)
  self.enter_data(*MailPageLocators.HANDLER, handler)
  self.enter_data(*MailPageLocators.TEXTBOX, text)
  button=self.browser.find_element(*MailPageLocators.SUBMIT)
  button.click()
  