import ctypes
import tkinter as tk
from tkinter import ttk

lib = ctypes.CDLL("./libcalc.so")

lib.calcular_imc.argtypes = [ctypes.c_float, ctypes.c_float]
lib.calcular_imc.restype = ctypes.c_float

lib.clasificar_imc.argtypes = [ctypes.c_float]
lib.clasificar_imc.restype = ctypes.c_char_p

lib.frecuencia_maxima.argtypes = [ctypes.c_int]
lib.frecuencia_maxima.restype = ctypes.c_int


font = ("Helvetica", 16, "italic")
root = tk.Tk()
root.title("Calculadora de Signos Vitales")
root.geometry("700x500")

tk.Label(root, text="CALCULADORA DE SIGNOS VITALES - R3DMOON", 
         font=font, fg ="white",bg="navy",
         padx = 12, pady=6 ).pack(pady=8)
tk.Label(root, text="Ingrese su edad debajo.", font=font,
         fg="white", bg = "navy", padx=12,pady=6).pack()


root.mainloop()