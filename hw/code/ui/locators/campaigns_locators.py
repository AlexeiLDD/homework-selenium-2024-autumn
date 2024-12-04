from selenium.webdriver.common.by import By


class CampaignsLocators:
    CAMPAIGN_LEFT_PANEL_BTN = (By.XPATH, '//*[@data-route="dashboardV2"]')
    CREATE_CAMPAIGN_TITLE = (By.TAG_NAME, 'h2')
    DIALOG_CLOSE_BTN = (By.XPATH, '//div[@aria-label="Закрыть"]')


class CampaignSettingsLocators:
    CREATE_CAMPAIGN_BTN = (By.XPATH, '//button[@data-testid="create-button"]')
    LEFT_SIDE_CAMPAIGN_TITLE = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[1]/div/div['
                                          '1]/div/section/div/div/div[1]/div[1]/div[1]/div/div[2]/div/span')
    CAMPAIGN_BUDGET = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[1]/div/div[1]/div/section/div/div/div['
                                 '2]/div/div/div/div/h4')
    DIALOG_CLOSE_BTN = (By.XPATH, '//*[@id="_modal_28"]/div/div/div[2]/div[1]/div/div/div/div/button')
    

    CAMPAIGN_TITLE = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div/section/div/div/div[1]/div')
    TITLE_INPUT = (By.TAG_NAME, 'textarea')

    CONTINUE_BTN = (By.XPATH, '//*[@id="footer"]/div/div/div[2]/div[2]/button')


class CampaignActionsLocators:
    DOMAIN_INPUT_SITE_ACTION = (By.TAG_NAME, 'input')
    DOMAIN_INPUT_ERR = (By.XPATH, '//*[@role="alert"]')
    BUDGET_INPUT_SITE_ACTION = (By.XPATH, '//input[@data-testid="targeting-not-set"]')

    SITE_ACTION_BTN = (By.XPATH, '//div[@data-id="site_conversions"]')
    CATALOG_ACTION_BTN = (By.XPATH, '//div[@data-id="ecomm"]')
    LEADADS_ACTION_BTN = (By.XPATH, '//div[@data-id="leadads"]')

    FEATURES_INPUT_SITE_ACTION = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div/section[2]/form/div[3]/div/span/textarea')
    ACTION_INPUT_SITE_ACTION = (By.XPATH, '//input[@role="combobox"]')
    OPTIMIZATION_SWITCH_SITE_ACTION = (By.XPATH, '//input[@data-testid="budget-optimization"]')
    DATES_INPUTS_SITE_ACTION = (By.XPATH, '//*[@data-name="dates"]')

    OBJECT_RADIOBTN_CATALOG_ACTION = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div/section[2]/form/div['
                                                '1]/div')
    DOMAIN_INPUT_CATALOG_ACTION = (By.XPATH, '//input[@placeholder="Введите ссылку на сайт"]')
    GOODS_INPUT_CATALOG_ACTION = (By.XPATH, '//input[@role="combobox"]')

    POLL_RADIOBTN = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div/section[2]/form/div[1]/div/label[2]/div')
    LEADFORM_SELECT_LEADADS_ACTION = (By.XPATH, '//input[@data-testid="lead-form-select"]')
    SPLIT_TEST_SWITCH_LEADADS_ACTION = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div/section[2]/form/div[2]/div/div[2]/label')
    TYPE_COMBOBOX_LEADADAS_ACTION = (By.XPATH, '//input[@role="combobox"]')


class CampaignBrandingLocators:
    BRANDING_TAB_BTN = (By.XPATH, '//*[@id="tab_branding"]')

    BANNER_BRANDING_BTN = (By.XPATH, '//div[@data-id="branding_multi"]')
    VIDEO_BRANDING_BTN = (By.XPATH, '//div[@data-id="branding_video"]')
    HTML_BRANDING_BTN = (By.XPATH, '//div[@data-id="branding_html5"]')
    PREMIUM_BRANDING_BTN = (By.XPATH, '//div[@data-id="branding_premium"]')

    DOMAIN_INPUT = (By.XPATH, '//input[@placeholder="Введите ссылку на сайт"]')
    PRICE_INPUT = (By.XPATH, '//input[@data-testid="fix-price"]')


class AdvertsGroupsLocators:
    REGION_BTN = (By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/main/div[2]/div/div/div/div/div/div[1]/section[2]/div[2]/fieldset/div/div/div[1]/div[2]/button[2]')
    AUDIENCE_VALUE = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[2]/section/div/div/div/div/div/div['
                                '3]/div[2]/div[2]')
    CONTINUE_BTN = (By.XPATH, '//*[@id="footer"]/div/div/div[2]/div[2]/button')

    NAME_CONTAINER = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/section')
    BETS_CONTAINER = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[1]/section[1]')
    REGIONS_CONTAINER = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[1]/section[2]')
    AUDIENCE_EXPANDING_CONTAINER = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[1]/section[3]')
    DEMOGRAPHIC_CONTAINER = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[1]/div/section[1]')
    BEHAVIOR_CONTAINER = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[1]/div/section[2]')
    AUDIENCE_CONTAINER = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[1]/div/section[3]')
    DEVICES_CONTAINER = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[1]/div/section[4]')
    URL_PARAMS_CONTAINER = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[1]/div/section[5]')
    PLACES_CONTAINER = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[1]/div/section[6]')


class AdvertsLocators:
    ADVERT_TITLE = (By.TAG_NAME, 'h2')
    PUBLISH_BTN = (By.XPATH, '//*[@id="footer"]/div/div/div[2]/div[2]/button/span')
