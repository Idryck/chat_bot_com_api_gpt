import openai

chave_api = "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"

openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagem=[]):
    lista_mensagem.append(
        { "role":"user", "content": mensagem }
    )
    resposta = openai.ChatCompletion.create (
        model = "gpt-3.5-turbo",
        messages = lista_mensagem,
    )
    return resposta['choices'] [0] ['message']

lista_mensagem =[]
while True:
    print("para sair escreva sair")
    texto=input("escreva aqui sua menagem:")

    if texto == "sair":
        break
    else:
        resposta=enviar_mensagem(texto)
        lista_mensagem.append(resposta)
        print("chatbot: ", resposta ["content"])


#print (enviar_mensagem ("pontos turisticos em cachoeir-ba"))



