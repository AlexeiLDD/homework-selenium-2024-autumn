import time

from ui.pages.base_page import BasePage
from ui.pages.registration_page import RegistrationPage
from ui.locators.vk_id_locators import VkIdPageLocators


class VkIdPage(BasePage):

    locators = VkIdPageLocators
    url = 'https://ads.vk.com/'

    def login(self, user, password):
        self.driver.maximize_window()
        self.click(self.locators.LOGIN_BUTTON, timeout=10)
        self.click(self.locators.LOGIN_VIA_MAIL_BUTTON, timeout=10)
        self.input(self.locators.EMAIL_INPUT, user, timeout=10)
        self.click(self.locators.ENTER_BUTTON, timeout=10)
        self.click(self.locators.CAN_NOT_LOGIN_LINK, timeout=10)
        self.click(self.locators.USE_PASSWORD_LINK, timeout=10)
        self.input(self.locators.PASSWORD_INPUT, password, timeout=10)
        self.click(self.locators.SUBMIT_BUTTON, timeout=10)
        time.sleep(30)
        self.wait(timeout=3000)
    
    def change_registration_page(self):
        return RegistrationPage(self.driver)
        