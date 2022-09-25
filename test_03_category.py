import pytest

class TestCategoryPage:

	pytest.category_id_to_be_deleted = None

	def test_delete_all_categories(self, category_page):
		category_page.visit()
		category_page.move_categories_to_trash()
		if category_page.is_there_category_deleted:
			assert category_page.scs_notice.text == 'Categories deleted.'

	def test_create_empty_category(self, category_page):
		category_page.visit()
		category_page.add_category()
		assert category_page.err_notice.text == 'A name is required for this term.'

	def test_create_category_with_name(self, category_page):
		category_page.visit()
		category_page.add_category('Functional Testing')
		assert category_page.scs_notice.text == 'Category added.'
		
	def test_create_category_name_and_slug(self, category_page):
		category_page.visit()
		category_page.add_category('Non-Functional Testing','non-functional')
		assert category_page.scs_notice.text == 'Category added.'

	def test_create_category_name_slug_and_description(self, category_page):
		category_page.visit()
		category_page.add_category('End to end Testing','e2e-testing','None','Test entire app via user interface')
		assert category_page.scs_notice.text == 'Category added.'

	def test_edit_category(self, category_page, category_edit_page):
		category_page.visit()
		category_page.click_on_edit_link()
		category_edit_page.wait_until_page_ready()
		pytest.category_id_to_be_deleted = category_edit_page.get_category_id()
		category_edit_page.edit_category(
			'Performance Testing',
			'performance-testing',
			'Non-Functional Testing',
			'Determine how a system performs in terms of responsiveness and stability')
		assert 'Category updated.' in category_edit_page.message.text

	def test_delete_category(self, category_page):
		category_page.visit()
		category_page.delete_category(pytest.category_id_to_be_deleted)
		assert category_page.is_this_category_deleted(pytest.category_id_to_be_deleted)
		
