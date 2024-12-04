from selenium.webdriver.common.by import By


class SiteLocators:
    PLACEHOLDER_EMPTY_LOCATOR = (By.XPATH, '//*[@id="pixels"]/div/div/h2')
    ADD_PIXEL_BUTTON = (By.XPATH, '//*[@id="pixels"]/div/div/div[2]/button')

    CHOOSE_DOMEN_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/label[1]')
    DOMEN_INPUT = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/span/input')
    SUBMIT_ADD_PIXEL_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[3]/div/button')

    ADD_NEW_PIXEL_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]')
    CONFIRM_HEADER = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/h2')
    CLOSE_DIALOG_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[3]')

    CURRENT_ID = (By.XPATH, '//*[@id="pixels"]/div/div[2]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div')
    KEBAB_MENU = (By.XPATH, '//*[@id="pixels"]/div/div[2]/div/div/div/div/div[1]/div[1]/div/div/div[5]/div/button')
    DELETE_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[1]/div[4]/div/label[2]')
    SUBMIT_DELETE_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/div/button[2]')

    SETTINGS_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/main/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[1]/div/div/div[4]/a')
    TAGS_SECTION = (By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/main/div[2]/div/div/div/div[2]/div/div[4]')

    INPUT_ERROR = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/span[2]')
    
