from selenium.webdriver.common.by import By


class MainLocators:
    FIRST_BULLET = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[4]/div[1]')
    SECOND_BULLET = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[4]/div[2]')
    THIRD_BULLET = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[4]/div[3]')

    CAROUSEL = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div')
    GET_BONUSES_BUTTON = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[1]/div[1]/a/button')
    START_ADS_BUTTON = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[2]/div[1]/a/button')
    MORE_DETAILS_BUTTON = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[3]/div[1]/a/button')

    COMPANY_CASE_HEADER = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[2]/h2')
    FIRST_CASE_TITLE = (By.XPATH, '/html/body/section/div[2]/div/div/div[2]/div/div[1]/div/div/a/div[2]')
    ALL_CASES = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[2]/a')

    WEBINARS_HEADER = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[3]/a/div[1]/div[1]')
    WEBINARS_DETAILS_BUTTON = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[3]/a/div[1]/button')

    NEWS_HEADER = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[4]/div/a/div/div[2]/div/div[2]')
    NEWS_DETAILS_BUTTON = (By.XPATH, '//*[@id="classic-layout"]/div[2]/div/div/div[4]/div/a/div/div[2]/button')

    ACCEPT_COOKIES_BUTTON = (By.XPATH, '/html/body/div/button')
