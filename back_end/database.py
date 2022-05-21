import sqlite3
from os.path import exists
from datetime import datetime


class DB:
    def __init__(self, file: str):
        self.database = file

        self.initDB()

    def save_usuario(self, nome: str, senha: str, admin: str):
        """
        salva o usuário no banco de dados na tabela 'usuarios'
        :param nome: str: nome do usuário
        :param senha: str: senha do usuário
        :param admin: str: 0 ou 1
        :return: None
        """
        self.connection = sqlite3.connect(self.database)
        cursor = self.connection.cursor()

        cursor.execute('insert into usuarios (nome, senha, admin) values (?, ?, ?)', [nome, senha, admin])

        self.connection.commit()
        self.connection.close()

    def save_evento(self, evento: str, usuario: str):
        """
        salva o evento no banco de dados na tabela 'eventos'
        :param evento: str: evento que ocorreu (ex. Abriu a porta 2)
        :param usuario: str: usuário responsável por gerar o evento
        :return: None
        """
        now = datetime.now()
        dia = f'{now.day}/{now.month}/{now.year}'
        horario = f'{now.hour}:{now.minute}:{now.second}'

        self.connection = sqlite3.connect(self.database)
        cursor = self.connection.cursor()

        cursor.execute('insert into eventos values (?, ?, ?, ?)', [dia, horario, evento, usuario])

        self.connection.commit()
        self.connection.close()

    def initDB(self):
        """
        Cria o database caso ainda não exista
        :return: None
        """
        if exists(self.database):
            return

        print('Criando database...')
        self.connection = sqlite3.connect(self.database)
        cursor = self.connection.cursor()

        cursor.execute("""create table usuarios (
                        nome text, 
                        senha text, 
                        admin blob)""")

        cursor.execute("""create table eventos (
                        data text,
                        horario text,
                        evento text,
                        usuario text)""")

        self.connection.close()


if __name__ == '__main__':
    g = DB('./database.db')

    g.save_usuario(nome='usuario1', senha='Senha123@!', admin='1')
    g.save_evento(evento='abriu a porta 1', usuario='usuario1')
