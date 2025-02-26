import pyautogui
import keyboard
import time
import threading

running = False

def clicker():
    while running:
        pyautogui.click() 
        time.sleep(0) 

def hold_key():
    keyboard.press('w')  
    while running:
        time.sleep(0)  

def toggle_action():
    global running
    running = not running
    if running:
        print("Авто-кликер включен и клавиша 'W' зажата.")
        threading.Thread(target=clicker).start() 
        threading.Thread(target=hold_key).start()  
    else:
        print("Авто-кликер выключен.")
        keyboard.release('w') 


keyboard.add_hotkey('e', toggle_action)  

print("Нажмите 'E' для включения/выключения авто-кликера и зажатия 'W'.")
keyboard.wait('esc')