from selenium.webdriver.common.by import By


class PersonalLocators:
    SETTINGS_BUTTON = (By.XPATH, '//a[@data-entityid="settings"]')
    SITE_BUTTON = (By.XPATH, '//a[@data-entityid="pixels"]')
    LEADFORMS_BUTTON = (By.XPATH, '//a[@data-entityid="leadads"]')
    AUDIENCES_BUTTON = (By.XPATH, '//a[@data-entityid="audience"]')

    DELETE_BUTTON = (By.XPATH, '//button[contains(@class, "DeleteAccount_button")]')
    DELETE_LEGAL_BUTTON = (By.XPATH, '//button[contains(@class, "DeleteAccount_button")]')
    SUBMIT_DELETE_BUTTON = (By.XPATH, '//div[contains(@class, "DeleteAccountConfirmModal_actions")]/button[2]')
    