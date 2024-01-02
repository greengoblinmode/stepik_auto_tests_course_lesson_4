from selenium.webdriver.common.by import By


class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    USER_ICON = (By.CLASS_NAME, "icon-user")


class BasketPageLocators():

    BASKET_BUTTON = (By.XPATH, "//*[@class='btn btn-default' and text()='View basket']")

    BASKET_STATUS = (By.ID, "content_inner")


class LoginPageLocators():

    LOGIN_FORM = (By.ID, "login_form")

    REGISTER_FORM = (By.ID, "register_form")

    LOGIN_EMAIL_INPUT = (By.ID, "id_login-username")

    LOGIN_PASS_INPUT = (By.ID, "id_login-password")

    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")

    REGISTER_PASS_INPUT = (By.ID, "id_registration-password1")

    REGISTER_CONFIRM_PASS_INPUT = (By.ID, "id_registration-password2")

    REGISTER_BUTTON = (By.XPATH, "//button[text()='Register']")


class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():

    ADD_PRODUCT_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")

    SUPPLY_NAME = [By.XPATH, "//div[@class='col-sm-6 product_main']//h1"]

    SUPPLY_PRICE = [By.XPATH, "//div[@class='col-sm-6 product_main']//p[@class='price_color']"]

    ADD_NOTIFY = [By.XPATH, "(//div[@class='alert alert-safe alert-noicon alert-success  fade in']//div[@class='alertinner '])[1]"]

    BASKET_TOTAL_NOTIFY = [By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//div[@class='alertinner ']//p[1]"]