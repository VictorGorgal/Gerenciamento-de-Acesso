import sqlite3
from os.path import exists
from datetime import datetime


class gerenciamento:
    def __init__(self, file):
        self.database = file

        self.initDB()

    def save_usuario(self, data):
        _, nome, senha, admin = data.split(';')

        self.connection = sqlite3.connect(self.database)
        cursor = self.connection.cursor()

        cursor.execute('insert into usuarios (nome, senha, admin) values (?, ?, ?)', [nome, senha, admin])

        self.connection.commit()
        self.connection.close()

    def save_evento(self, data):
        _, evento, usuario = data.split(';')

        now = datetime.now()
        dia = f'{now.day}/{now.month}/{now.year}'
        horario = f'{now.hour}:{now.minute}:{now.second}'

        self.connection = sqlite3.connect(self.database)
        cursor = self.connection.cursor()

        cursor.execute('insert into eventos values (?, ?, ?, ?)', [dia, horario, evento, usuario])

        self.connection.commit()
        self.connection.close()

    def initDB(self):  # cria o database caso ainda nao exista
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
    data = 'usuario;nathalia;amorzin;1'  # (tipo,nome,senha,admin)
    data2 = 'evento;porta2 aberta;nathalia'  # (tipo, evento)

    g = gerenciamento('./database.db')
    g.save_usuario(data)
    g.save_evento(data2)
