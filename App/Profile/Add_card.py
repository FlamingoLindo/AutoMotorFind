import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import customtkinter as tk
from tkinter import simpledialog
import random
import time  
import os
import sys

from dotenv import load_dotenv
load_dotenv()

# Add the path to the directory containing the Functions module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Functions.Rand_CPF import gera_e_valida_cpf

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

screenshot_dir = r'Images\Screenshot'
os.makedirs(screenshot_dir, exist_ok=True)
screenshot_path = os.path.join(screenshot_dir, 'screenshot.png')


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='flamingo_lindo',
    language='pt',
    printPageSourceOnFindFailure = True,
    eventTimings = True,
    noReset = True,
    appPackage = 'com.mestresdaweb.motorfind',
    appActivity = 'com.mestresdaweb.motorfind.MainActivity'
)

appium_server_url = 'http://localhost:4723'


CARD_NUM = "5260925819223282"
CARD_EXP = "052026"
CARD_CVV = "925"

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
            
    def test_add_card(self) -> None:
        try:
            # Wait untill the app has loaded
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'))
            )

            # Inputs the email
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("insira seu e-mail")'))
            ).send_keys(os.getenv("CLIENT_LOGIN"))

            # Inputs the password
            password = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Insira sua senha")'))
            ).send_keys(os.getenv("CLIENT_PASSWORD"))
            
            # Button click
            next_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)'))
            ).click()
            
            time.sleep(1)
            
            print("First step done 🟢")
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot_path)
            print("There has been an error on the first step 🔴")
            print(e)
            raise  
            
        try:
            time.sleep(1.4)
            
            # Open profile
            profile_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button[2]'))
            ).click()
            
            # Open account information
            wallet = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'))
            ).click()
            
            time.sleep(0.5)
            
            print("Second step done 🟢")
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot_path)
            print("There has been an error on the second step 🔴")
            print(e)
            raise  
            
        try:
            # 
            add_card_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(0)'))
            ).click()
            
            # 
            card_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ex. José A V Andrade")'))
            ).send_keys("NOME CARTAO")
            
            # 
            card_num = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1234-5678-9012-3456")'))
            ).send_keys(CARD_NUM)
            
            # 
            card_exp = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00/00")'))
            ).send_keys(CARD_EXP)
            
            # 
            cvv = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("000")'))
            ).send_keys(CARD_CVV)
            
            # 
            cpf = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("23800247828")'))
            ).send_keys(gera_e_valida_cpf())
            
            # 
            save = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)'))
            ).click()
            
            # 
            continue_modal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continuar")'))
            ).click()
            
            print("Third step done 🟢")
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot_path)
            print("There has been an error on the third step 🔴")
            print(e)
            raise  

            
                
if __name__ == '__main__':
    unittest.main()