from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        add_button.click()
    

    def get_supply_name(self):
        return self.browser.find_element(*ProductPageLocators.SUPPLY_NAME).text


    def get_supply_price(self):
        return self.browser.find_element(*ProductPageLocators.SUPPLY_PRICE).text
    

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_NOTIFY), \
       "Success message is presented, but should not be"


    def should_lost_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_NOTIFY), \
       "Success message is presented, but should not be"


    def check_add_notify(self, noti):
        NOTIFY_LOCATOR = self.browser.find_element(*ProductPageLocators.ADD_NOTIFY)
        add_noti = NOTIFY_LOCATOR.text
        assert noti == add_noti, f"Текст уведомления не совпадает, актуальный текст: {add_noti}"

    
    def check_basket_total(self, sum):
        BASKET_LOCATOR = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_NOTIFY)
        basket_sum = BASKET_LOCATOR.text
        assert sum == basket_sum, f"Сумма в корзине изменилась, актуальная сумма: {basket_sum}"