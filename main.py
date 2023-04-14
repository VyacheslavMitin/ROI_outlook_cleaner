import pyautogui as pg
import time
import keyboard

LIMIT = 1600  # количество раз

time.sleep(5)  # таймаут для на переключение в аутлук
print(f"Старт начала работы скрипта по удалению писем {quantitas} раз")

for i in range(LIMIT):
    # СТАРЫЙ КОД
    # keyboard.press('shift')
    # time.sleep(0.5)
    # pg.press('down', presses=10)
    # time.sleep(0.5)
    # keyboard.release('shift')
    # time.sleep(0.5)
    # pg.press ('delete')
    # time.sleep(0.1)
    # keyboard.press_and_release('shift', 'tab')
    # pg.hotkey('shift', 'tab')
    # time.sleep(0.1 )
    # pg.press('space')

    pg.press ('delete')  # достаточно одного делита


pg.alert(f"Окончание скрипта удаления писем")
