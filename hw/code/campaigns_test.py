from datetime import date
import pytest

from base import BaseCase

from ui.pages.campaigns_page import CampaignsPage, CampaignSettings

campaigns_url = 'https://ads.vk.com/hq/dashboard/ad_plans'


class TestCampaignsPage(BaseCase):
    authorize = True

    def open_campaigns(self):
        self.campaigns_page = CampaignsPage(self.driver)

        self.campaigns_page.open_campaigns()

    @pytest.mark.skip('skip')
    def test_open_campaigns(self):
        self.open_campaigns()

        title = self.campaigns_page.get_campaigns()

        assert campaigns_url in self.driver.current_url
        assert title.text == 'Создайте первую рекламную кампанию'

    
    def create_campaign(self):
        self.open_campaigns()

        self.settings_page = CampaignSettings(self.driver)

        self.settings_page.create_campaign()

    @pytest.mark.skip('skip')
    def test_find_campaign_info(self):
        self.create_campaign()

        info = self.settings_page.find_campaign_info()

        title = f'Кампания {date.today()}'

        assert info['budget'] == '0 ₽'
        assert info['title'] == title

    @pytest.mark.skip('skip')
    def test_change_campaign_title(self):
        self.create_campaign()

        new_title = 'Test'

        title = self.settings_page.change_campaign_title(new_title)

        assert title == new_title

    @pytest.mark.skip('skip')
    def test_incorrect_domain_site_action(self):
        self.create_campaign()

        err = self.settings_page.change_domain_site_action('фывфвы')

        assert err == 'Неверный формат URL'

    @pytest.mark.skip('skip')
    def test_correct_domain_site_action(self):
        self.create_campaign()

        err = self.settings_page.change_domain_site_action('vk.com')
        exists = self.settings_page.check_inputs_site_action()

        assert err is None
        assert exists

    @pytest.mark.skip('skip')
    def test_correct_list_catalog_action(self):
        self.create_campaign()

        exists = self.settings_page.check_inputs_catalog_action()

        assert exists

    @pytest.mark.skip('skip') # TODO
    def test_polls_leadads_action(self):
        self.create_campaign()

        exists = self.settings_page.check_polls_leadads_action()

        assert exists

    @pytest.mark.skip('skip') # TODO
    def test_leadform_leadads_action(self):
        self.create_campaign()

        exists = self.settings_page.check_leadform_leadads_action()

        assert exists

    @pytest.mark.skip('skip')
    def test_default_price_banner_branding(self):
        self.create_campaign()

        price = self.settings_page.check_default_price_banner_branding()

        assert price == '70 ₽'

    @pytest.mark.skip('skip')
    def test_default_price_video_branding(self):
        self.create_campaign()

        price = self.settings_page.check_default_price_video_branding()

        assert price == '100 ₽'

    @pytest.mark.skip('skip')
    def test_default_price_html_branding(self):
        self.create_campaign()

        price = self.settings_page.check_default_price_html_branding()

        assert price == '50 ₽'

    @pytest.mark.skip('skip')
    def test_default_price_premium_branding(self):
        self.create_campaign()

        price = self.settings_page.check_default_price_premium_branding()

        assert price == '380 ₽'

    @pytest.mark.skip('skip')
    def switch_to_adverts_groups(self):
        self.create_campaign()
        self.settings_page.switch_to_adverts_groups()

    @pytest.mark.skip('skip')
    def test_adverts_groups_containers(self):
        self.switch_to_adverts_groups()

        exists = self.settings_page.check_adverts_groups_containers()

        assert exists

    @pytest.mark.skip('skip')
    def test_audience_changes(self):
        self.switch_to_adverts_groups()

        audience = self.settings_page

        assert audience['old'] != audience['new']

    @pytest.mark.skip('skip')
    def switch_to_adverts(self):
        self.switch_to_adverts_groups()
        self.settings_page.switch_to_adverts()

    @pytest.mark.skip('skip')
    def test_advert_title(self):
        title = self.settings_page.check_advert_title()

        assert 'Объявление' in title

    @pytest.mark.skip('skip')
    def test_publish_btn(self):
        exists = self.settings_page.check_publish_btn()

        assert exists
