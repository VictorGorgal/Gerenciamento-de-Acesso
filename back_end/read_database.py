import sqlite3


class readDB:
    def __init__(self, file):
        self.file = file

    def get_usuarios(self):
        """
        :return: list[tuple]: lista contendo todos os usuários cadastrados no banco de dados
        """
        connection = sqlite3.connect(self.file)
        cursor = connection.cursor()

        rows = cursor.execute('select * from usuarios').fetchall()

        connection.close()

        return rows

    def get_eventos(self):
        """
        :return: list[tuple]: lista contendo todos os eventos salvos no banco de dados
        """
        connection = sqlite3.connect(self.file)
        cursor = connection.cursor()

        rows = cursor.execute('select * from eventos').fetchall()

        connection.close()

        return rows


# Mostrar os conteúdos do banco de dados no terminal:
if __name__ == '__main__':
    read = readDB('./database.db')

    print('Users:')
    for i, user in enumerate(read.get_usuarios()):
        print(i, user)

    print('Eventos')
    for event in read.get_eventos():
        print(event)

    print(read.get_usuarios())
