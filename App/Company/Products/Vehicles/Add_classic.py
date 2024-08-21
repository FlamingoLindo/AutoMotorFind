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
            # Open company menu
            company_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button[1]'))
            ).click()
            
            # Open company's products
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
            # Ask how many products are going to be made
            product_amount = int(get_user_input("How many?"))
            for _ in range(product_amount):
                # Click the add product button
                add_product = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(0)'))
                ).click()
                
                # Input product name
                product_name = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o nome do produto")'))
                ).send_keys(f'Auto Product {count}')
                
                # Input product quantity
                product_quantity = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")'))
                ).send_keys(count)
                
                # Generates random value
                rand_value = random.randint(5, 999)
                # Input product random value
                product_value = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="R$ 00,00"]'))
                ).send_keys(rand_value)
                
                # Open category dropdown
                category = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Escolha a categoria")'))
                )
                category.click()
        
                # Select category item
                category_type = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@text="Clássicos"]'))
                ).click()
                
                # Swipes to the bottom of the page
                self.driver.swipe(start_x=500, start_y=1600, end_x=500, end_y=700, duration=80)
                
                # Open subcategory dropdown
                sub_category = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Escolha a subcategoria")'))
                ).click()
                    
                # Select subcategory item
                sub_category_item = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@text="ALTERAR"]'))
                ).click()
                
                # Click the "Product is" dropdown
                prod_condition_dropdown = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(20)'))
                ).click()
                
                # Select product condition
                
                # Click the 'add photo' button
                add_photo_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)'))
                ).click()

                # Click the 'album' button
                albuns = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Álbuns'))
                )
                albuns.click()

                # Open the favorites album
                favorites = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(0)'))
                        )
                favorites.click()
                
                # Click at the first image
                image = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(0)'))
                        )
                image.click()

                # Open negotiation dropdown
                negotiaton_dropdown = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Sim, '))
                ).click()
                
                # Negotiation select
                
                # Shift type dropdown
                shift_type_dropdown = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Escolha o tipo de câmbio, '))
                ).click()
                
                # Select shift type
                
                # Click highlight dropdown
                highlight_dropdown = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Não, '))
                ).click()
                
                # Select highlight option
                
                
                
                # Swipes to the top of the page
                self.driver.swipe(start_x=500, start_y=700, end_x=500, end_y=1600, duration=80)

                # Click the details button
                details_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Detalhes'))
                ).click()

                # Open the brand dropdown
                brand = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Escolha a marca do produto, '))
                ).click()
                
                # Select brand option
                
                # Generates random kilometers
                rand_km = random.randint(0, 9999)
                # Input random kilometer
                km = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("000 Km")'))
                ).send_keys(rand_km)

                # Generate random year
                rand_year = random.randint(1980, 2025)
                # Input random year
                km = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0000")'))
                ).send_keys(rand_km)

                # Click color dropdown
                color_dropdown = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Escolha a cor do produto, '))
                ).click()
                
                # Select color

                # Generate random speed
                rand_speed = random.randint(100, 300)
                # Inputs random speed
                speed = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("000 km/h")'))
                ).send_keys(rand_km)

                # Generate random torque
                rand_torque = random.randint(1, 999)
                # Input random torque
                torque = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("000 Nm")'))
                ).send_keys(rand_torque)
                
                # Swipes to the bottom of the page
                self.driver.swipe(start_x=500, start_y=1600, end_x=500, end_y=700, duration=80)
                
                # Generate random power
                rand_power = random.randint(1, 9999)
                # Input random power
                power = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("000 PS")'))
                ).send_keys(rand_torque)

                # Input link :Tomfoolery:
                link = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("www.linkdoproduto.com/categoria/subcategoria/produto01")'))
                ).send_keys("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

                # Input description
                description = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Descreva o que contém na embalagem do produto")'))
                ).send_keys(f"Auto descriptions {count}")
                
                # Click the continue button
                continue_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Adicionar produto").instance(1)'))
                ).click()
                
                # Closes the modal 
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