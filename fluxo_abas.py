# from modulos.abas.aba_clientes import montar_aba_clientes
# from modulos.abas.editor_codigo import AbaEditorCodigo
#
# def trocar_aba(nome_aba, master):
#     if nome_aba == "cadastro":
#         from modulos.abas.aba_cadastro import montar_aba_cadastro
#         return montar_aba_cadastro(master)
#     elif nome_aba == "financeiro":
#         from modulos.abas.aba_financeiro import montar_aba_financeiro
#         return montar_aba_financeiro(master)
#     elif nome_aba == "relatórios":
#         from modulos.abas.aba_relatorios import montar_aba_relatorios
#         return montar_aba_relatorios(master)
#     elif nome_aba == "consulta":
#         from modulos.abas.aba_consulta import montar_aba_consulta
#         return montar_aba_consulta(master)
#     elif nome_aba == "clientes":
#         from modulos.abas.aba_clientes import montar_aba_clientes
#         return montar_aba_clientes(master)
#     elif nome_aba == "clima":
#         from modulos.abas.aba_clima import montar_aba_clima
#         return montar_aba_clima(master)
#
#     # Adicione outras abas conforme necessário
#     else:
#         print(f"❌ Aba '{nome_aba}' não reconhecida.")
#         return None
#
#
#
# def trocar_aba(nome_aba, master):
#     if nome_aba == "editor_codigo":
#         return AbaEditorCodigo(master)
#     # ... outras abas