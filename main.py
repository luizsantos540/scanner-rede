def solicitar_ip():
    ip = input("Digite o endereço IP que deseja verificar: ")
    return ip


ip = solicitar_ip()

print(f"IP informado: {ip}")