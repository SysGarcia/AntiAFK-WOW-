import random
import pyautogui
import threading
import time 
from win32api import GetSystemMetrics
import psutil
import os

stop_event = threading.Event()
process_name = "WowClassic.exe"

def CloseProgram():
  exit()

def random_number():
    return random.uniform(0, 1)

def keypress_action():
    while not stop_event.is_set():  # Mientras el evento no esté activado
      time.sleep(random_number())
      if random.randint(0, 1) == 1:
        key = "a"
      else:
        key = "d"
      pyautogui.press(key)
      print(key)

def search_image():
  while not stop_event.is_set():
    time.sleep(30)
    try:
      region = (GetSystemMetrics(0) // 2, 0, GetSystemMetrics(0) // 2, GetSystemMetrics(1))  # Mitad derecha
      location = pyautogui.locateCenterOnScreen(r"Assets/Ony.png", grayscale=True, confidence=0.9, region=region)

      if location:
        print("Si que la hay en:", location)
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                p = psutil.Process(proc.pid)
                p.terminate()
                os.system("shutdown.exe /h")
                CloseProgram()

        stop_event.set()
    except Exception as e:
        print("No hay imagen en la pantalla. Error:", e)

def start_action(start_button, stop_button):
    global thread
    stop_event.clear()  # Asegura que el evento está en estado "no detenido"
    
    start_button.config(bg="#338525", activebackground="#235e19")
    stop_button.config(bg="#a81b30", activebackground="#871627")
    
    thread = threading.Thread(target=keypress_action, daemon=True)
    thread_image_recognition = threading.Thread(target=search_image, daemon=True)
    thread.start()
    thread_image_recognition.start()

def stop_action(start_button, stop_button):
    stop_event.set()  # Detiene el bucle en keypress_action

    start_button.config(bg="#ededed")
    stop_button.config(bg="#ededed")