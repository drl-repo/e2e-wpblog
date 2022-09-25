from locators.dashboard import locators
from seleniumpagefactory.Pagefactory import PageFactory

class DashboardPage(PageFactory):
	
	URL = '/wp-admin'

	def __init__(self, driver):
		self.driver = driver
		self.locators = locators
