import pyautogui as pg
import time
import keyboard

quantitas = 3487  # количество раз

time.sleep(5)  # таймаут для на переключение в аутлук
print("Старт начала работы скрипта по удалению писем")

for i in range (quantitas):
    # keyboard.press('shift')
    # time.sleep(0.5)
    # pg.press('down', presses=10)
    # time.sleep(0.5)
    # keyboard.release('shift')
    # time.sleep(0.5)
    pg.press ('delete')
    # time.sleep(0.1)
    keyboard.press_and_release('shift', 'tab')
    # pg.hotkey('shift', 'tab')
    # time.sleep(0.1 )
    pg.press('space')
