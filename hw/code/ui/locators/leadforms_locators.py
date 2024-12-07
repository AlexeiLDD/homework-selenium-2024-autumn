from selenium.webdriver.common.by import By

class LeadFormsLocators:
    LEADFORMS_TAB_BUTTON = (By.XPATH, "//a[@data-route='leadads' and @data-testid='left-menu']")
    NO_LEADFORMS_LABEL = (By.XPATH, "//h2[contains(@class, 'vkuiPlaceholder__header')]")

    CREATE_LEAD_FORM_BUTTON = (By.XPATH, "//button[@test-id='create-leadform-button']")
    NEW_LEAD_FORM_HEADER_LABEL = (By.XPATH, "//h2[contains(@class, 'ModalSidebarPage_title')]")

    MORE_TEXT_BUTTON_INACTIVE = (By.XPATH, "//label[contains(@class, 'vkuiSegmentedControlOption')]")
    SHORT_FORM_DESCRIPTION_HEADER_LABEL = (By.XPATH, "//h5[contains(@class, 'vkuiTypography')]")

    LONG_FORM_DESCRIPTION_HEADER_LABEL = (By.XPATH, "//h5[contains(@class, 'vkuiTypography') and contains(text(), 'Длинное описание')]")
    LEAD_MAGNIT_BUTTON = (By.XPATH, "//label[contains(@class, 'vkuiSegmentedControlOption')]//span[text()='Лид-магнит']")

    DISCOUNT_CHECKBOX = (By.XPATH, "//label[contains(@class, 'vkuiRadio')]//span[text()='Скидка']")
    BONUS_CHECKBOX = (By.XPATH, "//label[contains(@class, 'vkuiRadio')]//span[text()='Бонус']")

    SIZE_OF_DISCOUNT_HEADER_LABEL = (By.XPATH, "//h5[contains(@class, 'vkuiTypography') and contains(@class, 'FormItemRx_top')]//span[text()='Размер скидки']")
    BONUS_DESCRIPTION_HEADER_LABEL = (By.XPATH, "//h5[contains(@class, 'vkuiTypography') and contains(@class, 'FormItemRx_top')]//span[text()='Описание бонуса']")

    UPLOAD_IMAGE_PLUS_BUTTON = (By.XPATH, "//div[contains(@class, 'vkuiImageBase') and contains(@class, 'vkuiAvatar')]")
    MEDIA_LIBRARY_MENU_HEADER_LABEL = (By.XPATH, "//h2[contains(@class, 'vkuiTypography') and contains(@class, 'ModalSidebarPage_title') and contains(@class, 'ModalSidebarPage_titleWithRight') and text()='Медиатека']")
    CLOSE_MEDIA_LIBRARY_MENU_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiIconButton') and contains(@class, 'vkuiIconButton--sizeY-none') and @aria-label='Close']")
    CLICKABLE_IMAGE = (By.XPATH, "//div[contains(@class, 'ImageItem_imageItem') and contains(@class, 'ImageItem_active')]")

    COMPANY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Название компании']")
    TITLE_INPUT = HEADER_TEXT_INPUT = (By.XPATH, "//input[@placeholder='Текст заголовка']")
    BONUS_DESCRIPTION_INPUT = (By.XPATH, "//input[@placeholder='Бонус']")

    FIRST_STEP_CONTINUE_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton') and contains(@class, 'vkuiButton--size-l') and contains(@class, 'vkuiButton--mode-primary') and @title='Продолжить']")
    REQUIRED_FIELD_LABEL = (By.XPATH, "//span[contains(@class, 'vkuiTypography') and contains(@class, 'vkuiFormItem__bottom') and contains(@class, 'vkuiFootnote') and @role='alert']")

    ADD_QUESTION_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton') and contains(@class, 'vkuiButton--size-l') and contains(@class, 'vkuiButton--mode-secondary') and contains(@class, 'vkuiButton--appearance-accent') and contains(@class, 'vkuiButton--align-center') and contains(@class, 'vkuiButton--stretched') and contains(@class, 'vkuiButton--with-icon') and contains(@class, 'vkuiTappable')]//span[contains(@class, 'vkuiButton__content')]")
    QUESTION_NUMBER_ONE_ITEM_LABEL = (By.XPATH, "//div[contains(@class, 'Question_questionHeaderLeft')]")

    QUESTION_TEXT_INPUT = (By.XPATH, "//span[contains(@class, 'vkuiFormField') and contains(@class, 'vkuiTextarea')]")
    QUESTION_ANSWER_ONE = (By.XPATH, "//input[@class='vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none' and @placeholder='Введите ответ']")
    QUESTION_ANSWER_TWO = (By.CSS_SELECTOR, "input.vkuiTypography.vkuiInput__el.vkuiText.vkuiText--sizeY-none[placeholder='Введите ответ']")

    SECOND_STEP_CONTINUE_BUTTON = (By.XPATH, "//button[@type='submit' and @title='Продолжить' and contains(@class, 'vkuiButton') and contains(@class, 'vkuiButton--mode-primary')]")
    RESULT_HEADER_LABEL = (By.XPATH, "//h4[contains(@class, 'vkuiTypography') and contains(@class, 'vkuiHeadline--level-1')]")

    THIRD_STEP_CONTINUE_BUTTON = (By.XPATH, "//button[@title='Продолжить' and contains(@class, 'vkuiButton')]/span//span[text()='Продолжить']")
    NOTIFICATIONS_HEADER_LABEL = (By.XPATH, "//h4[contains(@class, 'Settings_headline') and text()='Уведомления']")

    FIO_INPUT = (By.XPATH, "//input[@placeholder='Введите фамилию, имя и отчество']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='Введите адрес']")
    SAVE_BUTTON = (By.XPATH, "//button[@title='Сохранить' and .//span[contains(text(), 'Сохранить')]]")

    ACTIVE_LEADFORD_ITEM = (By.XPATH, "//div[@role='gridcell' and contains(text(), 'Активна')]")
