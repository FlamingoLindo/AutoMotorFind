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
from Functions.Rand_CPF import gera_e_valida_cpf
from Functions.Rand_CPNJ import gera_cnpj
from Functions.Get_country import random_country_func

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

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
        
        # For for the amount of accounts asked
        for _ in range(account_amount_int):
            
            # Print the iteration
            print(f"Creating account {count}")
            
            # Open the client register page
            register_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Cadastrar"]'))
            ).click()

            # Inputs the name
            name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Ex. José Santos"]'))
            )
            name.send_keys(f"Cliente Automático {count}")

            # Inputs the email
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Ex. nome@email.com"]'))
            )
            email.send_keys(f"email{count}@gmail.com")

            # Generate random phone number (1)
            rand_phone = random.randint(11111111111, 99999999999)
            # Inputs the phone number (2)
            phone = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="(00) 9 1234-56789"]'))
            )
            phone.send_keys(f"{rand_phone}")

            # Button click
            next_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Próximo"]/android.view.ViewGroup/android.view.View'))
            ).click()

            time.sleep(1.5)
            
            # Inputs CPF
            cpf = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="000.000.000-00"]'))
            )
            cpf.send_keys(gera_e_valida_cpf())  
            
            # Inputs CNPJ
            cnpj = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="00.000.000/0000-00"]'))
            )
            cnpj.send_keys(gera_cnpj())  
            
            # Generate random phone number (2)
            rand_phone2 = random.randint(11111111111, 99999999999)
            # Inputs random phone number (2)
            phone2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="(00) 9 1234-56789"]'))
            )
            phone2.send_keys(f'{rand_phone2}')
            
            # Button click
            next_btn2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'))
            ).click()
            time.sleep(1.5)
            
            # Open country dropdown
            country_dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Selecione o país, "]'))
            ).click()

            rand_country = random_country_func()
            
            # Search country
            country_search= WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Buscar"]'))
            ).send_keys(rand_country)
            
            time.sleep(1)
            
            # Select country
            self.driver.tap([(255, 840)])
              
            # Inputs CEP (cant make a function that generates random CEPs)
            cep = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="00000-000"]'))
            )
            cep.send_keys('39408197')
            
            # Generates random adress number
            rand_num = random.randint(1, 999)
            # Inputs random adress number
            num = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Número"]'))
            )
            num.send_keys(f'{rand_num}')
            
            # Swipes tot the bottom of the page, so appium can see the button
            self.driver.swipe(start_x=500, start_y=1600, end_x=500, end_y=700, duration=100)

            # Button click
            next_btn3 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View")'))
            ).click()

            # Inputs password (1)
            password1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.EditText[@text="Senha@!23"])[1]'))
            )
            password1.send_keys(f'{password}')
            
            # Input password confirmation, has to be by tap, because I couldn't find a way for appium to input the password
            
            # Open password confirmation
            self.driver.tap([(500, 830)], 100)
            time.sleep(0.6)
            # A
            self.driver.tap([(111, 1884)])
            # a
            self.driver.tap([(111, 1884)])
            # 1
            self.driver.tap([(70, 1596)])
            # 2
            self.driver.tap([(164, 1596)])
            # 3
            self.driver.tap([(270, 1596)])
            # 4
            self.driver.tap([(382, 1596)])
            # 5
            self.driver.tap([(480, 1600)])
            # 6
            self.driver.tap([(580, 1600)])
            # 7
            self.driver.tap([(680, 1600)])
            # 8
            self.driver.tap([(780, 1600)])
            # shift
            self.driver.tap([(90, 2027)])
            # !
            self.driver.tap([(70, 1596)])

            # Close keyboard
            self.driver.tap([(720, 1160)], 100)
            
            # End of password confirmation tapping

            # Button click
            next_btn4 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'))
            ).click()

            # Select interests
            # Car
            car = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Carros"]/android.view.View'))
            ).click()

            # Classic
            classic = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Clássicos"]/android.view.ViewGroup'))
            ).click()

            # Parts
            parts = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Peças"]/android.view.ViewGroup'))
            ).click()
            
            # Bikes
            bikes = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Motos"]/android.view.ViewGroup'))
            ).click()

            # Racing
            race = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Race"]/android.view.ViewGroup'))
            ).click()

            # Drag
            drag = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Drag"]/android.view.ViewGroup'))
            ).click()
            
            # Trucks
            truck = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Trucks"]/android.view.ViewGroup'))
            ).click()

            # Services
            service = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Serviços"]/android.view.ViewGroup'))
            ).click()

            # Button click
            next_btn5 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(8)'))
            ).click()

            # Agree of terms and conditions
            agree = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup'))
            ).click()

            # Click the accept button
            accpet_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View")'))
            ).click()
            
            time.sleep(1.5)
            
            # Close the registration modal, so it closes
            done_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(5)'))
            ).click()
            
            print(f"Account {count} created \n ------------------------")
            
            count += 1

if __name__ == '__main__':
    unittest.main()