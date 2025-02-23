<div align="center">

# Buff Catcher 🏁🎮  

![imagen](https://github.com/user-attachments/assets/fe6ca833-6fda-497f-b6c9-525a87970ae7)

**Buff Catcher** es una herramienta anti-AFK para *World of Warcraft Classic*. Su objetivo es evitar la desconexión automática del juego simulando actividad y, opcionalmente, detectando una imagen específica en la pantalla para ejecutar una acción automatizada.  

## 🚀 Características  
- **Simulación de actividad:** Presiona teclas aleatoriamente (`A` y `D`) con intervalos variables para evitar la desconexión por inactividad.  
- **Detección de imagen:** Busca una imagen específica en la pantalla (ejemplo: `Assets/Ony.png`) y, si la encuentra, cierra el proceso del juego y suspende el sistema.  
- **Interfaz gráfica:** Desarrollada con Tkinter, permite iniciar y detener la simulación con botones.  
- **Diseño compacto:** Ventana pequeña con diseño minimalista y opción para estar siempre visible (`topmost`).  

## 🖥️ Requisitos  
- Python 3  
- Bibliotecas necesarias (instalables con `pip`):  
  ```sh
  pip install pillow pyautogui psutil pywin32
  ```

## 🖼️ Capturas  
![Interfaz de Buff Catcher](Assets/screenshot.png)  

## ⚙️ Uso  
1. Ejecuta el script:  
   ```sh
   python buff_catcher.py
   ```  
2. Haz clic en `Start` para activar la simulación anti-AFK.  
3. Opcionalmente, la herramienta buscará la imagen en la pantalla y, si la encuentra, cerrará el juego y suspenderá el PC.  
4. Para detener la simulación manualmente, haz clic en `Stop`.  

## 🛠️ Configuración  
- Puedes cambiar la imagen objetivo en `Assets/Ony.png` para personalizar la detección.  
- Modifica los tiempos y teclas en el código según tus necesidades.  

## 🐟 Licencia  
Este proyecto está bajo la licencia MIT.  

---

</div>

