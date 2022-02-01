from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_good_to_basket(self):
        self.should_be_add_button()
        self.push_add_button()
        self.solve_quiz_and_get_code()
        self.title_message_correct()
        self.price_message_correct()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), 'There is no login button'

    def push_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def title_message_correct(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        add_book_message = self.browser.find_element(*ProductPageLocators.ADD_BOOK_MESSAGE).text
        assert book_title == add_book_message, 'The title is wrong'

    def price_message_correct(self):
        price_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        actual_price = self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE).text
        assert price_message == actual_price, 'The price is wrong'

