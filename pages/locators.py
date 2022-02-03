from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_link')
    BASKET_LINK = (By.CSS_SELECTOR, 'header div div div.basket-mini.pull-right.hidden-xs span a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    EMTPY_BSK_MSG = (By.CSS_SELECTOR, '#content_inner p')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#content_inner div.form-group.clearfix div div a')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    PASSWORD = (By.ID, 'id_registration-password1')
    PASSWORD_CONFIRMATION = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.XPATH, "//button[@value='Register']")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_PRICE = (By.CSS_SELECTOR, '#content_inner article div:nth-child(2) p')
    ACTUAL_PRICE = (By.CSS_SELECTOR, '#messages div:nth-child(3) div strong')
    ADD_BOOK_MESSAGE = (By.CSS_SELECTOR, '#messages div div strong')
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div div')

