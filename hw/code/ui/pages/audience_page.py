from ui.locators.audience_locators import AudiencesLocators
from ui.pages.base_page import BasePage
import time


class AudiencePage(BasePage):
    url = "https://ads.vk.com/hq/audience"
    locators = AudiencesLocators

    def click_list_users_tab(self):
        self.click(self.locators.LIST_USERS_TAB, timeout=10)

    def click_offline_conversation_tab(self):
        self.click(self.locators.OFFLINE_CONVERSIONS_TAB, timeout=10)

    def check_open_audience_tab(self):
        self.find(self.locators.NO_AUDIENCES_LABEL, timeout=10)

    def check_open_list_users_tab(self):
        self.find(self.locators.NO_LIST_USERS_LABEL, timeout=10)

    def check_open_offline_conversation_tab(self):
        self.find(self.locators.NO_OFFLINE_CONVERSIONS_LABEL, timeout=10)

    def click_create_audience_button(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON, timeout=10)

    def check_create_audience_menu(self):
        self.find(self.locators.CREATE_AUDIENCE_HEADER_LABEL, timeout=10)

    def click_add_source_button(self):
        self.click(self.locators.ADD_SOURCE_BUTTON, timeout=10)

    def check_include_source_menu(self):
        self.find(self.locators.INCLUDE_SOURCE_HEADER_LABEL, timeout=10)

    def click_key_words_button(self):
        self.click(self.locators.KEY_WORDS_BUTTON, timeout=10)

    def check_key_words_menu(self):
        self.find(self.locators.KEY_WORDS_HEADER_LABEL, timeout=10)

    def input_key_word(self):
        self.input(self.locators.KEY_WORDS_INPUT, 'биткоин', timeout=10)

    def check_hint_key_words(self):
        self.find(self.locators.KEY_WORDS_HINT_LABEL, timeout=10)

    def click_key_word_hint_button(self):
        self.click(self.locators.KEY_WORDS_HINT_LABEL, timeout=10)

    def check_key_word_hint_opened(self):
        self.find(self.locators.KEY_WORDS_HINT_WINDOW, timeout=10)

    def click_add_all_button(self):
        self.click(self.locators.KEY_WORDS_HINT_ADD_BUTTON, timeout=10)

    def check_key_words_added(self):
        textarea_element = self.find(self.locators.KEY_WORDS_INPUT, timeout=10)

        textarea_text = textarea_element.get_attribute("value")  # Используем "value" для получения введённого текста

        # Подсчитать количество слов
        word_count = len(textarea_text.split())
        print("word_count = ", word_count)

        return word_count

    def click_save_key_words_button(self):
        self.click(self.locators.KEY_WORDS_SAVE_BUTTON, timeout=10)

    def check_key_words_item_added(self):
        self.find(self.locators.KEY_WORDS_ITEM_HEADER_LABEL, timeout=10)

    def click_save_audience_button(self):
        self.click(self.locators.SAVE_AUDIENCE_BUTTON, timeout=10)

    def check_audience_item_added(self):
        self.find(self.locators.AUDIENCE_ITEM , timeout=10)

    def click_audience_checkbox(self):
        self.click(self.locators.AUDIENCE_CHECKBOX , timeout=10)

    def check_share_audience_button_active(self):
        self.find(self.locators.SHARE_AUDIENCE_BUTTON, timeout=10)

    def click_audience_share_button(self):
        self.click(self.locators.SHARE_AUDIENCE_BUTTON , timeout=10)

    def check_audience_share_modal_opened(self):
        self.find(self.locators.SAVE_SHARE_AUDIENCE_BUTTON , timeout=10)

    def click_cancel_share_audience_button(self):
        self.click(self.locators.CANCEL_SHARE_AUDIENCE_BUTTON , timeout=10)

    def click_delete_audience_button(self):
        self.click(self.locators.DELETE_AUDIENCE_BUTTON , timeout=10)

    def check_delete_audience_menu_opened(self):
        self.find(self.locators.DELETE_AUDIENCE_HEADER_LABEL , timeout=10)

    def click_delete_audience_button_inside_modal(self):
        self.click(self.locators.DELETE_AUDIENCE_INSIDE_MODAL_DELETE_BUTTON , timeout=10)

    def click_upload_list_button(self):
        self.click(self.locators.UPLOAD_LIST_BUTTON , timeout=10)

    def check_upload_list_menu_opened(self):
        self.find(self.locators.UPLOAD_LIST_HEADER_LABEL , timeout=10)

    def click_delete_offline_upload_list_button(self):
        self.click(self.locators.OFFLINE_UPLOAD_LIST_BUTTON , timeout=10)

    def check_offline_upload_list_menu_opened(self):
        self.find(self.locators.OFFLINE_UPLOAD_LIST_HEADER_LABEL , timeout=10)
