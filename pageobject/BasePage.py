from seleniumpagefactory.Pagefactory import PageFactory
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(PageFactory):
	
	BASE_URL = 'http://localhost/wordpress'

	def visit(self):
		self.driver.get(self.BASE_URL+self.URL)

	def get_element(self, locator):
		selenium_locator = self.selenium_locator(locator)
		return self.driver.find_element(* selenium_locator)
	
	def get_elements(self, locator):
		selenium_locator = self.selenium_locator(locator)
		return self.driver.find_elements(* selenium_locator)
	
	def scroll_to_element(self, locator):
		actions = ActionChains(self.driver)
		selenium_locator = self.selenium_locator(locator)
		element = self.driver.find_element(* selenium_locator)
		actions.scroll_to_element(element)
		actions.perform()

	def is_element_exist(self, locator):
		try:
			self.get_element(locator)
		except NoSuchElementException:
			return False
		return True

	def selenium_locator(self, locator):
		#TYPE_OF_LOCATORS
		if locator[0].lower() in PageFactory.TYPE_OF_LOCATORS:
			return (PageFactory.TYPE_OF_LOCATORS[locator[0].lower()], locator[1])
		raise Exception("Invalid locator strategis")

	def is_element_removed(self, locator, timeout=5):
		try:
			wait = WebDriverWait(self.driver, timeout)
			locator = self.selenium_locator(locator)
			wait.until(EC.invisibility_of_element_located(locator))
			return True
		except TimeoutException:
			return False