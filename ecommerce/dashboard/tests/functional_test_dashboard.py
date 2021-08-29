import pytest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass


class Test_URL_Chrome(Basic_Chrome_Test):
    def test_open_url(self):

        self.driver.get(("%s%s" % (self.live_server_url, "/admin/login/")))

        user_name = driver.find_element_by_name("username")
        user_password = driver.find_element_by_name("password")

        submit = driver.find_element_by_xpath("//input[@value='Log in']")

        user_name.send_keys("admin")
        user_password.send_keys("password")

        submit.send_keys(Keys.RETURN)

        assert "admin" in driver.page_source


# class LoginFormTest(LiveServerTestCase):
#     def testform(self):
#         options = Options()
#         options.headless = False
#         driver = webdriver.Chrome(chrome_options=options)

#         driver.get(("%s%s" % (self.live_server_url, "/admin/login/")))

#         user_name = driver.find_element_by_name("username")
#         user_password = driver.find_element_by_name("password")

#         submit = driver.find_element_by_xpath("//input[@value='Log in']")

#         user_name.send_keys("admin")
#         user_password.send_keys("password")

#         submit.send_keys(Keys.RETURN)

#         assert "admin" in driver.page_source
