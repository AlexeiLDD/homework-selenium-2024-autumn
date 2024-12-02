from selenium.webdriver.common.by import By


class VkIdPageLocators:
    LOGIN_BUTTON = (By.LINK_TEXT, 'Перейти в кабинет')
    LOGIN_VIA_MAIL_BUTTON = (By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="или войти через VK ID с использованием данных из сервиса"])[1]/following::*[name()="svg"][2]')
    EMAIL_INPUT = (By.NAME, 'username')
    ENTER_BUTTON = (By.XPATH, '//div[@id="root"]/div/div/div/div/div/form/div[2]/div[2]/div[3]/div/div/div/button/span')
    CAN_NOT_LOGIN_LINK = (By.LINK_TEXT, 'Не могу войти')
    USE_PASSWORD_LINK = (By.LINK_TEXT, 'Использовать пароль для входа')
    PASSWORD_INPUT = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.XPATH, '//div[@id="root"]/div/div/div/div/div/form/div[2]/div/div[3]/div/div/div/button/span')