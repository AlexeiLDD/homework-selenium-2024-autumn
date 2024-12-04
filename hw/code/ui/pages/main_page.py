from ui.pages.base_page import BasePage
from ui.locators.main_locators import MainLocators


class MainPage(BasePage):

    locators = MainLocators
    url = 'https://ads.vk.com/'

    def pass_func(self):
        pass

    def accept_cookies(self):
        self.click(self.locators.ACCEPT_COOKIES_BUTTON, timeout=10)

    def setup(self):
        self.driver.maximize_window()
        self.accept_cookies()

    def main_page_state(self):
        self.setup()

        self.find(self.locators.CAROUSEL, timeout=10)
        cases = self.find(self.locators.COMPANY_CASE_HEADER, timeout=10)
        webinars = self.find(self.locators.WEBINARS_HEADER, timeout=10)
        self.find(self.locators.NEWS_HEADER, timeout=10)

        return cases, webinars

    def carousel_first_section(self):
        self.setup()

        self.click(self.locators.FIRST_BULLET, timeout=10)
        self.click(self.locators.GET_BONUSES_BUTTON, timeout=10)
    
    def carousel_second_section(self):
        self.setup()

        self.click(self.locators.SECOND_BULLET, timeout=10)
        self.click(self.locators.START_ADS_BUTTON, timeout=10)

    def carousel_third_section(self):
        self.setup()

        self.click(self.locators.THIRD_BULLET, timeout=10)
        self.click(self.locators.MORE_DETAILS_BUTTON, timeout=10)
    
    def choose_case(self):
        self.setup()

        case = self.find(self.locators.FIRST_CASE_TITLE, timeout=10)
        self.scroll_into_element(case)
        self.click(self.locators.FIRST_CASE_TITLE, timeout=10)

        return case.text
    
    def show_all_cases(self):
        self.setup()

        all_cases = self.find(self.locators.ALL_CASES, timeout=10)
        self.scroll_into_element(all_cases)
        self.click(self.locators.ALL_CASES, timeout=10)

    def show_all_webinars(self):
        self.setup()

        all_webinars = self.find(self.locators.WEBINARS_DETAILS_BUTTON, timeout=10)
        self.scroll_into_element(all_webinars)
        self.click(self.locators.WEBINARS_DETAILS_BUTTON, timeout=10)

    def choose_news(self):
        self.setup()

        news = self.find(self.locators.NEWS_HEADER, timeout=10)
        self.scroll_into_element(news)
        self.click(self.locators.NEWS_DETAILS_BUTTON, timeout=10)

        return news.text
