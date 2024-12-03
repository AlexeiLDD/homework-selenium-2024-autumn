import time

from selenium.webdriver.support.ui import Select

from ui.pages.base_page import BasePage
from ui.locators.registration_locators import RegistrationLocators
from ui.pages.personal_page import PersonalPage


class RegistrationPage(BasePage):

    locators = RegistrationLocators
    url = 'https://ads.vk.com/hq/registration'

    def setup(self):
        self.driver.maximize_window()
        self.click(self.locators.CREATE_NEW_BUTTON, timeout=10)

    def teardown(self):
        self.click(self.locators.MAILING_CHECKBOX, timeout=10)
        self.click(self.locators.SUBMIT_BUTTON, timeout=10)

        return PersonalPage(self.driver)

    def registration_success(self):
        self.setup()

        title = self.find(self.locators.TITLE_NEW, timeout=10)

        Select(self.find(self.locators.COUNTRY_SELECT)).select_by_visible_text('')
        Select(self.find(self.locators.CURRENCY_SELECT)).select_by_visible_text('')

        self.input(self.locators.EMAIL_INPUT, 'example@mail.ru', timeout=10)
       
        return title

    def registration_ads_individual_rus_seccess(self):
        self.setup()

        self.click(self.locators.ADS_TYPE, timeout=10)

        self.click(self.locators.COUNTRY_SELECT_BUTTON, timeout=10)
        self.click(self.locators.COUNTRY_SELECT_RUSSIA, timeout=10)

        self.click(self.locators.CURRENCY_SELECT_BUTTON, timeout=10)
        self.click(self.locators.CURRENCY_SELECT_RUB, timeout=10)

        self.input(self.locators.EMAIL_INPUT, 'example@mail.ru', timeout=10)

        self.click(self.locators.IND_TYPE, timeout=10)

        self.find(self.locators.INN_INPUT, timeout=10)
        self.find(self.locators.NAME_INPUT, timeout=10)

