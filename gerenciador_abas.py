# modulos/controladores/gerenciador_abas.py

class GerenciadorAbas:
    def __init__(self):
        self.abas = {}

    def registrar_aba(self, nome, funcao):
        self.abas[nome] = funcao

    def trocar_aba(self, nome_aba, master):
        try:
            return self.abas[nome_aba](master)
        except KeyError:
            print(f"❌ Aba '{nome_aba}' não reconhecida.")
            return None

# Instância global (opcional)
gerenciador = GerenciadorAbas()

# def trocar_aba(nome_aba, master):
#     return gerenciador.trocar_aba(nome_aba, master)

def trocar_aba(self, nome_aba, master):
    print(f"🔄 Trocando para aba: {nome_aba}")
    try:
        return self.abas[nome_aba](master)
    except KeyError:
        print(f"❌ Aba '{nome_aba}' não reconhecida.")
        return None
    except Exception as e:
        print(f"❌ Erro ao abrir aba '{nome_aba}': {e}")
        return None