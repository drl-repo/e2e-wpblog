import random
from selenium.webdriver.common.alert import Alert
from locators.category import locators
from pageobject.BasePage import BasePage
from pageobject.pagecomponent.CategoryFormComponent import CategoryFormComponent
from pageobject.pagecomponent.ActionsLinkComponent import ActionsLinkComponent
from helper.wait import *

class CategoryPage(BasePage):
	
	URL = '/wp-admin/edit-tags.php?taxonomy=category'
	is_there_category_deleted = False
	category_deleted = None

	def __init__(self, driver):
		self.driver = driver
		self.locators = locators
		self.action_link = ActionsLinkComponent(driver)

	def move_categories_to_trash(self):
		category_list = self.get_elements(self.locators['tbl_list_category'])
		if 	len(category_list) > 1:
			self.check_all_categories()
			self.slc_action.select_element_by_text('Delete')
			self.btn_do_action.click()
			is_there_category_deleted = True
		else:
			if self.cbx_all_category.is_selected():
				self.cbx_all_category.click()

	def check_all_categories(self):
		self.cbx_all_category.click()

	#the value of default parent in dropdown is string 'None'
	def add_category(self, name=None, slug=None, parent='None', desc=None):
		category_form = CategoryFormComponent(self.driver)
		category_form.fill(True, name, slug, parent, desc)

	def click_on_edit_link(self, row_id=None):
		self.action_link.show_action_link(row_id)
		self.action_link.lnk_to_edit.click()

	def delete_category(self, row_id=None):
		self.action_link.show_action_link(row_id)
		self.action_link.lnk_to_delete.click()
		Wait(self.driver).until_alert_presence()
		Alert(self.driver).accept()

	def is_this_category_deleted(self, row_id):
		locator = ('CSS','#tag-'+row_id)
		return self.is_element_removed(locator)

		
