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
    
    # Click the register button
    register_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]')
                                                    )
                        ).click()
    
    # Inputs name
    name_input = wait.until(EC.element_to_be_clickable((By.ID, 'name')
                                                    )
                        ).send_keys(create_random_name() +  f' Automatico (WEB) {count} ' + get_time())
    
    # Inputs email
    email_input = wait.until(EC.element_to_be_clickable((By.ID, 'email')
                                                    )
                        ).send_keys(create_random_name() + f'@gmail.com')
    
    # Generate random phone number (1)
    rand_phone = random.randint(11111111111, 99999999999)
    # Inputs phone number
    phone_input = wait.until(EC.element_to_be_clickable((By.ID, 'phone')
                                                    )
                        ).send_keys(rand_phone)
    
    # Click next button 1
    next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dCoGxG')
                                                    )
                        ).click()
    
    # Inputs random CPF
    cpf_input = wait.until(EC.element_to_be_clickable((By.ID, 'cpf')
                                                    )
                        ).send_keys(gera_e_valida_cpf())
    
    """# Inputs random CPNJ
    cnpj_input = wait.until(EC.element_to_be_clickable((By.ID, 'cnpj')
                                                    )
                        ).send_keys(gera_cnpj())"""
    
    # Generate random phone number (1)
    rand_telephone = random.randint(11111111111, 99999999999)
    # Inputs random telephone number
    telephone_input = wait.until(EC.element_to_be_clickable((By.ID, 'telephone')
                                                    )
                        ).send_keys(rand_telephone)

    # Click next button 2
    next_btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.hvAiZb')
                                                    )
                        ).click()
    
    # Click the country dropdown
    country_dorpdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.jSZTir')
                                                    )
                        ).click()
    
    # Serach Brazil
    country_search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eSxcE')
                                                    )
                        ).send_keys("Brasil")
    
    # Select Brazil
    country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.gNYYxY')
                                                    )
                        ).click()
    
    # Inputs CEP
    cep_input = wait.until(EC.element_to_be_clickable((By.ID, 'cep')
                                                    )
                        ).send_keys('01001-000')
    
    # Inputs adress number
    number_input = wait.until(EC.element_to_be_clickable((By.ID, 'number')
                                                    )
                        ).send_keys(count)

    time.sleep(1.5)
    
    # Click next button 3
    next_btn3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.hNJTTa')
                                                    )
                        ).click()
    
    # Inputs password
    password = wait.until(EC.element_to_be_clickable((By.NAME, 'password')
                                                    )
                        ).send_keys("Aa12345678!")
    
    # Inputs password confirmatios
    password = wait.until(EC.element_to_be_clickable((By.NAME, 'confirm_password')
                                                    )
                        ).send_keys("Aa12345678!")
    
    # Click next button 4
    next_btn4 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.jLEUkB')
                                                    )
                        ).click()
    
    time.sleep(2)
    
    count_inte = 1

    for i in range(1, 9):
        
        # Selects all 8 interests
        interests = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f'(//input[@type="checkbox"])[{count_inte}]')
        )).click()
            
        count_inte += 1

        
    # Click next button 5
    next_btn5 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.hFGBKx')
                                                    )
                        ).click()

    # Agree to the terms and conditions
    terms = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.jncpFj')
                                                    )
                        ).click()
    
    # Click the continue button
    continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.FegBo')
                                                    )
                        ).click()
    
    # Close modal
    modal = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dNCRpz')
                                                    )
                        ).click()
    
    # Click the account menu
    account_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bNVGjx')
                                                    )
                        ).click()
    
    # Exit account
    exit = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[8]')
                                                    )
                        ).click()
    
    # Print the accout creation iteration
    print(f"Account {count} created")
    
    count +=1
    
get_user_input("DONE")
# Close the browser
driver.quit()
