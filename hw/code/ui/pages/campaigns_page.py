import time

from selenium.webdriver import Keys
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from ui.pages.base_page import BasePage, PageNotOpenedException
from ui.locators.campaigns_locators import (CampaignsLocators, CampaignSettingsLocators, CampaignActionsLocators,
                                            CampaignBrandingLocators, AdvertsGroupsLocators, AdvertsLocators)


class CampaignsPage(BasePage):
    
    locators = CampaignsLocators
    url = 'https://ads.vk.com/hq/overview'

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url in self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def open_campaigns(self):
        self.click(self.locators.CAMPAIGN_LEFT_PANEL_BTN, timeout=5)

    def get_campaigns(self):
        title = self.find(self.locators.CREATE_CAMPAIGN_TITLE, timeout=5)

        return title


class CampaignSettings(BasePage):
    locators = CampaignSettingsLocators
    action_locators = CampaignActionsLocators
    branding_locators = CampaignBrandingLocators
    groups_locators = AdvertsGroupsLocators
    adverts_locators = AdvertsLocators
    url = 'https://ads.vk.com/hq/dashboard/ad_plan'

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url in self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def create_campaign(self):
        try:
            self.click(self.locators.CREATE_CAMPAIGN_BTN, timeout=5)
        except ElementClickInterceptedException:
            self.click(self.locators.DIALOG_CLOSE_BTN, timeout=5)
            self.click(self.locators.CREATE_CAMPAIGN_BTN, timeout=5)

    def find_campaign_info(self):
        title = self.find(self.locators.LEFT_SIDE_CAMPAIGN_TITLE, timeout=5).text
        budget = self.find(self.locators.CAMPAIGN_BUDGET, timeout=5).text

        return {'title': title, 'budget': budget}

    def change_campaign_title(self, new_title):
        self.click(self.locators.CAMPAIGN_TITLE, timeout=5)
        self.input(self.locators.TITLE_INPUT, new_title, timeout=5)
        self.input(self.locators.TITLE_INPUT, Keys.ENTER, timeout=5)

        title = self.find(self.locators.LEFT_SIDE_CAMPAIGN_TITLE, timeout=5).text

        return title

    def change_domain_site_action(self, domain):
        self.click(self.action_locators.SITE_ACTION_BTN, timeout=5)

        self.input(self.action_locators.DOMAIN_INPUT_SITE_ACTION, domain, timeout=5)
        self.input(self.action_locators.DOMAIN_INPUT_SITE_ACTION, Keys.ENTER, timeout=5)

        try:
            err = self.find(self.action_locators.DOMAIN_INPUT_ERR, timeout=5).text
        except TimeoutException:
            err = None

        return err

    def check_inputs_site_action(self):
        try:
            self.find(self.action_locators.FEATURES_INPUT_SITE_ACTION, timeout=5)
            self.find(self.action_locators.ACTION_INPUT_SITE_ACTION, timeout=3)
            self.find(self.action_locators.OPTIMIZATION_SWITCH_SITE_ACTION, timeout=3)
            self.find(self.action_locators.DATES_INPUTS_SITE_ACTION, timeout=3)

            return True

        except TimeoutException:
            return False

    def check_inputs_catalog_action(self):
        self.click(self.action_locators.CATALOG_ACTION_BTN, timeout=5)

        try:
            self.find(self.action_locators.OBJECT_RADIOBTN_CATALOG_ACTION, timeout=3)
            self.find(self.action_locators.DOMAIN_INPUT_CATALOG_ACTION, timeout=3)
            self.find(self.action_locators.GOODS_INPUT_CATALOG_ACTION, timeout=3)

            return True

        except TimeoutException:
            return False

    def check_polls_leadads_action(self):
        self.click(self.action_locators.LEADADS_ACTION_BTN, timeout=5)
        self.click(self.action_locators.POLL_RADIOBTN, timeout=5)

        try:
            self.find(self.action_locators.TYPE_COMBOBOX_LEADADAS_ACTION, timeout=3)

            return True

        except TimeoutException:
            return False

    def check_leadform_leadads_action(self):
        self.click(self.action_locators.LEADADS_ACTION_BTN, timeout=5)
    
        try:
            self.find(self.action_locators.SPLIT_TEST_SWITCH_LEADADS_ACTION, timeout=5)
            self.find(self.action_locators.LEADFORM_SELECT_LEADADS_ACTION, timeout=3)

            return True

        except TimeoutException:
            return False

    def check_default_price_branding(self):
        self.input(self.branding_locators.DOMAIN_INPUT, 'vk.com', timeout=5)
        self.input(self.branding_locators.DOMAIN_INPUT, Keys.ENTER, timeout=5)

        price = self.find(self.branding_locators.PRICE_INPUT, timeout=5).get_property('value')

        return price

    def check_default_price_banner_branding(self):
        self.click(self.branding_locators.BRANDING_TAB_BTN, timeout=50)
        self.click(self.branding_locators.BANNER_BRANDING_BTN, timeout=5)

        return self.check_default_price_branding()

    def check_default_price_video_branding(self):
        self.click(self.branding_locators.BRANDING_TAB_BTN, timeout=5)
        self.click(self.branding_locators.VIDEO_BRANDING_BTN, timeout=5)

        return self.check_default_price_branding()

    def check_default_price_html_branding(self):
        self.click(self.branding_locators.BRANDING_TAB_BTN, timeout=5)
        self.click(self.branding_locators.HTML_BRANDING_BTN, timeout=5)

        return self.check_default_price_branding()

    def check_default_price_premium_branding(self):
        self.click(self.branding_locators.BRANDING_TAB_BTN, timeout=5)
        self.click(self.branding_locators.PREMIUM_BRANDING_BTN, timeout=5)

        price = self.find(self.branding_locators.PRICE_INPUT, timeout=5).get_property('value')

        return price

    def switch_to_adverts_groups(self):
        self.change_domain_site_action('vk.com')
        self.input(self.action_locators.BUDGET_INPUT_SITE_ACTION, 222, timeout=5)
        self.input(self.action_locators.BUDGET_INPUT_SITE_ACTION, Keys.ENTER, timeout=10)
        self.click(self.locators.CONTINUE_BTN, timeout=5)
        self.click(self.locators.CONTINUE_BTN, timeout=5)

    def check_adverts_groups_containers(self):
        try:
            self.find(self.groups_locators.NAME_CONTAINER, timeout=30)
            self.find(self.groups_locators.BETS_CONTAINER, timeout=3)
            self.find(self.groups_locators.REGIONS_CONTAINER, timeout=3)
            self.find(self.groups_locators.AUDIENCE_EXPANDING_CONTAINER, timeout=3)
            self.find(self.groups_locators.DEMOGRAPHIC_CONTAINER, timeout=3)
            self.find(self.groups_locators.BEHAVIOR_CONTAINER, timeout=3)
            self.find(self.groups_locators.AUDIENCE_CONTAINER, timeout=3)
            self.find(self.groups_locators.DEVICES_CONTAINER, timeout=3)
            self.find(self.groups_locators.URL_PARAMS_CONTAINER, timeout=3)
            self.find(self.groups_locators.PLACES_CONTAINER, timeout=3)

            return True

        except TimeoutException:
            return False

    def change_audience(self):
        old_audience = self.find(self.groups_locators.AUDIENCE_VALUE, timeout=5)

        self.click(self.groups_locators.REGION_BTN, timeout=10)

        new_audience = self.find(self.groups_locators.AUDIENCE_VALUE, timeout=5).text

        return {'old': old_audience, 'new': new_audience}

    def switch_to_adverts(self):
        self.click(self.groups_locators.REGION_BTN, timeout=10)
        self.click(self.groups_locators.CONTINUE_BTN, timeout=5)

    def check_advert_title(self):
        title = self.find(self.adverts_locators.ADVERT_TITLE, timeout=5).text

        return title

    def check_publish_btn(self):
        try:
            self.find(self.adverts_locators.PUBLISH_BTN, timeout=5)

            return True
        except TimeoutException:
            return False
