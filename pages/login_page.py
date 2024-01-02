from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "URL не содержит в себе искомую подстроку"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Форма авторизации не отображается"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не отображается"


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def register_new_user(self, email, password):
        self.go_to_login_page()
        login_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        login_input.click()
        login_input.send_keys(email)
        pass_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_INPUT)
        pass_input.click()
        pass_input.send_keys(password)
        pass_conf_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASS_INPUT)
        pass_conf_input.click()
        pass_conf_input.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()