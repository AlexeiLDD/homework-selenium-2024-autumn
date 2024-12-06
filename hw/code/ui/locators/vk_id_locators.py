from selenium.webdriver.common.by import By


class VkIdPageLocators:
    LOGIN_BUTTON = (By.XPATH, '//div[contains(@class, "navigation_right")]/a')
    LOGIN_VIA_MAIL_BUTTON = (By.XPATH, '//button[@data-test-id="oAuthService_mail_ru"]')
    EMAIL_INPUT = (By.NAME, 'username')
    ENTER_BUTTON = (By.XPATH, '//button[@data-test-id="next-button"]')
    CAN_NOT_LOGIN_LINK = (By.XPATH, '//a[@data-test-id="auth-problems"]')
    USE_PASSWORD_LINK = (By.XPATH, '//li[@data-test-id="auth-by-password"]/div[2]/a')
    PASSWORD_INPUT = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.XPATH, '//button[@data-test-id="submit-button"]')
    