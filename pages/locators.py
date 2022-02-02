from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.XPATH, '//a[text()="View basket"]')


class BasketPageLocators:
    EMTPY_BSK_MSG = (By.CSS_SELECTOR, '#content_inner p')
    CHECKOUT_BUTTON = (By.XPATH, "//a[text()='Proceed to checkout']")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_PRICE = (By.CSS_SELECTOR, '#content_inner article div:nth-child(2) p')
    ACTUAL_PRICE = (By.CSS_SELECTOR, '#messages div:nth-child(3) div strong')
    ADD_BOOK_MESSAGE = (By.CSS_SELECTOR, '#messages div div strong')
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div div')

