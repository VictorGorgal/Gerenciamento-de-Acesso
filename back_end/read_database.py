import sqlite3


class readDB:
    def __init__(self, file):
        self.file = file

    def get_usuarios(self):
        connection = sqlite3.connect(self.file)
        cursor = connection.cursor()

        rows = cursor.execute('select * from usuarios').fetchall()

        connection.close()

        return rows

    def get_eventos(self):
        connection = sqlite3.connect(self.file)
        cursor = connection.cursor()

        rows = cursor.execute('select * from eventos').fetchall()

        connection.close()

        return rows


if __name__ == '__main__':
    read = readDB('./database.db')

    print('Users:')
    for i, user in enumerate(read.get_usuarios()):
        print(i, user)

    print('Eventos')
    for event in read.get_eventos():
        print(event)

    print(read.get_usuarios())
