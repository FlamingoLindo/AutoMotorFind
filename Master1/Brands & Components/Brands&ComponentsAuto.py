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
load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

# Sets image path
image_path = r'C:\Users\josef\Desktop\AfterLifeDeath\MotorFind\AutoMotorFind\Images\logo.svg'

# Driver stuff
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('MASTER_URL'))

wait = WebDriverWait(driver, 5)

# Email input
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')
                                                    )
                         ).send_keys(os.getenv("MASTER_LOGIN"))

# Password input
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')
                                                       )
                            ).send_keys(os.getenv("MASTER_PASSWORD"))

# Login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

# Oen brands page 
brands_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[9]')
                                                  )
                       ).click()

# Randonmly choose if its going to be Brands or Components
choose = 1#random.randint(1,2)
banana = 1
if choose == 1:
    
    # Asks the amount of brands to be created
    brand_input_str = get_user_input("How many?")
    brand_input_int = int(brand_input_str)
    for _ in range(brand_input_int):    
        
        # Randonmly choose the category type
        categ_type = random.randint(1,8)
    
        # Open category
        open_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[1]')
                                                        )
                            ).click()
        
        # Clicks at the add brand button
        add_brand_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[2]/div[1]')
                                                    )
                        ).click()
        
        # Inputs the brand image
        image_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[2]/label[2]')
                                                    )
                        ).click()
        
        time.sleep(1)
        
        pyautogui.write(image_path)
        pyautogui.press('enter')
        
        # Input the brand title
        title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="title"]')
                                                    )
                        ).send_keys(f"Marca {banana}")

        # Clicks at the register button
        register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[1]/div/button[2]')
                                                  )
                       ).click()
        
        time.sleep(2)        
        
        # Confirm brand creation
        done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/button')
                                                  )
                       ).click()
            
        """switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.esbzDM')
                                                  )
                       ).click()"""
        
        # Closes category
        close_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[1]')
                                                        )
                            ).click()

        banana += 1
        
elif choose == 2:
    
    # Opens components page
    components_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div[2]')
                                                  )
                       ).click()
    
    # Ask how many components to be create
    components_amount_str = get_user_input("How many?")
    components_amount_int = int(components_amount_str)
    for _ in range(components_amount_int):
        
        # Opens the component create modal
        add_component = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/button')
                                                  )
                       ).click()

        # Inputs component title       
        component_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="title"]')
                                                  )
                       ).send_keys(f"Componente {banana}")
        
        # Register the component
        register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[5]/form/div[1]/div/button[2]')
                                                  )
                       ).click()
        
        # Confirm the component creation
        done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[5]/div/button')
                                                  )
                       ).click()
        
        """switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.esbzDM')
                                                  )
                       ).click()"""
        
        time.sleep(1.3)
        banana += 1
        
get_user_input("DONE")
# Close the browser
driver.quit()
