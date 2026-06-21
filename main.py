import socket


def solicitar_ip():
    ip = input("Digite o endereço IP que deseja verificar: ")
    return ip


def verificar_porta(ip, porta):
    try:
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

    except socket.gaierror:
        print("Erro: Endereço IP inválido ou não encontrado.")
        return False
    except socket.error:
        print("Erro: Houve um problema de conexão com a rede.")
        return False
    return True


ip = solicitar_ip()

for porta in range(1, 16):
    if not verificar_porta(ip, porta):
        break