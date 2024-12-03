import pytest
import time

from base import BaseCase


class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.skip('skip')
    @pytest.mark.usefixtures('credentials')
    def test_login(self, credentials):
        self.login_page.login(credentials['user'], credentials['password'])

        assert self.driver.current_url == 'https://ads.vk.com/hq/registration' or self.driver.current_url == 'https://ads.vk.com/hq/overview'


class TestRegistration(BaseCase):
    authorize = True

    @pytest.mark.skip('skip')
    def test_registration_success(self):
        registration_page = self.login_page.change_registration_page()

        title = registration_page.registration_success()
        assert title.text == 'Регистрация кабинета'

        personal_page = registration_page.teardown()

        personal_page.delete_accaunt()


    def test_registration_ads_individual_rus_seccess(self):
        registration_page = self.login_page.change_registration_page()

        registration_page.registration_ads_individual_rus_seccess()

        personal_page = registration_page.teardown()

        personal_page.delete_accaunt()


    @pytest.mark.skip('skip')
    def test_switch_language(self):
        registration_page = self.login_page.change_registration_page()

        title = registration_page.find(registration_page.locators.TITLE, timeout=1)

        registration_page.click(registration_page.locators.RUSSIAN_SELECT, timeout=1)
        assert title.text == 'Добро пожаловать\nв VK Рекламу'

        registration_page.click(registration_page.locators.ENGLISH_SELECT, timeout=1)
        assert title.text == 'Welcome \nto VK Ads'

