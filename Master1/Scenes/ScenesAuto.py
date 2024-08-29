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

# Sets images path
image_paths_string  = os.getenv('IMAGE_PATHS')
image_paths = image_paths_string.split(',')

count = 1

# Input email
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')
                                                    )
                         ).send_keys(os.getenv("MASTER_LOGIN"))

# Input password
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')
                                                       )
                            ).send_keys(os.getenv("MASTER_PASSWORD"))

# Click the login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

# Opens the scnes page
scnes_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[5]')
                                                  )
                       ).click()

# Ask how mant scenes are going to be created
scnes_amount = int(get_user_input("How many scenes?"))

count_ev = 1
count_no = 1
count_vi = 1

for _ in range(scnes_amount):
    
    # Opens the register scene button
    register_scene = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div/div/button'))
                                ).click()
    
    # Input image
    scene_image = wait.until(EC.presence_of_element_located((By.ID, 'image'))
                             ).send_keys(random.choice(image_paths))
    time.sleep(1.3)

    # Random type
    type_ = random.randint(1, 3)
    
    title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="title"]')))
    
    description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="description"]')))
    
    if type_ == 1:
        # Input title
        title.send_keys(f"Evento {count_ev}")
        description.send_keys(f'Descrição evento {count_ev}')
        count_ev += 1  
    elif type_ == 2:
        # Input title
        title.send_keys(f"Notícia {count_no}")
        description.send_keys(f'Descrição notícia {count_no}')
        count_no += 1  
    elif type_ == 3:
        # Input title
        title.send_keys(f"Vídeo {count_vi}")
        description.send_keys(f'Descrição vídeo {count_vi}')
        count_vi += 1  

    # Open the category dropdown
    categ_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[4]/div'))
                                ).click()
    
    # Random category
    categ_type = random.randint(1, 8)
    
    # Select the random category                                                           
    categ_select = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[3]/form/div[4]/div[2]/div[{categ_type}]'))
                              ).click()

    # Close category dropdown
    categ_close_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[4]/div[1]'))
                                      ).click()
    
    # Opens the type dropdown
    type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[6]/div/div'))
                               ).click()
  
    # Select the random type
    type_select = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[3]/form/div[6]/div/div[2]/div[{type_}]'))
                             ).click()

    videos = ['https://www.youtube.com/watch?v=XpvladeVFq4','https://www.youtube.com/watch?v=mcaLnV15_8U&t=127s','https://www.youtube.com/watch?v=O0cs8aIXgkc',
              'https://www.youtube.com/watch?v=14r73tVLD5A', 'https://www.youtube.com/watch?v=pQaG0ay957M']
    
    i = random.randint(0,4)
    
    # Input link
    link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link"]'))
                      ).send_keys(videos[i])

    
    
    # Register button
    register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[1]/div/button[2]'))
                          ).click()
    
    # Confirms the scene creation
    done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/button'))
                      ).click()
    
    """open_scene_choice = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{type_}]/div[1]'))
                                   ).click()
    
    time.sleep(1)
    
    switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.esbzDM'))
                        ).click()
    
    time.sleep(0.5)
    
    close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dbdqeU'))
                       ).click()
    
    time.sleep(0.5)
    
    close2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.kVnpAj'))
                        ).click()
    
    close_scene_choice = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{type_}]/div[1]'))
                                    ).click()"""
    
    count += 1 
    
    time.sleep(0.5)
    
get_user_input("DONE")
# Close the browser
driver.quit()