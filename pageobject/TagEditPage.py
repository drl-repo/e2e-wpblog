from locators.tag import locators
from pageobject.BasePage import BasePage
from pageobject.pagecomponent.TagFormComponent import TagFormComponent
from helper.wait import Wait

class TagEditPage(BasePage):
	
	def __init__(self, driver):
		self.driver = driver
		self.locators = locators

	def wait_until_page_ready(self):
		locator = self.selenium_locator(self.locators['page_heading'])
		Wait(self.driver).until_text_shown(locator,'Edit Tag')

	def edit_tag(self, tag_name=None, tag_slug=None, tag_desc=None):
		tag_form = TagFormComponent(self.driver)
		tag_form.fill(False, tag_name, tag_slug, tag_desc)

	def get_tag_id(self):
		tag_element = self.get_element(self.locators['inp_tag_id'])
		return tag_element.get_attribute('value')


