
# tela_principal.py

import tkinter as tk
from tkinter import ttk
import os

from abas.aba_inativos import montar_aba_inativos
from dados_compartilhados import montar_dados_compartilhados
from modulos.abas.aba_cadastro import montar_aba_cadastro
from modulos.abas.aba_clientes import montar_aba_clientes
from modulos.abas.aba_consulta import montar_aba_consulta
from modulos.abas.aba_financeiro import montar_aba_financeiro
from modulos.abas.aba_relatorios import montar_aba_relatorios
from modulos.abas.aba_clima import montar_aba_clima
from modulos.recursos.aba_itau import criar_aba_itau
from modulos.abas.aba_config import montar_aba_config
from modulos.abas.editor_codigo import AbaEditorCodigo
from modulos.abas.ferramentas.barra_som import criar_barra_som
from modulos.abas.aba_consulta import montar_aba_consulta

def criar_player():
    pass

from modulos.banco.database import testar_conexao
from modulos.recursos.conexao_utils import conexao_valida  # aqui conexao_valida  grifado em vermelho
from modulos.componentes.barra_som_widget import criar_barra_som

from modulos.controladores.gerenciador_abas import GerenciadorAbas
from modulos.componentes.menu_lateral_widget import MenuAdmin

# def montar_centro_controle(janela):
#     from modulos.recursos.centro_controle_relatorios import montar_centro_controle
#     montar_centro_controle(janela)

#from modulos.abas.aba_inativos import montar_aba_inativos

gerenciador = GerenciadorAbas()
# Importações internas para evitar ciclos
# gerenciador.registrar_aba("cadastro", montar_aba_cadastro) # lambda master: __import__("modulos.abas.aba_cadastro").abas.aba_cadastro.montar_aba_cadastro(master))
# gerenciador.registrar_aba("financeiro", montar_aba_financeiro) # lambda master: __import__("modulos.abas.aba_financeiro").abas.aba_financeiro.montar_aba_financeiro(master))
# gerenciador.registrar_aba("clientes", montar_aba_clientes) # lambda master: __import__("modulos.abas.aba_clientes").abas.aba_clientes.montar_aba_clientes(master))
# gerenciador.registrar_aba("editor_codigo") # lambda master: __import__("modulos.abas.editor_codigo").abas.editor_codigo.AbaEditorCodigo(master))
# gerenciador.registrar_aba("clima", montar_aba_clima) # lambda master: __import__("modulos.abas.aba_clima").abas.aba_clima.montar_aba_clima(master))
# gerenciador.registrar_aba("config", montar_aba_config) # lambda master: __import__("modulos.abas.aba_config").abas.aba_config.montar_aba_config(master))
# gerenciador.registrar_aba("relatorios", montar_aba_relatorios) # lambda master: __import__("modulos.abas.aba_relatorios").abas.aba_relatorios.montar_aba_relatorios(master))
# gerenciador.registrar_aba("itau") #  lambda master: __import__("modulos.abas.aba_itau").abas.aba_itau.montar_aba_itau(master))
# gerenciador.registrar_aba("dados_compartilhados", montar_dados_compartilhados) # lambda master: __import__("modulos.abas.aba_dados_compartilhados").abas.aba_dados_compartilhados.montar_aba_dados_compartilhados(master))
# gerenciador.registrar_aba("montar_aba_inativos", montar_aba_inativos) # lambda master: __import__("modulos.abas.aba_dados_compartilhados").abas.aba_dados_compartilhados.montar_aba_dados_compartilhados(master))

gerenciador.registrar_aba("cadastro", montar_aba_cadastro)
gerenciador.registrar_aba("financeiro", montar_aba_financeiro)
gerenciador.registrar_aba("clientes", montar_aba_clientes)
gerenciador.registrar_aba("editor_codigo", AbaEditorCodigo)
gerenciador.registrar_aba("clima", montar_aba_clima)
gerenciador.registrar_aba("config", montar_aba_config)
gerenciador.registrar_aba("relatorios", montar_aba_relatorios)
gerenciador.registrar_aba("itau", criar_aba_itau)
gerenciador.registrar_aba("dados_compartilhados", montar_dados_compartilhados)
gerenciador.registrar_aba("montar_aba_inativos", montar_aba_inativos)
gerenciador.registrar_aba("consulta", montar_aba_consulta)

# ... e assim por diante

def verificar_conexao():
    testar_conexao()
    if conexao_valida():
        print("✅ Conexão OK")
    else:
        print("❌ Erro na conexão")

verificar_conexao()

def iniciar_janela_principal(usuario_logado):
    janela = tk.Tk()
    janela.title("Sistema Principal")
    janela.geometry("1024x768")

    # Layout da janela
    janela.grid_rowconfigure(0, weight=1)
    janela.grid_columnconfigure(0, weight=1)

    # Frame principal
    frame_principal = tk.Frame(janela)
    frame_principal.grid(row=1, column=0, sticky="nsew")
    frame_principal.grid_rowconfigure(0, weight=1)
    frame_principal.grid_columnconfigure(0, weight=0)
    frame_principal.grid_columnconfigure(1, weight=0)
    frame_principal.grid_columnconfigure(2, weight=1)

    # Topo com barra de som
    frame_topo = tk.Frame(janela)
    frame_topo.grid(row=0, column=0, sticky="ew")
    frame_topo.grid_columnconfigure(0, weight=1)
    barra_som = criar_barra_som(frame_topo)
    barra_som.grid(row=0, column=0, sticky="ew", padx=10, pady=5)



    # Menu lateral (se for admin)
    if usuario_logado.perfil == "admin":
        conteudo_coluna = 2
    else:
        conteudo_coluna = 1



    # Área de conteúdo

    conteudo = tk.Frame(frame_principal, bg="white")
    conteudo.grid(row=0, column=conteudo_coluna, sticky="nsew")


    # Notebook com abas
    notebook = ttk.Notebook(conteudo)
    notebook.grid(row=0, column=0, sticky="nsew")

    # Menu lateral (somente para admin)
    if usuario_logado.perfil == "admin":
        menu_admin = MenuAdmin(
            master=frame_principal,
            perfil_usuario=usuario_logado.perfil,
            gerenciador_abas=gerenciador,
            notebook=notebook
        )
        menu_admin.grid(row=0, column=1, sticky="ns")

    # Abas principais
    notebook.add(montar_aba_clientes(notebook), text="📋 Clientes")
    notebook.add(montar_aba_cadastro(notebook), text="📋 Cadastro")
    notebook.add(montar_aba_consulta(notebook), text="🔍 Consulta")
    notebook.add(montar_aba_financeiro(notebook), text="💰 Financeiro")
    notebook.add(montar_aba_relatorios(notebook), text="📊 Relatórios")
    notebook.add(montar_aba_clima(notebook), text="🌦️ Clima")
    notebook.add(criar_aba_itau(notebook), text="🏦 Itaú")
    notebook.add(montar_aba_config(notebook), text="⚙️ Configurações")
    #notebook.add(montar_aba_inativos(notebook), text="🚫 Inativos")


    # Área de conteúdo
    #conteudo = tk.Frame(frame_principal, bg="white")

    janela.mainloop()

class MenuLateral(tk.Frame):
    def __init__(self, master, perfil_usuario, gerenciador_abas):
        super().__init__(master, bg="#f0f0f0")
        self.gerenciador = gerenciador_abas
        self.perfil = perfil_usuario
        self.montar_menu()

    def montar_menu(self):
        abas_disponiveis = ["cadastro", "clientes", "editor_codigo", "clima", "config", "consulta", "financeiro",
                            "relatórios", "itau", "dados_compartilhados"]

        if self.perfil == "admin":
            abas_disponiveis.append("editor_codigo")

        for i, nome_aba in enumerate(abas_disponiveis):
            btn = tk.Button(
                self,
                text=nome_aba.capitalize(),
                command=lambda aba=nome_aba: self.gerenciador.trocar_aba(aba, self.master)
            )
            btn.grid(row=i, column=0, sticky="ew", padx=10, pady=5)

        # Expande a coluna para ocupar toda a largura disponível
        self.grid_columnconfigure(0, weight=1)

def caminho_imagem(nome):
    base = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base, "imagensipojucao", "imagens", nome)

def criar_player_som(janela):
        from modulos.componentes.player_widget import PlayerSom  # exemplo
        player = PlayerSom(janela)
        return player



