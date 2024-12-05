from base import BaseCase
from ui.locators.intermediate_locators import IntermediateLocators


class TestMain(BaseCase):
    authorize = False
    locators = IntermediateLocators
    
    def test_main_page_state(self):
        cases, webinars = self.main_page.main_page_state()

        cases_title = 'Кейсы компаний'
        assert cases.text == cases_title, f'Expected cases title to be {cases_title}, but got {cases.text}'

        webinars_title = 'Обучающие вебинары'
        assert webinars.text == webinars_title, f'Expected webinars title to be {webinars_title}, but got {webinars.text}'


    def test_carousel_first_section(self):
        self.main_page.carousel_first_section()

        url = 'https://ads.vk.com/promo/firstbonus'
        self.wait_url_loading(url)
        assert url in self.driver.current_url, f'Expected URL to be {url}, but got {self.driver.current_url}'

        header = self.main_page.find(self.locators.PROMO_FIRSTBONUS_HEADER, timeout=10)
        
        header_title = 'Прибавляем 10 000₽ к бюджету'
        assert header.text == header_title, f'Expected webinars title to be {header_title}, but got {header.text}'

    def test_carousel_second_section(self):
        self.main_page.carousel_second_section()

        url = 'https://id.vk.com/auth'
        self.wait_url_loading(url)
        assert url in self.driver.current_url, f'Expected URL to be {url}, but got {self.driver.current_url}'
    

    def test_carousel_third_section(self):
        self.main_page.carousel_third_section()

        url = 'https://adblogger.vk.com/for-advertisers'
        self.wait_url_loading(url)
        assert url in self.driver.current_url, f'Expected URL to be {url}, but got {self.driver.current_url}'

    
    def test_choose_case(self):
        case_text = self.main_page.choose_case()

        url = 'https://ads.vk.com/cases'
        self.wait_url_loading(url)
        assert url in self.driver.current_url, f'Expected URL to be {url}, but got {self.driver.current_url}'

        header = self.main_page.find(self.locators.SINGLE_HEADER, timeout=10)
        
        assert header.text == case_text, f'Expected case title to be {case_text}, but got {header.text}'

    
    def test_show_all_cases(self):
        self.main_page.show_all_cases()

        url = 'https://ads.vk.com/cases'
        self.wait_url_loading(url)
        assert url in self.driver.current_url, f'Expected URL to be {url}, but got {self.driver.current_url}'

        header = self.main_page.find(self.locators.All_HEADER, timeout=10)

        cases_title = 'Кейсы'
        assert header.text == cases_title, f'Expected cases title to be {cases_title}, but got {header.text}'


    def test_show_all_webinars(self):
        self.main_page.show_all_webinars()

        url = 'https://ads.vk.com/events'
        self.wait_url_loading(url)
        assert url in self.driver.current_url, f'Expected URL to be {url}, but got {self.driver.current_url}'

        header = self.main_page.find(self.locators.All_HEADER, timeout=10)
        
        events_title = 'Мероприятия'
        assert header.text == events_title, f'Expected events title to be {events_title}, but got {header.text}'


    def test_choose_news(self):
        news_text = self.main_page.choose_news()

        url = 'https://ads.vk.com/news'
        self.wait_url_loading(url)
        assert url in self.driver.current_url, f'Expected URL to be {url}, but got {self.driver.current_url}'

        header = self.main_page.find(self.locators.SINGLE_HEADER, timeout=10)
        
        assert header.text == news_text, f'Expected news title to be {news_text}, but got {header.text}'
