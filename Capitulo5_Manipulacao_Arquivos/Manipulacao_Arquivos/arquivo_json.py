import json

dicionario = {
    "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"],
    "Florinda":["Florinda Flores", "26/11/2017", "Recep_01"]
}

with open("bd1.json", "w") as json_file:
        json.dump(dicionario,json_file)

print(dicionario)

# with open("bd.json", "r") as arq_json:
#     dicionario = json.load(arq_json)
#     print(dicionario)
#     for chave, dados in dicionario.items():
#         print(chave + " | " + str(dados))