from locators.tag import locators
from pageobject.BasePage import BasePage

class TagFormComponent(BasePage):

	def __init__(self, driver):
		self.driver = driver
		self.locators = locators


	def fill(self, is_new, tag_name, tag_slug, tag_desc):

		if tag_name is not None:
			inp_tag_name = self.inp_tag_name if is_new else self.inp_name_edit
			inp_tag_name.clear()
			inp_tag_name.send_keys(tag_name)
		
		if tag_slug is not None:
			inp_tag_slug = self.inp_tag_slug if is_new else self.inp_slug_edit
			inp_tag_slug.clear()
			inp_tag_slug.send_keys(tag_slug)

		if tag_desc is not None:
			inp_tag_desc = self.inp_tag_desc if is_new else self.inp_desc_edit
			inp_tag_desc.clear()
			inp_tag_desc.send_keys(tag_desc)
		if is_new:
			self.btn_tag_add.click()
		else:
			self.btn_tag_save.click()
