import pyautogui as pg
import time
import keyboard


time.sleep(3)  # таймаут для на переключение в аутлук


for i in range (100):
    keyboard.press('shift')
    time.sleep(0.5)
    pg.press('down', presses=10)
    time.sleep(0.5)
    keyboard.release('shift')
    time.sleep(0.5)
    pg.press('delete')
    time.sleep(0.5)
    keyboard.press_and_release('shift', 'tab')
    # pg.hotkey('shift', 'tab')
    time.sleep(0.5)
    pg.press('space')
