import random
import pyautogui
import threading
import time
from win32api import GetSystemMetrics
import psutil
import os
import tkinter as tk
import datetime

stop_event = threading.Event()
process_name = "WowClassic.exe"
first_time = True

def CloseProgram():
    global stop_event
    stop_event.set()
    os._exit(0)  # Salida segura del programa

def random_number():
    return random.uniform(0.5, 2)  # Evita valores extremadamente pequeños

def keypress_action(secondary_frame, canvas, label=""):
    global stop_event
    if stop_event.is_set():
        return  # Si el evento está activado, detener la función
    if label and label != "":
        label.destroy()
        time.sleep(0.5)  # Espera antes de crear el nuevo label
    
    key = "a" if random.randint(0, 1) == 1 else "d"
    pyautogui.press(key)

    # Actualizar el label en el hilo principal
    tiempo_actual = time.strftime("%H:%M:%S", time.localtime())
    new_label = tk.Label(secondary_frame, text=f"{tiempo_actual} {key}", bg="#000000", fg="#faeb14", font=("Helvetica", 13))
    new_label.pack(fill="both", expand=True)

    # Actualizar la barra de desplazamiento
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.yview_moveto(1)  # Mueve el scroll al final

    # Volver a ejecutar después de un tiempo aleatorio en el hilo principal
    secondary_frame.after(int(random_number() * 1000), lambda: keypress_action(secondary_frame, canvas))
    
def search_image(terciary_frame, canvas_terciary, label2=""):
  global stop_event
  if stop_event.is_set():
    return  # Si el evento está activado, detener la función

  if label2 and label2 != "":
    label2.destroy()
    time.sleep(0.5)  # Espera antes de crear el nuevo label
  
  tiempo_actual = time.strftime("%H:%M:%S", time.localtime())

  try:
    region = (GetSystemMetrics(0) // 2, 0, GetSystemMetrics(0) // 2, GetSystemMetrics(1))  # Mitad derecha
    location = pyautogui.locateCenterOnScreen(r"Assets/Ony.png", grayscale=True, confidence=0.9, region=region)
    if location:
      new_label = tk.Label(terciary_frame, text=f"{tiempo_actual} Buffo Onyxia encontrado!", bg="#000000", fg="#13dde8", font=("Helvetica", 13))
      new_label.pack(fill="both", expand=True)
      
      canvas_terciary.update_idletasks()
      canvas_terciary.config(scrollregion=canvas_terciary.bbox("all"))
      canvas_terciary.yview_moveto(1)  # Mueve el scroll al final

      for proc in psutil.process_iter():
        if proc.name() == process_name:
          p = psutil.Process(proc.pid)
          p.terminate()
          CloseProgram()

      stop_event.set()
  except Exception as e:   
    tiempo_actual_separado = tiempo_actual.split(":")
    tiempo = datetime.datetime(100, 1, 1, int(tiempo_actual_separado[0]), int(tiempo_actual_separado[1]), int(tiempo_actual_separado[2]))

    # Sumar 30 segundos
    tiempo_siguiente_busqueda = tiempo + datetime.timedelta(seconds=30)

    # Formatear hora, minuto y segundo con ceros cuando sea necesario
    hora_formateada = str(tiempo_siguiente_busqueda.hour).zfill(2)
    minuto_formateado = str(tiempo_siguiente_busqueda.minute).zfill(2)
    segundo_formateado = str(tiempo_siguiente_busqueda.second).zfill(2)

    new_label = tk.Label(terciary_frame, text=f"{tiempo_actual} Buffo Onyxia no encontrado!", bg="#000000", fg="#de1f45", font=("Helvetica", 13))
    new_label.pack(side=tk.TOP, anchor=tk.NW)
    new_label = tk.Label(terciary_frame, text=f"Siguiente busqueda a las {hora_formateada}:{minuto_formateado}:{segundo_formateado}", bg="#000000", fg="#13dde8", font=("Helvetica", 13))
    new_label.pack(side=tk.TOP, anchor=tk.NW)
    
    # Actualizar la barra de desplazamiento
    canvas_terciary.update_idletasks()
    canvas_terciary.config(scrollregion=canvas_terciary.bbox("all"))
    canvas_terciary.yview_moveto(1)  # Mueve el scroll al final
    
    terciary_frame.after(30000, lambda: search_image(terciary_frame, canvas_terciary))
        
def start_action(start_button, stop_button, secondary_frame, terciary_frame, canvas, canvas_terciary):
    global stop_event
    stop_event.clear()

    start_button.config(bg="#338525", activebackground="#235e19")
    stop_button.config(bg="#a81b30", activebackground="#871627")

    # Crear el Label en el hilo principal
    label = tk.Label(secondary_frame, text="Esperando acción...", bg="#000000", fg="#faeb14",font=("Helvetica", 13))
    label.pack()

    label2 = tk.Label(terciary_frame, text="Esperando captura...", bg="#000000", fg="#faeb14",font=("Helvetica", 13))
    label2.pack()

    label.after(1000, lambda: keypress_action(secondary_frame, canvas, label))
    label2.after(1000, lambda: search_image(terciary_frame, canvas_terciary, label2))

def stop_action(start_button, secondary_frame,terciary_frame,stop_button):
    global stop_event
    stop_event.set()  # Detiene el bucle en keypress_action
    for widget in secondary_frame.winfo_children():
        widget.destroy()
    for widget in terciary_frame.winfo_children():
        widget.destroy()
    start_button.config(bg="#ededed")
    stop_button.config(bg="#ededed")