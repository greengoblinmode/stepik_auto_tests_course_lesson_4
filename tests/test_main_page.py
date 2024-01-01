import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    login_page = LoginPage(browser, url)
    main_page.open()                      # открываем страницу
    main_page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    main_page.should_be_login_link()
    time.sleep(2)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, url)
    basket_page = BasketPage(browser, url)
    main_page.open()
    main_page.go_to_basket()
    basket_page.check_basket("Your basket is empty. Continue shopping")