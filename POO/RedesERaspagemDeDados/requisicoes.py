import requests

response = requests.get("http://www.betrybe.com/")
print(response.status_code)
print(response.headers)
print(response.headers["Content-Type"])

# # Bytes recebidos em resposta
print(response.content)

# # Conteúdo recebido da requisição
print(response.text)

# Requisição do tipo post
response = requests.post("http://httpbin.org/post", data="some content")
print(response.text)

# # Requisição enviando cabeçalho (header)
response = requests.get("http://httpbin.org/get", headers={"Accept": "application/json"})
print(response.text)

# Requisição a recurso binário
response = requests.get("http://httpbin.org/image/png")

import shutil
from uuid import uuid4

r = requests.get(("https://i.pinimg.com/474x/45/b1/90/45b190ad74960773d664cff4b6520230.jpg"), stream=True)
if r.status_code == 200:
    token = uuid4()
    with open(f'./img/{token}.png', 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)


# Recurso JSON
response = requests.get("http://httpbin.org/get")
# Equivalente ao json.loads(response.content)
print(response.json())

# Podemos também pedir que a resposta lance uma exceção caso o status não seja OK
response = requests.get("http://httpbin.org/status/404")
response.status_code
response.raise_for_status()
