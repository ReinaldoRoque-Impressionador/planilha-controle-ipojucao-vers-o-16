import tkinter as tk
from tkinter import ttk
from modulos.controladores.gerenciador_abas import GerenciadorAbas

def menu_lateral(frame_principal):
    def abrir_aba(nome):
        conteudo = GerenciadorAbas(nome, frame_principal)
        if conteudo:
            conteudo.grid(row=0, column=1, sticky="nsew")

    # Criação do frame do menu
    menu = tk.Frame(frame_principal, bg="#d3d3d3", width=200)
    menu.grid(row=0, column=0, sticky="ns")

    estilo = ttk.Style()
    estilo.configure("TButton", padding=6, relief="flat", background="#f0f0f0")

    botoes = [
        ("Cadastro", lambda: abrir_aba("cadastro")),
        ("Financeiro", lambda: abrir_aba("financeiro")),
        ("Relatórios", lambda: abrir_aba("relatorios")),
        ("Consulta", lambda: abrir_aba("consulta")),
        ("Clientes", lambda: abrir_aba("clientes")),
        ("Clima", lambda: abrir_aba("clima"))
    ]

    # Criação e posicionamento dos botões
    for i, (texto, comando) in enumerate(botoes):
        btn = ttk.Button(menu, text=texto, command=comando)
        btn.grid(row=i, column=0, sticky="ew", padx=10, pady=5)

    menu.grid_columnconfigure(0, weight=1)


# class MenuAdmin(tk.Frame):
#     def __init__(self, master, *args, **kwargs):
#         super().__init__(master, bg="#f5f5f5", width=180, *args, **kwargs)
#         self._criar_estilo()
#         self._criar_botoes()

class MenuAdmin(tk.Frame):
    def __init__(self, master, perfil_usuario, gerenciador_abas, notebook, *args, **kwargs):
        super().__init__(master, bg="#f5f5f5", width=180, *args, **kwargs)
        self.perfil = perfil_usuario
        self.gerenciador = gerenciador_abas
        self.notebook = notebook
        self._criar_estilo()
        self._criar_botoes()


    def _criar_estilo(self):
        estilo = ttk.Style()
        estilo.configure("Admin.TButton", padding=6, relief="flat", background="#e0e0e0")

    def _abrir_aba(self, nome):
        conteudo = trocar_aba(nome, self.master)
        if conteudo:
            conteudo.grid(row=0, column=1, sticky="nsew")

    def _criar_botoes(self):
        botoes_admin = [
            ("Aba Itaú", lambda: self._abrir_aba("aba_itau")),
            ("Editor de Código", lambda: self._abrir_aba("editor_codigo")),
            ("Logs do Sistema", lambda: self._abrir_aba("logs")),
            ("Config Avançada", lambda: self._abrir_aba("config_avancada"))
        ]

        for i, (texto, comando) in enumerate(botoes_admin):
            btn = ttk.Button(self, text=texto, command=comando, style="Admin.TButton")
            btn.grid(row=i, column=0, sticky="ew", padx=10, pady=5)

        self.grid_columnconfigure(0, weight=1)

    def _criar_botoes(self):
        abas_disponiveis = ["cadastro", "clientes", "editor_codigo", "clima", "config", "consulta", "financeiro",
                            "relatorios", "itau", "dados_compartilhados"]

        if self.perfil == "admin":
            abas_disponiveis.append("editor_codigo")

        for i, nome_aba in enumerate(abas_disponiveis):
            btn = tk.Button(
                self,
                text=nome_aba.capitalize(),
                command=lambda aba=nome_aba: self.gerenciador.trocar_aba(aba, self.notebook)
            )
            btn.grid(row=i, column=0, sticky="ew", padx=10, pady=5)

        self.grid_columnconfigure(0, weight=1)

def montar_menu_lateral_clientes(container, acoes):
    frame_menu = ttk.LabelFrame(container, text="Menu Cliente")
    frame_menu.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

    for i, (nome_botao, funcao_callback) in enumerate(acoes.items()):
        btn = ttk.Button(frame_menu, text=nome_botao, command=funcao_callback)
        btn.grid(row=i, column=0, padx=5, pady=5, sticky="ew")

# import tkinter as tk
# from tkinter import ttk
# from modulos.controladores.fluxo_abas import trocar_aba
#
#
# def menu_lateral(frame_principal):
#     def abrir_aba(nome):
#         conteudo = trocar_aba(nome, frame_principal)
#         if conteudo:
#             conteudo.grid(row=0, column=1, sticky="nsew")
#
#     botoes = [
#         ("Cadastro", lambda: abrir_aba("cadastro")),
#         ("Financeiro", lambda: abrir_aba("financeiro")),
#         ("Relatórios", lambda: abrir_aba("relatorios")),
#         ("Consulta", lambda: abrir_aba("consulta")),
#         ("Clientes", lambda: abrir_aba("clientes")),
#         ("Clima", lambda: abrir_aba("clima"))
#
#     ]
#
# # Criação e posicionamento dos botões com grid
# for i, (texto, comando) in enumerate(botoes):
#     btn = ttk.Button(menu, text=texto, command=comando)
#     btn.grid(row=i, column=0, sticky="ew", padx=10, pady=5)
#
# # Expansão horizontal dos botões
# menu.grid_columnconfigure(0, weight=1)






# #importação após reestruturação do projeto
# from recursos import aba_itau
# import tkinter as tk
# from tkinter import ttk
#
# from modulos.abas.aba_cadastro import montar_aba_cadastro
# from modulos.abas.aba_financeiro import chamar_aba_financeiro
# from modulos.abas.aba_clientes import chamar_aba_clientes
# from modulos.abas.aba_consulta import chamar_aba_consulta
# from modulos.abas.aba_relatorios import chamar_aba_relatorios
# from modulos.abas.aba_clima import montar_aba_clima
# from modulos.recursos.aba_itau import criar_aba_itau
# #importações após reestruturação do projeto



# def menu_lateral(frame_principal):
#     menu = tk.Frame(frame_principal, bg="gray", width=200)
#     menu.pack(side="left", fill="y")
#
#     ttk.Button(menu, text="Login", command=criar_login).grid(row=0, column=0, sticky="ns")
#
#     ttk.Button(menu, text="Cadastro", command=chamar_aba_cadastro).grid(row=0, column=0, sticky="ns")
#     ttk.Button(menu, text="Financeiro", command=chamar_aba_financeiro).grid(row=0, column=0, sticky="ns")
#
#     ttk.Button(menu, text="Clientes", command=chamar_aba_clientes).grid(row=0, column=0, sticky="ns")
#     ttk.Button(menu, text="Consulta", command=chamar_aba_consulta).grid(row=0, column=0, sticky="ns")
#
#     ttk.Button(menu, text="Relatórios", command=chamar_aba_relatorios).grid(row=0, column=0, sticky="ns")
#
#     ttk.Button(menu, text="Clima", command=montar_aba_clima).grid(row=0, column=0, sticky="ns")
#
#     ttk.Button(menu, text="Itaú", command=criar_aba_itau).grid(row=0, column=0, sticky="ns")
#
#     # etc...



    # def menu_lateral(frame_principal):
#     # Criação do menu lateral
#     menu = tk.Frame(frame_principal, bg="#d3d3d3", width=200)
#     menu.grid(row=0, column=0, sticky="ns")  # fixa na lateral esquerda
#
#     # Estilo opcional para os botões
#     estilo = ttk.Style()
#     estilo.configure("TButton", padding=6, relief="flat", background="#f0f0f0")
#
#     # Lista de botões com seus textos e comandos
#     botoes = [
#         ("Login", criar_login),
#         ("Cadastro", chamar_aba_cadastro),
#         ("Financeiro", chamar_aba_financeiro),
#         ("Clientes", chamar_aba_clientes),
#         ("Consulta", chamar_aba_consulta),
#         ("Relatórios", chamar_aba_relatorios),
#         ("Clima", montar_aba_clima),
#         ("Itaú", criar_aba_itau)
#     ]
