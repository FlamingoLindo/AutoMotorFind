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

plan_amount_str = get_user_input("How many?")
plan_amount_int = int(plan_amount_str)
count = 1
for _ in range(plan_amount_int):
    add_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div/button')
                                                    )
                        ).click()
    
    
    plan_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(f"Plan {count}")
    
    categ_drop_down = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[4]/form/div[3]/div[1]/div')
                                                    )
                        ).click()
    
    categ_choose = random.randint(1, 6)  
    categ_option_click = wait.until(EC.presence_of_element_located
                            ((By.CSS_SELECTOR, f".sc-5220e5de-12:nth-child({categ_choose})")
                                )
                            ).click()
    
    subcateg_drop_down = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[4]/form/div[3]/div[2]/div')
                                                    )
                        ).click()
    
    subcateg_choose = random.randint(1, 6)
    subcateg_option_click = wait.until(EC.presence_of_element_located
                            ((By.CSS_SELECTOR, f".sc-5220e5de-12:nth-child({subcateg_choose})")
                                )
                            ).click()
    
    sub_fee_input = random.randint(1,9999999)
    sub_fee = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="subscriptionFeeValue"]')
                                                    )
                        ).send_keys(sub_fee_input)

    charge_input = random.randint(1,9999999)
    charge = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="chargingValue"]')
                                                    )
                        ).send_keys(charge_input)
    
    time_drop_down = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[4]/form/div[5]/div/div/div')
                                                           )
                                ).click()
    
    time_input = random.randint(1, 3)
    time_option_click = wait.until(EC.presence_of_element_located
                            ((By.CSS_SELECTOR, f".sc-5220e5de-12:nth-child({time_input})")
                                )
                            ).click()
    
    
    
    
# Close the browser
driver.quit()
