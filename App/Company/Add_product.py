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
    enableMultiWindows = True,
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
            # 
            company_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button[1]'))
            ).click()
            
            # 
            my_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(3)'))
            ).click()
            
            print("Second step done 🟢")
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot_path)
            print("There has been an error on the second step 🔴")
            print(e)
            raise  
            
        try:
            product_amount_str = get_user_input("How many?")
            product_amount_int = int(product_amount_str)
            for _ in range(product_amount_int):
                # 
                add_product = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(0)'))
                ).click()
                
                # 
                product_name = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o nome do produto")'))
                ).send_keys(f'Auto Product {count}')
                
                # 
                product_quantity = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")'))
                ).send_keys(count)
                
                #
                rand_value = random.randint(5, 99999999)
                # 
                product_value = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="R$ 00,00"]'))
                ).send_keys(rand_value)
                
                """# 
                category = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Escolha a categoria, '))
                )
                category.click()"""

                """# 
                sub_category = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Escolha a subcategoria, '))
                )
                sub_category.click()"""

                #
                self.driver.swipe(start_x=500, start_y=1600, end_x=500, end_y=700, duration=80)
                
                #
                add_photo_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)'))
                ).click()

                #
                albuns = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Álbuns'))
                )
                albuns.click()

                #
                favorites = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(0)'))
                        )
                favorites.click()
                
                #
                image = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(0)'))
                        )
                image.click()

                """# 
                negotiaton = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Escolha a subcategoria, '))
                ).click()"""

                #
                self.driver.swipe(start_x=500, start_y=700, end_x=500, end_y=1600, duration=80)

                # 
                details_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Detalhes'))
                ).click()

                """# 
                brand = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Escolha a marca do produto, '))
                ).click()"""
                
                #
                rand_km = random.randint(0, 9999)
                # 
                km = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("000 Km")'))
                ).send_keys(rand_km)

                #
                rand_year = random.randint(1980, 2025)
                # 
                km = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0000")'))
                ).send_keys(rand_km)

                # 
                color = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ex. Preto")'))
                ).send_keys(f"Auto color {count}")

                #
                rand_speed = random.randint(200, 300)
                # 
                speed = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("000 km/h")'))
                ).send_keys(rand_km)

                #
                rand_torque = random.randint(1, 999)
                # 
                torque = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("000 Nm")'))
                ).send_keys(rand_torque)
                
                #
                rand_power = random.randint(1, 9999)
                # 
                power = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("000 PS")'))
                ).send_keys(rand_torque)

                #
                self.driver.swipe(start_x=500, start_y=1600, end_x=500, end_y=700, duration=80)

                # 
                link = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("www.linkdoproduto.com/categoria/subcategoria/produto01")'))
                ).send_keys("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

                # 
                description = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Descreva o que contém na embalagem do produto")'))
                ).send_keys(f"Auto descriptions {count}")
                
                # 
                continue_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Adicionar produto").instance(1)'))
                ).click()
                
                # 
                done = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continuar")'))
                ).click()

                count += 1
            
            print("Third step done 🟢")
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot_path)
            print("There has been an error on the third step 🔴")
            print(e)
            raise  

            
                
if __name__ == '__main__':
    unittest.main()