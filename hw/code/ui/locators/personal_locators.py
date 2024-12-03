from selenium.webdriver.common.by import By


class PersonalLocators:
    SETTINGS_BUTTON = (By.XPATH, '//div[@id="root"]/div/div/div/div/div/div/div/div/div[2]/section/a/div[2]/div')
    DELETE_BUTTON = (By.XPATH, '//div[@id="settings"]/div/form/section[9]/button/span/span')
    SUBMIT_DELETE_BUTTON = (By.XPATH, '//div[@role="dialog"]/div/div/div[2]/div/div/div/div[2]/button[2]/span')

    