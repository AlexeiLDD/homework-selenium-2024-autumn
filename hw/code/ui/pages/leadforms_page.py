from ui.locators.leadforms_locators import LeadFormsLocators
from ui.pages.base_page import BasePage


class LeadFormsPage(BasePage):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadFormsLocators

    def __init__(self, driver):
        self.driver = driver

    def click_leadforms_tab_button(self):
        try:
            self.click(self.locators.LEADFORMS_TAB_BUTTON, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking on leadforms tab button: {e}")

    def check_no_leadforms_label(self):
        try:
            self.find(self.locators.NO_LEADFORMS_LABEL, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking no leadforms label: {e}")

    def click_create_lead_from_button(self):
        try:
            self.click(self.locators.CREATE_LEAD_FORM_BUTTON, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking on create lead form button: {e}")

    def check_new_leadform_menu_1st_step_label(self):
        try:
            self.find(self.locators.NEW_LEAD_FORM_HEADER_LABEL, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking new lead form menu 1st step label: {e}")

    def click_more_text_button(self):
        try:
            self.click(self.locators.MORE_TEXT_BUTTON_INACTIVE, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking more text button: {e}")

    def check_long_for_description_label(self):
        try:
            self.find(self.locators.LONG_FORM_DESCRIPTION_HEADER_LABEL, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking long form description label: {e}")

    def click_lead_magnit_button(self):
        try:
            self.click(self.locators.LEAD_MAGNIT_BUTTON, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking lead magnit button: {e}")

    def check_size_of_discount_header_label(self):
        try:
            self.find(self.locators.SIZE_OF_DISCOUNT_HEADER_LABEL, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking size of discount header label: {e}")

    def click_bonus_checkbox_button(self):
        try:
            self.click(self.locators.BONUS_CHECKBOX, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking bonus checkbox button: {e}")

    def check_bonus_description_label(self):
        try:
            self.find(self.locators.BONUS_DESCRIPTION_HEADER_LABEL, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking bonus description label: {e}")

    def click_upload_image_plus_button(self):
        try:
            self.click(self.locators.UPLOAD_IMAGE_PLUS_BUTTON, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking upload image plus button: {e}")

    def check_media_library_menu(self):
        try:
            self.find(self.locators.MEDIA_LIBRARY_MENU_HEADER_LABEL, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking media library menu: {e}")

    def click_clickable_image_button(self):
        try:
            self.click(self.locators.CLICKABLE_IMAGE, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking clickable image button: {e}")

    def input_company_name(self):
        try:
            self.input(self.locators.COMPANY_NAME_INPUT, 'Рога и Копыта', timeout=10)
        except Exception as e:
            print(f"Error occurred while inputting company name: {e}")

    def input_title(self):
        try:
            self.input(self.locators.TITLE_INPUT, 'У нас есть рога и копыта', timeout=10)
        except Exception as e:
            print(f"Error occurred while inputting title: {e}")

    def click_1st_step_continue_button(self):
        try:
            self.click(self.locators.FIRST_STEP_CONTINUE_BUTTON, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking 1st step continue button: {e}")

    def check_required_field_label(self):
        try:
            self.find(self.locators.REQUIRED_FIELD_LABEL, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking required field label: {e}")

    def input_bonus_description(self):
        try:
            self.input(self.locators.BONUS_DESCRIPTION_INPUT, 'Вот тебе бонус', timeout=10)
        except Exception as e:
            print(f"Error occurred while inputting bonus description: {e}")

    def check_add_question_label(self):
        try:
            self.find(self.locators.ADD_QUESTION_BUTTON, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking add question label: {e}")

    def click_add_question_button(self):
        try:
            self.click(self.locators.ADD_QUESTION_BUTTON, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking add question button: {e}")

    def check_question_item_label(self):
        try:
            self.find(self.locators.QUESTION_NUMBER_ONE_ITEM_LABEL, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking question item label: {e}")

    def input_question_text(self):
        try:
            self.input(self.locators.QUESTION_TEXT_INPUT, 'Оказавшись перед зеркалом, что вы ему скажете?',
                       timeout=10)
        except Exception as e:
            print(f"Error occurred while inputting question text: {e}")

    def input_question_answer_one(self):
        try:
            self.input(self.locators.QUESTION_ANSWER_ONE, 'Да', timeout=10)
        except Exception as e:
            print(f"Error occurred while inputting question answer one: {e}")

    def input_question_answer_two(self):
        try:
            self.input(self.locators.QUESTION_ANSWER_TWO, 'Нет', timeout=10)
        except Exception as e:
            print(f"Error occurred while inputting question answer two: {e}")

    def click_2nd_step_continue_button(self):
        try:
            self.click(self.locators.SECOND_STEP_CONTINUE_BUTTON, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking 2nd step continue button: {e}")

    def check_result_header_label(self):
        try:
            self.find(self.locators.RESULT_HEADER_LABEL, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking result header label: {e}")

    def click_3rd_step_continue_button(self):
        try:
            self.click(self.locators.THIRD_STEP_CONTINUE_BUTTON, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking 3rd step continue button: {e}")

    def check_notification_label(self):
        try:
            self.find(self.locators.NOTIFICATIONS_HEADER_LABEL, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking notification label: {e}")

    def input_fio(self):
        try:
            self.input(self.locators.FIO_INPUT, 'Иванов Иван Иванович', timeout=10)
        except Exception as e:
            print(f"Error occurred while inputting FIO: {e}")

    def input_address(self):
        try:
            self.input(self.locators.ADDRESS_INPUT, 'Проспект Мира, дом Кефира', timeout=10)
        except Exception as e:
            print(f"Error occurred while inputting address: {e}")

    def click_save_button(self):
        try:
            self.click(self.locators.SAVE_BUTTON, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking save button: {e}")

    def check_active_leadform_label(self):
        try:
            self.find(self.locators.ACTIVE_LEADFORD_ITEM, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking active leadform label: {e}")

