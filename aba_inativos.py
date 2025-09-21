import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import os
import pygame


from datetime import datetime, timedelta
from modulos.banco.db_models import Cliente, Pagamento
from modulos.banco.database import database

def buscar_clientes_inativos(dias_limite=15):
    limite = datetime.today().date() - timedelta(days=dias_limite)
    clientes = database.query(Cliente).all()
    inativos = []

    for cliente in clientes:
        ultimo = (
            database.query(Pagamento)
            .filter(Pagamento.cliente_id == cliente.id)
            .order_by(Pagamento.data_pagamento.desc())
            .first()
        )
        if not ultimo or ultimo.data_pagamento < limite:
            dias = (datetime.today().date() - (ultimo.data_pagamento if ultimo else cliente.data_cadastro)).days
            inativos.append((cliente, dias))

    return inativos

def montar_aba_inativos(master, inner_frame):
    inner_frame = ttk.Frame(master)
    inner_frame.grid(row=0, column=0, sticky="nsew")


    frame = ttk.LabelFrame(master, text="Clientes Inativos")
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    inativos = buscar_clientes_inativos()

    for i, (cliente, dias) in enumerate(inativos):
        info = f"{cliente.nome} ({cliente.nome_pet}) - {dias} dias sem retorno"
        ttk.Label(frame, text=info).grid(row=i, column=0, sticky="w")

        ttk.Button(frame, text="Lembrar", command=lambda c=cliente: lembrar_cliente(c)).grid(row=i, column=1)
        ttk.Button(frame, text="Agendar", command=lambda c=cliente: abrir_agendamento(c)).grid(row=i, column=2)
    return inner_frame