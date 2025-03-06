import requests

# URL do servidor Flask
url = 'http://127.0.0.1:5000/login'

# Solicitar login e senha ao usuário
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

# Dados que serão enviados para o servidor
dados = {
    'login': login,
    'senha': senha
}

# Enviar a requisição POST
response = requests.post(url, json=dados)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Exibir a resposta do servidor
    resposta_servidor = response.json()
    print("Resposta do servidor:")
    print(f"Login: {resposta_servidor['login']}")
    print(f"Senha: {resposta_servidor['senha']}")
else:
    print(f"Erro ao se comunicar com o servidor. Status code: {response.status_code}")
