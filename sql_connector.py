import sqlite3


class Connector:
    def try_connection(self): pass

    def prepare(self, query): pass

    def dispose(self): pass


class SqliteConnector(Connector):

    def __init__(self):
        self.__conn = None

    def try_connection(self):
        self.__conn = sqlite3.connect('database.db')
        pass

    def execute(self, query):
        if self.__conn.isClosed():
            self.try_connection()

        cursor = self.__conn.cursor()
        cursor.execute(query)

        return cursor

    def dispose(self):
        self.__conn.close()

    def commit(self):
        self.__conn.commit()
