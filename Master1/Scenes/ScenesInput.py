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

# Input email
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')
                                                    )
                         ).send_keys(os.getenv("MASTER_LOGIN"))

# Input password
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')
                                                       )
                            ).send_keys(os.getenv("MASTER_PASSWORD"))

# Click at the login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

# Open scnes page
scnes_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[7]')
                                                  )
                       ).click()

# Asks the amount of scenes
scnes_amount_str = get_user_input("How many scenes?")
scnes_amount_int = int(scnes_amount_str)
for _ in range(scnes_amount_int):
    
    # Open the register a scene modal
    register_scene = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div/div/button')
                                                  )
                       ).click()
    
    # Input image
    scene_image = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[2]/label[2]')
                                                  )
                       ).click()
    time.sleep(1.3)
    image_path = get_user_input("Image path")
    pyautogui.write(image_path)
    pyautogui.press('enter')
    
    # Ask scene title
    title_input = get_user_input("Scene tilte")
    
    # Input title
    title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="title"]')
                                                  )
                       ).send_keys(title_input)
    
    # Open category dropdown
    categ_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[4]/div')
                                                  )
                       ).click()
    
    # Ask the category type
    categ_type = get_user_input("(Carros, Motos, Trucks, Race, Drag, Peças, Serviços, Clássicos").title()

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
    
    # Select the category                
    categ_select = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[3]/form/div[4]/div[2]/div[{num}]')
                                                )
                    ).click()

    # Close category dropdown
    categ_close_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[4]/div[1]')
                                                  )
                       ).click()
    
    # Open type dropdown
    type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[6]/div/div')
                                                )
                    ).click()
    
    # Ask the type
    type_input = get_user_input("Eventos, Notícias, Vídeos").title()

    category_map = {
        "Eventos": 1,
        "Notícias": 2,
        "Vídeos": 3
    }

    num2 = category_map.get(type_input)
  
    # Select the type
    type_select = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[3]/form/div[6]/div/div[2]/div[{num2}]')
                                                )
                    ).click()
    
    # Ask for a link
    link_input = get_user_input("Scene link")
    
    # Input link
    link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link"]')
                                                  )
                       ).send_keys(link_input)

    # Ask description
    description_input = get_user_input("Scene description")
    
    # Input descriptio
    description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="description"]')
                                                  )
                       ).send_keys(description_input)
    
    # Click at the register page
    register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[1]/div/button[2]')
                                                )
                    ).click()
    
    # Confirms the scene creation
    done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/button')
                                                )
                    ).click()
    
    """open_scene_choise = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{num2}]/div[1]')
                                                )
                    ).click()
    
    time.sleep(1)
    
    switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.esbzDM')
                                                  )
                       ).click()
    
    time.sleep(1)
    
    close_scene_choise = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{num2}]/div[1]')
                                                )
                    ).click()"""
    
get_user_input("DONE")
# Close the browser
driver.quit()
