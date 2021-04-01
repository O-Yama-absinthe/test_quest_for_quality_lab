from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
 def __init__(self, browser, url, timeout=10):
  self.browser=browser
  self.url=url
  self.browser.implicitly_wait(timeout)
  
  
 def is_element_present(self, how, what):
  try:
   self.browser.find_element(how, what)
  except (NoSuchElementException):
   return False
  return True 
  
 
 def open(self):
  self.browser.get(self.url)
  
  
 def enter_data(self, how, what, data, timeout=10):
  self.browser.implicitly_wait(timeout)
  assert self.is_element_present(how, what)
  enter = self.browser.find_element(how, what)
  enter.send_keys(data)
 