import pytest

from base import BaseCase
from ui.pages.site_page import SitePage


class TestSite(BaseCase):
    authorize = True

    @pytest.fixture
    def site_page(self):
        self.personal_page = self.login_page.change_personal_page()

        self.get_site_page()

        return SitePage(self.driver)
    

    def get_site_page(self):
        self.personal_page.click(self.personal_page.locators.SITE_BUTTON, timeout=10)

        self.wait_url_loading('https://ads.vk.com/hq/pixels')
    

    def delete_pixel(self, site_page):
        site_page.delete_pixel()
        site_page.empty_page()


    def test_empty_page(self, site_page):
        title = site_page.empty_page()

        empty_page_title = 'Нет привязанных пикселей трекинга'
        assert title.text == empty_page_title, f'Expected empty page title to be {empty_page_title}, but got {title.text}'
    

    def test_add_pixel_sucess(self, site_page):
        title = site_page.add_valid_pixel()
        created_id = title.text.split()[-1]

        site_page.close_confirm_dialog()

        current_id = site_page.get_pixel_id().text

        assert created_id == current_id, f'Expected created id to be {created_id}, but got {current_id}'

        self.delete_pixel(site_page)


    def test_add_pixel_failed(self, site_page):
        site_page.add_unvalid_pixel()
        error = site_page.get_domen_input_error()

        error_message = 'Введите корректный адрес сайта (вида: example.ru)'
        assert error.text == error_message, f'Expected error message to be {error_message}, but got {error.text}'


    def test_get_setting(self, site_page):
        title = site_page.add_valid_pixel()
        created_id = title.text.split()[-1]

        site_page.close_confirm_dialog()
        site_page.get_pixel_id()
        site_page.get_settings()

        url = f'https://ads.vk.com/hq/pixels/{created_id}/events'
        self.wait_url_loading(url)
        assert url in self.driver.current_url, f'Expected URL to be {url}, but got {self.driver.current_url}'

        self.get_site_page()
        self.delete_pixel(site_page)

    
    def test_get_tags(self, site_page):
        title = site_page.add_valid_pixel()
        created_id = title.text.split()[-1]

        site_page.close_confirm_dialog()
        site_page.get_pixel_id()
        site_page.get_settings()
        self.wait_url_loading('events')
        site_page.get_tags()

        url = f'https://ads.vk.com/hq/pixels/{created_id}/tags'
        self.wait_url_loading(url)
        assert url in self.driver.current_url, f'Expected URL to be {url}, but got {self.driver.current_url}'

        self.get_site_page()
        self.delete_pixel(site_page)
