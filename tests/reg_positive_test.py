from pages.auth import *
from selenium.webdriver.common.by import By
from pages.settings import valid_phone, valid_login, valid_password, \
    fake_firstname, fake_lastname, fake_password
import time
import pytest


class TestRegistration:

    @pytest.mark.reg
    @pytest.mark.positive
    def test_get_registration_valid(self, browser):
        """Регистрация пользователя с валидными данными.
        В случае успешного ввода данных и отправки системой кода на указанный email будем считать регистрацию успешно пройденной."""


        """Активируем окно ввода данных для прохождения регистрации на сайте"""
        # Нажимаем на кнопку Зарегистрироваться:
        page = AuthPage(browser)
        page.enter_reg_page()
        browser.implicitly_wait(2)
        assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

        page = RegPage(browser)
        # Вводим имя:
        page.enter_firstname(fake_firstname)
        browser.implicitly_wait(5)
        # Вводим фамилию:
        page.enter_lastname(fake_lastname)
        browser.implicitly_wait(5)
        # Вводим адрес почты/Email:
        page.enter_email('st.shad@mail.ru')
        browser.implicitly_wait(3)
        # Вводим пароль:
        page.enter_password(fake_password)
        browser.implicitly_wait(3)
        # Вводим подтверждение пароля:
        page.enter_pass_conf(fake_password)
        browser.implicitly_wait(3)
        # Нажимаем на кнопку 'Зарегистрироваться':
        page.btn_click()

        assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


