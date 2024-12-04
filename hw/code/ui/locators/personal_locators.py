from selenium.webdriver.common.by import By


class PersonalLocators:
    SETTINGS_BUTTON = (By.XPATH, '//div[@id="root"]/div/div/div/div/div/div/div/div/div[2]/section/a/div[2]/div')
    SITE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section[2]/div/a[2]')
    LEADFORMS_BUTTON = (By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section[2]/div/a[4]")
    AUDIENCES_BUTTON = (By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section[1]/a[3]")

    DELETE_BUTTON = (By.XPATH, '//div[@id="settings"]/div/form/section[9]/button/span/span')
    SUBMIT_DELETE_BUTTON = (By.XPATH, '//div[@role="dialog"]/div/div/div[2]/div/div/div/div[2]/button[2]/span')
    