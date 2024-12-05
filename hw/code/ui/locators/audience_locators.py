from selenium.webdriver.common.by import By

class AudiencesLocators:
    AUDIENCES_BUTTON = (By.XPATH, "//a[@data-testid='left-menu' and contains(., 'Аудитории')]")
    NO_AUDIENCES_LABEL = (By.XPATH, "//h2[contains(@class, 'vkuiPlaceholder__header') and text()='Аудиторий пока нет']")

    LIST_USERS_TAB = (By.XPATH, "//div[@data-testid='tabs-item' and @id='tab_audience.users_list']")
    NO_LIST_USERS_LABEL = (By.XPATH, "//h2[text()='Списков пользователей пока нет']")

    OFFLINE_CONVERSIONS_TAB = (By.XPATH, "//div[@data-testid='tabs-item' and @id='tab_audience.offline_conversion']")
    NO_OFFLINE_CONVERSIONS_LABEL = (By.XPATH, "//h2[text()='Списков офлайн-конверсий пока нет']")

    CREATE_AUDIENCE_BUTTON = (By.XPATH, "//button[span/span[text()='Создать аудиторию']]")
    CREATE_AUDIENCE_HEADER_LABEL = (By.XPATH, "//h2[text()='Создание аудитории']")

    ADD_SOURCE_BUTTON = (By.XPATH, "//button[span/span[text()='Добавить источник']]")
    INCLUDE_SOURCE_HEADER_LABEL = (By.XPATH, "//h2[text()='Включить источник']")

    KEY_WORDS_BUTTON = (By.XPATH, "//div[contains(@class, 'SourceType_button__c4PpZ')]//span[text()='Ключевые фразы']")
    KEY_WORDS_HEADER_LABEL = (By.XPATH, "//h2[text()='Ключевые фразы']")

    KEY_WORDS_INPUT = (By.XPATH, "//textarea[@placeholder='Введите фразу и нажмите Enter']")
    KEY_WORDS_HINT_LABEL = (By.XPATH, "//div[contains(@class, 'Hint_hintTrigger__ixYRu') and starts-with(text(), 'Показать')]")
    KEY_WORDS_HINT_WINDOW = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-tertiary') and span/span[text()='Отмена']]")

    KEY_WORDS_HINT_ADD_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary') and span/span[text()='Добавить все']]")

    KEY_WORDS_SAVE_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary') and span/span[text()='Добавить все']]")
    KEY_WORDS_ITEM_HEADER_LABEL = (By.XPATH, "//h4[contains(@class, 'vkuiHeadline--level-1') and text()='Ключевые фразы']")

    SAVE_AUDIENCE_BUTTON = (By.XPATH, "//button[@data-testid='submit' and span/span[text()='Сохранить']]")
    AUDIENCE_ITEM = (By.XPATH, "//*[@id='audience']/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/h5")
    AUDIENCE_CHECKBOX = (By.XPATH, "//*[@id='audience']/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[1]/label")

    SHARE_AUDIENCE_BUTTON = (By.XPATH, "//span[contains(@class, 'vkuiButton__in')]/span/svg[use[@xlink:href='#share_outline_24']]")
    OPEN_ACCESS_HEADER_LABEL = (By.XPATH, "//*[@id='_modal_40-label']")

    SAVE_SHARE_AUDIENCE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/button[2]")
    CANCEL_SHARE_AUDIENCE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/button[1]")

    DELETE_AUDIENCE_BUTTON = (By.XPATH, "//span[contains(@class, 'vkuiButton__in')]/span/svg[use[@xlink:href='#delete_outline_24']]")
    DELETE_AUDIENCE_HEADER_LABEL = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/h2")

    DELETE_AUDIENCE_INSIDE_MODAL_DELETE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/button[2]")

    UPLOAD_LIST_BUTTON = (By.XPATH, "//*[@id='audience.users_list']/div/div[2]/div/div[2]/div/div/div[2]/div/button")
    UPLOAD_LIST_HEADER_LABEL = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div/div[1]/h2")

    OFFLINE_UPLOAD_LIST_BUTTON = (By.XPATH, "//*[@id='audience.offline_conversion']/div/div[2]/div/div[1]/div[1]/div/button")
    OFFLINE_UPLOAD_LIST_HEADER_LABEL = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div/div[1]/h2")
