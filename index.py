import requests
import json
import string
import hashlib

requisicao = https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=dbe5421d5d8160f6094d1f402b28c8be16f28f95
r = requests.get(requesicao)

#conteudo json
json = json.dumps(r.json())

arquivo = open("answer.json", "w")
arquivo.write(json)