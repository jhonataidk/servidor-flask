import socket

def send_login(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Envia login e senha no formato "login:senha"
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    message = f"{login}:{senha}"
    client_socket.send(message.encode('utf-8'))

    # Recebe a resposta do servidor
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Resposta do servidor: {response}")

    client_socket.close()

if __name__ == "__main__":
    send_login()