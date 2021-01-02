# responsavel pela conexao
import socket

# endereco a conectar
ip = 'bancocn.com'
# portas a serem testadas
portas = [21, 23, 80, 443, 8080]

# loop
for porta in portas:
    # cliente recebe o socket de protocolo: IP, TCP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tempo limite de conexao
    cliente.settimeout(0.1)
    # local da conexao
    codigo = cliente.connect_ex((ip, porta))
    # em caso de sucesso
    if codigo == 0:
        # exiba a porta aberta
        print (porta, "OPEN")
