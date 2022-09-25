import random
from locators.category import locators
from pageobject.BasePage import BasePage
from pageobject.pagecomponent.CategoryFormComponent import CategoryFormComponent
from helper.wait import Wait

class CategoryEditPage(BasePage):
	
	def __init__(self, driver):
		self.driver = driver
		self.locators = locators

	def wait_until_page_ready(self):
		locator = self.selenium_locator(self.locators['page_heading'])
		Wait(self.driver).until_text_shown(locator,'Edit Category')
	
	#the value of default parent in dropdown is string 'None'
	def edit_category(self, name=None, slug=None, parent='None',desc=None):
		category_form = CategoryFormComponent(self.driver)
		category_form.fill(False, name, slug, parent, desc)

	def get_category_id(self):
		category_element = self.get_element(self.locators['inp_cat_id'])
		return category_element.get_attribute('value')