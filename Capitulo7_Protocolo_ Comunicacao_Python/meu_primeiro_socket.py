import socket

resp="S"
while (resp=="S"):
    url=input("Digite uma url: ")
    ip=socket.gethostname()
    print("O IP referente a url informada e: ", ip)
    resp=input("Digite <s> para continuar: ").upper()