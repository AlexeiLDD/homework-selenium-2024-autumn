from ui.locators.audience_locators import AudiencesLocators
from ui.pages.base_page import BasePage
import time

class AudiencePage(BasePage):
    url = "https://ads.vk.com/"
    locators = AudiencesLocators

    def click_audience_button(self):
        try:
            self.click(self.locators.AUDIENCES_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking audience button: {e}")

    def click_list_users_tab(self):
        try:
            self.click(self.locators.LIST_USERS_TAB, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking list users tab: {e}")

    def click_offline_conversation_tab(self):
        try:
            self.click(self.locators.OFFLINE_CONVERSIONS_TAB, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking offline conversation tab: {e}")

    def check_open_audience_tab(self):
        try:
            self.find(self.locators.NO_AUDIENCES_LABEL, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking open audience tab: {e}")

    def check_open_list_users_tab(self):
        try:
            self.find(self.locators.NO_LIST_USERS_LABEL, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking open list users tab: {e}")

    def check_open_offline_conversation_tab(self):
        try:
            self.find(self.locators.NO_OFFLINE_CONVERSIONS_LABEL, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking open offline conversation tab: {e}")

    def click_create_audience_button(self):
        try:
            self.click(self.locators.CREATE_AUDIENCE_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking create audience button: {e}")

    def check_create_audience_menu(self):
        try:
            self.find(self.locators.CREATE_AUDIENCE_HEADER_LABEL, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking create audience menu: {e}")

    def click_add_source_button(self):
        try:
            self.click(self.locators.ADD_SOURCE_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking add source button: {e}")

    def check_include_source_menu(self):
        try:
            self.find(self.locators.INCLUDE_SOURCE_HEADER_LABEL, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking include source menu: {e}")

    def click_key_words_button(self):
        try:
            self.click(self.locators.KEY_WORDS_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking key words button: {e}")

    def check_key_words_menu(self):
        try:
            self.find(self.locators.KEY_WORDS_HEADER_LABEL, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking key words menu: {e}")

    def input_key_word(self):
        try:
            self.input(self.locators.KEY_WORDS_INPUT, 'биткоин', timeout=1000)
            time.sleep(3)
        except Exception as e:
            print(f"Error occurred while inputting key word: {e}")

    def check_hint_key_words(self):
        try:
            self.find(self.locators.KEY_WORDS_HINT_LABEL, timeout=1000)
            time.sleep(1)
        except Exception as e:
            print(f"Error occurred while checking hint key words: {e}")

    def click_key_word_hint_button(self):
        try:
            self.click(self.locators.KEY_WORDS_HINT_LABEL, timeout=1000)
            time.sleep(1)
        except Exception as e:
            print(f"Error occurred while clicking key word hint button: {e}")

    def check_key_word_hint_opened(self):
        try:
            self.find(self.locators.KEY_WORDS_HINT_WINDOW, timeout=1000)
            time.sleep(1)
        except Exception as e:
            print(f"Error occurred while checking key word hint opened: {e}")

    def click_add_all_button(self):
        try:
            self.click(self.locators.KEY_WORDS_HINT_ADD_BUTTON, timeout=1000)
            time.sleep(1)
        except Exception as e:
            print(f"Error occurred while clicking add all button: {e}")

    def check_key_words_added(self):
        try:
            textarea_element = self.find(self.locators.KEY_WORDS_INPUT, timeout=1000)
            textarea_text = textarea_element.get_attribute(
                "value")  # Используем "value" для получения введённого текста
            # Подсчитать количество слов
            word_count = len(textarea_text.split())
            print("word_count = ", word_count)
            return word_count
        except Exception as e:
            print(f"Error occurred while checking key words added: {e}")

    def click_save_key_words_button(self):
        try:
            self.click(self.locators.KEY_WORDS_SAVE_BUTTON, timeout=1000)
            time.sleep(1)
        except Exception as e:
            print(f"Error occurred while clicking save key words button: {e}")

    def check_key_words_item_added(self):
        try:
            self.find(self.locators.KEY_WORDS_ITEM_HEADER_LABEL, timeout=1000)
            time.sleep(1)
        except Exception as e:
            print(f"Error occurred while checking key words item added: {e}")

    def click_save_audience_button(self):
        try:
            self.click(self.locators.SAVE_AUDIENCE_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking save audience button: {e}")

    def check_audience_item_added(self):
        try:
            self.find(self.locators.AUDIENCE_ITEM, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking audience item added: {e}")

    def click_audience_checkbox(self):
        try:
            self.click(self.locators.AUDIENCE_CHECKBOX, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking audience checkbox: {e}")

    def check_share_audience_button_active(self):
        try:
            self.find(self.locators.SHARE_AUDIENCE_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking share audience button active: {e}")

    def click_audience_share_button(self):
        try:
            self.click(self.locators.SHARE_AUDIENCE_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking audience share button: {e}")

    def check_audience_share_modal_opened(self):
        try:
            self.find(self.locators.SAVE_SHARE_AUDIENCE_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking audience share modal opened: {e}")

    def click_cancel_share_audience_button(self):
        try:
            self.click(self.locators.CANCEL_SHARE_AUDIENCE_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking cancel share audience button: {e}")

    def click_delete_audience_button(self):
        try:
            self.click(self.locators.DELETE_AUDIENCE_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking delete audience button: {e}")

    def check_delete_audience_menu_opened(self):
        try:
            self.find(self.locators.DELETE_AUDIENCE_HEADER_LABEL, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking delete audience menu opened: {e}")

    def click_delete_audience_button_inside_modal(self):
        try:
            self.click(self.locators.DELETE_AUDIENCE_INSIDE_MODAL_DELETE_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking delete audience button inside modal: {e}")

    def click_upload_list_button(self):
        try:
            self.click(self.locators.UPLOAD_LIST_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking upload list button: {e}")

    def check_upload_list_menu_opened(self):
        try:
            self.find(self.locators.UPLOAD_LIST_HEADER_LABEL, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking upload list menu opened: {e}")

    def click_delete_offline_upload_list_button(self):
        try:
            self.click(self.locators.OFFLINE_UPLOAD_LIST_BUTTON, timeout=1000)
        except Exception as e:
            print(f"Error occurred while clicking delete offline upload list button: {e}")

    def check_offline_upload_list_menu_opened(self):
        try:
            self.find(self.locators.OFFLINE_UPLOAD_LIST_HEADER_LABEL, timeout=1000)
        except Exception as e:
            print(f"Error occurred while checking offline upload list menu opened: {e}")








