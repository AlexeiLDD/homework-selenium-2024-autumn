from selenium.webdriver.common.by import By

class LeadFormsLocators:
    LEADFORMS_TAB_BUTTON = (By.XPATH, "//a[contains(@class, 'vkuiSimpleCell') and span/span[text()='Лид-формы и опросы']]")
    NO_LEADFORMS_LABEL = (By.XPATH, "//h2[contains(@class, 'vkuiPlaceholder__header') and text()='Лид-форм пока нет']")

    CREATE_LEAD_FORM_BUTTON = (By.XPATH, "//button[contains(@class, 'LeadForms_createButton__BKYWP') and span/span[text()='Создать лид-форму']]")
    NEW_LEAD_FORM_HEADER_LABEL = (By.XPATH, "//h2[contains(@class, 'ModalSidebarPage_title__Uu-FC') and text()='Новая лид-форма']")

    MORE_TEXT_BUTTON_INACTIVE = (By.XPATH, "//label[contains(@class, 'vkuiSegmentedControlOption')]//span[text()='Больше текста']")
    SHORT_FORM_DESCRIPTION_HEADER_LABEL = (By.XPATH, "//h5[contains(@class, 'vkuiTypography') and contains(@class, 'FormItemRx_top__Onz0a') and text()='Описание формы']")

    LONG_FORM_DESCRIPTION_HEADER_LABEL = (By.XPATH, "//h5[contains(@class, 'vkuiTypography') and contains(@class, 'FormItemRx_top__Onz0a') and text()='Длинное описание (не более 2 переносов строк подряд)']")
    LEAD_MAGNIT_BUTTON = (By.XPATH, "//label[contains(@class, 'vkuiSegmentedControlOption')]//span[text()='Лид-магнит']")

    DISCOUNT_CHECKBOX = (By.XPATH, "//label[contains(@class, 'vkuiRadio')]//span[text()='Скидка']")
    BONUS_CHECKBOX = (By.XPATH, "//label[contains(@class, 'vkuiRadio')]//span[text()='Бонус']")

    SIZE_OF_DISCOUNT_HEADER_LABEL = (By.XPATH, "//h5[contains(@class, 'vkuiTypography') and contains(@class, 'FormItemRx_top__Onz0a')]//span[text()='Размер скидки']")
    BONUS_DESCRIPTION_HEADER_LABEL = (By.XPATH, "//h5[contains(@class, 'vkuiTypography') and contains(@class, 'FormItemRx_top__Onz0a')]//span[text()='Описание бонуса']")

    UPLOAD_IMAGE_PLUS_BUTTON = (By.XPATH, "//div[contains(@class, 'vkuiImageBase') and contains(@class, 'vkuiAvatar')]")
    MEDIA_LIBRARY_MENU_HEADER_LABEL = (By.XPATH, "//h2[contains(@class, 'vkuiTypography') and contains(@class, 'ModalSidebarPage_title__Uu-FC') and contains(@class, 'ModalSidebarPage_titleWithRight__Ywhiy') and text()='Медиатека']")
    CLOSE_MEDIA_LIBRARY_MENU_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiIconButton') and contains(@class, 'vkuiIconButton--sizeY-none') and @aria-label='Close']")
    CLICKABLE_IMAGE = (By.XPATH, "//div[contains(@class, 'ImageItem_imageItem__WiiIG') and contains(@class, 'ImageItem_active__1fy0f')]")

    COMPANY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Название компании']")
    TITLE_INPUT = HEADER_TEXT_INPUT = (By.XPATH, "//input[@placeholder='Текст заголовка']")
    BONUS_DESCRIPTION_INPUT = (By.XPATH, "//input[@placeholder='Бонус']")

    FIRST_STEP_CONTINUE_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton') and contains(@class, 'vkuiButton--size-l') and contains(@class, 'vkuiButton--mode-primary') and @title='Продолжить']")
    REQUIRED_FIELD_LABEL = (By.XPATH, "//span[contains(@class, 'vkuiTypography') and contains(@class, 'vkuiFormItem__bottom') and contains(@class, 'vkuiFootnote') and @role='alert']")

    ADD_QUESTION_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton') and contains(@class, 'vkuiButton--size-l') and contains(@class, 'vkuiButton--mode-secondary') and contains(@class, 'vkuiButton--appearance-accent') and contains(@class, 'vkuiButton--align-center') and contains(@class, 'vkuiButton--stretched') and contains(@class, 'vkuiButton--with-icon') and contains(@class, 'vkuiTappable')]//span[contains(@class, 'vkuiButton__content') and text()='Добавить вопрос']")
    QUESTION_NUMBER_ONE_ITEM_LABEL= (By.XPATH, "//div[contains(@class, 'Question_questionHeaderLeft__yHzJa') and text()='Вопрос № 1']")

    QUESTION_TEXT_INPUT = (By.XPATH, "//span[contains(@class, 'vkuiFormField') and contains(@class, 'vkuiTextarea')]/textarea[@placeholder='Напишите вопрос']")
    QUESTION_ANSWER_ONE = (By.XPATH, "//input[@class='vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none' and @placeholder='Введите ответ']")
    QUESTION_ANSWER_TWO = (By.CSS_SELECTOR, "input.vkuiTypography.vkuiInput__el.vkuiText.vkuiText--sizeY-none[placeholder='Введите ответ']")

    SECOND_STEP_CONTINUE_BUTTON = (By.XPATH, "//button[@type='submit' and @title='Продолжить' and contains(@class, 'vkuiButton') and contains(@class, 'vkuiButton--mode-primary')]")
    RESULT_HEADER_LABEL = (By.XPATH, "//h4[contains(@class, 'vkuiTypography') and contains(@class, 'vkuiHeadline--level-1') and text()='Результат']")

    THIRD_STEP_CONTINUE_BUTTON = (By.XPATH, "//button[@title='Продолжить' and contains(@class, 'vkuiButton')]/span//span[text()='Продолжить']")
    NOTIFICATIONS_HEADER_LABEL = (By.XPATH, "//h4[contains(@class, 'Settings_headline') and text()='Уведомления']")

    FIO_INPUT = (By.XPATH, "//input[@placeholder='Введите фамилию, имя и отчество']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='Введите адрес']")
    SAVE_BUTTON = (By.XPATH, "//button[@title='Сохранить' and .//span[contains(text(), 'Сохранить')]]")

    ACTIVE_LEADFORD_ITEM = (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/main/div[2]/div/div/div[2]/section/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div/div/div[4]")
