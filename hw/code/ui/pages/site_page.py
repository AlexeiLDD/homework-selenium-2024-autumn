from ui.pages.base_page import BasePage
from ui.locators.site_locators import SiteLocators

VALID_DOMEN = 'www.vol-4-ok.ru'
UNVALID_DOMEN = 'url'

class SitePage(BasePage):

    locators = SiteLocators
    url = 'https://ads.vk.com/hq/pixels'

    def empty_page(self):
        self.find(self.locators.ADD_PIXEL_BUTTON, timeout=10)
        placeholder_title = self.find(self.locators.PLACEHOLDER_EMPTY_LOCATOR, timeout=10)

        return placeholder_title
    
    def add_valid_pixel(self):
        self.click(self.locators.ADD_PIXEL_BUTTON, timeout=10)

        self.click(self.locators.CHOOSE_DOMEN_BUTTON, timeout=10)
        self.input(self.locators.DOMEN_INPUT, VALID_DOMEN, timeout=10)

        self.click(self.locators.SUBMIT_ADD_PIXEL_BUTTON, timeout=10)
        self.click(self.locators.ADD_NEW_PIXEL_BUTTON, timeout=10)

        header = self.find(self.locators.CONFIRM_HEADER, timeout=10)

        return header
    
    def add_unvalid_pixel(self):
        self.click(self.locators.ADD_PIXEL_BUTTON, timeout=10)

        self.click(self.locators.CHOOSE_DOMEN_BUTTON, timeout=10)
        self.input(self.locators.DOMEN_INPUT, UNVALID_DOMEN, timeout=10)

        self.click(self.locators.SUBMIT_ADD_PIXEL_BUTTON, timeout=10)
    
    def close_confirm_dialog(self):
        self.click(self.locators.CLOSE_DIALOG_BUTTON, timeout=10)

    def get_pixel_id(self):
        id = self.find(self.locators.CURRENT_ID, timeout=10)

        return id
    
    def delete_pixel(self):
        self.click(self.locators.KEBAB_MENU, timeout=15)
        self.click(self.locators.DELETE_BUTTON, timeout=10)
        self.click(self.locators.SUBMIT_DELETE_BUTTON, timeout=10)

    def get_settings(self):
        self.click(self.locators.SETTINGS_BUTTON, timeout=10)

    def get_tags(self):
        self.click(self.locators.TAGS_SECTION, timeout=10)

    def get_domen_input_error(self):
        error = self.find(self.locators.INPUT_ERROR, timeout=10)

        return error
