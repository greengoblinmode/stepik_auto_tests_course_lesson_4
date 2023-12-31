from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")

    REGISTER_FORM = (By.ID, "register_form")

    LOGIN_EMAIL_INPUT = (By.ID, "id_login-username")

    LOGIN_PASS_INPUT = (By.ID, "id_login-password")

    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")

    REGISTER_PASS_INPUT = (By.ID, "id_registration-password1")

    REGISTER_CONFIRM_PASS_INPUT = (By.ID, "id_registration-password2")


class ProductPageLocators():
    ADD_PRODUCT_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")