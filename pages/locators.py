from selenium.webdriver.common.by import By


class MainPageLocators():
 LOGIN_FORM=(By.CSS_SELECTOR, ".email-input")
 PASS_BUTTON=(By.CSS_SELECTOR, ".button.svelte-1eyrl7y")
 PASS_FORM=(By.CSS_SELECTOR, ".password-input")
 REMEMBER_ME=(By.CSS_SELECTOR, "#saveauth")
 ENTER_BUTTON=(By.CSS_SELECTOR,".second-button")
 
class MailPageLocators():
 MAILTO=(By.CSS_SELECTOR, ".head_container--3W05z .container--H9L5q.size_s_compressed--2c-eV")
 MAIL_BUTTON=(By.CSS_SELECTOR,".compose-button__txt")
 MAIL_BUTTON_SMALLER=(By.CSS_SELECTOR,".compose-button")
 HANDLER=(By.CSS_SELECTOR,".subject__container--HWnat .container--H9L5q")
 TEXTBOX=(By.XPATH ,"/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]/div[1]")
 SUBMIT=(By.XPATH, "/html/body/div[15]/div[2]/div/div[2]/div[1]/span[1]/span/span")
