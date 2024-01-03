nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
prioridade="NÃO"
if idade>=65:
    prioridade="SIM"
    print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)
else:
    print("O paciente " + nome + " Nao possui atendimento prioritario!")
print("FIM")