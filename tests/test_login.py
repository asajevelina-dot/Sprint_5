import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators as Locators

BASE_URL = "https://stellarburgers.education-services.ru"

class TestLogin:
    
    def test_login_from_main_button(self, browser, register_user):
        browser.get(BASE_URL)
        browser.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT_LOGIN))
        browser.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(register_user["email"])
        browser.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(register_user["password"])
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert browser.current_url == BASE_URL + "/"
        print("✅ Вход через главную кнопку")
    
    def test_login_from_personal_account_button(self, browser, register_user):
        browser.get(BASE_URL)
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT_LOGIN))
        browser.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(register_user["email"])
        browser.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(register_user["password"])
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert browser.current_url == BASE_URL + "/"
        print("✅ Вход через личный кабинет")
    
    def test_login_from_registration_page(self, browser, register_user):
        browser.get(f"{BASE_URL}/register")
        browser.find_element(*Locators.LOGIN_LINK_FROM_REGISTER).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT_LOGIN))
        browser.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(register_user["email"])
        browser.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(register_user["password"])
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert browser.current_url == BASE_URL + "/"
        print("✅ Вход со страницы регистрации")
    
    def test_login_from_forgot_password_page(self, browser, register_user):
        browser.get(f"{BASE_URL}/forgot-password")
        browser.find_element(*Locators.LOGIN_LINK_FROM_FORGOT).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT_LOGIN))
        browser.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(register_user["email"])
        browser.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(register_user["password"])
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert browser.current_url == BASE_URL + "/"
        print("✅ Вход со страницы восстановления")
