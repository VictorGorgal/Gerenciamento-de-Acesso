import serial
from threading import Thread


class arduinoSerial:
    def __init__(self, mostrar, salvar):
        # Mude a porta serial
        self.node = serial.Serial('COM3', 115200, timeout=5)
        self.mostrar = mostrar
        self.salvar = salvar
        self.p1 = Thread(target=self.ler_serial)
        self.p1.start()

    def ler_serial(self):
        while True:
            recieved = self.node.readline()
            self.recebido(recieved)

    def recebido(self, entrada):
        if len(entrada) > 150:
            return
        if entrada == b'':
            return

        entrada = entrada.decode('ascii').strip()

        if entrada.split(',')[0] == 'banco-de-dados':
            self.salvar(f'salvando: {entrada.split(",")[1:]}')
            return

        self.mostrar(entrada)

    def enviar_serial(self, texto):
        self.node.write(texto.encode())


if __name__ == '__main__':
    def m(entrada):
        print(entrada)


    def s(entrada):
        print(f'salvar: {entrada}')


    ser = arduinoSerial(m, s)
