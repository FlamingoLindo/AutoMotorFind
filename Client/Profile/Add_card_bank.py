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

ACC_NUM = "04537173"
AGENCY = "3264"

CARD_NUM = '5289265985168111'
EXPI_DATE = '0925'
CVV = '266'


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

try:
    # Drive stuff
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    driver.get(os.getenv('CLIENT_URL'))

    wait = WebDriverWait(driver, 5)
except Exception as e:
    print('There has been an error initialising the chrome driver')
    print(e)

try:
    # Click the login button
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.hygPet')
                                                        )
                            ).click() 

    # Get login
    login = get_user_input('Email')

    # Input login
    login_input = wait.until(EC.element_to_be_clickable((By.ID, 'email')
                                                        )
                            ).send_keys(login)

    # Get password
    password = get_user_input('Password')

    # Input password
    password_input = wait.until(EC.element_to_be_clickable((By.ID, 'password')
                                                        )
                            ).send_keys(password)

    # Logs in 
    do_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eaqkjo')
                                                        )
                            ).click() 
except Exception as e:
    print('There has been an error on the login')
    print(e)

try:
    # Click options
    options = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bNVGjx')
                                                        )
                            ).click() 

    # Click my profile option
    my_profile_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[4]')
                                                        )
                            ).click()

    # Click wallet option
    wallet_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/button[4]')
                                                        )
                            ).click()  
except Exception as e:
    print('There has been an error opening the profile options')
    print(e)
    
"""
try:
    # Click add bank account
    add_bank_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/button')
                                                        )
                            ).click()  

    # Diced cpf or cnpj
    cpf_or_cnpj = random.randint(1,2)

    if cpf_or_cnpj == 1:
        cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf_cnpj"]')
                                                        )
                            ).send_keys(gera_e_valida_cpf()) 
    else:
        cnpj_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf_cnpj"]')
                                                        )
                            ).send_keys(gera_cnpj()) 
        
    # Input account number
    acc_num = wait.until(EC.element_to_be_clickable((By.ID, 'account_number')
                                                        )
                            ).send_keys(ACC_NUM)

    # Input agency
    agency = wait.until(EC.element_to_be_clickable((By.ID, 'agency')
                                                        )
                            ).send_keys(AGENCY) 

    # Click the account type dropdown
    acc_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/form/div[4]/div/div')
                                                        )
                            ).click() 
        
    # Account type decision
    acc_type_random = random.randint(1,2)

    acc_type_input = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/form/div[4]/div/div[2]/div[{acc_type_random}]/span')
                                                    )
                        ).click() 

    # Click bank type dropdown
    bank_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/form/div[5]/div/div')
                                                        )
                            ).click() 

    # Bank type decision
    bank_type_random = random.randint(1,4)

    bank_type_input = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/form/div[5]/div/div[2]/div[{bank_type_random}]')
                                                    )
                        ).click() 

    # Click the sabe button
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/form/div[6]/button[1]')
                                                    )
                        ).click() 
except Exception as e:
    print('There has been an error while creating the bank account')
    print(e)
"""
try:
    # Ask for the amount of cards to be created
    card_amount_str = get_user_input('Card amount?')
    card_amount_int = int(card_amount_str)
    for _ in range(card_amount_int):

        # Click the add card button
        add_card_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/button')
                                                        )
                            ).click()

        # CPF or CNPJ decision
        cpf_or_cnpj = random.randint(1,2)

        if cpf_or_cnpj == 1:
            cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf_cnpj"]')
                                                            )
                                ).send_keys(gera_e_valida_cpf()) 
        else:
            cnpj_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf_cnpj"]')
                                                            )
                                ).send_keys(gera_cnpj())
            
        # Input card name
        name_input = wait.until(EC.element_to_be_clickable((By.ID, 'name')
                                                        )
                            ).send_keys('autonome')

        # Inpur card number
        card_num = wait.until(EC.element_to_be_clickable((By.ID, 'card_number')
                                                        )
                            ).send_keys(CARD_NUM)

        # Input card expiration date
        expi_date = wait.until(EC.element_to_be_clickable((By.ID, 'date')
                                                        )
                            ).send_keys(EXPI_DATE)

        # Input card cvv
        cvv = wait.until(EC.element_to_be_clickable((By.ID, 'cvv')
                                                        )
                            ).send_keys(CVV)

        # Click save button
        save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/form/div[5]/button[1]')
                                                        )
                            ).click()
except Exception as e:
    print('There has been an error creating the credit card')
    print(e)
    
    
get_user_input("DONE")
# Close the browser
driver.quit()
