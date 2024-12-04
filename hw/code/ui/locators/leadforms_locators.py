from selenium.webdriver.common.by import By

class LeadFormsLocators:
    LEADFORMS_TAB_BUTTON = (By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section[2]/div/a[4]")
    NO_LEADFORMS_LABEL = (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/main/div[2]/div/div/div[2]/section/div/div/div/div/div/div[2]/div[2]/div/div/div/div/h2")

    CREATE_LEAD_FORM_BUTTON= (By.XPATH, '//*[@id="leadads.leadforms"]/div/div[2]/div/div[2]/div/button')

    NEW_LEAD_FORM_HEADER_LABEL= (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[1]/h2")

    MORE_TEXT_BUTTON_INACTIVE= (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[4]/div/div/div/label[2]")
    SHORT_FORM_DESCRIPTION_HEADER_LABEL = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[8]/div/h5")

    LONG_FORM_DESCRIPTION_HEADER_LABEL= (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[8]/h5")
    LEAD_MAGNIT_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[4]/div/div/div/label[3]")

    DISCOUNT_CHECKBOX = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[8]/div/label[1]")
    BONUS_CHECKBOX = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[8]/div/label[2]")

    SIZE_OF_DISCOUNT_HEADER_LABEL = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[9]/h5")
    BONUS_DESCRIPTION_HEADER_LABEL = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[9]/h5")

    UPLOAD_IMAGE_PLUS_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[5]/div/div/div[1]/div")
    MEDIA_LIBRARY_MENU_HEADER_LABEL = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div[1]/h2")
    CLOSE_MEDIA_LIBRARY_MENU_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div[1]/h2")
    CLICKABLE_IMAGE = (By.XPATH, "//*[@id='media-library-image']/div/div")

    COMPANY_NAME_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[6]/div/span[1]/input")
    TITLE_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[7]/div/span[1]/input")
    BONUS_DESCRIPTION_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[9]/span[1]/input")

    FIRST_STEP_CONTINUE_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/button[2]")
    REQUIRED_FIELD_LABEL = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[9]/span[2]/div")

    ADD_QUESTION_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[1]/button")
    QUESTION_NUMBER_ONE_ITEM_LABEL= (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[1]/div[2]/div/div[1]/div[1]")

    QUESTION_TEXT_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[1]/div[2]/div/div[2]/span[1]/textarea")
    QUESTION_ANSWER_ONE = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/span/input")
    QUESTION_ANSWER_TWO = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div/span/input")

    SECOND_STEP_CONTINUE_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/button[2]")
    RESULT_HEADER_LABEL = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[1]/h4")

    THIRD_STEP_CONTINUE_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/button[2]")
    NOTIFICATIONS_HEADER_LABEL = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[1]/h4")

    FIO_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[6]/div[2]/span[1]/input")
    ADDRESS_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[6]/div[3]/span[1]/input")
    SAVE_BUTTON = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/button[2]")

    ACTIVE_LEADFORD_ITEM = (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/main/div[2]/div/div/div[2]/section/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div/div/div[4]")
