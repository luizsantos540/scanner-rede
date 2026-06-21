import socket


def solicitar_ip():
    ip = input("Digite o endereço IP que deseja verificar: ")
    return ip


def verificar_porta(ip, porta):

    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    conexao.settimeout(1)

    resultado = conexao.connect_ex((ip, porta))

    if resultado == 0:
        print(f"Porta {porta}: ABERTA")
    else:
        print(f"Porta {porta}: FECHADA")

    conexao.close()


ip = solicitar_ip()

portas = [21, 22, 80, 443]

for porta in portas:
    verificar_porta(ip, porta)