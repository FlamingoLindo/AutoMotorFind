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
import pyautogui
load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

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

# Clicks the login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

# Opens the brands page
brands_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[9]')
                                                  )
                       ).click()

# Ask wich option
choose = get_user_input("Brand(1) or Component(2)").title()

# User choose "BRAND"
if choose == "Brand" or choose == "1":
    
    # Ask what type of category
    categ_type = get_user_input("Carros, Motos, Trucks, Race, Drag, Peças, Serviços, Clássicos").title()
    category_map = {
        "Carros": 1,
        "Motos": 2,
        "Trucks": 3,
        "Race": 4,
        "Drag": 5,
        "Peças": 6,
        "Serviços": 7,
        "Clássicos": 8
    }

    num = category_map.get(categ_type)
        
    open_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{num}]/div[1]')
                                                    )
                        ).click()
    
    # Ask amount of brands to be created
    brand_input_str = get_user_input("How many brands?")
    brand_input_int = int(brand_input_str)
    for _ in range(brand_input_int):    
        
        # Opens the brand creation modal
        add_brand_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{num}]/div[2]/div[1]')
                                                    )
                        ).click()
        
        # Inputs the brand image
        image_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[2]/label[2]')
                                                    )
                        ).click()
        
        time.sleep(1)
        
        image_path = get_user_input("Image path")
        pyautogui.write(image_path)
        pyautogui.press('enter')
        
        # Inputs the brand title
        title_input = get_user_input("Title")
        title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="title"]')
                                                    )
                        ).send_keys(title_input)
                                                      
        # Registers the brand              
        register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[1]/div/button[2]')
                                                  )
                       ).click()
        
        # Confirms the brand creation
        done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/button')
                                                  )
                       ).click()
        
        """time.sleep(1.3)
        
        switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.esbzDM')
                                                  )
                       ).click()"""
        
        time.sleep(1.3)
        
# User choose "COMPONENT"
elif choose == "Component" or choose == "2":
    
    # Opens the components page
    components_page = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div[2]')
                                                  )
                       ).click()
    
    # Asks how many components are going to be created
    components_amount_str = get_user_input("How many components?")
    components_amount_int = int(components_amount_str)
    for _ in range(components_amount_int):
        
        # Opens the creation component modal
        add_component = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/button')
                                                  )
                       ).click()

        # Inputs the component title
        component_title_input = get_user_input("Title")
        component_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="title"]')
                                                  )
                       ).send_keys(component_title_input)
        
        # Clicks the register button
        register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[5]/form/div[1]/div/button[2]')
                                                  )
                       ).click()
        
        # Confirms the component creation
        done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[5]/div/button')
                                                  )
                       ).click()
        
        """time.sleep(1.3)
        
        switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.esbzDM')
                                                  )
                       ).click()"""
        
        time.sleep(1.3)

get_user_input("DONE")
# Close the browser
driver.quit()
