from locators.post import locators
from pageobject.pagecomponent.PostFormComponent import PostFormComponent
from pageobject.BasePage import BasePage

class PostAddPage(BasePage):

	URL = '/wp-admin/post-new.php'

	def __init__(self, driver):
		self.driver = driver
		self.locators = locators
		self.PostFormComponent = PostFormComponent(driver)

	def add_post(self, title=None, content=None, tags=[]):
		self.PostFormComponent.fill(True, title, content, tags)