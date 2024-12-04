from ui.pages.base_page import BasePage
from ui.locators.vk_id_locators import VkIdPageLocators
from ui.pages.audience_page import AudiencePage
from ui.pages.leadforms_page import LeadFormsPage

import time

class VkIdPage(BasePage):

    locators = VkIdPageLocators
    url = 'https://ads.vk.com/'

    def login(self, user, password):
        self.driver.maximize_window()
        self.click(self.locators.LOGIN_BUTTON, timeout=1000)
        self.click(self.locators.LOGIN_VIA_MAIL_BUTTON, timeout=1000)
        self.input(self.locators.EMAIL_INPUT, user, timeout=1000)
        self.click(self.locators.ENTER_BUTTON, timeout=1000)
        self.click(self.locators.CAN_NOT_LOGIN_LINK, timeout=1000)
        self.click(self.locators.USE_PASSWORD_LINK, timeout=1000)
        self.input(self.locators.PASSWORD_INPUT, password, timeout=1000)
        self.click(self.locators.SUBMIT_BUTTON, timeout=1000)
        time.sleep(30)

    def change_audience_page(self):
        return AudiencePage(self.driver)

    def change_leadforms_page(self):
        return LeadFormsPage(self.driver)
        