import pytest

class TestPostPage:
	pytest.post_id_to_be_deleted = None

	def test_visit_post_list(self, post_page):
		post_page.visit()
		assert post_page.page_heading.text == 'Posts'
	
	def test_delete_multiple_post(self, post_page):
		post_page.move_multiple_post_to_trash()
		if post_page.has_post_been_deleted:
			assert 'moved to the Trash' in post_page.notice.text
	
	
	def test_create_new_post(self, post_add_page):
		post_add_page.visit()
		post_title = 'This post is written by Selenium'
		post_body = '''
					WebDriver drives a browser natively, as a user would, 
					either locally or on a remote machine using the selenium server,
					marks a leap forward in terms of browser automation
					'''
		tags = ['Selenium']
		post_add_page.add_post(post_title, post_body, tags)
		assert 'Post published' in post_add_page.notice.text

	def test_update_post(self, post_page, post_edit_page):
		post_page.visit()
		post_page.click_on_edit_link()
		post_edit_page.wait_until_page_ready()
		pytest.post_id_to_be_deleted = post_edit_page.get_post_id()
		post_title = 'Automate your mobile app'
		post_body = 'Appium, this tool is awesome to start automating your mobile app'
		tags = ['Appium']
		post_edit_page.update_post(post_title, post_body, tags)
		assert 'Post updated' in post_edit_page.notice.text
	
	def test_delete_newly_created_post(self, post_page):
		post_page.visit()
		post_page.delete_post(pytest.post_id_to_be_deleted)
		assert post_page.is_this_post_deleted(pytest.post_id_to_be_deleted)
	
	