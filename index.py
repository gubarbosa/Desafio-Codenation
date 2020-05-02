import requests
import json
import string
import hashlib

#faz a requisicao HTTP
requisicao = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=dbe5421d5d8160f6094d1f402b28c8be16f28f95"
r = requests.get(requisicao)

#conteudo json
json_file = json.dumps(r.json())

#cria um arquivo json com o conteudo da requisicao
arquivo = open("answer.json", "w")
arquivo.write(json_file)

#obter o número de casas e o texto cifrado do arquivo
with open('answer.json', 'r') as arquivo:
    arq_json = json.load(arquivo)

    texto_cifrado = arq_json['cifrado']
    numero_casas = arq_json['numero_casas']

arquivo.close()

#alfabeto da biblioteca string
alfabeto = string.ascii_lowercase
texto_decifrado = ""

for i in texto_cifrado:

    if i in alfabeto:
        index = alfabeto.index(i) - numero_casas

        if index < 0:
            index += len(alfabeto)
        
        texto_decifrado += alfabeto[index]
    
    else:
        texto_decifrado += i


#gera o resumo criptografado em sha1
sha1 = hashlib.sha1(texto_decifrado.encode()).hexdigest()

print(texto_decifrado, sha1)


with open("answer.json", "r") as arquivo:
    arquivo_json = json.load(arquivo)
    arquivo_json['decifrado'] = texto_decifrado
    arquivo_json['resumo_criptografico'] = sha1

with open("answer.json", "w") as arquivo:
    arquivo_json = json.dumps(arquivo_json, indent=4)
    arquivo.write(arquivo_json)

#envia arquivo para API
url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=dbe5421d5d8160f6094d1f402b28c8be16f28f95"
resposta = {'answer': open('answer.json', 'rb')}
r = requests.post(url, files=resposta)