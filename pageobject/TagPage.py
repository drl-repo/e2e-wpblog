from selenium.webdriver.common.alert import Alert
from locators.tag import locators
from pageobject.BasePage import BasePage
from pageobject.pagecomponent.TagFormComponent import TagFormComponent
from pageobject.pagecomponent.ActionsLinkComponent import ActionsLinkComponent
from helper.wait import *

class TagPage(BasePage):
	
	URL	=	'/wp-admin/edit-tags.php?taxonomy=post_tag';
	is_there_tag_deleted = False

	def __init__(self, driver):
		self.driver = driver
		self.locators = locators
		self.action_link = ActionsLinkComponent(driver)

	def bulk_delete_all(self):
		empty_list = self.is_element_exist(self.locators['tbl_no_item'])
		if not empty_list:
			self.cbx_all_tag.click()
			self.slc_bulk_action.select_element_by_text('Delete')
			self.btn_bulk_action.click()
		else:
			if self.cbx_all_tag.is_selected():
				self.cbx_all_tag.click()

	def add_tag(self, tag_name=None, tag_slug=None, tag_desc=None):
		tag_form = TagFormComponent(self.driver)
		tag_form.fill(True, tag_name, tag_slug, tag_desc)

	def click_on_edit_link(self, row_id=None):
		self.action_link.show_action_link(row_id)
		self.action_link.lnk_to_edit.click()

	def delete_tag(self, row_id=None):
		self.action_link.show_action_link(row_id)
		self.action_link.lnk_to_delete.click()
		Wait(self.driver).until_alert_presence()
		Alert(self.driver).accept()

	def is_this_tag_deleted(self, row_id):
		locator = ('CSS','#tag-'+row_id)
		return self.is_element_removed(locator)


