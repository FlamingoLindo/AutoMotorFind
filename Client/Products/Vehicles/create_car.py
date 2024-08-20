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
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.hygPet')
                                                        )
                            ).click() 

    # Input login
    login_input = wait.until(EC.element_to_be_clickable((By.ID, 'email')
                                                        )
                            ).send_keys('mingau@gmail.com')

    # Input password
    password_input = wait.until(EC.element_to_be_clickable((By.ID, 'password')
                                                        )
                            ).send_keys('12345678')

    # Logs in 
    do_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eaqkjo')
                                                        )
                            ).click() 
except Exception as e:
    print('There has been an error on the login')
    print(e)

try:
    count = 1
    
    # Click options
    options = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bNVGjx')
                                                        )
                            ).click() 

    # Click my profile option
    my_sales_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[2]')
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
        
        # Click type option 1
        type_vehicle = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@id='react-select-2-option-0']")
                                                            )
                                ).click()
        
        # Product name
        name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                            )
                                ).send_keys(f'Auto Car {count}')
        
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
        car_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-3-option-0']")
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
        is_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-5-option-0']")
                                                            )
                                ).click()
        
        # 
        negociation_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[8]/div/div')
                                                            )
                                ).click()
        
        # 
        negociation_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-6-option-0']")
                                                            )
                                ).click()
        
        # 
        address_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[9]/div/div')
                                                            )
                                ).click()
        
        # 
        adress_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-7-option-0']")
                                                            )
                                ).click()
        
        # Sets images path
        vehicles_paths_string  = os.getenv('CAR_IMAGES')
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
            
        # 
        details_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/button[2]")
                                                            )
                                ).click()
        
        # 
        brand_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div')
                                                            )
                                ).click()
        
        # 
        brand_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-8-option-0']")
                                                            )
                                ).click()
        
        # 
        rand_km = random.randint(0,1000)
        km = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kilometers"]')
                                                            )
                                ).send_keys(rand_km)
        
        # 
        rand_year = random.randint(1900,2024)
        year = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="year"]')
                                                            )
                                ).send_keys(rand_year)
        
        # 
        color_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]/div[4]/div/div')
                                                            )
                                ).click()
        
        # 
        rand_color = random.randint(0,4)
        brand_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@id='react-select-9-option-{rand_color}']")
                                                            )
                                ).click()
        
        # 
        rand_speed = random.randint(5,600)
        speed = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="topSpeed"]')
                                                            )
                                ).send_keys(rand_speed)
        
        # 
        rand_torq = random.randint(1,5000)
        torq = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="torque"]')
                                                            )
                                ).send_keys(rand_torq)
        
        # 
        rand_power = random.randint(1,5000)
        power = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="power"]')
                                                            )
                                ).send_keys(rand_power)
        
        #
        link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link"]')
                                                            )
                                ).send_keys('https://motorfind-client.netlify.app/manageproduct/add')
        
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
        
        count += 1
except Exception as e:
    print('There has been an error opening products creation page')
    print(e)

    

    
    
get_user_input("DONE")
# Close the browser
driver.quit()
