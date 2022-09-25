import pytest

class TestTagPage:

	pytest.tag_id_to_be_deleted = None

	def test_move_all_tag_to_trash(self, tag_page):
		tag_page.visit()
		tag_page.bulk_delete_all()
		if tag_page.is_there_tag_deleted:
			assert tag_page.scs_notice.text == 'Tags deleted.'

	def test_create_empty_tag(self, tag_page):
		tag_page.visit()
		tag_page.add_tag()
		assert tag_page.err_notice.text == 'A name is required for this term.'

	def test_create_tag_with_name(self, tag_page):
		tag_page.visit()
		tag_page.add_tag('Selenium')
		assert tag_page.scs_notice.text == 'Tag added.'
	
	def test_create_tag_with_name_and_slug(self, tag_page):
		tag_page.visit()
		tag_page.add_tag('Appium','appium')
		assert tag_page.scs_notice.text == 'Tag added.'

	def test_create_tag_with_name_slug_and_description(self, tag_page):
		tag_page.visit()
		tag_page.add_tag('Robot Framework','robotframework','Robot framework is generic open source automation framework')
		assert tag_page.scs_notice.text == 'Tag added.'
	
	def test_edit_tag(self, tag_page, tag_edit_page):
		tag_page.visit()
		tag_page.click_on_edit_link()
		tag_edit_page.wait_until_page_ready()
		pytest.tag_id_to_be_deleted = tag_edit_page.get_tag_id()
		tag_edit_page.edit_tag('Cypress','cypress','The web has evolved. finally, testing has too.')
		assert 'Tag updated.' in tag_edit_page.message.text
	
	def test_delete_tag(self, tag_page):
		tag_page.visit()
		tag_page.delete_tag(pytest.tag_id_to_be_deleted)
		assert tag_page.is_this_tag_deleted(pytest.tag_id_to_be_deleted)