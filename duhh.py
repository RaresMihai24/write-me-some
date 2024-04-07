import pyautogui
import time
import random

def scrie_text(text):
    time.sleep(2)
    pyautogui.write(text)
    pyautogui.press('enter')
    time.sleep(0.5)

mesaje = [
    "ex2",
]


greetings = [
    "ex1",
]


for _ in range(1):
    mesaj_aleatoriu = random.choice(greetings)
    scrie_text(mesaj_aleatoriu)

for _ in range(9):
    mesaj_aleatoriu1 = random.choice(mesaje)
    scrie_text(mesaj_aleatoriu1)
