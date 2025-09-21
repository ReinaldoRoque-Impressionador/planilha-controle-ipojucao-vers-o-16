# import pygame
# import os
# from tkinter import ttk
#
# from abas import dados_compartilhados as dc
#
# # 🔧 Inicializa o mixer apenas uma vez
# pygame.mixer.init()
#
# # 🎚️ Controle global do som
# som_global_ativo = True
#
#
#
# def criar_aba_audio_avancado(notebook):
#     frame = ttk.Frame(notebook)
#
#     status_label = ttk.Label(frame, text="🔈 Som Global Ativado")
#     status_label.pack(pady=5)
#
#     def atualizar_status():
#         texto = "🔈 Som Global Ativado" if dc.som_global_ativo else "🔇 Som Global Desativado"
#         status_label.config(text=texto)
#
#     ttk.Button(frame, text="Ativar Som", command=lambda: [ativar_som(), atualizar_status()]).pack(pady=2)
#     ttk.Button(frame, text="Desativar Som", command=lambda: [desativar_som(), atualizar_status()]).pack(pady=2)
#
#     ttk.Button(frame, text="▶️ Tocar Música de Fundo", command=lambda: tocar_musica("sons/abertura.mp3")).pack(pady=5)
#     ttk.Button(frame, text="⏹️ Parar Música", command=parar_musica).pack(pady=2)
#
#     ttk.Button(frame, text="🔔 Tocar Som Curto", command=lambda: tocar_som_curto("sons/sucesso.mp3")).pack(pady=5)
#
#     ttk.Label(frame, text="Evento Sonoro:").pack(pady=5)
#     eventos = ["erro", "login_sucesso", "abertura"]
#     var_evento = tk.StringVar(value=eventos[0])
#     ttk.Combobox(frame, textvariable=var_evento, values=eventos, state="readonly").pack()
#
#     ttk.Button(frame, text="🔊 Tocar Evento", command=lambda: som_evento(var_evento.get())).pack(pady=5)
#
#     return frame
#
#
#
#
#
#
#
# # 🎵 Tocar música longa (com ou sem repetição)
# def tocar_musica(path, repetir=True):
#     if som_global_ativo and os.path.exists(path):
#         pygame.mixer.music.load(path)
#         pygame.mixer.music.play(-1 if repetir else 0)
#
# # 🔈 Tocar efeito sonoro curto
# def tocar_som_curto(path):
#     if som_global_ativo and os.path.exists(path):
#         som = pygame.mixer.Sound(path)
#         som.play()
#
# # ⏹️ Parar música atual
# def parar_musica():
#     pygame.mixer.music.stop()
#
# # 🔇 Desativar som global
# def desativar_som():
#     global som_global_ativo
#     som_global_ativo = False
#     parar_musica()
#
# # 🔊 Ativar som global
# def ativar_som():
#     global som_global_ativo
#     som_global_ativo = True
#
# def som_evento(tipo):
#     sons = {
#         "erro": "sons/erro.mp3",
#         "login_sucesso": "sons/sucesso.mp3",
#         "abertura": "sons/abertura.mp3"
#     }
#
#     caminho = sons.get(tipo)
#     if caminho and som_global_ativo:
#         try:
#             pygame.mixer.music.load(caminho)
#             pygame.mixer.music.play()
#         except Exception as e:
#             print(f"🔇 Erro ao tocar som '{tipo}': {e}")