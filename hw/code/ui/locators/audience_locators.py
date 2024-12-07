from selenium.webdriver.common.by import By

class AudiencesLocators:
    AUDIENCES_BUTTON = (By.XPATH, "//a[@data-route='audience' and contains(@class, 'sidebar_menuItem')]")
    NO_AUDIENCES_LABEL = (By.XPATH, "//h2[contains(@class, 'vkuiPlaceholder__header')]")

    LIST_USERS_TAB = (By.XPATH, "//div[@role='tab' and @data-testid='tabs-item' and contains(@class, 'vkuiTabsItem') and @aria-controls='audience.users_list']")
    NO_LIST_USERS_LABEL = (By.XPATH, "//h2[contains(@class, 'vkuiPlaceholder__header')]")

    OFFLINE_CONVERSIONS_TAB = (By.XPATH, "//div[@role='tab' and @data-testid='tabs-item' and contains(@class, 'vkuiTabsItem') and @aria-controls='audience.offline_conversion']")
    NO_OFFLINE_CONVERSIONS_LABEL = (By.XPATH, "//h2[contains(@class, 'vkuiPlaceholder__header')]")

    CREATE_AUDIENCE_BUTTON = (By.XPATH, "//button[@data-testid='create-audience']")
    CREATE_AUDIENCE_HEADER_LABEL = (By.XPATH, "//h2[contains(@class, 'ModalSidebarPage_title')]")

    ADD_SOURCE_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton') and contains(@class, 'vkuiButton--stretched')]")
    INCLUDE_SOURCE_HEADER_LABEL = (By.XPATH, "//h2[contains(@class, 'ModalSidebarPage_title')]")

    KEY_WORDS_BUTTON = (By.XPATH, "//div[contains(@class, 'SourceType_button') and contains(@class, 'vkuiSimpleCell')]")
    KEY_WORDS_HEADER_LABEL = (By.XPATH, "//h2[contains(@class, 'ModalSidebarPage_title')]")

    KEY_WORDS_INPUT = (By.XPATH, "//textarea[contains(@class, 'vkuiTextarea__el')]")
    KEY_WORDS_HINT_LABEL = (By.XPATH, "//div[contains(@class, 'Hint_hintTrigger')]")
    KEY_WORDS_HINT_WINDOW = (By.XPATH, "//div[contains(@class, 'KeyPhrasesSuggesions_suggestionItemText')]")

    KEY_WORDS_HINT_ADD_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'vkuiButton') and contains(@class, 'vkuiButton--hover')]")

    KEY_WORDS_SAVE_BUTTON = (By.XPATH, "//button[@type='submit' and @data-testid='submit']")
    KEY_WORDS_ITEM_HEADER_LABEL = (By.XPATH, "//h4[contains(@class, 'vkuiHeadline--sizeY-none') and contains(@class, 'vkuiTypography--weight-1')]")

    SAVE_AUDIENCE_BUTTON = (By.XPATH, "//button[@type='submit' and @data-testid='submit']")
    AUDIENCE_ITEM = (By.XPATH, "//div[@role='gridcell' and contains(@class, 'BaseTable__row-cell')]")
    AUDIENCE_CHECKBOX = (By.XPATH, "//div[contains(@class, 'vkuiCheckbox__icon') and contains(@class, 'vkuiCheckbox__icon--off')]")

    SHARE_AUDIENCE_BUTTON = (By.XPATH, "//button[@data-testid='share-button']")
    OPEN_ACCESS_HEADER_LABEL = (By.XPATH, "//div[contains(@class, 'vkuiRadio__container')]")

    SAVE_SHARE_AUDIENCE_BUTTON = (By.XPATH, "//button[@type='submit' and @data-testid='submit']")
    CANCEL_SHARE_AUDIENCE_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")

    DELETE_AUDIENCE_BUTTON = (By.XPATH, "//button[@data-testid='remove-items-button']")
    DELETE_AUDIENCE_HEADER_LABEL = (By.XPATH, "//h2[contains(@class, 'RemoveItemsModal_title')]")

    DELETE_AUDIENCE_INSIDE_MODAL_DELETE_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton') and contains(@class, 'vkuiButton--stretched')]")

    UPLOAD_LIST_BUTTON = (By.XPATH, "//button[@data-testid='create-audience']")
    UPLOAD_LIST_HEADER_LABEL = (By.XPATH, "//h2[contains(@class, 'ModalSidebarPage_title')]")

    OFFLINE_UPLOAD_LIST_BUTTON = (By.XPATH, "//button[@data-testid='create-audience']")
    OFFLINE_UPLOAD_LIST_HEADER_LABEL = (By.XPATH, "//h2[contains(@class, 'ModalSidebarPage_title')]")
