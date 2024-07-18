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

image_path = r'C:\Users\josef\Desktop\AfterLifeDeath\MotorFind\AutoMotorFind\Images\logo.svg'

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

brands_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[9]')
                                                  )
                       ).click()

choose = 1#random.randint(1,2)
banana = 1
if choose == 1:
    
    brand_input_str = get_user_input("How many?")
    brand_input_int = int(brand_input_str)
    for _ in range(brand_input_int):    
        categ_type = random.randint(1,8)
    
        open_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[1]')
                                                        )
                            ).click()
        
        add_brand_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[2]/div[1]')
                                                    )
                        ).click()
        
        image_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[2]/label[2]')
                                                    )
                        ).click()
        
        time.sleep(1)
        
        pyautogui.write(image_path)
        pyautogui.press('enter')
        
        title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="title"]')
                                                    )
                        ).send_keys(f"Marca {banana}")

        register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[1]/div/button[2]')
                                                  )
                       ).click()
        
        time.sleep(2)        
        
        done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/button')
                                                  )
                       ).click()
            
        """switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.esbzDM')
                                                  )
                       ).click()"""
        
        close_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[1]')
                                                        )
                            ).click()

        banana += 1
        
elif choose == 2:
    components_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div[2]')
                                                  )
                       ).click()
    
    components_amount_str = get_user_input("How many?")
    components_amount_int = int(components_amount_str)
    for _ in range(components_amount_int):
        add_component = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/button')
                                                  )
                       ).click()

       
        component_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="title"]')
                                                  )
                       ).send_keys(f"Componente {banana}")
        
        register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[5]/form/div[1]/div/button[2]')
                                                  )
                       ).click()
        
        done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[5]/div/button')
                                                  )
                       ).click()
        
        """switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.esbzDM')
                                                  )
                       ).click()"""
        
        time.sleep(1.3)
        banana += 1
        
# Close the browser
driver.quit()
