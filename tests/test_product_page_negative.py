import time
import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage


pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    main_page = MainPage(browser, url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page = ProductPage(browser, url)
    main_page.open()                      # открываем страницу
    time.sleep(2)
    product_page.add_product()
    time.sleep(2)
    main_page.solve_quiz_and_get_code()
    time.sleep(2)
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    main_page = MainPage(browser, url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page = ProductPage(browser, url)
    main_page.open()                      # открываем страницу
    time.sleep(2)
    product_page.should_not_be_success_message()


pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    main_page = MainPage(browser, url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page = ProductPage(browser, url)
    main_page.open()                      # открываем страницу
    time.sleep(2)
    product_page.add_product()
    time.sleep(2)
    main_page.solve_quiz_and_get_code()
    time.sleep(2)
    product_page.should_lost_success_message()