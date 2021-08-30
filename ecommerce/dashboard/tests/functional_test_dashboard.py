import pytest
from selenium.webdriver.common.keys import Keys


def test_django_dashboard(live_server, browser):
    """A Selenium test."""

    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    user_name = browser.find_element_by_name("username")
    user_password = browser.find_element_by_name("password")
    submit = browser.find_element_by_xpath("//input[@value='Log in']")

    user_name.send_keys("admin")
    user_password.send_keys("password")
    submit.send_keys(Keys.RETURN)

    assert "admin" in browser.page_source
