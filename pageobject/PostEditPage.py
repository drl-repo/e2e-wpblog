from locators.post import locators
from pageobject.pagecomponent.PostFormComponent import PostFormComponent
from pageobject.BasePage import BasePage
from pageobject.PostPage import PostPage
from helper.wait import Wait

class PostEditPage(BasePage):

	def __init__(self, driver):
		self.driver = driver
		self.locators = locators
		self.PostPage = PostPage(driver)
		self.PostFormComponent = PostFormComponent(driver)

	def wait_until_page_ready(self):
		locator = self.selenium_locator(self.locators['page_heading'])
		Wait(self.driver).until_text_shown(locator,'Edit Post')

	def update_post(self, title=None, content=None, tags=[]):
		self.PostFormComponent.fill(False, title, content, tags)

	def get_post_id(self):
		#unfortunately, seleniumpagefactory package does not support hidden element
		#so we need to go back using pure selenium class
		hidden_element = self.get_element(self.locators['inp_post_id'])
		#assign to variabel, we need it later
		return hidden_element.get_attribute('value')