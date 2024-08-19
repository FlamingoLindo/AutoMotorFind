import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import customtkinter as tk
from tkinter import simpledialog
import random
import time  
import os
import sys

from dotenv import load_dotenv
load_dotenv()

# Add the path to the directory containing the Functions module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Functions.Get_time import get_time

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

screenshot_dir = r'Images\Screenshot'
os.makedirs(screenshot_dir, exist_ok=True)
screenshot_path = os.path.join(screenshot_dir, 'screenshot.png')


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='flamingo_lindo',
    language='pt',
    printPageSourceOnFindFailure = True,
    eventTimings = True,
    noReset = True,
    enableMultiWindows = True,
    appPackage = 'com.mestresdaweb.motorfind',
    appActivity = 'com.mestresdaweb.motorfind.MainActivity'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_edit_account(self) -> None:
        count = 1
        
        try:
            # Wait untill the app has loaded
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'))
            )

            # Inputs the email
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("insira seu e-mail")'))
            ).send_keys(get_user_input("Email"))

            # Inputs the password
            password = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Insira sua senha")'))
            ).send_keys(get_user_input("Password"))
            
            # Button click
            next_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)'))
            ).click()
            
            time.sleep(1)
            
            print("First step done 🟢")
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot_path)
            print("There has been an error on the first step 🔴")
            print(e)
            raise 
        
        try:
            
            # Click chat icon
            chat_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button[5]'))
            ).click()
            
            time.sleep(1)
            
            # Click first chat
            first_chat = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(18)'))
            ).click()
            
            time.sleep(1)
            
            message_amount_str = get_user_input("How many messages?")
            message_amount_int = int(message_amount_str)
            for i in range(message_amount_int):
                # Type in chat
                chat = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.EditText'))
                )
                
                chat.send_keys(f'Message: {count} ', get_time())
                
                # Send messages
                send_message = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'))
                )
                
                send_message.click() 
                
                chat.send_keys('😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😗😙😚🙂🤗🤩🤔🤨😐😑😶🙄😏😣😥😮🤐😯😪😫🥱😴😌😛😜😝🤤😒😓😔😕🙃🤑😲☹🙁😖😞😟😤😢😭😦😧😨😩🤯😬😰😱🥵🥶😳🤪😵😡😠🤬😷🤒🤕🤢🤮🤧😇🥳🥴🥺🤠😈👿👹👺💀👻👽👾🤖💩👋🤚🖐✋🖖👌🤏✌🤞🤟🤘🤙👈👉👆👇🖕☝👍👎✊👊🤛🤜👏🙌👐🤲🤝🙏✍💅🤳💪🦵🦶👂👃👣👀👁👅👄🧠🫀🫁🦷🦴👤👥👶🧒👦👧🧑👱👨🧔👩🧓👴👵🙍🙎🙅🙆🙇🤦🤷💁🙋🧏🙇💇💆🧑‍🦰🧑‍🦱🧑‍🦲🧑‍🦳👕👖🧣🧤🧥🧦👗👘👚👛👜👝🛍🎒👞👟👠👡👢👑👒🎩🎓🧢⛑⚽🏀🏈⚾🥎🎾🏐🏉🥏🎱🏓🏸🥅🏒🏑🥍🏏⛳🪁🏹🎣🤿🥊🥋🎽🛷⛸🥌🛹🛼🛶⛷🏂🏋🤼🤸🤾🏌🏇🧘🏄🏊🤽🚣🏆🎖🏅🥇🥈🥉🍏🍎🍐🍊🍋🍌🍉🍇🍓🫐🍈🍒🍑🥭🍍🥥🥝🍅🍆🥑🥦🥬🥒🌽🥕🧄🧅🥔🍠🍯🍳🥚🥓🥩🍗🍖🍤🥞🥐🍞🥯🥨🥖🍔🍟🍕🌭🥪🌮🌯🥙🧆🍜🍲🍛🍣🍱🍤🍙🍚🍘🍥🥮🍢🍡🍧🍨🍦🍰🎂🍮🍭🍬🍫🍿🧂🍩🍪🧋🍺🍻🍷🍸🍹🥂🥃🍶🧃🧉🧊🐶🐱🐭🐹🐰🦊🐻🐼🦥🦦🦨🦘🦡🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🦆🦅🦉🦇🐺🐗🐴🦄🐝🪲🐞🦋🐌🐚🐛🦟🦗🕷🕸🦂🐢🐍🦎🦖🦕🐙🦑🦐🦞🐠🐟🐡🐬🦈🐳🐋🦭🐊🐅🐆🦓🦍🦧🦣🐘🦏🦛🐪🐫🦙🦘🐃🐂🐄🐎🐖🐏🐑🦙🐐🐓🦃🦤🐇🐁🐀🐿🦔🐾🌍🌎🌏🌕🌖🌗🌘🌑🌒🌓🌔🌚🌝🌞🌛🌜🌡☀🌤⛅🌥🌦☁🌧⛈🌩🌨❄⛄🌬💨💧💦☔☂☃🌈🌂🎃🎄🎆🎇🧨✨🎈🎉🎊🎋🎍🎎🎏🎐🎑🧧🎀🎁🎫🎟🎗🏵🎖🏆🥇🥈🥉⚽🏀🏈⚾🎱🏓🏸🎾🥏🏐🏉🥅⛸🎳🎯🎮🎰🎲🎯🏆🏅🎗🏵🎟🎫🎰🎮🎲🧩🧸👾🛸🚀🛸🚁✈🛩🚁🛥🛶⛵🚤🚢🚂🚃🚄🚅🚆🚇🚉🚊🚋🚍🚎🚐🚑🚒🚓🚔🚕🚗🚙🚚🚛🚜🛵🛴🚲🛺🏍🛺🚚🛺🛴🚲🚛🚜🛵! # $ % &  ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~ ¢ £ ¥ © ® ™ § ¶ † ‡ • ‣ ☆ ★ ☇ ☈ ☉ ☊ ☋ ☌ ☍ ⌁ ⌂ ⌐ ⌠ ⌡ ⌢ ⌣ ⌤ ⌥ ⌦ ⌧ ⌨ ⌫ ⌬ ⌭ ⌮ ⌯ 〃 〄 々 〒 〓 〠 〡 〢 〣 〤 〥 〦 〧 〨 〩 〪 〫 〬 〭 〮 〯 〰 〱 〲 〳 〴 〵 〶 〷 〸 〹 〺 〻 〼 〽 〾 〿ABCDEFGHIJKLMNOPQRSTUVWXYZΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن هـ و يא ב ג ד ה ו ז ח ט י כ ל מ נ ס ע פ צ ק ר ש תก ข ฃ ค ฅ ฆ ง จ ฉ ช ซ ฌ ญ ฎ ฏ ฐ ฑ ฒ ณ ด ต ถ ท ธ น บ ป ผ ฝ พ ฟ ภ ม ย ร ฤ ล ฦ ว ศ ษ ส ห ฬ อ ฮअ आ इ ई उ ऊ ऋ ऌ ए ऐ ओ औ क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह一 二 三 四 五 六 七 八 九 十 口 日 月 田 目 木 林 森 水 火 金 土あ い う え お か き く け こ さ し す せ そ た ち つ て と な に ぬ ね の は ひ ふ へ ほ ま み む め も や ゆ よ ら り る れ ろ わ を んア イ ウ エ オ カ キ ク ケ コ サ シ ス セ ソ タ チ ツ テ ト ナ ニ ヌ ネ ノ ハ ヒ フ ヘ ホ マ ミ ム メ モ ヤ ユ ヨ ラ リ ル レ ロ ワ ヲ ン') 
                send_message.click()
                
                
                
                
                print(f'Message {count} sent!')
                
                count += 1
                
            print("Second step done 🟢")
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot_path)
            print("There has been an error on the second step 🔴")
            print(e)
            raise
                
if __name__ == '__main__':
    unittest.main()