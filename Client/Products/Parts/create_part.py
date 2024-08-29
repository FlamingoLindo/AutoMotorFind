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
import pyautogui
load_dotenv()

# Add the path to the directory containing the Functions module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..','..'))

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
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eAOppz')
                                                        )
                            ).click() 

    # Input login
    login_input = wait.until(EC.element_to_be_clickable((By.ID, 'email')
                                                        )
                            ).send_keys('caos@gmail.com')

    # Input password
    password_input = wait.until(EC.element_to_be_clickable((By.ID, 'password')
                                                        )
                            ).send_keys('12345678')

    # Logs in 
    do_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fAJeQq')
                                                        )
                            ).click() 
except Exception as e:
    print('There has been an error on the login')
    print(e)

try:
    count = 1
    
    time.sleep(2)
    
    # Click sales
    sales = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eAOppz')
                                                        )
                            ).click() 
    
    amount_str = get_user_input("How many?")
    amount_int = int(amount_str)
    for i in range(amount_int):
        
        # Click add product button
        add_prod_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/button[1]')
                                                            )
                                ).click()

        # Click add product button 2
        add_prod_btn2 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/button[1]')
                                                            )
                                ).click()
          
        # Click type dropdown
        type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div')
                                                            )
                                ).click()
        
        # Click type option 2
        type_part = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@id='react-select-2-option-1']")
                                                            )
                                ).click()
        
        # Product name
        name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                            )
                                ).send_keys(f'Auto Part {count}')
        
        # Product quantity
        rand_qnt = random.randint(100,999)
        quantity = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quantity"]')
                                                            )
                                ).send_keys(rand_qnt)
        
        # Product value
        rand_value = random.randint(100,1500)
        value = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="value"]')
                                                            )
                                ).send_keys(rand_value)
        
        # Click category dropdown
        category_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[5]/div[2]/div')
                                                            )
                                ).click()
        
        # Click category option 1 ("Carros")
        part_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-3-option-5']")
                                                            )
                                ).click()
        
        # 
        sub_category_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[6]/div[2]/div')
                                                            )
                                ).click()
        
        # 
        car_sub_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-4-option-0']")
                                                            )
                                ).click()
        
        # 
        product_is_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[7]/div/div')
                                                            )
                                ).click()
        
        # 
        random_is = random.randint(0,1)
        is_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@id='react-select-5-option-{random_is}']")
                                                            )
                                ).click()
        
        # 
        negociation_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[8]/div/div')
                                                            )
                                ).click()
        
        # 
        random_negociation = random.randint(0,1)
        negociation_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@id='react-select-6-option-{random_negociation}']")
                                                            )
                                ).click()
        
        #
        highlight_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[9]/div/div')
                                                            )
                                ).click()
        
        # 
        highlight_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-select-7-option-0']")
                                                            )
                                ).click()
        
        # Sets images path
        vehicles_paths_string  = os.getenv('PARTS_IMAGES')
        vehicles_image_paths = vehicles_paths_string.split(',')
        
        for _ in range(3):
            #
            image = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[2]/div[1]/div[2]/label/img')
                                                                )
                                    ).click()
            
            rand_img = random.choice(vehicles_image_paths)
            
            time.sleep(1)
            
            pyautogui.write(rand_img)
            
            time.sleep(1)
            
            pyautogui.press('enter')
            
            time.sleep(0.8)
            
        # 
        address_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[10]/div/div')
                                                            )
                                ).click()
        
        # 
        adress_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-8-option-0']")
                                                            )
                                ).click()
            
        # 
        details_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/button[2]")
                                                            )
                                ).click()
        
        # 
        brand_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div')
                                                            )
                                ).click()
        
        # 
        rand_brand = random.randint(0,2)
        brand_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@id='react-select-9-option-{rand_brand}']")
                                                            )
                                ).click()
            
        # 
        rand_year = random.randint(1900,2024)
        year = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="year"]')
                                                            )
                                ).send_keys(rand_year)
        
        # 
        color_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/div/div')
                                                            )
                                ).click()
        
        # 
        rand_color = random.randint(0,4)
        brand_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@id='react-select-10-option-{rand_color}']")
                                                            )
                                ).click()
        
        #
        rand_dim = random.randint(100, 999)
        dim = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dimensions"]')
                                                            )
                                ).send_keys(f'{rand_dim} cm {rand_dim} cm {rand_dim} cm')
        
        #
        rand_weight = random.randint(1, 999)
        weight = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="weight"]')
                                                            )
                                ).send_keys(rand_weight)
        
        #
        code = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="code"]')
                                                            )
                                ).send_keys(f'Auto code {count}')
        
        #
        desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="description"]')
                                                            )
                                ).send_keys(f'AUTOMATIC DESCRIPTION {count}')
        
        #
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[3]/button[1]")
                                                            )
                                ).click()
        
        time.sleep(5)
        
        pyautogui.press('f5')
        
        time.sleep(2)
        
        count += 1
except Exception as e:
    print('There has been an error opening products creation page')
    print(e)


get_user_input("DONE")
# Close the browser
driver.quit()
