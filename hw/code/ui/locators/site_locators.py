from selenium.webdriver.common.by import By


class SiteLocators:
    PLACEHOLDER_EMPTY_LOCATOR = (By.XPATH, '//*[@id="pixels"]/div/div/h2')
    ADD_PIXEL_BUTTON = (By.XPATH, '//div[@class="vkuiPlaceholder__action"]/button')

    CHOOSE_DOMEN_BUTTON = (By.XPATH, '//input[@value="domain"]')
    DOMEN_INPUT = (By.XPATH, '//div[@name="domain"]/span/input')
    SUBMIT_ADD_PIXEL_BUTTON = (By.XPATH, 'div[@role="group"]/button')

    ADD_NEW_PIXEL_BUTTON = (By.XPATH, '//div[contains(@class, "FlowSelectStep_cellsWrap")]/div[2]')
    CONFIRM_HEADER = (By.XPATH, '//h2[contains(@class, "vkuiInternalModalCardBase__header")]')
    CLOSE_DIALOG_BUTTON = (By.XPATH, '//div[contains(@class, "vkuiModalDismissButton")]')

    CURRENT_ID = (By.XPATH, '//div[@class="BaseTable__row PixelsList__row"]/div[2]/div')
    KEBAB_MENU = (By.XPATH, '//div[@class="BaseTable__row PixelsList__row"]/div[5]/div/button')
    DELETE_BUTTON = (By.XPATH, '//div[contains(@class, "ContextMenu_dropdown")/label[2]')
    SUBMIT_DELETE_BUTTON = (By.XPATH, '//div[@class="vkuiModalCardBase__actions"]/div/button[2]')

    SETTINGS_BUTTON = (By.XPATH, '//a[@data-route="pixels.events"]')
    TAGS_SECTION = (By.ID, 'tab_pixels.audience_tags')

    INPUT_ERROR = (By.XPATH, '//span[@role="alert"]')
    
