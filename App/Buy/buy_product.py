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

from Functions.Get_time import get_time

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
    enableMultiWindows = True,
    appPackage = 'com.mestresdaweb.motorfind',
    appActivity = 'com.mestresdaweb.motorfind.MainActivity'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_edit_account(self) -> None:
        count = 1
        
        try:
            # Wait untill the app has loaded
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'))
            )

            # Inputs the email
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("insira seu e-mail")'))
            ).send_keys(get_user_input("Email"))

            # Inputs the password
            password = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Insira sua senha")'))
            ).send_keys(get_user_input("Password"))
            
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
            for _ in range(9999):
                # Inputs the email
                drag = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)'))
                ).click()

                time.sleep(1.5)
                
                # Inputs the password
                drag2 = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'))
                ).click()
                
                # Inputs the password
                buy_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Comprar'))
                ).click()
                
                time.sleep(1)
                
                cred_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Cartão de Crédito"))'))
                )

                cred_btn.click()

                # Inputs the password
                buy_btn2 = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Continuar'))
                ).click()
                
                end_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Confirmar compra'))
                ).click()
                
                time.sleep(5.3)
                
                modal = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View")'))
                ).click()
                
            
                  
            print("First step done 🟢")
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot_path)
            print("There has been an error on the first step 🔴")
            print(e)
            raise 
        
        
                
if __name__ == '__main__':
    unittest.main()