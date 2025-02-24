import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import utils as Utils

master = tk.Tk()
master.geometry('250x120+0+0')
master.overrideredirect(True)
master.call('wm', 'attributes', '.', '-topmost', '1')

secondary = tk.Tk()
secondary.geometry('550x120+0+120')
secondary.overrideredirect(True)
secondary.call('wm', 'attributes', '.', '-topmost', '1')

terciary = tk.Tk()
terciary.geometry('550x120+0+240')
terciary.overrideredirect(True)
terciary.call('wm', 'attributes', '.', '-topmost', '1')

# Establecer el fondo de la ventana secundaria al color que se hará transparente
secondary.config(bg="#000000")
secondary.attributes("-transparentcolor", "#000000")

terciary.config(bg="#000000")
terciary.attributes("-transparentcolor", "#000000")

# Contenedor principal
main_frame = tk.Frame(master, bg="#f0f0f0", highlightbackground="#3d3d3d", highlightthickness=1)
main_frame.pack(fill="both", expand=True)

# Frame superior dividido en dos
top_frame = tk.Frame(main_frame, bg="#f0f0f0")
top_frame.pack(fill="both", expand=True, side="top")

# Frame izquierdo (mitad de la ventana)
left_frame = tk.Frame(top_frame, bg="#f0f0f0")
left_frame.pack(fill="both", expand=True, side="left")

tk.Label(left_frame, text="Buff catcher", font=("Helvetica", 16), anchor='w', bg="#f0f0f0", fg="#0a0a0a").pack(fill='both')
tk.Label(left_frame, text="A wow antiafk tool", font=("Helvetica", 12), bg="#f0f0f0", fg="#0a0a0a", anchor='w').pack(fill='both')

# Frame derecho (mitad de la ventana)
right_frame = tk.Frame(top_frame, bg="#f0f0f0")
right_frame.pack(fill="both", expand=True, side="right")

tk.Button(right_frame, text="❌", font=("Helvetica", 9), command=Utils.CloseProgram, anchor="n", width=5,
          border=0, background="#d63155", activebackground="#ba2949", highlightthickness=4,
          highlightcolor="#37d3ff", highlightbackground="#37d3ff", borderwidth=1).pack(side="right", anchor="ne")

bottom_frame = tk.Frame(main_frame, bg="#f0f0f0")
bottom_frame.pack(side="bottom", fill="x")

s = ttk.Style()
s.configure('TSeparator', background='#0d0d0d')

border = ttk.Separator(bottom_frame, orient="horizontal")
border.pack(fill="x", pady=2, padx=2)

img = ImageTk.PhotoImage(Image.open(r"Assets/Ony.png"))
tk.Label(bottom_frame, image=img, bg="#f0f0f0").pack(side=tk.LEFT, padx=5)

Start = tk.Button(bottom_frame, bg="#ededed", text="Start", font=("Helvetica", 12),
                  command=lambda: Utils.start_action(Start, Stop, secondary_frame, terciary_frame, canvas_secondary,canvas_terciary), activebackground="#235e19")
Stop = tk.Button(bottom_frame, bg="#ededed", text="Stop", font=("Helvetica", 12),
                 command=lambda: Utils.stop_action(Start, secondary_frame, terciary_frame, Stop), activebackground="#871627")

Start.pack(side=tk.LEFT, padx=5, pady=10, fill="both", expand=True)
Stop.pack(side=tk.LEFT, padx=5, pady=10, fill="both", expand=True)

canvas_secondary = tk.Canvas(secondary, bg="#000000", highlightbackground="#000000")

secondary_frame = tk.Frame(canvas_secondary, bg="#000000")
canvas_secondary.pack(side="left", fill="both", expand=True)
canvas_secondary.create_window((0, 0), window=secondary_frame, anchor="nw")

canvas_terciary = tk.Canvas(terciary, bg="#000000", highlightbackground="#000000")

terciary_frame = tk.Frame(canvas_terciary, bg="#000000")
canvas_terciary.pack(side="left", fill="both", expand=True)
canvas_terciary.create_window((0, 0), window=terciary_frame, anchor="nw")

tk.mainloop()
