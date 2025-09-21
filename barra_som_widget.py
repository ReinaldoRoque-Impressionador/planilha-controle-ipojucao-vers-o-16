# barra_som_widget.py

import tkinter as tk
from tkinter import ttk
from modulos.recursos.som import tocar_som, alternar_som

def criar_barra_som(master):
    frame = ttk.Frame(master)
    frame.grid(row=0, column=1, sticky="nsew")

    ttk.Label(frame, text="🔊 Controle de Som", font=("Arial", 16)).pack(pady=10)

    botao_som = ttk.Button(frame, text="🔈 Som Ativado", command=lambda: alternar_som(botao_som))
    botao_som.pack(pady=5)

    ttk.Button(frame, text="Testar Som", command=lambda: tocar_som("sons/musica_abertura.mp3")).pack(pady=5)

    return frame