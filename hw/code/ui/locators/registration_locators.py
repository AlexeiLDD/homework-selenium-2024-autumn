from selenium.webdriver.common.by import By


class RegistrationLocators:
    ADS_TYPE = (By.XPATH, '//div[@id="registration.new"]/div/div[2]/section/form/div/div/label/div/div/div')
    AGENCY_TYPE = (By.XPATH, '//div[@id="registration.new"]/div/div[2]/section/form/div/div/label[2]/div/div/div')

    CREATE_NEW_BUTTON = (By.XPATH, '//div[@id="click-createNewButton"]/p')
    TYPE_RADIO = (By.NAME, 'userType')

    COUNTRY_SELECT = (By.NAME, 'country')
    COUNTRY_SELECT_BUTTON = (By.XPATH, '//input[@value=""]')
    COUNTRY_SELECT_RUSSIA = (By.XPATH, '//div[@id=":r2:-1"]')
    COUNTRY_SELECT_BELARUS = (By.XPATH, '//div[@id=":r2:-3"]')
    COUNTRY_SELECT_AZERBAIJAN = (By.XPATH, '//div[@id=":r2:-5"]')

    CURRENCY_SELECT = (By.NAME, 'currency')
    CURRENCY_SELECT_BUTTON = (By.XPATH, '//div[@id="registration.new"]/div/div[2]/section/form/div/div[3]/div/div/div/input')
    CURRENCY_SELECT_RUB = (By.XPATH, '//div[@id=":r3:-RUB"]')

    EMAIL_INPUT = (By.NAME, 'email')
    MAILING_CHECKBOX = (By.XPATH, '//div[@id="registration.new"]/div/div[2]/section/form/div/div[10]/label/div[4]/div/span/div/span')
    MAILING_CHECKBOX_LEGAL = (By.XPATH, '//div[@id="registration.new"]/div/div[2]/section/form/div/div[8]/label')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')

    IND_TYPE = (By.XPATH, '//div[@id="registration.new"]/div/div[2]/section/form/div/div[5]/label/div/div/div/span/div/span')
    LEGAL_TYPE = (By.XPATH, '//div[@id="registration.new"]/div/div[2]/section/form/div/div[5]/label[2]/div/div/div/span/div/span')
    INN_INPUT = (By.NAME, 'inn')
    NAME_INPUT = (By.NAME, 'name')

    RUSSIAN_SELECT = (By.XPATH, '//div[@id="registration"]/div/div[2]/div/section/div/div/label/h4')
    ENGLISH_SELECT = (By.XPATH, '//div[@id="registration"]/div/div[2]/div/section/div/div/label[2]/h4')

    TITLE = (By.CLASS_NAME, 'registration_panelTitle__jHdpM')
    TITLE_NEW = (By.CLASS_NAME, 'HeaderNav_headerFormTitle__1WolE')
    WARNING_CONTAINER = (By.CLASS_NAME, 'Warning_container__WlR61')
    ALERT_CONTAINER = (By.XPATH, '//span[@role="alert"]')
