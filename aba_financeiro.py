#from dados_compartilhados import var_raca, caracteristicas_racas
#from main import aba_financeiro, inner_frame
from modulos.recursos.dados_compartilhados import variaveis
import pygame
pygame.mixer.init()
from modulos.recursos.funcoes_auxiliares import caminho_arquivo
import os
logo_splash = caminho_arquivo("splash.png", subpasta=os.path.join("../..", "..", "imagensipojucao"))
som_relatorio = caminho_arquivo("relatorio_finalizado.mp3", subpasta="sons")
from PIL import Image, ImageTk
import os
#from mascote import mostrar_mascote_expressivo

#from .mascote import mostrar_mascote_expressivo
from modulos.recursos.utils_mensagens import formatar_mensagem_bancaria
from tkinter import messagebox

from modulos.banco.database import testar_conexao
from modulos.recursos.conexao_utils import conexao_valida

from modulos.componentes.mascote_widget import mostrar_mascote_expressivo


# def montar_aba_financeiro(master):
#     label = tk.Label(master, text="Exemplo")
#     label.grid(row=0, column=0, padx=10, pady=10)


def montar_aba_financeiro(master):
    inner_frame = ttk.Frame(master)
    inner_frame.grid(row=0, column=0, sticky="nsew")

    label = tk.Label(inner_frame, text="Exemplo")
    label.grid(row=0, column=0, padx=10, pady=10)

    return inner_frame



# img = carregar_imagem_tk("logo_ipojucao.png")
# label.config(image=img)
# label.img_ref = img  # manter referência


def inicializar_financeiro(master):
    dc.inicializar_variaveis(master)


def verificar_conexao():
    testar_conexao()
    if conexao_valida():
        print("✅ Conexão OK")
    else:
        print("❌ Erro na conexão")

verificar_conexao()

# enviar_mensagem_whatsapp("+5511999999999", "Olá, Reinaldo! Teste de envio via Python.")
# #🧪 Dica para testes
# #Use um número seu ou de teste no formato internacional:
# #• 	Brasil:  + DDD + número
# #Exemplo: +5511981772847

#🧠 Dica extra: envio imediato
#Se quiser enviar sem agendamento, pode usar:

#Mas essa função pode ser menos confiável dependendo da versão do navegador.


import datetime

# ===============================
# Importações Após Reestruturação do Projeto (abaixo)

from modulos.recursos import dados_compartilhados as dc

# específicamente para abas financeiro e relatórios

import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from collections import defaultdict

from modulos.banco.db_models import Pagamento
from modulos.banco.database import database
import modulos.recursos.centro_controle_relatorios as relatorios

def gerar_relatorio_financeiro(data_inicio, data_fim):
    # Consulta ao banco com filtro por data
    pagamentos = database.query(Pagamento).filter(
        Pagamento.data_pagamento >= data_inicio,
        Pagamento.data_pagamento <= data_fim
    ).all()

    # Agrupamento por forma de pagamento
    resumo = defaultdict(lambda: {"quantidade": 0, "total": 0})
    for p in pagamentos:
        forma = p.forma_pagamento
        resumo[forma]["quantidade"] += 1
        resumo[forma]["total"] += p.valor

    # Monta linhas para PDF
    linhas_pdf = [
        f"📊 Relatório Financeiro",
        f"🗓️ Período: {data_inicio.strftime('%d/%m/%Y')} até {data_fim.strftime('%d/%m/%Y')}",
        "----------------------------------------"
    ]
    for forma, dados in resumo.items():
        linha = f"{forma}: {dados['quantidade']} pagamentos | Total: R${dados['total']:.2f}"
        linhas_pdf.append(linha)

    # Monta linhas para Excel
    linhas_excel = [["Forma de Pagamento", "Quantidade", "Total"]]
    for forma, dados in resumo.items():
        linhas_excel.append([forma, dados["quantidade"], dados["total"]])

    # Exporta os relatórios
    relatorios.gerar_relatorio_pdf(linhas_pdf, nome_arquivo="financeiro.pdf")
    relatorios.gerar_excel(linhas_excel, nome_arquivo="financeiro.xlsx")

    tocar_som_relatorio()

    print("✅ Relatórios gerados com sucesso.")

# Interface simples para teste
def montar_interface():
    root = tk.Tk()
    root.title("Relatório Financeiro")
    root.geometry("400x200")

    ttk.Label(root, text="Data Inicial:").grid(row=0, column=0, padx=10, pady=10)
    calendario_inicio = DateEntry(root, locale="pt_BR")
    calendario_inicio.grid(row=0, column=1)

    ttk.Label(root, text="Data Final:").grid(row=1, column=0, padx=10, pady=10)
    calendario_fim = DateEntry(root, locale="pt_BR")
    calendario_fim.grid(row=1, column=1)

    def ao_gerar():
        data_i = calendario_inicio.get_date()
        data_f = calendario_fim.get_date()
        gerar_relatorio_financeiro(data_i, data_f)

    ttk.Button(root, text="Gerar Relatório", command=ao_gerar).grid(row=2, column=0, columnspan=2, pady=20)






# Simulação de dados financeiros
# resumo_financeiro = {
#     "Cartão de Crédito": {"quantidade": 10, "total": 1500.00},
#     "Cartão de Dédito": {"quantidade": 13, "total": 1800.00},
#     "PIX": {"quantidade": 5, "total": 800.00},
#     "Dinheiro": {"quantidade": 3, "total": 450.00}
# }
#
# # Monta lista de linhas para PDF
# linhas_pdf = [
#     "📊 Relatório Financeiro",
#     "----------------------------"
# ]
# for forma, dados in resumo_financeiro.items():
#     linha = f"{forma}: {dados['quantidade']} pagamentos | Total: R${dados['total']:.2f}"
#     linhas_pdf.append(linha)
#
# # Monta lista de linhas para Excel
# linhas_excel = [["Forma de Pagamento", "Quantidade", "Total"]]
# for forma, dados in resumo_financeiro.items():
#     linhas_excel.append([forma, dados["quantidade"], dados["total"]])
#
# # ✅ Chamada correta das funções
# relatorios.gerar_relatorio_pdf(linhas_pdf, nome_arquivo="financeiro.pdf")
# relatorios.gerar_excel(linhas_excel, nome_arquivo="financeiro.xlsx")


# relatorios.gerar_relatorio_pdf()
# relatorios.gerar_excel()
from modulos.abas.mensageiro import enviar_mensagem_whatsapp
# específicamente para abas financeiro e relatórios.



# Importações Após Reestruturação do Projeto (acima)
# ===============================


from tkcalendar import Calendar  # certifique-se de que essa linha está no topo

def criar_aba_financeiro(master):
    inner_frame = ttk.Frame(master)
    inner_frame.grid(row=0, column=0, sticky="nsew")

    frame = ttk.LabelFrame(container, text="Financeiro")
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Teste: Adicionando um calendário
    calendario = Calendar(frame, selectmode='day', year=2025, month=8, day=17)
    calendario.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    return inner_frame
# def montar_aba_financeiro(aba_financeiro):
#     # === Scrollable frame ===
#     # Criação do canvas e da scrollbar
#     canvas = tk.Canvas(aba_financeiro)
#     scrollbar_y = ttk.Scrollbar(aba_financeiro, orient="vertical", command=canvas.yview)
#     canvas.configure(yscrollcommand=scrollbar_y.set)
#
#     # Posicionamento usando .grid()
#     canvas.grid(row=0, column=0, sticky="nsew")  # Ocupa toda a célula
#     scrollbar_y.grid(row=0, column=1, sticky="ns")  # Fica ao lado do canvas, altura total
#
#     # Frame interno rolável
#     scrollable_frame = ttk.Frame(canvas)
#     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#
#     # Atualiza o scrollregion automaticamente
#     scrollable_frame.bind(
#         "<Configure>",
#         lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
#     )



def montar_aba_financeiro(aba_financeiro, inner_frame):
    def mostrar_mensagem():
        mensagem = formatar_mensagem_bancaria()
        messagebox.showinfo("Resumo Financeiro", mensagem)
    def atualizar_pagamento():
        status = dc.var_status_pagamento.get()
        if status == "pago":
            for rb in [dc.radiobutton_pix, dc.radiobutton_debito, dc.radiobutton_credito, dc.radiobutton_dinheiro]:
                rb.config(state="normal")
        else:
            dc.var_pagamento.set("")
            for rb in [dc.radiobutton_pix, dc.radiobutton_debito, dc.radiobutton_credito, dc.radiobutton_dinheiro]:
                rb.config(state="disabled")

    mostrar_mascote_expressivo("positivo")

    # Permitir expansão
    aba_financeiro.grid_rowconfigure(0, weight=1)
    aba_financeiro.grid_columnconfigure(0, weight=1)

    frame_formas = ttk.LabelFrame(inner_frame, text="Método de Pagamento")
    frame_formas.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

    dc.radiobutton_pix = ttk.Radiobutton(frame_formas, text="PIX", value="pix", variable=dc.var_pagamento)
    dc.radiobutton_pix.grid(row=0, column=0, padx=10, pady=5)

    dc.radiobutton_debito = ttk.Radiobutton(frame_formas, text="Débito", value="debito", variable=dc.var_pagamento)
    dc.radiobutton_debito.grid(row=0, column=1, padx=10, pady=5)

    dc.radiobutton_credito = ttk.Radiobutton(frame_formas, text="Crédito", value="credito", variable=dc.var_pagamento)
    dc.radiobutton_credito.grid(row=1, column=0, padx=10, pady=5)

    dc.radiobutton_dinheiro = ttk.Radiobutton(frame_formas, text="Dinheiro", value="dinheiro",
                                              variable=dc.var_pagamento)
    dc.radiobutton_dinheiro.grid(row=1, column=1, padx=10, pady=5)

    for rb in [dc.radiobutton_pix, dc.radiobutton_debito, dc.radiobutton_credito, dc.radiobutton_dinheiro]:
        rb.config(state="disabled")


    # Canvas + Scrollbar
    canvas = tk.Canvas(aba_financeiro)
    scrollbar_y = ttk.Scrollbar(aba_financeiro, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar_y.set)

    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar_y.grid(row=0, column=1, sticky="ns")

    # Frame rolável

    porte = dc.variaveis["var_porte"].get()

    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    inner_frame.bind("<Configure>", ajustar_scroll)

    # === A partir daqui, crie widgets dentro do inner_frame ===

    # Exemplo básico
    frame_exemplo = ttk.LabelFrame(inner_frame, text="Seção de Exemplo")
    frame_exemplo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    ttk.Label(frame_exemplo, text="Alguma informação importante").grid(row=0, column=0, sticky="w")

    # Repita quantos blocos quiser (outros frames, grids, entradas, etc.)

    # Se quiser ativar algo quando o porte mudar
    dc.var_porte.trace_add("write", lambda *args: atualizar_exemplo())
    info = caracteristicas_racas.get(var_raca.get(), {})

def atualizar_exemplo():
    porte = dc.var_porte.get()
    print(f"Porte selecionado na aba é: {porte}")
    # === Frame serviços ===
    frame_servicos = ttk.LabelFrame(inner_frame, text="Serviços Disponíveis")
    frame_servicos.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Campos para nome do cliente e nome do pet
    ttk.Label(inner_frame, text="Nome do Cliente:").grid(row=0, column=0, padx=10, pady=5)
    entry_nome_cliente = ttk.Entry(inner_frame)
    entry_nome_cliente.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(inner_frame, text="Nome do Pet:").grid(row=1, column=0, padx=10, pady=5)
    entry_nome_pet = ttk.Entry(inner_frame)
    entry_nome_pet.grid(row=1, column=1, padx=10, pady=5)

    dc.servicos_disponiveis = [
        "Banho", "Hidratação", "Desembolo", "Remoção de Pelos", "Corte de Unhas", "Tosa Higiênica",
        "Tosa na Máquina", "Tosa na Tesoura", "Leva e Trás"]


dc.variaveis_servicos = {}
dc.labels_valores = {}

# A FUNÇÃO ABAIXO É PARA COLETAR SERVIÇOS PRESTADOS E VALORES PARA ENVIAR AO CLIENTE VIA WHATSAPP
#📊 Etapa 2: Função para coletar os dados da aba_financeiro
#Na , crie uma função:
def coletar_servicos_selecionados():
    servicos = []
    valores = {}
    for servico in dc.servicos_disponiveis:
        var = dc.variaveis_servicos.get(servico)
        val = dc.labels_valores.get(servico)
        if var and var.get():  # Checkbox marcado
            servicos.append(servico)
            valores[servico] = float(val["text"].replace("R$", "").strip()) if val else 0
    return servicos, valores





def atualizar_dados_base_no_porte_preco():
    #porte = dc.var_porte.get()
    porte = variaveis["var_porte"].get()
    preco_banho = dc.dados_pet.get(porte, {}).get("preços", {}).get("Banho", 0)
    print(f"Banho para porte {porte} custa R$ {preco_banho}")


# aba_financeiro.py
# def montar_aba_financeiro(aba_financeiro, frame):
#     from dados_compartilhados import var_porte, dados_pet
#     ...



# Função para ativar/desativar métodos de pagamento
# def atualizar_pagamento():
#     global var_pagamento  # Declare a variável como global
#     if var_status_pagamento.get() == "pago":
#         # Ativar botões de pagamento
#         radiobutton_pix.config(state="normal")
#         radiobutton_debito.config(state="normal")
#         radiobutton_credito.config(state="normal")
#         radiobutton_dinheiro.config(state="normal")
#     else:
#         # Resetar e desabilitar botões de pagamento
#         var_pagamento.set("")
#         radiobutton_pix.config(state="disabled")
#         radiobutton_debito.config(state="disabled")
#         radiobutton_credito.config(state="disabled")
#         radiobutton_dinheiro.config(state="disabled")


# === Opções de forma de pagamento ===
#dc.var_pagamento = tk.StringVar(value="")




# Inicialmente desativar os botões






# Função para atualizar os valores exibidos
# def atualizar_valores():
#     porte_selecionado = var_porte.get().strip()
#     for servico in servicos_disponiveis:
#         if variaveis_servicos[servico].get():
#             valor = dados_pet[porte_selecionado]["preços"].get(servico, 0)
#             labels_valores[servico].config(text=f"R$ {valor:2f}")
#         else:
#             labels_valores[servico].config(text="")

def limpar_selecoes():
    # Implemente a lógica para limpar as seleções
    for var in variaveis_servicos.values():
        var.set(False)  # Desmarca todos os Checkbuttons
    entry_desconto_fixo.delete(0, tk.END)
    entry_desconto_percentual.delete(0, tk.END)
    label_resultado.config(text="Total com desconto: R$ 0.00")

def atualizar_pagamento():
    status = dc.var_status_pagamento.get()
    print(f"Status de pagamento atualizado: {status}")
    if status == "pago":
        for rb in [dc.radiobutton_pix, dc.radiobutton_debito, dc.radiobutton_credito, dc.radiobutton_dinheiro]:
            rb.config(state="normal")
    else:
        dc.var_pagamento.set("")
        for rb in [dc.radiobutton_pix, dc.radiobutton_debito, dc.radiobutton_credito, dc.radiobutton_dinheiro]:
            rb.config(state="disabled")


# Função para criar a aba de configuração
def criar_aba_config(parent):
    frame_config = ttk.Frame(parent)
    frame_config.grid(row=0, column=0, sticky="nsew")

    porte_combo = ttk.Combobox(
        frame_config,
        textvariable=dc.variaveis["var_porte"],
        values=list(dados_pet.keys()),
        state="readonly"
    )
    porte_combo.grid(row=0, column=1, padx=10, pady=5)

    porte_combo.bind("<<ComboboxSelected>>", lambda event: atualizar_precos_e_classificacoes())

    # Seleção do porte
    # label_porte = ttk.Label(frame_config, text="Selecione o Porte:")
    # label_porte.grid(row=0, column=0, padx=10, pady=5)
    #
    # porte_combo = ttk.Combobox(frame_config, textvariable=var_porte, values=list(dados_pet.keys()))
    # porte_combo.grid(row=0, column=1, padx=10, pady=5)
    # porte_combo.bind("<<ComboboxSelected>>", lambda event: atualizar_valores())  # Atualiza valores ao mudar o porte
    #
    # return frame_config


# Adiciona a aba "Financeiro" ao notebook
def adicionar_aba_financeiro(notebook, inner_frame):
    aba_financeiro = ttk.Frame(notebook)
    notebook.add(aba_financeiro, text="Financeiro")
    montar_aba_financeiro(aba_financeiro, inner_frame)

# Função para criar a aba financeiro
def criar_aba_financeiro(parent):
    frame_financeiro = ttk.Frame(parent)
    frame_financeiro.grid(row=0, column=0, sticky="nsew")

# Criando um Frame para serviços
    frame_servicos = ttk.LabelFrame(inner_frame, text="Serviços Disponíveis")
    frame_servicos.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

    dc.servicos_disponiveis = [
        "Banho", "Hidratação", "Desembolo", "Remoção de Pelos", "Corte de Unhas", "Tosa Higiênica", "Tosa na Máquina",
        "Tosa na Tesoura", "Leva e Trás"]

    # dc.variaveis_servicos = {}
    # dc.labels_valores = {}

    dc.variaveis_servicos = {}
    dc.labels_valores = {}
    dc.entrys_desconto_individual = {}  # ← Novo dicionário para entrada de desconto

    for i, servico in enumerate(dc.servicos_disponiveis):
        dc.variaveis_servicos[servico] = tk.BooleanVar()

        #  Checkbutton do serviço
        chk = ttk.Checkbutton(frame_servicos, text=servico, variable=dc.variaveis_servicos[servico])
        chk.grid(row=i, column=0, sticky="w")

        # Label de valor do serviço

        dc.labels_valores[servico] = ttk.Label(frame_servicos, text="R$ 0.00")
        dc.labels_valores[servico].grid(row=i, column=1, sticky="w")

        # Entry para desconto individual
        entry_desconto = ttk.Entry(frame_servicos, width=10)
        entry_desconto.grid(row=i, column=2, padx=5)
        entry_desconto.insert(0, "")  # opcional: sugestão visual como "R$" ou "%"
        dc.entrys_desconto_individual[servico] = entry_desconto

    # === Frame desconto ===
    frame_desc = ttk.LabelFrame(inner_frame, text="Abatimentos")
    frame_desc.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Botão dentro do escopo correto
    ttk.Button(frame_desc, text="Mostrar Resumo", command=mostrar_mensagem).grid(row=4, column=0, columnspan=2, pady=10)

    dc.var_desconto_fixo = tk.BooleanVar()
    dc.var_desconto_percentual = tk.BooleanVar()

    ttk.Checkbutton(frame_desc, text="Desconto Fixo (R$)", variable=dc.var_desconto_fixo).grid(row=0, column=0,
                                                                                               sticky="w")
    dc.entry_desconto_fixo = ttk.Entry(frame_desc)
    dc.entry_desconto_fixo.grid(row=0, column=1, padx=5, pady=5)

    ttk.Checkbutton(frame_desc, text="Desconto Percentual (%)", variable=dc.var_desconto_percentual).grid(row=1,
                                                                                                          column=0,
                                                                                                          sticky="w")
    dc.entry_desconto_percentual = ttk.Entry(frame_desc)
    dc.entry_desconto_percentual.grid(row=1, column=1, padx=5, pady=5)

    ttk.Button(frame_desc, text="Calcular Total", command=calcular_total).grid(row=2, column=0, pady=10)
    ttk.Button(frame_desc, text="Limpar", command=limpar_selecoes).grid(row=2, column=1)

    dc.label_resultado = ttk.Label(frame_desc, text="Total com desconto: R$ 0,00")
    dc.label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

    # === Forma de pagamento ===
    frame_pagamento = ttk.LabelFrame(inner_frame, text="Forma de Pagamento")
    frame_pagamento.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    #dc.var_status_pagamento = tk.StringVar(value="Em Aberto")
    status = dc.variaveis["var_status_pagamento"].get()

    ttk.Radiobutton(frame_pagamento, text="Pago", variable=dc.var_status_pagamento, value="pago", command=atualizar_pagamento).grid(row=0, column=0,
                                                                                                       sticky="w")
    ttk.Radiobutton(frame_pagamento, text="Em Aberto", variable=dc.var_status_pagamento, value="Em Aberto", command=atualizar_pagamento).grid(row=0,
                                                                                                                 column=1,
                                                                                                                 sticky="w")

    # === Calendário ===
    frame_calendario = ttk.LabelFrame(inner_frame, text="Data do Serviço")
    frame_calendario.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    dc.calendario_servico = DateEntry(frame_calendario, year=2025, locale="pt_br")
    dc.calendario_servico.pack(padx=10, pady=5)

    dc.variaveis["var_porte"].trace_add("write", lambda *args: atualizar_precos_e_classificacoes())
    porte_combo.bind("<<ComboboxSelected>>", lambda event: atualizar_precos_e_classificacoes())
    #dc.variaveis["var_porte"].trace_add("write", lambda *args: atualizar_precos_e_classificacoes())
    #dc.var_porte.trace_add("write", lambda *args: atualizar_valores())

# Dicionário para armazenar desconto por serviço (opcional)
dc.descontos_por_servico = {}  # {"Banho": {"tipo": "fixo", "valor": 10.0}}

# Variável para armazenar desconto total
dc.desconto_total = {"tipo": None, "valor": 0.0}



def atualizar_precos_e_classificacoes():
    porte = dc.variaveis["var_porte"].get().strip()
    tipo_pacote = dc.variaveis.get("var_tipo_pacote", tk.StringVar()).get()
    dados_porte = dc.dados_pet.get(porte, {})
    descontos_por_servico = dc.variaveis.get("descontos_por_servico", {})
    desconto_total = dc.variaveis.get("desconto_total", {})
    total = 0.0
    usados = []

    for servico in dc.servicos_disponiveis:
        var_servico = dc.variaveis_servicos.get(servico)
        label = dc.labels_valores.get(servico)

        if var_servico and var_servico.get():
            preco_base = dados_porte.get("preços", {}).get(servico, 0.0)
            tipo = "Avulso"

            if tipo_pacote in dc.pacotes_servicos:
                pacote = dc.pacotes_servicos[tipo_pacote]
                usados.append(servico)

                # Verifica se ainda pode usar serviço incluído
                if servico == "Banho" and usados.count("Banho") <= len(pacote["incluidos"]):
                    tipo = "Pacote"
                    preco_base = 0.0
                elif servico in pacote["bonus_opcoes"] and not any(s in usados for s in pacote["bonus_opcoes"] if s != servico):
                    tipo = "Bônus"
                    preco_base = 0.0

            # Aplicar desconto por serviço
            desconto = descontos_por_servico.get(servico, {})
            if desconto:
                if desconto.get("tipo") == "percentual":
                    preco_base *= (1 - desconto["valor"])
                elif desconto.get("tipo") == "fixo":
                    preco_base = max(preco_base - desconto["valor"], 0)

            # Soma apenas se não for gratuito
            if preco_base > 0.0:
                total += preco_base

            label.config(text=f"R$ {preco_base:.2f} ({tipo})")
        else:
            label.config(text="")

    # Desconto total aplicado sobre o valor
    if desconto_total:
        if desconto_total.get("tipo") == "percentual":
            total *= (1 - desconto_total["valor"])
        elif desconto_total.get("tipo") == "fixo":
            total = max(total - desconto_total["valor"], 0)

    dc.label_resultado.config(text=f"Total com desconto: R$ {total:.2f}")



# def mostrar_mensagem():
#     mensagem = formatar_mensagem_bancaria()
#     messagebox.showinfo("Resumo Financeiro", mensagem)




# def atualizar_precos_e_classificacoes():
#     porte = dc.variaveis["var_porte"].get().strip()
#     dados_porte = dados_pet.get(porte, {})
#     descontos_por_servico = dc.variaveis.get("descontos_por_servico", {})
#     desconto_total = dc.variaveis.get("desconto_total", {})
#
#     servicos_selecionados = [s for s in servicos_disponiveis if dc.variaveis[s].get()]
#     total = 0.0
#
#     for servico in servicos_disponiveis:
#         label = labels_valores[servico]
#
#         if dc.variaveis[servico].get():
#             preco_base = dados_porte.get("preços", {}).get(servico, 0.0)
#
#             # Classificação
#             if servico in dados_porte.get("pacote", []):
#                 tipo = "Pacote"
#             elif servico in dados_porte.get("bonus", []):
#                 tipo = "Bônus"
#                 preco_base = 0.0
#             else:
#                 tipo = "Avulso"
#
#             # Desconto por serviço
#             desconto = descontos_por_servico.get(servico, {})
#             if desconto:
#                 if desconto["tipo"] == "percentual":
#                     preco_base *= (1 - desconto["valor"])
#                 elif desconto["tipo"] == "fixo":
#                     preco_base = max(preco_base - desconto["valor"], 0)
#
#             total += preco_base
#             label.config(text=f"R$ {preco_base:.2f} ({tipo})")
#         else:
#             label.config(text="")
#
#     # Desconto total
#     if desconto_total:
#         if desconto_total["tipo"] == "percentual":
#             total *= (1 - desconto_total["valor"])
#         elif desconto_total["tipo"] == "fixo":
#             total = max(total - desconto_total["valor"], 0)
#
#     label_resultado.config(text=f"Total com desconto: R$ {total:.2f}")

# def atualizar_valores():
#     porte_selecionado = dc.var_porte.get().strip()
#     precos = dc.dados_pet.get(porte, {}).get("preços", {})
#
#     for servico in dc.servicos_disponiveis:
#         if dc.variaveis_servicos[servico].get():
#             #valor = precos.get(servico, 0)
#             valor = dc.dados_pet[porte_selecionado]["preços"].get(servico, 0)
#             dc.labels_valores[servico].config(text=f"R$ {valor:.2f}")
#         else:
#             dc.labels_valores[servico].config(text="")


def limpar_selecoes():
    for var in dc.variaveis_servicos.values():
        var.set(False)
    dc.entry_desconto_fixo.delete(0, tk.END)
    dc.entry_desconto_percentual.delete(0, tk.END)
    dc.label_resultado.config(text="Total com desconto: R$ 0.00")
    dc.desconto_total = {"tipo": None, "valor": 0.0}
    dc.descontos_por_servico.clear()

# def limpar_selecoes():
#     for var in dc.variaveis_servicos.values():
#         var.set(False)
#     dc.entry_desconto_fixo.delete(0, tk.END)
#     dc.entry_desconto_percentual.delete(0, tk.END)
#     dc.label_resultado.config(text="Total com desconto: R$ 0,00")


def calcular_total():
    porte = dc.var_porte.get().strip()
    precos = dc.dados_pet.get(porte, {}).get("preços", {})
    total = 0.0

    # Calcula o total dos serviços selecionados
    for servico, var in dc.variaveis_servicos.items():
        if var.get():
            preco_base = precos.get(servico, 0.0)

            # 🧮 Verifica se há desconto individual preenchido
            entrada = dc.entrys_desconto_individual.get(servico)
            valor_digitado = entrada.get().strip() if entrada else ""

            if valor_digitado.endswith("%"):
                try:
                    percentual = float(valor_digitado[:-1].replace(',', '.')) / 100
                    preco_base *= (1 - percentual)
                except:
                    pass
            elif valor_digitado:
                try:
                    desconto_fixo = float(valor_digitado.replace(',', '.'))
                    preco_base = max(preco_base - desconto_fixo, 0)
                except:
                    pass

            total += preco_base

def rodape_imagem(frame_pai):
    caminho_img = os.path.join("imagensipojucao", "rodape", "footer.png")
    if os.path.exists(caminho_img):
        img = Image.open(caminho_img).resize((1000, 80))
        img_tk = ImageTk.PhotoImage(img)
        rodape = tk.Label(frame_pai, image=img_tk)
        rodape.image = img_tk  # mantém referência da imagem

        # Posiciona no final da grid
        rodape.grid(row=999, column=0, columnspan=999, sticky="ew")  # usa row "alta" para evitar conflito
    else:
        print("Imagem do rodapé não encontrada.")

def chamar_aba_financeiro(notebook):
    frame = criar_aba_financeiro(notebook)
    notebook.add(frame, text="Financeiro")


#barra_audio(frame_aba_financeiro)  # ou frame_aba_menu, frame_aba_config, etc.




def enviar_mensagem_whatsapp(numero, mensagem):
    agora = datetime.datetime.now()
    hora = agora.hour
    minuto = agora.minute + 2  # agenda para 2 minutos depois

    kit.sendwhatmsg(numero, mensagem, hora, minuto)
    print(f"✅ Mensagem agendada para {numero}")

    enviar_mensagem_whatsapp("+5511999999999", "Olá, Reinaldo! Teste de envio via Python.")

# def registrar_pagamento(cliente_nome, valor, telefone):
#     # Simula o registro do pagamento
#     print(f"💰 Pagamento registrado: {cliente_nome} - R${valor:.2f}")
#
#     # Monta a mensagem
#     mensagem = (
#         f"Olá, {cliente_nome}!\n"
#         f"Confirmamos o recebimento do seu pagamento de R${valor:.2f}.\n"
#         f"Obrigado por confiar em nossos serviços! 😊"
#     )
#
#     # Envia via WhatsApp
#     enviar_mensagem_whatsapp(telefone, mensagem)
#

def registrar_pagamento(cliente_nome, valor, telefone):
    from modulos.recursos.utils_mensagens import enviar_mensagem_whatsapp
    print(f"💰 Pagamento registrado: {cliente_nome} - R${valor:.2f}")

    mensagem = (
        f"Olá, {cliente_nome}!\n"
        f"Confirmamos o recebimento do seu pagamento de R${valor:.2f}.\n"
        f"Obrigado por confiar em nossos serviços! 😊"
    )

    enviar_mensagem_whatsapp(telefone, mensagem)

#✅ Passo 3: Testar a integração Você pode testar com:



# registrar_pagamento("Reinaldo", 150.00, "+5511981772847")


#🧠 Dicas extras

#valide o número antes de enviar
# pode adicionar logs ou salvar o status do envio
#para múltiplos clientes use um loop dom lista de pagamentos.


# Se quiser, posso te ajudar a criar uma interface gráfica com botão “Confirmar e Enviar” ou até integrar com banco de dados. Quer seguir por esse caminho?















    # Verifica se tem desconto por serviço específico
    #         desconto = dc.descontos_por_servico.get(servico)
    #         if desconto:
    #             if desconto["tipo"] == "percentual":
    #                 preco_base *= (1 - desconto["valor"] / 100)
    #             elif desconto["tipo"] == "fixo":
    #                 preco_base = max(preco_base - desconto["valor"], 0.0)
    #
    #         total += preco_base
    #
    # # Verifica se há desconto total
    # if dc.var_desconto_fixo.get():
    #     try:
    #         valor = float(dc.entry_desconto_fixo.get().replace(',', '.'))
    #         dc.desconto_total = {"tipo": "fixo", "valor": valor}
    #         total = max(total - valor, 0.0)
    #     except ValueError:
    #         pass  # ou exibir aviso elegante
    #
    # elif dc.var_desconto_percentual.get():
    #     try:
    #         pct = float(dc.entry_desconto_percentual.get().replace(',', '.'))
    #         dc.desconto_total = {"tipo": "percentual", "valor": pct}
    #         total *= (1 - pct / 100)
    #     except ValueError:
    #         pass  # ou exibir aviso elegante
    #
    # dc.label_resultado.config(text=f"Total com desconto: R$ {total:.2f}")

# def calcular_total():
#     total = 0
#     porte = dc.var_porte.get()
#     precos = dc.dados_pet.get(porte, {}).get("preços", {})
#
#     for servico, var in dc.variaveis_servicos.items():
#         if var.get():
#             total += precos.get(servico, 0)
#
#     if dc.var_desconto_fixo.get():
#         valor = dc.entry_desconto_fixo.get()
#         #if valor.replace(',', '').replace('.', '').isdigit():
#         try:
#             valor_float = float(valor.replace(',', '.'))
#             total -= valor_float
#         except ValueError:
#             pass  # ou exibir uma mensagem de erro elegante
#             total -= float(valor.replace(',', '.'))
#
#     if dc.var_desconto_percentual.get():
#         pct = dc.entry_desconto_percentual.get()
#         if pct.replace(',', '').replace('.', '').isdigit():
#             total -= total * (float(pct.replace(',', '.')) / 100)
#
#     dc.label_resultado.config(text=f"Total com desconto: R$ {total:.2f}")



    # Criando Checkbuttons para serviços
    # global variaveis_servicos
    # variaveis_servicos = {}
    # servicos_disponiveis = ["Banho", "Hidratação", "Desembolo", "Remoção de Pelos",
    #                         "Corte de Unhas", "Escovação de Dentes", "Tosa Higiênica",
    #                         "Tosa na Máquina", "Tosa na Tesoura", "Leva e Trás"]

#     global labels_valores  # Dicionário para armazenar os labels de valores
#     labels_valores = {}
#
#     for i, servico in enumerate(servicos_disponiveis):
#         variaveis_servicos[servico] = tk.BooleanVar()
#         check_servico = ttk.Checkbutton(frame_servicos, text=servico, variable=variaveis_servicos[servico])
#         check_servico.grid(row=i, column=0, sticky="w")
#
#         # Criando label para exibir o valor do serviço
#         labels_valores[servico] = ttk.Label(frame_servicos, text="")
#         labels_valores[servico].grid(row=i, column=1, sticky="w")
#
#     # Criando o Frame para abatimentos
#     frame_abatimentos = ttk.LabelFrame(frame_financeiro, text="Abatimentos")
#     frame_abatimentos.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
#
#     # Variáveis para abatimentos
#     global var_desconto_fixo, var_desconto_percentual, entry_desconto_fixo, entry_desconto_percentual
#     var_desconto_fixo = tk.BooleanVar()
#     var_desconto_percentual = tk.BooleanVar()
#
#     # Checkbuttons para aplicar abatimentos
#     check_fixo = ttk.Checkbutton(frame_abatimentos, text="Desconto Fixo (R$)", variable=var_desconto_fixo)
#     check_fixo.grid(row=0, column=0, sticky="w")
#
#     entry_desconto_fixo = ttk.Entry(frame_abatimentos)
#     entry_desconto_fixo.grid(row=0, column=1, padx=10, pady=5, sticky="w")
#
#     check_percentual = ttk.Checkbutton(frame_abatimentos, text="Desconto Percentual (%)", variable=var_desconto_percentual)
#     check_percentual.grid(row=1, column=0, sticky="w")
#
#     entry_desconto_percentual = ttk.Entry(frame_abatimentos)
#     entry_desconto_percentual.grid(row=1, column=1, padx=10, pady=5, sticky="w")
#
#     # Botão para calcular total
#     botao_calcular = ttk.Button(frame_abatimentos, text="Calcular Total", command=calcular_total)
#     botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)
#
#     # Botão para limpar seleções
#     botao_limpar = ttk.Button(frame_abatimentos, text="Limpar Seleções", command=limpar_selecoes)
#     botao_limpar.grid(row=2, column=2, padx=10)
#
#     def reavaliar_precos(*args):
#         porte = var_porte.get()
#         precos = dados_pet.get(porte, {}).get("preços", {})
#         # atualiza os campos da aba_financeiro com esses preços
#
#     var_porte.trace_add("write", reavaliar_precos)
#
#     # Label para exibir o resultado do cálculo
#     global label_resultado
#     label_resultado = ttk.Label(frame_abatimentos, text="Total com desconto: R$")
#     label_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
#
#     # Frame para os métodos de pagamento
#     frame_pagamento = ttk.LabelFrame(frame_financeiro, text="Forma de Pagamento")
#     frame_pagamento.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
#
#     # Variável para definir se o pagamento foi feito ou está em aberto
#     global var_status_pagamento
#     var_status_pagamento = tk.StringVar(value="Nenhuma Opção Marcada")
#
#     # Botões para definir o status do pagamento
#     ttk.Label(frame_financeiro, text="Status do Pagamento:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
#     botao_pago = tk.Radiobutton(frame_financeiro, text="Pago", variable=var_status_pagamento, value="pago", command=atualizar_pagamento)
#     botao_pago.grid(row=3, column=1, sticky="w")
#
#     botao_em_aberto = tk.Radiobutton(frame_financeiro, text="Em Aberto", variable=var_status_pagamento, value="Em Aberto", command=atualizar_pagamento)
#     botao_em_aberto.grid(row=3, column=2, sticky="w")
#
#
# # Crie a aba e adicione ao notebook
# criar_aba_financeiro(aba_financeiro)
#
# # Calendário Data do Serviço
# frame_calendario_financeiro = ttk.LabelFrame(aba_financeiro, text="Data do Serviço")
# frame_calendario_financeiro.grid(row=0, column=4, padx=10, pady=10, sticky="w")
# calendario_financeiro = DateEntry(frame_calendario_financeiro, year=2025, locale='pt_br')
# calendario_financeiro.grid(row=0, column=4 , padx=10, pady=10, sticky='nsew')
#
# # Calendário Data Efetivação do Pagamento
# frame_calendario_financeiro = ttk.LabelFrame(aba_financeiro, text="Data do Pagamento")
# frame_calendario_financeiro.grid(row=0, column=5, padx=10, pady=10, sticky="w")
# calendario_financeiro = DateEntry(frame_calendario_financeiro, year=2025, locale='pt_br')
# calendario_financeiro.grid(row=0, column=5 , padx=10, pady=10, sticky='nsew')
#
# def calcular_total():
#     total = 0  # Inicializa o total
#     # Obtém o porte selecionado
#     porte_selecionado = var_porte.get().strip()
#
#     # Verifica se o porte está no dicionário de preços
#     if porte_selecionado in dados_pet:
#         precos = dados_pet[porte_selecionado]["preços"]
#
#         # Soma os preços dos serviços selecionados
#         for servico, variavel in variaveis_servicos.items():
#             if variavel.get():  # Verifica se o serviço está selecionado
#                 total += precos.get(servico, 0)  # Adiciona o preço do serviço
#
#     # Calcula descontos se aplicáveis
#     if var_desconto_fixo.get():
#         desconto_fixo = entry_desconto_fixo.get()
#         if desconto_fixo.isdigit():
#             total -= float(desconto_fixo)
#
#     if var_desconto_percentual.get():
#         desconto_percentual = entry_desconto_percentual.get()
#         if desconto_percentual.isdigit():
#             total -= total * (float(desconto_percentual) / 100)
#
#     # Botões para definir o status do pagamento
#     ttk.Label(frame_financeiro, text="Status do Pagamento:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
#     botao_pago = tk.Radiobutton(frame_financeiro, text="Pago", variable=var_status_pagamento, value="pago", command=atualizar_pagamento)
#     botao_pago.grid(row=3, column=1, sticky="w")
#
#     botao_em_aberto = tk.Radiobutton(frame_financeiro, text="Em Aberto", variable=var_status_pagamento, value="Em Aberto", command=atualizar_pagamento)
#     botao_em_aberto.grid(row=3, column=2, sticky="w")
#
# # Crie a aba e adicione ao notebook
# criar_aba_financeiro(aba_financeiro)
#
# # Calendário Data do Serviço
# frame_calendario_financeiro = ttk.LabelFrame(aba_financeiro, text="Data do Serviço")
# frame_calendario_financeiro.grid(row=0, column=4, padx=10, pady=10, sticky="w")
# calendario_financeiro = DateEntry(frame_calendario_financeiro, year=2025, locale='pt_br')
# calendario_financeiro.grid(row=0, column=4 , padx=10, pady=10, sticky='nsew')
#
# # Calendário Data Efetivação do Pagamento
# frame_calendario_financeiro = ttk.LabelFrame(aba_financeiro, text="Data do Pagamento")
# frame_calendario_financeiro.grid(row=0, column=5, padx=10, pady=10, sticky="w")
# calendario_financeiro = DateEntry(frame_calendario_financeiro, year=2025, locale='pt_br')
# calendario_financeiro.grid(row=0, column=5 , padx=10, pady=10, sticky='nsew')
#
