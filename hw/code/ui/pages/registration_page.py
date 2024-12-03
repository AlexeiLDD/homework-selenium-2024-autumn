import time

from selenium.webdriver.support.ui import Select

from ui.pages.base_page import BasePage
from ui.locators.registration_locators import RegistrationLocators
from ui.pages.personal_page import PersonalPage


VALID_EMAIL = 'example@mail.ru'
UNVALID_INN = '1234567890'

class RegistrationPage(BasePage):

    locators = RegistrationLocators
    url = 'https://ads.vk.com/hq/registration'

    def setup(self):
        self.driver.maximize_window()
        self.click(self.locators.CREATE_NEW_BUTTON, timeout=10)

    def teardown(self):
        self.click(self.locators.SUBMIT_BUTTON, timeout=10)

        return PersonalPage(self.driver)
    
    def input_valid_email(self):
        self.input(self.locators.EMAIL_INPUT, VALID_EMAIL, timeout=10)
    
    def input_email(self, email):
        self.input(self.locators.EMAIL_INPUT, email, timeout=10)
    
    def clear_email(self):
        self.clear(self.locators.EMAIL_INPUT, timeout=10)

    def input_unvalid_inn(self):
        self.input(self.locators.INN_INPUT, UNVALID_INN, timeout=10)

    def registration_success(self):
        self.setup()

        title = self.find(self.locators.TITLE_NEW, timeout=10)

        Select(self.find(self.locators.COUNTRY_SELECT)).select_by_visible_text('')
        Select(self.find(self.locators.CURRENCY_SELECT)).select_by_visible_text('')

        self.input_valid_email()

        self.click(self.locators.MAILING_CHECKBOX, timeout=10)
       
        return title

    def registration_ads_individual_rus_success(self):
        self.setup()

        self.click(self.locators.ADS_TYPE, timeout=10)

        self.click(self.locators.COUNTRY_SELECT_BUTTON, timeout=10)
        self.click(self.locators.COUNTRY_SELECT_RUSSIA, timeout=10)

        self.click(self.locators.CURRENCY_SELECT_BUTTON, timeout=10)
        self.click(self.locators.CURRENCY_SELECT_RUB, timeout=10)

        self.input_valid_email()

        self.click(self.locators.IND_TYPE, timeout=10)

        self.find(self.locators.INN_INPUT, timeout=10)
        self.find(self.locators.NAME_INPUT, timeout=10)

        self.click(self.locators.MAILING_CHECKBOX, timeout=10)


    def registration_ads_legal_belarus_success(self):
        self.setup()

        self.click(self.locators.ADS_TYPE, timeout=10)

        self.click(self.locators.COUNTRY_SELECT_BUTTON, timeout=10)
        self.click(self.locators.COUNTRY_SELECT_BELARUS, timeout=10)

        self.input_valid_email()

        self.click(self.locators.LEGAL_TYPE, timeout=10)

        self.click(self.locators.MAILING_CHECKBOX_LEGAL, timeout=10)
    

    def registration_agency_success(self):
        self.setup()

        self.click(self.locators.AGENCY_TYPE, timeout=10)

        self.input_valid_email()

        self.click(self.locators.LEGAL_TYPE, timeout=10)

        self.click(self.locators.MAILING_CHECKBOX_LEGAL, timeout=10)

    def prohibited_country_registration(self):
        self.setup()

        self.click(self.locators.ADS_TYPE, timeout=10)
        self.click(self.locators.IND_TYPE, timeout=10)

        self.click(self.locators.COUNTRY_SELECT_BUTTON, timeout=10)
        self.click(self.locators.COUNTRY_SELECT_AZERBAIJAN, timeout=10)

        self.find(self.locators.WARNING_CONTAINER, timeout=10)
        button = self.find(self.locators.SUBMIT_BUTTON, timeout=10)

        return button
    
    def unvalid_email_registration(self, emails_list):
        self.setup()

        self.click(self.locators.ADS_TYPE, timeout=10)
        self.click(self.locators.IND_TYPE, timeout=10)

        for email in emails_list:
            self.clear_email()
            self.input_email(email)
            self.click(self.locators.ADS_TYPE, timeout=10)
            alert = self.find(self.locators.ALERT_CONTAINER, timeout=10)
            
            yield alert.text
    
    def empty_registration(self):
        self.setup()

        self.click(self.locators.SUBMIT_BUTTON, timeout=10)

        alert = self.find(self.locators.ALERT_CONTAINER, timeout=10)

        return alert

    def unvalid_inn_registration(self):
        self.setup()

        self.click(self.locators.ADS_TYPE, timeout=10)
        self.click(self.locators.IND_TYPE, timeout=10)

        self.input_valid_email()
        self.input_unvalid_inn()

        self.click(self.locators.SUBMIT_BUTTON, timeout=10)

        alert = self.find(self.locators.ALERT_CONTAINER, timeout=10)

        return alert
    
