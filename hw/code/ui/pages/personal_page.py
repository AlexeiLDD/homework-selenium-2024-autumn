from ui.pages.base_page import BasePage
from ui.locators.personal_locators import PersonalLocators
from ui.pages.main_page import MainPage


class PersonalPage(BasePage):

    locators = PersonalLocators
    url = 'https://ads.vk.com/hq/overview'

    def delete_accaunt(self):
        self.click(self.locators.SETTINGS_BUTTON, timeout=10)
        self.click(self.locators.DELETE_BUTTON,timeout=10)
        self.click(self.locators.SUBMIT_DELETE_BUTTON, timeout=10)

        return MainPage(self.driver)
    
    def delete_legal_accaunt(self):
        self.click(self.locators.SETTINGS_BUTTON, timeout=10)
        self.click(self.locators.DELETE_LEGAL_BUTTON,timeout=10)
        self.click(self.locators.SUBMIT_DELETE_BUTTON, timeout=10)

        return MainPage(self.driver)