from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_checkout_button()
        self.should_be_empty_basket_message()

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMTPY_BSK_MSG), "Empty basket message isn't presented"

    def should_not_be_checkout_button(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), "Basket isn't empty"

