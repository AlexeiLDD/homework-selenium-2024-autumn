from base import BaseCase
from ui.locators.intermediate_locators import IntermediateLocators


class TestMain(BaseCase):
    authorize = False
    locators = IntermediateLocators
    
    def test_main_page_state(self):
        cases, webinars = self.main_page.main_page_state()

        assert cases.text == 'Кейсы компаний'
        assert webinars.text == 'Обучающие вебинары'


    def test_carousel_first_section(self):
        self.main_page.carousel_first_section()

        url = 'https://ads.vk.com/promo/firstbonus'
        self.wait_url_loading(url)
        assert url in self.driver.current_url

        header = self.main_page.find(self.locators.PROMO_FIRSTBONUS_HEADER, timeout=10)
        
        assert header.text == 'Прибавляем 10 000₽ к бюджету'
    

    def test_carousel_second_section(self):
        self.main_page.carousel_second_section()

        url = 'https://id.vk.com/auth'
        self.wait_url_loading(url)
        assert url in self.driver.current_url
    

    def test_carousel_third_section(self):
        self.main_page.carousel_third_section()

        url = 'https://adblogger.vk.com/for-advertisers'
        self.wait_url_loading(url)
        assert url in self.driver.current_url

    
    def test_choose_case(self):
        case_text = self.main_page.choose_case()

        url = 'https://ads.vk.com/cases'
        self.wait_url_loading(url)
        assert url in self.driver.current_url

        header = self.main_page.find(self.locators.SINGLE_HEADER, timeout=10)
        
        assert header.text == case_text

    
    def test_show_all_cases(self):
        self.main_page.show_all_cases()

        url = 'https://ads.vk.com/cases'
        self.wait_url_loading(url)
        assert url in self.driver.current_url

        header = self.main_page.find(self.locators.All_HEADER, timeout=10)
        
        assert header.text == 'Кейсы'


    def test_show_all_webinars(self):
        self.main_page.show_all_webinars()

        url = 'https://ads.vk.com/events'
        self.wait_url_loading(url)
        assert url in self.driver.current_url

        header = self.main_page.find(self.locators.All_HEADER, timeout=10)
        
        assert header.text == 'Мероприятия'


    def test_choose_news(self):
        news_text = self.main_page.choose_news()

        url = 'https://ads.vk.com/news'
        self.wait_url_loading(url)
        assert url in self.driver.current_url

        header = self.main_page.find(self.locators.SINGLE_HEADER, timeout=10)
        
        assert header.text == news_text
