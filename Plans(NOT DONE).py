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
import pyautogui
import sys
load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

def gera_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    soma = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
    cpf.append((soma * 10) % 11)
    soma = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
    cpf.append((soma * 10) % 11)
    cpf_formatado = ''.join(map(str, cpf))
    return cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]

def gera_parcela():
    return str(random.randint(1, 999999999))

def gera_aviso():
    return str(random.randint(1, 29))

def register_catg():
    car_catg_title_input = get_user_input("Category name       ")
    car_catg_info_input = get_user_input("Category info        ")

    car_catg_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(car_catg_title_input)

    car_catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                    )
                        ).send_keys(car_catg_info_input)

    register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[2]/button[2]')
                                                    )
                        ).click()   
    
    done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/button')
                                                    )
                        ).click() 

driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('MASTER_URL'))

wait = WebDriverWait(driver, 5)


email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')
                                                    )
                         ).send_keys(os.getenv("MASTER_LOGIN"))

password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')
                                                       )
                            ).send_keys(os.getenv("MASTER_PASSWORD"))

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

plans_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[5]')
                                                  )
                       ).click()

plan_amount_str = get_user_input("How many plans do you wish to create?")
plan_amount_int = int(plan_amount_str)
for _ in range(plan_amount_int):
    add_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div/button')
                                                    )
                        ).click()
    
    plan_name_input = get_user_input("Plan name                   ")
    plan_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(plan_name_input)
    
    categ_drop_down = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[4]/form/div[3]/div[1]/div')
                                                    )
                        ).click()
    
    categ_choose = get_user_input("Todas, Carros, Clássicos, Motos, Trucks, Race").title()
    
    category_map = {
        "Todas": 1,
        "Carros": 2,
        "Clássicos": 3,
        "Motos": 4,
        "Trucks": 5,
        "Race": 6
    }
    num = category_map.get(categ_choose)

    categ_option_click = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[4]/form/div[3]/div[1]/div[2]/div[{num}]')
                                                    )
                        ).click()
    
    subcateg_drop_down = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[4]/form/div[3]/div[2]/div')
                                                    )
                        ).click()
    
    subcateg_choose = get_user_input("Todas, Super esportivo, Clássicos, Placa preta, Premium, Esportivos").title()
    
    subcateg_map = {
        "Todas": 1,
        "Super esportivo": 2,
        "Clássicos": 3,
        "Placa preta": 4,
        "Premium": 5,
        "Esportivos": 6
    }
    num2 = subcateg_map.get(subcateg_choose)

    subcateg_option_click = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[4]/form/div[3]/div[2]/div[2]/div[{num2}]')
                                                    )
                        ).click()
    
    sub_fee_input = get_user_input("Subscription fee value")
    sub_fee = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tax"]')
                                                    )
                        ).send_keys(sub_fee_input)

    charge_input = get_user_input("How much do you want to charge?")
    charge = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="charges"]')
                                                    )
                        ).send_keys(charge_input)
    
    time_drop_down = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[4]/form/div[5]/div/div/div')
                                                           )
                                ).click()
    
    time_input = get_user_input("Ano, Mês, Semestre, Única").title()
    time_map = {
        "Ano": 1,
        "Mês": 2,
        "Semestre": 3,
        "Única": 4
    }
    num3 = subcateg_map.get(time_input)
    
    time_option_click = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[4]/form/div[5]/div/div/div[2]/div[{num3}]')
                                                              )
                                   ).click()
    
    
# Close the browser
driver.quit()
