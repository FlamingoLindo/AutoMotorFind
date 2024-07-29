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
from datetime import datetime 
import sys

# Add the path to the directory containing the Functions module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Functions.Rand_CPF import gera_e_valida_cpf
from Functions.Rand_CPNJ import gera_cnpj
from Functions.Get_country import random_country_func
from Functions.Create_name import create_random_name

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

def get_time():
    date_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
    return date_time

screenshot_dir = r'Images\Screenshot'
os.makedirs(screenshot_dir, exist_ok=True)
screenshot_path = os.path.join(screenshot_dir, 'screenshot.png')

password = 'Aa12345678!'

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

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    

    def test_create_account(self) -> None:
        count = 1
        
        # Ask the amount of accounts to be created
        account_amount_str = get_user_input("How many?")
        account_amount_int = int(account_amount_str)
        
        for _ in range(account_amount_int):
            try:
                # Print the iteration
                print(f"Creating account {count} 🔄️")
                
                # Open the client register page
                register_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cadastrar")'))
                ).click()

                # Inputs the name
                name = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ex. José Santos")'))
                ).send_keys(create_random_name() +  f' Automatico {count} ' + get_time())
            
                # Inputs the email
                email = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ex. nome@email.com")'))
                ).send_keys(create_random_name() + f'@gmail.com')

                # Generate random phone number (1)
                rand_phone = random.randint(11111111111, 99999999999)
                # Inputs the phone number (2)
                phone = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("(00) 9 1234-56789")'))
                ).send_keys(f"{rand_phone}")
                
                # Button click
                next_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)'))
                ).click()
                
                print("First step done 🟢")
            except Exception as e:
                self.driver.get_screenshot_as_file(screenshot_path)
                print("There has been an error on the first step 🔴")
                print(e)
                break
            
            time.sleep(1.5)
            try:
                # Inputs CPF
                cpf = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("000.000.000-00")'))
                ).send_keys(gera_e_valida_cpf()) 
                
                # Inputs CNPJ
                cnpj = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00.000.000/0000-00")'))
                ).send_keys(gera_cnpj())

                # Generate random phone number (2)
                rand_phone2 = random.randint(11111111111, 99999999999)
                # Inputs random phone number (2)
                phone2 = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("(00) 9 1234-56789")'))
                ).send_keys(f'{rand_phone2}')
                            
                # Button click
                next_btn2 = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'))
                ).click()
            
                print("Second step done 🟢")
            except Exception as e:
                self.driver.get_screenshot_as_file(screenshot_path)
                print("There has been an error on the second step 🔴")
                print(e)
                break
            
            time.sleep(1.5)
            
            try:
                # Open country dropdown
                country_dropdown = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Selecione o país, '))
                ).click()

                rand_country = random_country_func()
                
                # Search country
                country_search= WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Buscar")'))
                ).send_keys(rand_country)
                
                time.sleep(1)
                
                # Select country
                country = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@text="{rand_country}"]'))
                ).click()
                
                # Inputs CEP (can't make a function that generates random CEPs)
                cep = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00000-000")'))
                ).send_keys('67140704')

                # Generates random address number
                rand_num = random.randint(1, 999)
                # Inputs random address number
                num = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Número"]'))
                ).send_keys(f'{rand_num}')

                # Swipes to the bottom of the page, so Appium can see the button
                self.driver.swipe(start_x=500, start_y=1600, end_x=500, end_y=700, duration=80)

                time.sleep(0.5)
                
                # Button click
                next_btn3 = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View")'))
                ).click()
                
                print("Third step done 🟢")
            except Exception as e:
                self.driver.get_screenshot_as_file(screenshot_path)
                print("There has been an error on the third step 🔴")
                print(e)
                break
            
            time.sleep(1.3)
            
            try:
                # Inputs password (1)
                password1 = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Senha@!23").instance(0)'))
                ).send_keys(f'{password}')

                # Inputs password (2)
                password2 = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Senha@!23")'))
                ).send_keys(f'{password}')

                # Button click
                next_btn4 = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'))
                ).click()

                print("Fourth step done 🟢")
            except Exception as e:
                self.driver.get_screenshot_as_file(screenshot_path)
                print("There has been an error on the fourth step 🔴")
                print(e)
                break
            
            time.sleep(0.5)
            
            try:
                # Select interests
                # Car
                car = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(0)'))
                ).click()

                # Classic
                classic = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)'))
                ).click()

                # Parts
                parts = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(2)'))
                ).click()
                
                # Bikes
                bikes = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(3)'))
                ).click()

                # Racing
                race = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'))
                ).click()

                # Drag
                drag = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)'))
                ).click()
                
                # Trucks
                truck = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(6)'))
                ).click()

                # Services
                service = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(7)'))
                ).click()

                # Button click
                next_btn5 = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(8)'))
                ).click()

                print("Fifth step done 🟢")
            except Exception as e:
                self.driver.get_screenshot_as_file(screenshot_path)
                print("There has been an error on the fifth step 🔴")
                print(e)
                break
            
            try: 
                # Agree of terms and conditions
                agree = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup'))
                ).click()

                # Click the accept button
                accept_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View")'))
                ).click()
                
                time.sleep(1.5)
                
                # Close the registration modal
                done_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(5)'))
                ).click()
                
                print("Sixth step done 🟢")
            except Exception as e:
                self.driver.get_screenshot_as_file(screenshot_path)
                print("There has been an error on the sixth step 🔴")
                print(e)
                break
            
            print(f"Account {count} created ✅ \n ------------------------")
            
            count += 1
                
if __name__ == '__main__':
    unittest.main()