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
        with open("resultado.txt", "a") as arquivo:
            arquivo.write(f"Porta {porta}: ABERTA\n")
    else:
        print(f"Porta {porta}: FECHADA")

    conexao.close()


ip = solicitar_ip()

for porta in range(1, 15):
    verificar_porta(ip, porta)