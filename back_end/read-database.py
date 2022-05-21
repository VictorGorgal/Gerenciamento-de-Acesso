import sqlite3


def main(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    print('Usuarios:')
    for row in cursor.execute('select rowid, * from usuarios'):
        # print(row)
        print(f'ID: {row[0]}, Nome: "{row[1]}", Senha: "{row[2]}", Admin: {row[3]}')
    print('-' * 50)
    print('Eventos:')
    for row in cursor.execute('select rowid, * from eventos'):
        print(row)


if __name__ == '__main__':
    main('./database.db')
