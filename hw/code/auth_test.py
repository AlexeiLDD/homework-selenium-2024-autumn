import pytest
import time

from base import BaseCase

class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.skip('skip')
    @pytest.mark.usefixtures('credentials')
    def test_login(self, credentials):
        self.login_page.login(credentials['user'], credentials['password'])
        time.sleep(3)
        assert self.driver.current_url == 'https://ads.vk.com/hq/registration' or self.driver.current_url == 'https://ads.vk.com/hq/overview'
