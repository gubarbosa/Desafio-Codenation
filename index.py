import requests
import json
import string
import hashlib

#faz a requisicao HTTP
requisicao = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=dbe5421d5d8160f6094d1f402b28c8be16f28f95"
r = requests.get(requisicao)

#conteudo json
json = json.dumps(r.json())

#cria um arquivo json com o conteudo da requisicao
arquivo = open("answer.json", "w")
arquivo.write(json)