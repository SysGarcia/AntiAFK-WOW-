import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os
import utils

master = tk.Tk()
master.geometry('250x120+0+0')
master.overrideredirect(True)
master.call('wm', 'attributes', '.', '-topmost', '1')

# Contenedor principal
main_frame = tk.Frame(master,bg="#f0f0f0",highlightbackground="#3d3d3d", highlightthickness=1)
main_frame.pack(fill="both", expand=True)

# Frame superior dividido en dos
top_frame = tk.Frame(main_frame,bg="#f0f0f0")
top_frame.pack(fill="both", expand=True, side="top")

# Frame izquierdo (mitad de la ventana)
left_frame = tk.Frame(top_frame, bg="#f0f0f0")
left_frame.pack(fill="both", expand=True, side="left")

Title = tk.Label(left_frame, text ="Buff catcher",font=("Helvetica", 16),anchor='w', bg="#f0f0f0", fg="#0a0a0a").pack(fill='both')
Description = tk.Label(left_frame, text ="A wow antiafk tool",font=("Helvetica", 12), bg="#f0f0f0", fg="#0a0a0a",anchor='w').pack(fill='both')

# Frame derecho (mitad de la ventana)
right_frame = tk.Frame(top_frame, bg="#f0f0f0")
right_frame.pack(fill="both", expand=True, side="right")

Exit = tk.Button(right_frame, text ="❌",font=("Helvetica", 9), command = utils.CloseProgram,anchor="n",width=5, 
                      border=0, 
                      background="#d63155", 
                      activebackground="#ba2949",
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=1).pack(side="right",anchor="ne")

bottom_frame = tk.Frame(main_frame, bg="#f0f0f0")
bottom_frame.pack(side="bottom", fill="x")

s = ttk.Style()
s.configure('TSeparator', background='#0d0d0d')

border = ttk.Separator(bottom_frame, orient="horizontal")
border.pack(fill="x", pady=2, padx=2)  

img = ImageTk.PhotoImage(Image.open("Ony.png"))
panel = tk.Label(bottom_frame, image=img,bg="#f0f0f0")
panel.pack(side=tk.LEFT, padx=5)

Start = tk.Button(bottom_frame, bg="#ededed", text="Start", font=("Helvetica", 12), command=lambda: utils.start_action(Start,Stop),activebackground="#235e19")
Stop = tk.Button(bottom_frame, bg="#ededed", text="Stop", font=("Helvetica", 12), command=lambda: utils.stop_action(Start,Stop), activebackground="#871627")

Start.pack(side=tk.LEFT, padx=5, pady=10,fill="both", expand=True)
Stop.pack(side=tk.LEFT, padx=5, pady=10,fill="both", expand=True)

tk.mainloop()