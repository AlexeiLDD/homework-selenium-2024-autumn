from datetime import date

from selenium.webdriver.support.wait import WebDriverWait

from base import BaseCase

from ui.pages.campaigns_page import CampaignsPage, CampaignSettings

campaigns_url = 'https://ads.vk.com/hq/dashboard/ad_plans'


class TestCampaigns(BaseCase):
    authorize = True

    def open_campaigns(self):
        self.campaigns_page = CampaignsPage(self.driver)

        self.campaigns_page.open_campaigns()


    def test_open_campaigns(self):
        self.open_campaigns()

        title = self.campaigns_page.get_campaigns()

        assert campaigns_url in self.driver.current_url
        assert title.text == 'Создайте первую рекламную кампанию'

    
    def create_campaign(self):
        self.open_campaigns()

        self.settings_page = CampaignSettings(self.driver)

        self.settings_page.create_campaign()


    def test_find_campaign_info(self):
        self.create_campaign()

        info = self.settings_page.find_campaign_info()

        title = f'Кампания {date.today()}'

        assert info['budget'] == '0 ₽'
        assert info['title'] == title


    def test_change_campaign_title(self):
        self.create_campaign()

        new_title = 'Test'

        title = self.settings_page.change_campaign_title(new_title)

        assert title == new_title


    def test_incorrect_domain_site_action(self):
        self.create_campaign()

        err = self.settings_page.change_domain_site_action('фывфвы')

        assert err == 'Неверный формат URL'


    def test_correct_domain_site_action(self):
        self.create_campaign()

        err = self.settings_page.change_domain_site_action('vk.com')
        exists = self.settings_page.check_inputs_site_action()

        assert err is None
        assert exists


    def test_correct_list_catalog_action(self):
        self.create_campaign()

        exists = self.settings_page.check_inputs_catalog_action()

        assert exists


    def test_polls_leadads_action(self):
        self.create_campaign()

        exists = self.settings_page.check_polls_leadads_action()

        assert exists


    def test_leadform_leadads_action(self):
        self.create_campaign()

        exists = self.settings_page.check_leadform_leadads_action()

        assert exists


    def test_default_price_banner_branding(self):
        self.create_campaign()

        price = self.settings_page.check_default_price_banner_branding()

        assert price == '70 ₽'


    def test_default_price_video_branding(self):
        self.create_campaign()

        price = self.settings_page.check_default_price_video_branding()

        assert price == '100 ₽'


    def test_default_price_html_branding(self):
        self.create_campaign()

        price = self.settings_page.check_default_price_html_branding()

        assert price == '50 ₽'


    def test_default_price_premium_branding(self):
        self.create_campaign()

        price = self.settings_page.check_default_price_premium_branding()

        assert price == '380 ₽'


    def switch_to_adverts_groups(self):
        self.create_campaign()
        self.settings_page.switch_to_adverts_groups()


    def test_adverts_groups_containers(self):
        self.switch_to_adverts_groups()

        WebDriverWait(self.driver, 10).until(lambda d: 'ad_group/new-ad-group' in d.current_url)

        exists = self.settings_page.check_adverts_groups_containers()

        assert exists


    def test_audience_changes(self):
        self.switch_to_adverts_groups()

        url = 'ad_group/new-ad-group'
        self.wait_url_loading(url)

        audience = self.settings_page.change_audience()

        assert audience['old'] != audience['new']


    def switch_to_adverts(self):
        self.switch_to_adverts_groups()
        self.settings_page.switch_to_adverts()


    def test_advert_title(self):
        self.switch_to_adverts()

        url = 'ad/new-ad-form'
        self.wait_url_loading(url)

        title = self.settings_page.check_advert_title()
        
        assert 'Объявление' in title


    def test_publish_btn(self):
        self.switch_to_adverts()

        url = 'ad/new-ad-form'
        self.wait_url_loading(url)

        exists = self.settings_page.check_publish_btn()

        assert exists
