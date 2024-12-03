from contextlib import contextmanager

import pytest

from selenium.webdriver.support.wait import WebDriverWait

from ui.pages.vk_id_page import VkIdPage
from ui.pages.main_page import MainPage


class BaseCase:
    driver = None
    authorize = True

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, credentials):
        self.driver = driver
        self.config = config

        self.login_page = VkIdPage(driver)
        self.main_page = MainPage(driver)
        if self.authorize:
            user = credentials['user']
            password = credentials['password']
            self.login_page.login(user, password)

    def wait_url_loading(self, url):
        WebDriverWait(self.driver, 10).until(lambda d: url in d.current_url)
