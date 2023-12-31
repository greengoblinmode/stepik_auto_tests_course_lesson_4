import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    login_page = LoginPage(browser, url)
    main_page.open()                      # открываем страницу
    main_page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    main_page.should_be_login_link()
    time.sleep(2)
    login_page.should_be_login_page()