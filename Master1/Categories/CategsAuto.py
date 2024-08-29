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

def register():
    register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[2]/button[2]')
                                                    )
                        ).click()   
    
    done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/button')
                                                    )
                        ).click() 
    
count = 0

car_sub = ["Sedan", "Hatchback", "SUV (Sport Utility Vehicle)", "Coupé", "Conversível", "Perua (Station Wagon)", "Minivan", "Picape", "Crossover", "Roadster", "Cabriolet", "SUV compacto", "SUV médio", "SUV grande", "Coupé esportivo", "Sedan de luxo", "Hatchback compacto", "Hatchback médio", "Hatchback esportivo", "Sedan compacto", "Sedan médio", "Sedan grande", "Van", "Carro elétrico", "Carro híbrido", "Carro a diesel", "Carro a gasolina", "Carro flex", "Carro conceito", "Superesportivo", "Muscle car", "Carro compacto", "Carro médio", "Carro de luxo", "Carro off-road", "Carro urbano", "SUV de luxo", "Sedan executivo", "Hatchback de entrada", "Coupé de quatro portas", "Carro esportivo", "Veículo utilitário"]
bike_sub = ["Esportiva", "Naked", "Custom", "Chopper", "Cruiser", "Touring", "Sport Touring", "Adventure", "Trail", "Dual Sport", "Enduro", "Motocross", "Supermoto", "Scooter", "Café Racer", "Bobber", "Street", "Retrô", "Scrambler", "Pocket Bike", "Mini Moto", "Trial", "Sidecar", "Quadriciclo", "Triciclo", "Motoneta", "Maxi Scooter", "Crossover", "Bobber", "Tourer", "Moto elétrica", "Moto de entrada", "Moto de médio porte", "Moto de alta cilindrada"]
truck_sub = ["Truck tradicional", "Truck de carga pesada", "Truck de carga leve", "Truck de reboque", "Truck de plataforma", "Truck baú", "Truck frigorífico", "Truck cegonheiro", "Truck de construção", "Truck de tanque", "Truck de entrega", "Truck off-road", "Truck agrícola", "Truck de combustível", "Truck de transporte de contêiner", "Truck de resíduos", "Truck de mineração", "Truck de transporte de veículos", "Truck de pipa", "Truck de mudança", "Truck de bombeiro", "Truck de guincho", "Truck de alimentos", "Truck de carga geral", "Truck de logística", "Truck com carroceria aberta", "Truck com carroceria fechada", "Truck de transporte de carga seca", "Truck de transporte de carga refrigerada", "Truck de transporte de líquidos", "Truck de transporte de cargas especiais"]
race_sub = ["Fórmula 1", "Fórmula E", "MotoGP", "Rali", "IndyCar", "NASCAR", "DTM (Deutsche Tourenwagen Masters)", "WRC (World Rally Championship)", "Superbike", "Endurance", "Le Mans", "Kart", "Drag Racing", "Touring Car", "Stock Car", "Rally Cross", "Sprint Car", "Oval Racing", "Off-road Racing", "Hill Climb", "Time Attack", "Track Day", "Racing Simulator", "Club Racing", "Formula 2", "Formula 3", "Formula Ford", "Super Trucks", "Classic Car Racing", "Historic Racing", "Road Racing", "Electric Racing", "Prototype Racing"]
parts_sub = ["Motor", "Câmbio", "Freios", "Suspensão", "Embreagem", "Radiador", "Bateria", "Alternador", "Filtro de ar", "Filtro de óleo", "Filtro de combustível", "Velas de ignição", "Injeção eletrônica", "Correia dentada", "Correia do alternador", "Bomba de água", "Bomba de combustível", "Sistema de escape", "Catalisador", "Amortecedores", "Molas", "Barra estabilizadora", "Semi-eixo", "Diferencial", "Eixo cardã", "Caixa de direção", "Volante", "Painel de instrumentos", "Airbag", "Sistema de som", "Faróis", "Lanternas", "Pisca-pisca", "Retrovisores", "Limpadores de para-brisa", "Para-brisas", "Para-choques", "Bancos", "Tapetes", "Vidros elétricos", "Travas elétricas", "Central multimídia", "Antena", "Tanque de combustível", "Macaco hidráulico", "Estepe", "Chave de roda", "Fusíveis", "Chicote elétrico", "Sistema de ar-condicionado", "Compressor de ar", "Condensador", "Evaporador", "Ventoinha", "Mangueiras", "Juntas homocinéticas", "Pastilhas de freio", "Discos de freio", "Tambor de freio", "Cilindro mestre", "Cilindro de roda", "Freio de mão", "Pedal de freio", "Pedal de embreagem", "Pedal do acelerador", "Roda", "Pneus", "Calotas", "Cubos de roda", "Rolamento de roda", "Terminais de direção", "Braços oscilantes", "Braços de controle", "Bandejas de suspensão", "Barra de torção", "Bielas", "Pistões", "Válvulas", "Cabeçote", "Coletor de admissão", "Coletor de escape", "Juntas do motor", "Sonda lambda", "Sensor de temperatura", "Sensor de rotação", "Sensor de detonação", "Sensor de oxigênio", "Módulo de injeção", "Chicote do motor"]
service_sub = ["Manutenção preventiva", "Manutenção corretiva", "Troca de óleo", "Troca de filtro", "Alinhamento", "Balanceamento", "Reparo de suspensão", "Troca de pastilhas de freio", "Reparo de freios", "Troca de pneus", "Troca de bateria", "Reparo de câmbio", "Troca de correias", "Reparo de motor", "Inspeção veicular", "Serviço de ar-condicionado", "Reparo de direção", "Troca de amortecedores", "Reparo de sistema de escape", "Limpeza de bico injetor", "Troca de velas de ignição", "Reparo de radiador", "Troca de bomba de combustível", "Ajuste de embreagem", "Troca de velas de aquecimento", "Reparo de direção hidráulica", "Troca de óleo de transmissão", "Reparo de diferencial", "Reparo de carroceria", "Restauração de pintura", "Serviço de polimento", "Lavagem de motor", "Desentupimento de sistema de combustível", "Reparo de sistemas elétricos", "Troca de sensores", "Reparo de iluminação", "Troca de para-brisa", "Inspeção de segurança", "Certificação de emissões", "Serviço de climatização", "Reparo de airbags", "Instalação de acessórios", "Reparo de sistema de navegação", "Ajuste de suspensão", "Reparo de transmissões automáticas", "Serviço de limpeza de filtros", "Troca de fluido de freio", "Serviço de diagnóstico computadorizado", "Alinhamento de faróis", "Reparo de eletrônica automotiva", "Troca de correia dentada", "Reparo de suspensão a ar", "Inspeção e manutenção de sistema de injeção", "Reparo de bombas de direção", "Serviço de manutenção preventiva"]
classic_sub = ["Clássicos dos anos 50", "Clássicos dos anos 60", "Clássicos dos anos 70", "Clássicos dos anos 80", "Clássicos dos anos 90", "Carros antigos restaurados", "Carros de corrida clássicos", "Carros esportivos clássicos", "Carros luxuosos clássicos", "Muscle cars clássicos", "Conversíveis clássicos", "Coupés clássicos", "Sedans clássicos", "Hatchbacks clássicos", "Peruas clássicas", "Pickups clássicas", "Clássicos europeus", "Clássicos americanos", "Clássicos japoneses", "Clássicos italianos", "Clássicos ingleses", "Clássicos alemães", "Carros vintage", "Carros pré-1940", "Carros clássicos de colecionador", "Carros clássicos de turismo", "Clássicos restaurados", "Clássicos com histórico de competição", "Clássicos com motor original", "Clássicos com modificações period correct", "Clássicos de luxo", "Clássicos de pequeno porte", "Clássicos de grande porte"]
drag_sub = ["Carro de Drag Racing", "Motocicleta de Drag Racing", "Dragster", "Top Fuel Dragster", "Funny Car", "Pro Stock", "Pro Mod", "Junior Dragster", "Street Legal", "Super Stock", "Bracket Racing", "Nostalgia Dragster", "Drag Racing Bike", "Turbocharged Dragster", "Nitro Dragster", "Electric Drag Racing", "Top Alcohol Dragster", "Funny Car Nitro", "Drag Racing Truck", "Drag Racing Coupe", "Drag Racing Sedan", "Drag Racing Roadster", "Turbocharged Pro Mod", "Blown Alcohol Dragster", "Supercharged Dragster", "Pro Street", "Drag Racing Series", "Drag Racing Event", "Drag Racing Team", "Drag Racing Car Parts", "Drag Racing Tires", "Drag Racing Wheels", "Drag Racing Suspension", "Drag Racing Engine", "Drag Racing Transmission", "Drag Racing Brakes", "Drag Racing Chassis", "Drag Racing Fuel System", "Drag Racing Exhaust", "Drag Racing Safety Gear", "Drag Racing Helmet", "Drag Racing Suit", "Drag Racing Gloves", "Drag Racing Shoes", "Drag Racing Parachute", "Drag Racing Seat", "Drag Racing Harness", "Drag Racing Roll Cage", "Drag Racing Fuel Cell", "Drag Racing Data Logger", "Drag Racing Timing System", "Drag Racing Track", "Drag Racing Pits", "Drag Racing Starting Line", "Drag Racing Finish Line", "Drag Racing Rules", "Drag Racing Regulations", "Drag Racing Categories", "Drag Racing Classes", "Drag Racing Records", "Drag Racing Tuning", "Drag Racing Adjustments", "Drag Racing Tactics", "Drag Racing Strategy", "Drag Racing Technology", "Drag Racing Innovations"]

#  Register car function
def register_car_catg():
    car_catg_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(car_sub[count])

    car_catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                    )
                        ).send_keys(f'Subcategoria {car_sub[count]}')
    
    register()

#  Register bike function
def register_bike_catg():
    bike = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(bike_sub[count])

    bike_catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                    )
                        ).send_keys(f'Subcategoria {bike_sub[count]}')

    register()

#  Register trucks function
def register_truck_catg():
    truck = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(truck_sub[count])

    truck_catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                    )
                        ).send_keys(f'Subcategoria {truck_sub[count]}')

    register()

#  Register race function
def register_race_catg():
    race = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(race_sub[count])

    race_catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                    )
                        ).send_keys(f'Subcategoria {race_sub[count]}')

    register()
    
#  Register drag function
def register_drag_catg():
    drag = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(drag_sub[count])

    drag_catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                    )
                        ).send_keys(f'Subcategoria {drag_sub[count]}')

    register()
    
#  Register parts function
def register_part_catg():
    part = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(parts_sub[count])

    part_catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                    )
                        ).send_keys(f'Subcategoria {parts_sub[count]}')

    register()

#  Register services function
def register_service_catg():
    service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(service_sub[count])

    service_catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                    )
                        ).send_keys(f'Subcategoria {service_sub[count]}')

    register()
    
#  Register classics function
def register_classic_catg():
    classic = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(classic_sub[count])

    classic_catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                    )
                        ).send_keys(f'Subcategoria {classic_sub[count]}')

    register()

# Driver stuff
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('MASTER_URL'))

wait = WebDriverWait(driver, 5)

# Inputs email
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')
                                                    )
                         ).send_keys(os.getenv("MASTER_LOGIN"))

# Inputs password
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')
                                                       )
                            ).send_keys(os.getenv("MASTER_PASSWORD"))

# Clicks the login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

# Opens the categories page
catgs_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[2]')
                                                  )
                       ).click()

time.sleep(0.5)

categ_type = int(get_user_input('Escolha a categoria: [1]Carros, [2]Motos, [3]Trucks, [4]Race, [5]Drag, [6]Peças, [7]Serviços, [8]Clássicos'))

# Randonmly choose the category type
#categ_type = 1#random.randint(1, 8)

# Ask how many categories are going to be created
categ_amount_str = get_user_input("How many categories?")
categ_amount_int = int(categ_amount_str)

# Open the categories page
open_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[1]/div[2]')
                                                )
                    ).click()

for _ in range(categ_amount_int):   
    
    # Opens the category creation modal
    add_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[2]/div[1]')
                                                    )
                        ).click()

    if categ_type == 1:
        register_car_catg()
        count += 1
    elif categ_type == 2:
        register_bike_catg()
        count += 1
    elif categ_type == 3:
        register_truck_catg()
        count += 1
    elif categ_type == 4:
        register_race_catg()
        count += 1
    elif categ_type == 5:
        register_drag_catg()
        count += 1
    elif categ_type == 6:
        register_part_catg()
        count += 1
    elif categ_type == 7:
        register_service_catg()
        count += 1
    elif categ_type == 8:
        register_classic_catg()
        count += 1
    else:
        print('No such category with inputed id')
    
    
    
    time.sleep(0.5)
    
get_user_input("DONE")
# Close the browser
driver.quit()
