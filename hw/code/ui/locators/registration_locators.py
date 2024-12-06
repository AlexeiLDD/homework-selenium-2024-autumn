from selenium.webdriver.common.by import By


class RegistrationLocators:
    CREATE_NEW_BUTTON = (By.XPATH, '//div[@id="click-createNewButton"]')

    ADS_TYPE = (By.XPATH, '//input[@data-testid="cabinet-advert"]')
    AGENCY_TYPE = (By.XPATH, '//input[@data-testid="cabinet-agency"]')

    COUNTRY_SELECT = (By.NAME, 'country')
    COUNTRY_SELECT_BUTTON = (By.XPATH, '//input[@data-testid="country"]')
    COUNTRY_SELECT_RUSSIA = (By.XPATH, '//div[@id=":r2:-1"]')
    COUNTRY_SELECT_BELARUS = (By.XPATH, '//div[@id=":r2:-3"]')
    COUNTRY_SELECT_AZERBAIJAN = (By.XPATH, '//div[@id=":r2:-5"]')

    CURRENCY_SELECT = (By.NAME, 'currency')
    CURRENCY_SELECT_BUTTON = (By.XPATH, '//input[@data-testid="currency"]')
    CURRENCY_SELECT_RUB = (By.XPATH, '//div[@id=":r3:-RUB"]')

    # Ближайшим элементом с уникалным идентификатором является форма
    MAILING_CHECKBOX = (By.XPATH, '//form[@class="vkuiFormLayout"]/div/div[10]/label')
    MAILING_CHECKBOX_LEGAL = (By.XPATH, '//form[@class="vkuiFormLayout"]/div/div[8]/label')

    EMAIL_INPUT = (By.NAME, 'email')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')

    IND_TYPE = (By.XPATH, '//input[@data-testid="physical"]')
    LEGAL_TYPE = (By.XPATH, '//input[@data-testid="juridical"]')
    INN_INPUT = (By.NAME, 'inn')
    NAME_INPUT = (By.NAME, 'name')

    RUSSIAN_SELECT = (By.XPATH, '//div[@role="radiogroup"]/label[1]')
    ENGLISH_SELECT = (By.XPATH, '//div[@role="radiogroup"]/label[2]')

    TITLE = (By.XPATH, '//h1[contains(@class, "registration_panelTitle")]')
    TITLE_NEW = (By.XPATH, '//h1[contains(@class, "HeaderNav_headerFormTitle")]')
    WARNING_CONTAINER = (By.XPATH, '//div[contains(@class, "Warning_container")]')
    ALERT_CONTAINER = (By.XPATH, '//span[@role="alert"]')
