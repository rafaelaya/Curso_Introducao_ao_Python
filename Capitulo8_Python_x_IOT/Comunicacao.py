import serial
from serial.tools import list_ports

#lista as portas do arduino.

for porta in list_ports.comports():
    print('Dispositivos: {} - porta: {} '.format(port.description, port.device))

conexao = serial.Serial("COM3", 115200)

acao=input ("Digite:\n<L> para Ligar\n<D> para Desligar: ").upper()
while acao=="L" or acao=="D":
    if acao=="L":
        conexao.write(b'1')
    else:
        conexao.write(b'0')
    acao = input ("Digite:\n<L> para Ligar\n para Desligar: ").upper()
conexao.close()
print("Conexao encerrada")