from contextlib import contextmanager

import pytest

from ui.pages.vk_id_page import VkIdPage


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
        if self.authorize:
            user = credentials['user']
            password = credentials['password']
            self.main_page = self.login_page.login(user, password)
