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

CARD_NUM = '5566956211903685'
EXPI_DATE = '0526'
CVV = '165'


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

#
login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.hygPet')
                                                    )
                        ).click() 

#
login = get_user_input('Email')

#
login_input = wait.until(EC.element_to_be_clickable((By.ID, 'email')
                                                    )
                        ).send_keys(login)

#
password = get_user_input('Password')

#
password_input = wait.until(EC.element_to_be_clickable((By.ID, 'password')
                                                    )
                        ).send_keys(password)

#
login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eaqkjo')
                                                    )
                        ).click() 

#
options = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bNVGjx')
                                                    )
                        ).click() 

#
my_profile_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[4]')
                                                    )
                        ).click()

#
wallet_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/button[4]')
                                                    )
                        ).click()  

"""#
add_bank_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/button')
                                                    )
                        ).click()  

#
cpf_or_cnpj = random.randint(1,2)

if cpf_or_cnpj == 1:
    cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf_cnpj"]')
                                                    )
                        ).send_keys(gera_e_valida_cpf()) 
else:
    cnpj_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf_cnpj"]')
                                                    )
                        ).send_keys(gera_cnpj()) 
    
#
acc_num = wait.until(EC.element_to_be_clickable((By.ID, 'account_number')
                                                    )
                        ).send_keys(ACC_NUM)

#
agency = wait.until(EC.element_to_be_clickable((By.ID, 'agency')
                                                    )
                        ).send_keys(AGENCY) 

#
acc_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/form/div[4]/div/div')
                                                    )
                        ).click() 
    
#
acc_type_random = random.randint(1,2)

acc_type_input = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/form/div[4]/div/div[2]/div[{acc_type_random}]/span')
                                                )
                    ).click() 

#
bank_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/form/div[5]/div/div')
                                                    )
                        ).click() 

#
bank_type_random = random.randint(1,4)

bank_type_input = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/form/div[5]/div/div[2]/div[{bank_type_random}]')
                                                  )
                    ).click() 

#
save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/form/div[6]/button[1]')
                                                  )
                    ).click() """

card_amount_str = get_user_input('Card amount?')
card_amount_int = int(card_amount_str)
for _ in range(card_amount_int):

    #
    add_card_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/button')
                                                    )
                        ).click()

    #
    cpf_or_cnpj = random.randint(1,2)

    if cpf_or_cnpj == 1:
        cpf_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf_cnpj"]')
                                                        )
                            ).send_keys(gera_e_valida_cpf()) 
    else:
        cnpj_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cpf_cnpj"]')
                                                        )
                            ).send_keys(gera_cnpj())
        
    #
    name_input = wait.until(EC.element_to_be_clickable((By.ID, 'name')
                                                    )
                        ).send_keys('autonome')

    #
    card_num = wait.until(EC.element_to_be_clickable((By.ID, 'card_number')
                                                    )
                        ).send_keys(CARD_NUM)

    #
    expi_date = wait.until(EC.element_to_be_clickable((By.ID, 'date')
                                                    )
                        ).send_keys(EXPI_DATE)

    #
    cvv = wait.until(EC.element_to_be_clickable((By.ID, 'cvv')
                                                    )
                        ).send_keys(CVV)

    #
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/form/div[5]/button[1]')
                                                    )
                        ).click()

get_user_input("DONE")
# Close the browser
driver.quit()
