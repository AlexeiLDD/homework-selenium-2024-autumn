import pytest

from base import BaseCase

from ui.pages.leadforms_page import LeadFormsPage


class TestLeadForms(BaseCase):
    authorize = True

    @pytest.fixture
    def change_leadforms_page(self):
        self.personal_page = self.login_page.change_personal_page()

        self.get_leadforms_page()

        return LeadFormsPage(self.driver)
    

    def get_leadforms_page(self):
        self.personal_page.click(self.personal_page.locators.LEADFORMS_BUTTON, timeout=10)

        self.wait_url_loading('https://ads.vk.com/hq/leadads/leadforms')


    def test_create_leadform_success(self, change_leadforms_page):
        change_leadforms_page.click_leadforms_tab_button()
        change_leadforms_page.check_no_leadforms_label()

        change_leadforms_page.click_create_lead_from_button()
        change_leadforms_page.check_new_leadform_menu_1st_step_label()

        change_leadforms_page.click_more_text_button()
        change_leadforms_page.check_long_for_description_label()

        change_leadforms_page.click_lead_magnit_button()
        change_leadforms_page.check_size_of_discount_header_label()

        change_leadforms_page.click_bonus_checkbox_button()
        change_leadforms_page.check_bonus_description_label()

        change_leadforms_page.click_upload_image_plus_button()
        change_leadforms_page.check_media_library_menu()

        change_leadforms_page.click_clickable_image_button()
        change_leadforms_page.check_new_leadform_menu_1st_step_label()

        change_leadforms_page.input_company_name()
        change_leadforms_page.input_title()

        change_leadforms_page.click_1st_step_continue_button()
        change_leadforms_page.check_required_field_label()

        change_leadforms_page.input_bonus_description()
        change_leadforms_page.click_1st_step_continue_button()
        change_leadforms_page.check_add_question_label()

        change_leadforms_page.click_add_question_button()
        change_leadforms_page.check_question_item_label()

        change_leadforms_page.input_question_text()
        change_leadforms_page.input_question_answer_one()
        change_leadforms_page.input_question_answer_two()

        change_leadforms_page.click_2nd_step_continue_button()
        change_leadforms_page.check_result_header_label()

        change_leadforms_page.click_3rd_step_continue_button()
        change_leadforms_page.check_notification_label()

        change_leadforms_page.input_fio()
        change_leadforms_page.input_address()

        change_leadforms_page.click_save_button()
        change_leadforms_page.check_active_leadform_label()
