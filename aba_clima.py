# import pygame
# pygame.mixer.init()

from pprint import pprint
import requests
import os

from tkinter import ttk


# importações após reestruturação do projeto

from modulos.recursos.utilitarios import caminho_arquivo

# e qualquer biblioteca de API externa (requests, etc.)

# importações após reestruturação do projeto


logo_splash = caminho_arquivo("splash.png", subpasta=os.path.join("..", "..", "imagensipojucao"))
som_relatorio = caminho_arquivo("relatorio_finalizado.mp3", subpasta="sons")

def montar_aba_clima(master):
    inner_frame = ttk.Frame(master)
    inner_frame.grid(row=0, column=0, sticky="nsew")



    api_key = "f1e5d72cde264a6c89615014250507"
    link_api = "http://api.weatherapi.com/v1/current.json"

    parametros = {
        "key": api_key,
        "q": "São Paulo",
        "lang": "pt"
    }

    resposta = requests.get(link_api, params=parametros)

    if resposta.status_code == 200:
        dados_requisicao = resposta.json()
        pprint(dados_requisicao)
        temp = dados_requisicao["current"]["temp_c"]
        descricao = dados_requisicao["current"]["condition"]["text"]
        print(temp)
        print(descricao)
    return inner_frame

api_key = "f1e5d72cde264a6c89615014250507"


link_api = "http://api.weatherapi.com/v1/current.json"

parametros = {
    "key": api_key,
    "q": "São Paulo",
    "lang": "pt"
}

resposta = requests.get(link_api, params=parametros)

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    pprint(dados_requisicao)
    temp = dados_requisicao["current"]["temp_c"]
    descricao = dados_requisicao["current"]["condition"]["text"]
    print(temp)
    print(descricao)




# status code
# 200 ->  deu certo a requisição
# 300 ->  redirecionada
# 400 ->  não conseguiu fazer a requisição
# 500 ->  deu um erro no sistemaa





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


#barra_audio(frame_aba_clima)  # ou frame_aba_menu, frame_aba_config, etc.