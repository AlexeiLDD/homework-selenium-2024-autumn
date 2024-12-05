from selenium.webdriver.common.by import By


class PersonalLocators:
    SETTINGS_BUTTON = (By.XPATH, '//a[@data-entityid="settings"]')
    SITE_BUTTON = (By.XPATH, '//a[@data-entityid="pixels"]')
    LEADFORMS_BUTTON = (By.XPATH, '//a[@data-entityid="leadads"]')
    AUDIENCES_BUTTON = (By.XPATH, '//a[@data-entityid="audience"]')

    DELETE_BUTTON = (By.XPATH, '//*[@id="settings"]/div/form/section[9]/button')
    DELETE_LEGAL_BUTTON = (By.XPATH, '//*[@id="settings"]/div/form/section[8]/button')
    SUBMIT_DELETE_BUTTON = (By.XPATH, '//div[@role="dialog"]/div/div/div[2]/div/div/div/div[2]/button[2]/span')
    