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

# Login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

# Open brands page 
brands_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[7]')
                                                  )
                       ).click()

#        
components_page = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fyxKfL'))
                        ).click()
    
time.sleep(1)

count = 0

components_list = ["Motor", "Câmbio", "Freios", "Suspensão", "Embreagem", "Radiador", "Bateria", "Alternador", "Filtro de ar", "Filtro de óleo", "Filtro de combustível", "Velas de ignição", "Injeção eletrônica", "Correia dentada", "Correia do alternador", "Bomba de água", "Bomba de combustível", "Sistema de escape", "Catalisador", "Amortecedores", "Molas", "Barra estabilizadora", "Semi-eixo", "Diferencial", "Eixo cardã", "Caixa de direção", "Volante", "Painel de instrumentos", "Airbag", "Sistema de som", "Faróis", "Lanternas", "Pisca-pisca", "Retrovisores", "Limpadores de para-brisa", "Para-brisas", "Para-choques", "Bancos", "Tapetes", "Vidros elétricos", "Travas elétricas", "Central multimídia", "Antena", "Tanque de combustível", "Macaco hidráulico", "Estepe", "Chave de roda", "Fusíveis", "Chicote elétrico", "Sistema de ar-condicionado", "Compressor de ar", "Condensador", "Evaporador", "Ventoinha", "Mangueiras", "Juntas homocinéticas", "Pastilhas de freio", "Discos de freio", "Tambor de freio", "Cilindro mestre", "Cilindro de roda", "Freio de mão", "Pedal de freio", "Pedal de embreagem", "Pedal do acelerador", "Roda", "Pneus", "Calotas", "Cubos de roda", "Rolamento de roda", "Terminais de direção", "Braços oscilantes", "Braços de controle", "Bandejas de suspensão", "Barra de torção", "Bielas", "Pistões", "Válvulas", "Cabeçote", "Coletor de admissão", "Coletor de escape", "Juntas do motor", "Sonda lambda", "Sensor de temperatura", "Sensor de rotação", "Sensor de detonação", "Sensor de oxigênio", "Módulo de injeção", "Chicote do motor", "Vareta de óleo", "Tampa de válvulas", "Válvula termostática", "Sensor de velocidade", "Reservatório de expansão", "Tampão do radiador", "Bomba de direção hidráulica", "Direção elétrica", "Volante do motor", "Eletroventilador", "Reservatório de óleo de freio", "Catalisador", "Silencioso", "Ponteira de escape", "Módulo ABS", "ECU (Unidade de Controle Eletrônico)", "Alarme", "Cintos de segurança", "Tapetes", "Acendedor de cigarros", "Palhetas do limpador", "Reservatório de água do limpador", "Interruptores de luz", "Relés", "Interruptor de ignição", "Chave de ignição", "Regulador de voltagem", "Transmissão automática", "Transmissão manual", "Conversor de torque", "Discos de embreagem", "Conjunto de embreagem", "Volante bimassa", "Unidades de controle", "Interruptor de luz de freio", "Interruptor de luz de ré", "Caixa de fusíveis", "Rede CAN", "Sensor MAF", "Sensor MAP", "Sensor de fluxo de ar", "Cabos de vela", "Distribuidor", "Rotor do distribuidor", "Bobina de ignição", "Interruptor do pedal de freio", "Servo-freio", "Comando de válvulas", "Polias", "Correia de acessórios", "Suporte do motor", "Batentes de suspensão", "Coifas de semi-eixo", "Junta de cabeçote", "Anéis de pistão", "Turbocompressor", "Intercooler", "Radiador de óleo", "Tubulações de ar condicionado", "Compressor de ar condicionado", "Válvula EGR", "Bloco do motor", "Carter", "Biela", "Comando de válvulas", "Tuchos", "Balanceiros", "Virabrequim", "Cabeçote", "Velas de aquecimento", "Eletrodo de ignição", "Turbina", "Injetores de combustível", "Bicos injetores", "Reservatório de óleo", "Caixa de marchas", "Haste de válvulas", "Carcaça do diferencial", "Juntas de homocinética", "Junta de cabeçote", "Juntas de vedação", "Retentores", "Mangueiras de água", "Mangueiras de óleo", "Abraçadeiras", "Cintas de fixação", "Painel de fusíveis", "Interruptor de ignição", "Comutador de ignição", "Caixa de direção hidráulica", "Caixa de direção elétrica", "Válvulas de admissão", "Válvulas de escape", "Resfriador de óleo", "Válvula de pressão", "Radiador de ar", "Sensor de pressão de óleo", "Sensor de nível de óleo", "Junta de cárter", "Junta de admissão", "Junta de escape", "Junta de vedação de válvulas", "Pinhão", "Coroa do diferencial", "Rolamentos do diferencial", "Eixo de transmissão", "Buchas de suspensão", "Amortecedor de direção", "Barra Panhard", "Coluna de direção", "Junta universal", "Tubos de escape", "Mola pneumática", "Suspensão a ar", "Disco de freio ventilado", "Disco de freio sólido", "Pinças de freio", "Mangueira de freio", "Conjunto de pedal de freio", "Suspensão McPherson", "Barra de direção", "Cremalheira de direção", "Engrenagem de direção", "Mecanismo de fechamento de portas", "Sensor de estacionamento", "Sistema de navegação", "Câmera de ré", "Retrovisor interno", "Controle de tração", "Controle de estabilidade", "Sensor de ângulo de direção", "Airbag lateral", "Airbag de cortina", "Sensor de impacto", "Módulo de airbag", "Correia do alternador", "Correia do compressor de ar", "Tensionador de correia", "Rolo guia", "Rolo tensor", "Disco de embreagem", "Placa de pressão", "Volante de inércia", "Carcaça da embreagem", "Atuador de embreagem", "Prato de pressão", "Eixo piloto", "Eixo secundário", "Diferencial traseiro", "Diferencial dianteiro", "Capô", "Porta-malas", "Porta", "Para-lama", "Painel traseiro", "Paralama traseiro", "Soleira", "Longarina", "Painel de instrumentos", "Interruptor de farol", "Botão de alarme", "Módulo de travamento", "Módulo de conforto", "Chicote do veículo", "Fusíveis principais", "Caixa de distribuição elétrica", "Relés de proteção", "Bateria auxiliar", "Sensor de temperatura do ar", "Sensor de temperatura do motor", "Sensor de nível de combustível", "Flutuador de combustível", "Medidor de combustível", "Bomba de óleo", "Bomba de vácuo", "Bomba de água auxiliar", "Polia do virabrequim", "Polia do comando", "Polia do alternador", "Polia do compressor", "Bico de injeção", "Sensores de admissão", "EGR (Recirculação de Gases de Exaustão)", "Tampa do tanque de combustível", "Travão de estacionamento", "Cabo de acelerador", "Sensor de posição do acelerador", "Módulo de controle do motor", "Conector OBD", "Interface de diagnóstico", "Interruptor do pedal de embreagem", "Válvula do tanque de combustível", "Mangueira do tanque", "Filtro de combustível", "Unidade de controle de combustível", "Rampa de injeção", "Sensor de detonação", "Sensor de fase", "Regulador de pressão de combustível", "Unidade de controle do ar condicionado", "Sensor de pressão do turbo", "Manômetro de óleo", "Medidor de temperatura do óleo", "Indicador de marcha", "Luz de aviso do airbag", "Luz de advertência de combustível", "Relógio digital", "Medidor de tensão", "Módulo de controle de faróis", "Relé de faróis", "Interruptor de luz de ré", "Sensor de velocidade da roda", "Sensor de rotação do motor", "Válvula solenóide", "Sensor de pressão do ar condicionado", "Termostato", "Sensor de posição do comando de válvulas", "Sensor de fluxo de ar", "Sonda lambda", "Catalisador", "Silenciador intermediário", "Silenciador traseiro", "Braço de controle inferior", "Braço de controle superior", "Mola de suspensão traseira", "Mola de suspensão dianteira", "Amortecedor traseiro", "Amortecedor dianteiro", "Barra estabilizadora traseira", "Barra estabilizadora dianteira", "Braço oscilante traseiro", "Braço oscilante dianteiro", "Bieleta da barra estabilizadora", "Pivô de suspensão", "Coxim do motor", "Coxim da transmissão", "Kit de amortecedor", "Kit de embreagem", "Suporte do radiador", "Suporte do motor", "Suporte da transmissão", "Cinto de segurança dianteiro", "Cinto de segurança traseiro", "Trava de capô", "Fecho do capô", "Cilindro mestre de freio", "Servo-freio", "Válvula de controle de ar", "Solenoide de partida", "Motor de partida", "Sensor de posição do virabrequim", "Relé de partida", "Bateria do controle remoto", "Sistema de acesso sem chave", "Receptor do controle remoto", "Central de travamento", "Central de conforto", "Módulo de controle do ABS", "Módulo de controle do ESP", "Módulo de controle da transmissão", "Módulo de controle do motor", "Módulo de controle da injeção", "Módulo de controle do airbag", "Módulo de controle da direção elétrica", "Módulo de controle de portas", "Módulo de controle de janelas", "Módulo de controle de iluminação", "Módulo de controle do teto solar", "Módulo de controle do espelho retrovisor", "Módulo de controle da câmera de ré", "Módulo de controle do sensor de estacionamento", "Módulo de controle do sistema de som", "Antena de rádio", "Conjunto de alto-falantes", "Tweeter", "Subwoofer"]

# Asks the amount of brands to be created
brand_input_str = get_user_input("How many?")
brand_input_int = int(brand_input_str)
for _ in range(brand_input_int):    
    
    # Click the add button
    add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'.fsHaFl'))
                        ).click()
        
    # Add tittle
    title = wait.until(EC.element_to_be_clickable((By.ID, 'title'))
                       ).send_keys(f'{components_list[count]}')

    # Click the register button
    register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dskIoT'))
                        ).click()
    
    # Close modal
    sucess = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[5]/div/button'))
                        ).click()
    
    # Activate the component
    activate = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.esbzDM'))
                           ).click()
    
    count += 1
    
    time.sleep(1)  

get_user_input("DONE")
# Close the browser
driver.quit()
