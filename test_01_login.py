class TestLoginPage:
	def test_login_without_account(self, login_page):
		login_page.visit()
		login_page.do_login()
		assert 'The username field is empty.' in login_page.err_notice.text 

	def test_login_using_valid_username_empty_password(self, login_page):
		login_page.visit()
		login_page.do_login('admin')
		assert 'The password field is empty.' in login_page.err_notice.text 

	def test_login_using_valid_username_invalid_password(self, login_page):
		login_page.visit()
		username = 'admin'
		login_page.do_login(username,'whatever')
		assert 'The password you entered for the username '+username+' is incorrect' in login_page.err_notice.text 

	def test_login_using_valid_credential(self, login_page, dashboard_page):
		login_page.visit()
		login_page.do_login('admin','wpblogauto')
		assert dashboard_page.page_heading.text == 'Dashboard'
