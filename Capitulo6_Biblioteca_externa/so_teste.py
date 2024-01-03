import getpass
# import platform
import getpass
# from datetime import datetime

# print("Nome do Computador..................: ", platform.node())
# print("Arquitetura.........................: ", platform.architecture())
# print("Nome do Sistema Operacional.........: ", platform.system())
# print("Versão do Sistema Operacional.......: ", platform.release())
# print("Tipo de Máquina.....................: ", platform.machine())
# print("Processador.........................: ", platform.processor())
# print("Versão do Python....................: ", platform.python_version())

# print(datetime.now())

# print(getpass.getuser())
# print(getpass.getpass("Digite sua senha"))

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha")

if usuario == 'Rafaela Gomes' and senha == '0'
    print('Bem-vinda Adele')
else:
    print('Voce nao tem acesso')