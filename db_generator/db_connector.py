import sqlite3


class DBConnector:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()
