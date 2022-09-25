from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wait:
	def __init__(self, driver, timeout=10):
		self.wait = WebDriverWait(driver, timeout)

	def until_text_shown(self, locator, textToBePresent):
		self.wait.until(EC.text_to_be_present_in_element(locator, textToBePresent))
		return self

	def until_visible(self, locator):
		self.wait.until(EC.visibility_of_element_located(locator))
		return self

	def until_invisible(self, locator):
		self.wait.until(EC.invisibility_of_element_located(locator))
		return self

	def until_presence(self, locator):
		self.wait.until(EC.presence_of_element_located(locator))
		return self

	def until_alert_presence(self):
		return self.wait.until(EC.alert_is_present())

	def until_staleness_of(self, locator):
		self.wait.until(EC.staleness_of(locator))
		return self
		