from locators.category import locators
from pageobject.BasePage import BasePage

class CategoryFormComponent(BasePage):
	
	def __init__(self, driver):
		self.driver = driver
		self.locators = locators

	def fill(self, is_new, name, slug, parent, desc):
		
		if name is not None:
			inp_cat_name = self.inp_cat_name if is_new else self.inp_name_edit
			inp_cat_name.clear()
			inp_cat_name.send_keys(name)
		
		if slug is not None:
			inp_cat_slug = self.inp_cat_slug if is_new else self.inp_slug_edit
			inp_cat_slug.clear()
			inp_cat_slug.send_keys(slug)

		if parent is not None:
			slc_cat_parent = self.slc_cat_parent if is_new else self.slc_parent_edit
			slc_cat_parent.select_element_by_text(parent)

		if desc is not None:
			inp_cat_desc = self.inp_cat_desc if is_new else self.inp_desc_edit
			inp_cat_desc.send_keys(desc)

		btn_cat_submit = self.btn_cat_add if is_new else self.btn_cat_save
		btn_cat_submit.click()