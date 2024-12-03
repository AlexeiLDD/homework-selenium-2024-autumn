import pytest
import time

from selenium.webdriver.support.wait import WebDriverWait

from hw.code.base import BaseCase

class TestAudience(BaseCase):
    authorize = True

    @pytest.mark.skip('skip')
    def test_audiences_tab_success(self):
        change_audience_page = self.login_page.change_audience_page()

        change_audience_page.click_audience_button()
        change_audience_page.check_open_audience_tab()

    @pytest.mark.skip('skip')
    def test_user_lists_success(self):
        change_audience_page = self.login_page.change_audience_page()

        change_audience_page.click_audience_button()
        change_audience_page.check_open_audience_tab()

        change_audience_page.click_list_users_tab()
        change_audience_page.check_open_list_users_tab()

        change_audience_page.click_upload_list_button()
        change_audience_page.check_upload_list_menu_opened()

    @pytest.mark.skip('skip')
    def test_offline_conversation_success(self):
        change_audience_page = self.login_page.change_audience_page()

        change_audience_page.click_audience_button()
        change_audience_page.check_open_audience_tab()

        change_audience_page.click_offline_conversation_tab()
        change_audience_page.check_open_offline_conversation_tab()

        change_audience_page.click_delete_offline_upload_list_button()
        change_audience_page.check_offline_upload_list_menu_opened()

    @pytest.mark.skip('skip')
    def test_create_audience_success(self):
        change_audience_page = self.login_page.change_audience_page()

        change_audience_page.click_audience_button()
        change_audience_page.check_open_audience_tab()

        change_audience_page.click_create_audience_button()
        change_audience_page.check_create_audience_menu()

        change_audience_page.click_add_source_button()
        change_audience_page.check_include_source_menu()

        change_audience_page.click_key_words_button()
        change_audience_page.check_key_words_menu()

        change_audience_page.input_key_word()
        change_audience_page.check_hint_key_words()

        change_audience_page.click_key_word_hint_button()
        change_audience_page.check_key_word_hint_opened()

        change_audience_page.click_add_all_button()
        word_count = change_audience_page.check_key_words_added()
        assert word_count > 5

        change_audience_page.click_save_key_words_button()
        change_audience_page.check_key_words_item_added()

        change_audience_page.click_save_audience_button()

    def test_create_audience_success(self):
        change_audience_page = self.login_page.change_audience_page()

        change_audience_page.click_audience_button()
        change_audience_page.check_audience_item_added()

        change_audience_page.click_audience_checkbox()
        change_audience_page.check_share_audience_button_active()

        # change_audience_page.click_audience_share_button()
        # change_audience_page.check_audience_share_modal_opened()
        # change_audience_page.click_cancel_share_audience_button()

        #change_audience_page.click_delete_audience_button()
        #change_audience_page.check_delete_audience_menu_opened()

        #change_audience_page.click_delete_audience_button_inside_modal()
        #change_audience_page.check_open_audience_tab()








