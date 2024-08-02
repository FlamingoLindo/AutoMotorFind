import customtkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
import random
import sys
load_dotenv()

# Add the path to the directory containing the Functions module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from App.Functions.Rand_CPF import gera_e_valida_cpf
from App.Functions.Rand_CPNJ import gera_cnpj
from App.Functions.Create_name import create_random_name
from App.Functions.Get_time import get_time

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

# Drive stuff
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('CLIENT_URL'))

wait = WebDriverWait(driver, 5)


count = 1

account_amount_str = get_user_input("How many?")
account_amount_int = int(account_amount_str)

for _ in range(account_amount_int):
    
    # 
    register_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]')
                                                    )
                        ).click()
    
    # 
    name_input = wait.until(EC.element_to_be_clickable((By.ID, 'name')
                                                    )
                        ).send_keys(create_random_name() +  f' Automatico (WEB) {count} ' + get_time())
    
    # 
    email_input = wait.until(EC.element_to_be_clickable((By.ID, 'email')
                                                    )
                        ).send_keys(create_random_name() + f'@gmail.com')
    
    # Generate random phone number (1)
    rand_phone = random.randint(11111111111, 99999999999)
    # 
    phone_input = wait.until(EC.element_to_be_clickable((By.ID, 'phone')
                                                    )
                        ).send_keys(rand_phone)
    
    # 
    next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dCoGxG')
                                                    )
                        ).click()
    
    # 
    cpf_input = wait.until(EC.element_to_be_clickable((By.ID, 'cpf')
                                                    )
                        ).send_keys(gera_e_valida_cpf())
    
    # 
    cnpj_input = wait.until(EC.element_to_be_clickable((By.ID, 'cnpj')
                                                    )
                        ).send_keys(gera_cnpj())
    
    # Generate random phone number (1)
    rand_telephone = random.randint(11111111111, 99999999999)
    # 
    telephone_input = wait.until(EC.element_to_be_clickable((By.ID, 'telephone')
                                                    )
                        ).send_keys(rand_telephone)

    # 
    next_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.hvAiZb')
                                                    )
                        ).click()
    
    # 
    country_dorpdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.jSZTir')
                                                    )
                        ).click()
    
    #
    country_search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eSxcE')
                                                    )
                        ).send_keys("Brasil")
    
    # 
    country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.gNYYxY')
                                                    )
                        ).click()
    
    #
    cep_input = wait.until(EC.element_to_be_clickable((By.ID, 'cep')
                                                    )
                        ).send_keys('01001-000')
    
    #
    number_input = wait.until(EC.element_to_be_clickable((By.ID, 'number')
                                                    )
                        ).send_keys(count)

    time.sleep(1.5)
    
    # 
    next_btn3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.hNJTTa')
                                                    )
                        ).click()
    
    #
    password = wait.until(EC.element_to_be_clickable((By.NAME, 'password')
                                                    )
                        ).send_keys("Aa12345678!")
    
    #
    password = wait.until(EC.element_to_be_clickable((By.NAME, 'confirm_password')
                                                    )
                        ).send_keys("Aa12345678!")
    
    # 
    next_btn4 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.jLEUkB')
                                                    )
                        ).click()
    
    time.sleep(2)
    
    count_inte = 1

    for i in range(1, 9):
        
        # Try using a different way to select checkboxes
        interests = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f'(//input[@type="checkbox"])[{count_inte}]')
        )).click()
            
        count_inte += 1

        
    # 
    next_btn5 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.hFGBKx')
                                                    )
                        ).click()
    
    # 
    terms = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.leEbPC')
                                                    )
                        ).click()
    
    # 
    continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.jjwRFZ')
                                                    )
                        ).click()
    
    # 
    modal = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dNCRpz')
                                                    )
                        ).click()
    # 
    account_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bNVGjx')
                                                    )
                        ).click()
    
    # 
    exit = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[8]')
                                                    )
                        ).click()
    
    count +=1
    
    print(f"Account {count} created")
    
get_user_input("DONE")
# Close the browser
driver.quit()
