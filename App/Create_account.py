import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

import time
from Functions.cpf import gera_e_valida_cpf
from Functions.cnpj import gera_cnpj

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='pt',
    locale='BR',
)


appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def swipe_to_end(self):
        self.driver.swipe(start_x=500, start_y=1600, end_x=500, end_y=700, duration=100)

    def test_create_account(self) -> None:
        el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="motorfind"]'))
        )
        el.click()

        register_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Cadastrar"]'))
        ).click()

        name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Ex. José Santos"]'))
        )
        name.send_keys("Nome")

        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Ex. nome@email.com"]'))
        )
        email.send_keys("email@gmail.com")

        phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="(00) 9 1234-56789"]'))
        )
        phone.send_keys("11987456321")

        next_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Próximo"]/android.view.ViewGroup/android.view.View'))
        ).click()

        time.sleep(1.5)
        
        cpf = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="000.000.000-00"]'))
        )
        cpf.send_keys(gera_e_valida_cpf())  
        
        cnpj = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="00.000.000/0000-00"]'))
        )
        cnpj.send_keys(gera_cnpj())  
        
        phone2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="(00) 9 1234-56789"]'))
        )
        phone2.send_keys('11923847569')
        
        next_btn2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'))
        ).click()
        time.sleep(1.5)
        
        cep = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="00000-000"]'))
        )
        cep.send_keys('39408197')
        
        num = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Número"]'))
        )
        num.send_keys('1')
        
        self.driver.swipe(start_x=500, start_y=1600, end_x=500, end_y=700, duration=100)

        next_btn3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View")'))
        ).click()

        password1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.EditText[@text="Senha@!23"])[1]'))
        )
        password1.send_keys('Aa12345678!')
        
        # Open password confirmation
        self.driver.tap([(500, 830)], 100)
        time.sleep(0.6)
        # A
        self.driver.tap([(111, 1884)])
        # a
        self.driver.tap([(111, 1884)])
        # 1
        self.driver.tap([(70, 1596)])
        # 2
        self.driver.tap([(164, 1596)])
        # 3
        self.driver.tap([(270, 1596)])
        # 4
        self.driver.tap([(382, 1596)])
        # 5
        self.driver.tap([(480, 1600)])
        # 6
        self.driver.tap([(580, 1600)])
        # 7
        self.driver.tap([(680, 1600)])
        # 8
        self.driver.tap([(780, 1600)])
        # shift
        self.driver.tap([(90, 2027)])
        # !
        self.driver.tap([(70, 1596)])

        # Close keyboard
        self.driver.tap([(720, 1160)], 100)

        """password2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'android.view.ViewGroup'))
        )
        password2.send_keys('Aa12345678!')"""

        next_btn4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'))
        ).click()

        car = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Carros"]/android.view.View'))
        ).click()

        classic = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Clássicos"]/android.view.ViewGroup'))
        ).click()

        restored = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Restaurados OEM"]/android.view.ViewGroup'))
        ).click()

        lane = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Pista"]/android.view.ViewGroup'))
        ).click()

        race = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Race"]/android.view.ViewGroup'))
        ).click()

        bikes = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Motos"]/android.view.ViewGroup'))
        ).click()
        
        drift = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Drift"]/android.view.ViewGroup'))
        ).click()

        black = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Placa preta"]/android.view.ViewGroup'))
        ).click()

        next_btn5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(8)'))
        ).click()

        agree = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup'))
        ).click()

        done_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View")'))
        ).click()

if __name__ == '__main__':
    unittest.main()