import pytest

from base import BaseCase


class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.usefixtures('credentials')
    def test_login(self, credentials):
        self.login_page.login(credentials['user'], credentials['password'])

        url = 'https://ads.vk.com/hq'
        self.wait_url_loading(url)
        assert url in self.driver.current_url, f'Expected URL to be {url}, but got {self.driver.current_url}'


class TestRegistration(BaseCase):
    authorize = True

    # Warning:
    # Метод необходим для сохранения консистентности!
    # Перед прохождением тестов регистрации необходимо удалить существующий аккаунт!
    def test_setup_class(self):
        personal_page = self.login_page.change_personal_page()

        main_page = personal_page.delete_accaunt()
        main_page.pass_func()

    def test_registration_success(self):
        registration_page = self.login_page.change_registration_page()

        correct_title = 'Регистрация кабинета'
        current_title = registration_page.registration_success()
        assert current_title.text == correct_title, f'Expected registration title to be {correct_title}, but got {current_title.text}'

        personal_page = registration_page.teardown()

        main_page = personal_page.delete_accaunt()
        main_page.pass_func()

    def test_registration_ads_individual_rus_success(self):
        registration_page = self.login_page.change_registration_page()

        registration_page.registration_ads_individual_rus_success()

        personal_page = registration_page.teardown()

        main_page = personal_page.delete_accaunt()
        main_page.pass_func()

    def test_registration_ads_legal_belarus_success(self):
        registration_page = self.login_page.change_registration_page()

        registration_page.registration_ads_legal_belarus_success()

        personal_page = registration_page.teardown()

        main_page = personal_page.delete_legal_accaunt()
        main_page.pass_func()

    # Warning:
    # Невозможно сохранение консистентности!
    # После регистрации кабинета агенства его удаление возможно только через службу поддержки!
    @pytest.mark.skip('skip')
    def test_registration_agency_success(self):
        registration_page = self.login_page.change_registration_page()

        registration_page.registration_agency_success()

        personal_page = registration_page.teardown()

        main_page = personal_page.delete_accaunt()
        main_page.pass_func()

    def test_prohibited_country_registration(self):
        registration_page = self.login_page.change_registration_page()

        button = registration_page.prohibited_country_registration()

        assert button.get_property('disabled'), 'Registration button is not disabled'
    

    def test_unvalid_email_registration(self):
        registration_page = self.login_page.change_registration_page()

        UNVALID_EMAILS = ['example', 'example@', 'example@mail.', 'example@mail.w']

        error_message = 'Некорректный email адрес'
        for text in registration_page.unvalid_email_registration(UNVALID_EMAILS):
            assert text == error_message, f'Expected error message to be {error_message}, but got {text}'
    

    def test_empty_registration(self):
        registration_page = self.login_page.change_registration_page()

        alert = registration_page.empty_registration()

        assert alert.text == 'Обязательное поле'


    def test_unvalid_inn_registration(self):
        registration_page = self.login_page.change_registration_page()

        alert = registration_page.unvalid_inn_registration()

        assert alert.text == 'Напишите не меньше 12 символов'


    def test_switch_language(self):
        registration_page = self.login_page.change_registration_page()

        title = registration_page.find(registration_page.locators.TITLE, timeout=1)

        russian_title = 'Добро пожаловать\nв VK Рекламу'
        registration_page.click(registration_page.locators.RUSSIAN_SELECT, timeout=1)
        assert title.text == russian_title, f'Expected russian title to be {russian_title}, but got {title.text}'

        english_title = 'Welcome \nto VK Ads'
        registration_page.click(registration_page.locators.ENGLISH_SELECT, timeout=1)
        assert title.text == english_title, f'Expected english title to be {english_title}, but got {title.text}'

    
    # Warning:
    # Метод необходим для сохранения консистентности!
    # После прохождения тестов регистрации необходимо заново зарегистрировать аккаунт!
    def test_teardown_class(self):
        registration_page = self.login_page.change_registration_page()

        registration_page.registration_success()
        registration_page.teardown()
        self.wait_url_loading('https://ads.vk.com/hq/overview')
