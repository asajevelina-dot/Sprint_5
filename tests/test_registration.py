import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators as Locators
from helpers.user_generator import generate_short_password

BASE_URL = "https://stellarburgers.education-services.ru"

class TestRegistration:
    
    def test_successful_registration(self, browser, user_data):
        browser.get(f"{BASE_URL}/register")
        
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.NAME_INPUT))
        browser.find_element(*Locators.NAME_INPUT).send_keys(user_data["name"])
        browser.find_element(*Locators.EMAIL_INPUT).send_keys(user_data["email"])
        browser.find_element(*Locators.PASSWORD_INPUT).send_keys(user_data["password"])
        browser.find_element(*Locators.REGISTER_BUTTON).click()
        
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert "login" in browser.current_url
        print("✅ Успешная регистрация!")
    
    def test_registration_error_short_password(self, browser, user_data):
        browser.get(f"{BASE_URL}/register")
        
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.NAME_INPUT))
        browser.find_element(*Locators.NAME_INPUT).send_keys(user_data["name"])
        browser.find_element(*Locators.EMAIL_INPUT).send_keys(user_data["email"])
        browser.find_element(*Locators.PASSWORD_INPUT).send_keys("12345")
        browser.find_element(*Locators.REGISTER_BUTTON).click()
        
        error = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(Locators.REGISTRATION_ERROR))
        assert "Некорректный пароль" in error.text
        print("✅ Ошибка для короткого пароля!")
