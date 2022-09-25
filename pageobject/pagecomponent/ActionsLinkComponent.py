from pageobject.BasePage import BasePage

class ActionsLinkComponent(BasePage):
	
	locators = {
		'first_row'		:	'#the-list tr:first-child',
		'other_row'		:	'#tag-',
		'post_row'		:	'#post-',	
	}

	def __init__(self, driver, is_post_page=False):
		self.driver = driver
		self.is_post_page = is_post_page

	def show_action_link(self, row_id=None):
		tr_locator = self.get_tablerow_locator(row_id)
		delete_selector = '.row-actions > .trash > a' if self.is_post_page else '.row-actions > .delete > a'
		self.locators['ttr_tag'] 			= ('CSS',tr_locator)
		self.locators['lnk_to_edit'] 		= ('CSS',tr_locator+' .row-actions > .edit > a')
		self.locators['lnk_to_delete'] 		= ('CSS',tr_locator+' '+delete_selector)

		self.ttr_tag.hover()

	def get_tablerow_locator(self, row_id):
		if row_id is not None:
			if self.is_post_page:
				return self.locators['post_row']+row_id
			else:
				return self.locators['other_row']+row_id
		return self.locators['first_row']	
