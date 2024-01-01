from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_basket(self, check):
        BASKET_STAT_LOCATOR = self.browser.find_element(*BasketPageLocators.BASKET_STATUS)
        status = BASKET_STAT_LOCATOR.text
        assert check == status, f"Текст уведомления не совпадает, актуальный текст: {status}"