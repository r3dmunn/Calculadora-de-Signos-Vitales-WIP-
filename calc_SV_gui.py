import ctypes
import tkinter as tk

lib = ctypes.CDLL("./libcalc.so")

lib.calcular_imc.argtypes = [ctypes.c_float, ctypes.c_float]
lib.calcular_imc.restype = ctypes.c_float

lib.clasificar_imc.argtypes = [ctypes.c_float]
lib.clasificar_imc.restype = ctypes.c_char_p

lib.frecuencia_maxima.argtypes = [ctypes.c_int]
lib.frecuencia_maxima.restype = ctypes.c_int