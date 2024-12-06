from selenium.webdriver.common.by import By


class MainLocators:
    FIRST_BULLET = (By.XPATH, '//div[contains(@class, "Bullets_wrapper")]/div[1]')
    SECOND_BULLET = (By.XPATH, '//div[contains(@class, "Bullets_wrapper")]/div[2]')
    THIRD_BULLET = (By.XPATH, '//div[contains(@class, "Bullets_wrapper")]/div[3]')

    CAROUSEL = (By.XPATH, '//div[contains(@class, "MainSlider_wrapper")]')
    GET_BONUSES_BUTTON = (By.XPATH, '//div[contains(@class, "MainSlider_wrapper")]/div[1]/div/a')
    START_ADS_BUTTON = (By.XPATH, '//div[contains(@class, "MainSlider_wrapper")]/div[2]/div/a')
    MORE_DETAILS_BUTTON = (By.XPATH, '//div[contains(@class, "MainSlider_wrapper")]/div[3]/div/a')

    COMPANY_CASE_HEADER = (By.XPATH, '//div[@data-test-id="main-page-vkads"]/div[2]/h2')
    # Выбор более точного локатора невозможен, так как заголовок не должен зависит от контента.
    # Иных уникальных атрибутов ближе к заголовку нет.
    FIRST_CASE_TITLE = (By.XPATH, '//div[@data-test-id="main-page-vkads"]/div[2]/div/div[1]/div/div/a/div[2]')
    ALL_CASES = (By.XPATH, '//div[@data-test-id="main-page-vkads"]/div[2]/a')

    WEBINARS_HEADER = (By.XPATH, '//div[@data-test-id="main-page-vkads"]/div[3]/a/div/div')
    WEBINARS_DETAILS_BUTTON = (By.XPATH, '//button[contains(@class, "GetStarted_button")]')

    NEWS_HEADER = (By.XPATH, '//div[contains(@class, "News_title")]')
    NEWS_DETAILS_BUTTON = (By.XPATH, '//button[contains(@class, "News_button")]')

    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//button[@data-test-id="cookie-banner-button-vkads"]')
