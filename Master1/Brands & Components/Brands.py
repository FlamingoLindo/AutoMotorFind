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

# Driver stuff
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

# Sets images path
car_image_paths_string  = os.getenv('CAR_LOGOS')
car_image_paths = car_image_paths_string.split(',')

bike_image_paths_string  = os.getenv('BIKE_LOGOS')
bike_image_paths = bike_image_paths_string.split(',')

truck_image_paths_string  = os.getenv('TRUCK_LOGOS')
truck_image_paths = truck_image_paths_string.split(',')

race_image_paths_string  = os.getenv('RACE_LOGOS')
race_image_paths = race_image_paths_string.split(',')

drag_image_paths_string  = os.getenv('DRAG_LOGOS')
drag_image_paths = drag_image_paths_string.split(',')

part_image_paths_string  = os.getenv('PARTS_LOGOS')
part_image_paths = part_image_paths_string.split(',')

service_image_paths_string  = os.getenv('SERVICE_LOGOS')
service_image_paths = service_image_paths_string.split(',')

classic_image_paths_string  = os.getenv('CLASSIC_LOGOS')
classic_image_paths = classic_image_paths_string.split(',')

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

# Open brands page 
brands_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[9]')
                                                  )
                       ).click()

count_car = 1
count_bikes = 1
count_trucks = 1 
count_race = 1
count_drag = 1
count_parts = 1
count_service = 1
count_classic = 1

# Randonmly choose the category type
categ_type = 8#random.randint(1,8)
        
#
cate_menu = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[1]'))
                        ).click()
    
time.sleep(1)
    
# Asks the amount of brands to be created
brand_input_str = get_user_input("How many?")
brand_input_int = int(brand_input_str)
for _ in range(brand_input_int):    
    
    # Click the add button
    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[2]/div[1]'))
                        ).click()
        
    # Finds tittle element
    title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="title"]')))

    if categ_type == 1:
        # Input title
        title.send_keys(f"Car brand {count_car}")
        
        # Send random car image
        car_images = wait.until(EC.presence_of_element_located((By.ID, 'image'))
                             ).send_keys(random.choice(car_image_paths))
        
        # Add 1 to car count
        count_car += 1  
            
    elif categ_type == 2:
        # Input title
        title.send_keys(f"Bike brand {count_bikes}")
        
        # Send random bike image
        bike_image = wait.until(EC.presence_of_element_located((By.ID, 'image'))
                             ).send_keys(random.choice(bike_image_paths))
        
        # Add 1 to bike count
        count_bikes += 1  
            
    elif categ_type == 3:
        # Input title
        title.send_keys(f"Truck brand {count_trucks}")
        
        # Send random truck image
        truck_image = wait.until(EC.presence_of_element_located((By.ID, 'image'))
                             ).send_keys(random.choice(truck_image_paths))
        
        # Add 1 to truck count
        count_trucks += 1
    
    elif categ_type == 4:
        # Input title
        title.send_keys(f"Race brand {count_race}")
        
        # Send random race image
        race_image = wait.until(EC.presence_of_element_located((By.ID, 'image'))
                             ).send_keys(random.choice(race_image_paths))
        
        # Add 1 to race count
        count_race += 1 
        
    elif categ_type == 5:
        # Input title
        title.send_keys(f"Drag brand {count_drag}")
        
        # Send random drag image
        drag_image = wait.until(EC.presence_of_element_located((By.ID, 'image'))
                             ).send_keys(random.choice(drag_image_paths))
        
        # Add 1 to drag count
        count_drag += 1 
        
    elif categ_type == 6:
        # Input title
        title.send_keys(f"Parts brand {count_parts}")
        
        # Send random part image
        part_image = wait.until(EC.presence_of_element_located((By.ID, 'image'))
                             ).send_keys(random.choice(part_image_paths))
        
        # Add 1 to part count
        count_parts += 1 
        
    elif categ_type == 7:
        # Input title
        title.send_keys(f"Service brand {count_service}")
        
        # Send random service image
        service_image = wait.until(EC.presence_of_element_located((By.ID, 'image'))
                             ).send_keys(random.choice(service_image_paths))
        
        # Add 1 to service count
        count_service += 1 
        
    elif categ_type == 8:
        # Input title
        title.send_keys(f"Classic brand {count_classic}")
        
        # Send random classic image
        classic_image = wait.until(EC.presence_of_element_located((By.ID, 'image'))
                             ).send_keys(random.choice(classic_image_paths))
        
        # Add 1 to classic count
        count_classic += 1 
    
    # Click save button
    save = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.kCJSfW'))
                           ).click()
    
    # Close modal
    sucess = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.kVnpAj'))
                           ).click()

    # Activate brand                                                                                                       
    activate = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'.esbzDM'))
                           ).click()
    
    time.sleep(1)
                                   
get_user_input("DONE")
# Close the browser
driver.quit()
