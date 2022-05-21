import serial
from threading import Thread
from back_end.database import DB


class arduinoSerial:
    def __init__(self, mostrar):
        # Mude a porta serial
        self.node = serial.Serial('COM3', 115200, timeout=5)
        self.DB = DB('./back_end/database.db')
        self.mostrar = mostrar
        self.p1 = Thread(target=self.ler_serial)
        self.p1.daemon = True  # termina a thread quando o aplicativo for fechado
        self.p1.start()

    def ler_serial(self):
        """
        Roda em uma thread separada da main, responsável pela leitura da informação enviada pelo node
        :return: None
        """
        while True:
            recieved = self.node.readline()
            self.recebido(recieved)

    def recebido(self, entrada):
        """
        Roda sempre que for recebido uma mensagem do nodeMCU
        :param entrada: linha recebida via serial
        :return: None
        """
        if len(entrada) > 150:
            return
        if entrada == b'':
            return

        entrada = entrada.decode('ascii').strip()

        if entrada.split(',')[0] == 'banco-de-dados':
            self.salvar(entrada.split(",")[1:])
            return

        self.mostrar(entrada)

    def enviar_serial(self, texto: str):
        """
        Envia a informação ao nodeMCU
        :param texto: str: informação a ser enviada
        :return: None
        """
        self.node.write(texto.encode())

    def salvar(self, text: str):
        """
        Função executada sempre que receber uma linha via serial que começa com 'banco-de-dados'
        :param text: str: informação a ser salva no banco de dados
        :return: None
        """
        tipo = text[0]
        if tipo == 'usuario':
            self.DB.save_usuario(text[1], text[2], text[3])

        if tipo == 'evento':
            self.DB.save_evento(text[1], text[2])
