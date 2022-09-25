from locators.post import locators
from pageobject.BasePage import BasePage
from pageobject.pagecomponent.ActionsLinkComponent import ActionsLinkComponent
from helper.wait import Wait

class PostPage(BasePage):

	URL = '/wp-admin/edit.php'

	has_post_been_deleted = False

	def __init__(self, driver):
		self.driver = driver
		self.locators = locators
		self.action_link = ActionsLinkComponent(driver, True)

	def check_all_post(self):
		get_all_post = self.get_elements(self.locators['tbl_post_list'])
		if len(get_all_post) > 0:
			self.cbx_all_post.click()
			return len(get_all_post)
		return 0

	def move_multiple_post_to_trash(self):
		if self.check_all_post() > 0:
			self.has_been_deleted = True 
			self.slc_bulk_action.select_element_by_text('Move to Trash')
			self.btn_bulk_action.click()

	def click_on_edit_link(self, row_id=None):
		self.action_link.show_action_link(row_id)
		self.action_link.lnk_to_edit.click()

	def delete_post(self, row_id=None):
		self.action_link.show_action_link(row_id)
		self.action_link.lnk_to_delete.click()

	def is_this_post_deleted(self, row_id):
		locator = ('CSS','#post-'+row_id)
		return self.is_element_removed(locator)