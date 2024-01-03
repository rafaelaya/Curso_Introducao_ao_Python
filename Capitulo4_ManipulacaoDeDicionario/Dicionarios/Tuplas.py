usuarios ={}
emails = ["xpto@xyz.com", "xkcd@phd.com"]

tupla = list (enumerate (emails))

for chave in range (0,len(tupla)):
    print("Email: ", tupla [chave] [1])
    usuarios [tupla [chave]] = [input("Digite o nome"), input("Digite o nivel")]

for chave, dado in usuarios.items():
    print("Usuario.:", chave [0])
    print("Email.:", chave[1])
    print("Nome.:", chave[0])
    print("Nivel.:", chave[1])