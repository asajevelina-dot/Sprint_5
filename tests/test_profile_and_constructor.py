import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators as Locators

BASE_URL = "https://stellarburgers.education-services.ru"

class TestProfile:
    
    def test_go_to_personal_account(self, login_user):
        browser = login_user
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PROFILE_EMAIL))
        assert "account" in browser.current_url
        print("✅ Переход в личный кабинет")
    
    def test_exit_from_account(self, login_user):
        browser = login_user
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        browser.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert "login" in browser.current_url
        print("✅ Выход из аккаунта")
    
    def test_go_to_constructor_from_profile(self, login_user):
        browser = login_user
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PROFILE_EMAIL))
        browser.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert browser.current_url == BASE_URL + "/"
        print("✅ Переход в конструктор")
    
    def test_go_to_main_from_profile_by_logo(self, login_user):
        browser = login_user
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PROFILE_EMAIL))
        browser.find_element(*Locators.LOGO).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert browser.current_url == BASE_URL + "/"
        print("✅ Переход по логотипу")

class TestConstructor:
    
    def test_buns_section_active(self, browser):
        browser.get(BASE_URL)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.BUNS_SECTION))
        active_tab = browser.find_element(*Locators.ACTIVE_TAB)
        assert active_tab.text == "Булки"
        print("✅ Раздел Булки")
    
    def test_sauces_section_clickable(self, browser):
        browser.get(BASE_URL)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.SAUCES_SECTION))
        browser.find_element(*Locators.SAUCES_SECTION).click()
        WebDriverWait(browser, 3).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Соусы"))
        assert browser.find_element(*Locators.ACTIVE_TAB).text == "Соусы"
        print("✅ Раздел Соусы")
    
    def test_fillings_section_clickable(self, browser):
        browser.get(BASE_URL)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.FILLINGS_SECTION))
        browser.find_element(*Locators.FILLINGS_SECTION).click()
        WebDriverWait(browser, 3).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Начинки"))
        assert browser.find_element(*Locators.ACTIVE_TAB).text == "Начинки"
        print("✅ Раздел Начинки")
