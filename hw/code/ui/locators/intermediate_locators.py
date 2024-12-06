from selenium.webdriver.common.by import By


class IntermediateLocators:
    PROMO_FIRSTBONUS_HEADER = (By.XPATH, '//h1[contains(@class, "OfferContent_title")]')

    HEADER = (By.XPATH,  '//h1[@data-test-id="summary-title-ads"]')
