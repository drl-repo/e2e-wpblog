from locators.login import locators
from pageobject.BasePage import BasePage

class LoginPage(BasePage):
	
	URL = '/wp-login.php'
	
	def __init__(self, driver):
		self.driver = driver
		self.locators = locators

	def do_login(self, username=None, password=None):
		inp_username = self.inp_username
		inp_password = self.inp_password
		
		if username is not None:
			inp_username.clear()
			inp_username.send_keys(username)

		if password is not None:
			inp_password.clear()
			inp_password.send_keys(password)

		self.btn_login.click()
