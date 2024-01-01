from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        add_button.click()
    

    def check_add_notify(self, noti):
        NOTIFY_LOCATOR = self.browser.find_element(*ProductPageLocators.ADD_NOTIFY)
        add_noti = NOTIFY_LOCATOR.text
        assert noti == add_noti, f"Текст уведомления не совпадает, актуальный текст: {add_noti}"

    
    def check_basket_total(self, sum):
        BASKET_LOCATOR = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        basket_sum = BASKET_LOCATOR.text
        assert sum == basket_sum, f"Сумма в корзине изменилась, актуальная сумма: {basket_sum}"