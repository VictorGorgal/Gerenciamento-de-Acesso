import serial
from threading import Thread
from back_end import gerenciamento


def ler_serial(node):
    while True:
        recieved = node.readline()
        recebido(recieved)


def enviar_serial(node):
    while True:
        entrada = input()
        node.write(entrada.encode())


def recebido(entrada):
    if len(entrada) > 150:
        return
    if entrada == b'':
        return

    entrada = entrada.decode('ascii').strip()

    if entrada.split(',')[0] == 'banco-de-dados':
        print(f'salvando: {entrada.split(",")[1:]}')
        return

    print(entrada)


if __name__ == '__main__':
    node = serial.Serial('COM3', 115200, timeout=5)

    processo1 = Thread(target=ler_serial, args=[node])
    processo2 = Thread(target=enviar_serial, args=[node])

    processo1.start()
    processo2.start()
