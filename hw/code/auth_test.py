import pytest
import time

from selenium.webdriver.support.wait import WebDriverWait

from base import BaseCase


class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.skip('skip')
    @pytest.mark.usefixtures('credentials')
    def test_login(self, credentials):
        self.login_page.login(credentials['user'], credentials['password'])

        self.wait_url_loading('ads.vk.com')
        assert self.driver.current_url == 'https://ads.vk.com/hq/registration' or self.driver.current_url == 'https://ads.vk.com/hq/overview'


class TestRegistration(BaseCase):
    authorize = True

    @pytest.mark.skip('skip')
    def test_registration_success(self):
        registration_page = self.login_page.change_registration_page()

        title = registration_page.registration_success()
        assert title.text == 'Регистрация кабинета'

        personal_page = registration_page.teardown()

        main_page = personal_page.delete_accaunt()
        main_page.pass_func()


    @pytest.mark.skip('skip')
    def test_registration_ads_individual_rus_success(self):
        registration_page = self.login_page.change_registration_page()

        registration_page.registration_ads_individual_rus_success()

        personal_page = registration_page.teardown()

        main_page = personal_page.delete_accaunt()
        main_page.pass_func()

    
    @pytest.mark.skip('skip')
    def test_registration_ads_legal_belarus_success(self):
        registration_page = self.login_page.change_registration_page()

        registration_page.registration_ads_legal_belarus_success()

        personal_page = registration_page.teardown()

        main_page = personal_page.delete_accaunt()
        main_page.pass_func()


    # Warning. 
    # Невозможно сохранение консистентности!
    # После регистрации кабинета агенства его удаление возможно только через службу поддержки!
    @pytest.mark.skip('skip')
    def test_registration_agency_success(self):
        registration_page = self.login_page.change_registration_page()

        registration_page.registration_agency_success()

        personal_page = registration_page.teardown()

        main_page = personal_page.delete_accaunt()
        main_page.pass_func() 


    @pytest.mark.skip('skip')
    def test_prohibited_country_registration(self):
        registration_page = self.login_page.change_registration_page()

        button = registration_page.prohibited_country_registration()

        assert button.get_property('disabled')
    

    @pytest.mark.skip('skip')
    def test_unvalid_email_registration(self):
        registration_page = self.login_page.change_registration_page()

        UNVALID_EMAILS = ['example', 'example@', 'example@mail.', 'example@mail.w']

        for text in registration_page.unvalid_email_registration(UNVALID_EMAILS):
            assert text == 'Некорректный email адрес'
    

    @pytest.mark.skip('skip')
    def test_empty_registration(self):
        registration_page = self.login_page.change_registration_page()

        alert = registration_page.empty_registration()

        assert alert.text == 'Обязательное поле'


    @pytest.mark.skip('skip')
    def test_unvalid_inn_registration(self):
        registration_page = self.login_page.change_registration_page()

        alert = registration_page.unvalid_inn_registration()

        assert alert.text == 'Напишите не меньше 12 символов'


    @pytest.mark.skip('skip')
    def test_switch_language(self):
        registration_page = self.login_page.change_registration_page()

        title = registration_page.find(registration_page.locators.TITLE, timeout=1)

        registration_page.click(registration_page.locators.RUSSIAN_SELECT, timeout=1)
        assert title.text == 'Добро пожаловать\nв VK Рекламу'

        registration_page.click(registration_page.locators.ENGLISH_SELECT, timeout=1)
        assert title.text == 'Welcome \nto VK Ads'

