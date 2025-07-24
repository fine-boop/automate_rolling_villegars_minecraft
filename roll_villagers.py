import pyautogui
import time
from pynput import keyboard
import os
import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def read_text_from_image(image_path):
    result = reader.readtext(image_path)
    return [detection[1] for detection in result]



def read_lower_screenshot():
    reader = easyocr.Reader(['en'])
    result = reader.readtext('screenshot_lower.png')
    for detection in result:
        print(detection[1]) 

def read_upper_screenshot():
    reader = easyocr.Reader(['en'])
    result = reader.readtext('screenshot_upper.png')
    for detection in result:
        print(detection[1]) 











def on_press(key):
    if key == keyboard.Key.page_up:
        os._exit(0)
listener = keyboard.Listener(on_press=on_press)
listener.start()

def screenshot_lower():
    x, y = pyautogui.position()
    top = y - 60
    region = (x + 35, top, 500, 100)
    screenshot1 = pyautogui.screenshot(region=region)
    screenshot1.save('screenshot_lower.png')
def screenshot_upper():
    x, y = pyautogui.position()
    top = y - 60
    region = (x + 35, top, 500, 100)
    screenshot2 = pyautogui.screenshot(region=region)
    screenshot2.save('screenshot_upper.png')


      




    
def setup():
    global enchanted_book
    print("Please equip your axe in hotbar slot 1, and lecterns in hotbar slot 2")
    print("Please set mouse sensitivity to 100%, and raw input to OFF in mouse settings")
    print("Please face your crosshair down while infront of your villegar")

    enchanted_book = input("What enchanted book would you like? Please enter with proper capitalization and no spelling errors, and the level inculded if there is one: \n \n ==>")

    print("Press enter when ready")
    input("")
    time.sleep(2)
    mine_lectern_collect_check_repeat()
    # pyautogui.keyDown('s')
    # time.sleep(.25)
    # pyautogui.keyUp('s')
    # pyautogui.moveRel(0, -37, duration=1)
    # mine_lectern_collect_check_repeat()

# def setup_no_text():
#     pyautogui.keyDown('s')
#     time.sleep(.25)
#     pyautogui.keyUp('s')
#     pyautogui.moveRel(0, -37, duration=1)
#     mine_lectern_collect_check_repeat()
    

def mine_lectern_collect_check_repeat():
    global enchanted_book
    while True:

        #setup by walking back and moving mouse
        pyautogui.keyDown('s')
        time.sleep(.25)
        pyautogui.keyUp('s')
        pyautogui.moveRel(0, -37, duration=1)


        #select axe
        pyautogui.press('1')
        
        #mine lectern
        pyautogui.mouseDown()
        time.sleep(.75)
        pyautogui.mouseUp()
        pyautogui.keyDown('w')
        time.sleep(.5)
        pyautogui.click(button='right')
        time.sleep(.5)
        pyautogui.keyUp('w')

        #walk backwards
        pyautogui.keyDown('s')
        time.sleep(.5)
        pyautogui.keyUp('s')

        #replace lectern, open trapdoor and point crosshair at villegar
        pyautogui.press('2')
        pyautogui.click(button='right')
        pyautogui.moveRel(0, -20, duration=1)
        pyautogui.click(button='right')
        
        #walk towards villegar and open trades menue
        pyautogui.keyDown('w')
        time.sleep(.5)
        pyautogui.keyUp('w')
        pyautogui.click(button='right')

        #villegar interaction here, takes screenshots1 and 2
        pyautogui.moveRel(-220, -140, duration=1)
        screenshot_lower()
        pyautogui.moveRel(0, -85, duration=1)
        screenshot_upper()
            
        lower_trade_list = read_text_from_image('screenshot_lower.png')
        upper_trade_list = read_text_from_image('screenshot_upper.png')

        lower_trade = ", ".join(lower_trade_list)
        upper_trade = ", ".join(upper_trade_list)

        print("Two trades detected")
        print(lower_trade)
        print(upper_trade)

        if enchanted_book in upper_trade:
            print(f"{enchanted_book} found. Exiting...")
            exit()
        elif enchanted_book in lower_trade:
            print(f"{enchanted_book} found. Exiting...")
            exit()
        else:
            print(f"{enchanted_book} not found. Continuing")

        
        pyautogui.press('e')

        #move backwards
        pyautogui.keyDown('w')
        time.sleep(.5)
        pyautogui.keyUp('w')
        #move mouse down

        pyautogui.moveRel(0, 75, duration=1)
        



    

setup()
