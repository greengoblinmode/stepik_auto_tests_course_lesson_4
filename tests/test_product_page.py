import time
import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    url = link
    main_page = MainPage(browser, url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page = ProductPage(browser, url)
    main_page.open()                      # открываем страницу
    time.sleep(2)
    supply_name = product_page.get_supply_name()
    supply_price = product_page.get_supply_price()
    product_page.add_product()
    time.sleep(2)
    main_page.solve_quiz_and_get_code()
    time.sleep(2)
    product_page.check_add_notify(f"{supply_name} has been added to your basket.")
    product_page.check_basket_total(f"Your basket total is now {supply_price}")


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    main_page = MainPage(browser, url)
    basket_page = BasketPage(browser, url)
    main_page.open()
    main_page.go_to_basket()
    basket_page.check_basket("Your basket is empty. Continue shopping")


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        self.login_page = LoginPage(browser, url)
        self.login_page.open()   
        self.login_page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        self.login_page.register_new_user(email, "zxc_36hF8_ojn")
        time.sleep(10)
        self.login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.product_page = ProductPage(browser, url)
        self.product_page.open()
        self.product_page.should_not_be_success_message()


    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.product_page = ProductPage(browser, url)
        self.product_page.open()
        supply_name = self.product_page.get_supply_name()
        supply_price = self.product_page.get_supply_price()
        self.product_page.add_product()
        self.product_page.check_add_notify(f"{supply_name} has been added to your basket.")
        self.product_page.check_basket_total(f"Your basket total is now {supply_price}")