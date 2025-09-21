# centro_controle_relatorios
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from openpyxl import Workbook
import os
from tkinter import ttk



#✅ Criação do frame antes de usar
frame_controle = ttk.Frame()
frame_controle.grid(row=0, column=0, padx=10, pady=10)




def montar_interface(janela):
    frame_controle = ttk.Frame(janela)
    frame_controle.grid(row=0, column=0, padx=10, pady=10)

    ttk.Label(frame_controle, text="De:").grid(row=4, column=0)
    # outros widgets que usam frame_controle...





def montar_centro_controle(janela):
    janela.title("Centro de Controle de Relatórios")
    frame_controle = ttk.Frame(janela)  # ou outro container como notebook ou aba
    frame_controle.grid(row=0, column=0, padx=10, pady=10)


# Seleção de período
    ttk.Label(frame_controle, text="De:").grid(row=4, column=0)
    data_inicio = DateEntry(frame_controle, width=12, background='darkblue', foreground='white', borderwidth=2)
    data_inicio.grid(row=4, column=1, padx=5)

    ttk.Label(frame_controle, text="Até:").grid(row=4, column=2)
    data_fim = DateEntry(frame_controle, width=12, background='darkblue', foreground='white', borderwidth=2)
    data_fim.grid(row=4, column=3, padx=5)



# Botão para aplicar filtro
    ttk.Button(frame_controle, text="Filtrar", command=lambda: filtrar_por_periodo).grid(row=4, column=4, padx=10)


def filtrar_por_periodo():
    inicio = data_inicio.get_date()
    fim = data_fim.get_date()

    historico = [
        {"data": date(2025, 8, 1), "info": "Exemplo 1"},
        {"data": date(2025, 8, 15), "info": "Exemplo 2"},
    ]

    # Filtrando dados fictícios para ilustrar
    dados_filtrados = [envio for envio in historico if inicio <= envio["data"] <= fim]

    # Atualiza o Treeview
    for item in treeview.get_children():
        treeview.delete(item)
    for envio in dados_filtrados:
        treeview.insert("", "end", values=(envio["data"].strftime("%d/%m/%Y %H:%M"), envio["cliente"], envio["status"]))

    ttk.Label(frame_controle, text="📋 Centro de Controle de Relatórios", font=("Segoe UI", 14)).grid(row=0, column=0, columnspan=3, pady=10)

# Histórico de envios
treeview = ttk.Treeview(frame_controle, columns=("Data", "Cliente", "Status"), show="headings")
treeview.heading("Data", text="Data/Hora")
treeview.heading("Cliente", text="Cliente")
treeview.heading("Status", text="Status")
treeview.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Status atual
label_status = ttk.Label(frame_controle, text="🔄 Aguardando envio...")
label_status.grid(row=2, column=0, columnspan=3)


def exportar_historico():
    print("📤 Exportando histórico...")  # Aqui você colocaria a lógica real de exportação
# Botão para exportar histórico
ttk.Button(frame_controle, text="Exportar Histórico", command=lambda: exportar_historico()).grid(row=3, column=0, pady=10)



def gerar_relatorio_pdf(dados, nome_arquivo="relatorio.pdf", pasta_destino="relatorios"):
    os.makedirs(pasta_destino, exist_ok=True)
    caminho = os.path.join(pasta_destino, nome_arquivo)

    c = canvas.Canvas(caminho, pagesize=A4)
    largura, altura = A4

    c.setFont("Helvetica", 12)
    c.drawString(50, altura - 50, "Relatório Financeiro")

    y = altura - 100
    for linha in dados:
        c.drawString(50, y, linha)
        y -= 20

    c.save()
    print(f"✅ PDF gerado em: {caminho}")
    return caminho

from reportlab.pdfgen import canvas

c = canvas.Canvas("teste.pdf")
c.drawString(100, 750, "Olá, Reinaldo!")
c.save()

print("PDF gerado com sucesso!")




def gerar_excel(dados, nome_arquivo="relatorio.xlsx", pasta_destino="relatorios"):
    os.makedirs(pasta_destino, exist_ok=True)
    caminho = os.path.join(pasta_destino, nome_arquivo)

    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório"

    for linha in dados:
        ws.append(linha)

    wb.save(caminho)
    print(f"✅ Excel gerado em: {caminho}")
    return caminho



c = canvas.Canvas("teste.pdf")
c.drawString(100, 750, "Olá, Reinaldo! PDF gerado com ReportLab.")
c.save()


