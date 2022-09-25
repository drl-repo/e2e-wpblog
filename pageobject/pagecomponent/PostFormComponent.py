from locators.post import locators
from pageobject.BasePage import BasePage
from helper.wait import Wait
import time
import random

class PostFormComponent(BasePage):

	def __init__(self, driver):
		self.driver = driver
		self.locators = locators

	def fill(self, is_new, title, content, tag_keywords):
		if title is not None:
			inp_post_title = self.inp_post_title
			if not is_new:
				inp_post_title.clear()
			inp_post_title.send_keys(title)

		if content is not None:
			#switching to iframe body
			self.driver.switch_to.frame(self.ifr_post_body)
			inp_post_body = self.inp_post_body
			if not is_new:
				inp_post_body.clear()
			inp_post_body.send_keys(content)
			self.driver.switch_to.default_content()

		self.select_post_categories_randomly()
		if len(tag_keywords) > 0:
			self.type_and_select_post_tags(0,tag_keywords)

		#then publish
		time.sleep(1)
		self.scroll_to_element(self.locators['btn_post_add'])
		self.btn_post_add.click()

	def select_post_categories_randomly(self):
		categories = self.get_elements(self.locators['cbx_post_categories'])
		index = 0
		for item in categories:
			rand = random.randint(0,len(categories) - 1)
			if index==rand:
				item.click()
			index += 1

	def type_and_select_post_tags(self, index, tag_keywords):

		if index < len(tag_keywords):
			keyword = tag_keywords[index].strip()
			#the keyword need more than 1 character to trigger autocomplete
			if len(keyword) > 1:
				self.inp_post_tags.send_keys(tag_keywords[index])
				#wait for autocomplete select
				locator = self.selenium_locator(self.locators['gif_tag_spinner'])
				Wait(self.driver).until_visible(locator).until_invisible(locator)

				tags = self.get_elements(self.locators['ddv_post_tags'])
				if len(tags) > 0:
					for tag in tags:
						tag.click()

				time.sleep(1)
				self.btn_tags_add.click()
				index += 1
				self.type_and_select_post_tags(index, tag_keywords)
