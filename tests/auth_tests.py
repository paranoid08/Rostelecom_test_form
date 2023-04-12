import ast
from pages.settings import *
import pickle
import time
import pytest
from pages.auth import *
from selenium.webdriver.common.by import By
from pages.settings import valid_phone, valid_login, valid_password, \
    invalid_ls, valid_email, valid_pass_reg, fake_email

@pytest.mark.reg
@pytest.mark.positive
def test_reg_page_open(browser):
    """ Проверка открытия страницы регистрации """
    page = AuthPage(browser)
    page.enter_reg_page()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

@pytest.mark.auth
@pytest.mark.positive
def test_auth_page_email_valid(browser):
    """Проверка авторизации по почте и паролю"""
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(valid_pass_reg)
    time.sleep(20)     # время на ввод капчи при ее появлении
    page.btn_click_enter()

    assert page.get_relative_link() == '/account_b2c/page'

@pytest.mark.negative
def test_auth_page_fake_email(browser):
    """Проверка авторизации по почте и паролю, неверная почта"""
    page = AuthPage(browser)
    page.enter_username(fake_email)
    page.enter_password(valid_pass_reg)
    time.sleep(20)     # время на ввод капчи при ее появлении
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)

    assert error_mess.text == 'Неверный логин или пароль'



