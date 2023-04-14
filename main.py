import pyautogui as pg
import time
import keyboard
import tqdm

LIMIT = 2000  # количество раз

time.sleep(5)  # таймаут для на переключение в аутлук

print(f"Старт начала работы скрипта по удалению писем {LIMIT} раз\n")

for i in tqdm.tqdm(range(LIMIT)):
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

    # print(f"Исполнение {i} из {LIMIT}")
    pg.press ('delete')  # достаточно одного делита

pg.alert(f"\nОкончание скрипта удаления писем {LIMIT} раз")
