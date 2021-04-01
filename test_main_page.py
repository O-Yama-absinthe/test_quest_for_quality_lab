from .pages.main_page import MainPage
from .pages.mail_page import MailPage

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
 link = "https://mail.ru/"
 page=MainPage(browser,link)
 page.open()
 #page.go_to_login_page()
 #page=LoginPage(browser)
 #browser.switch_to.frame(browser.find_elements_by_tag_name("iframe")[3])
 page.login_user()
 link = "https://e.mail.ru/inbox/?back=1"
 page=MailPage(browser,link)
# page.open()
 page.send_message()