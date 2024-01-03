# arquivo = open ("primeiro_arquivo.txt", "w")

# arquivo.write("Meu primeiro arquivo")

# arquivo.close()

# with open ("primeiro_arquivo.txt", "a") as arquivo:
#     arquivo.write("\nHakuna Matata!!")

with open ("primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
    print(linha)