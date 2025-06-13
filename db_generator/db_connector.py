import sqlite3


class DBConnector:

    def __init__(self):
        # установка соединения с базой
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        print('DBConnector: Connection with DB opened.')
        self.drop_table_card_states()

        # создание таблицы с комбинациями, если её нет в базе
        """
        all_tables = self.get_all_tables()
        all_tables_names = list()
        for table in all_tables:
            all_tables_names.append(table[1])
        if 'card_states' not in all_tables_names:
            self.create_table_card_states()
            print('DBConnector: card_states table created.')
        else:
            print('DBConnector: card_states table already exists.')
        """

    def create_table_card_states(self):
        self.cursor.execute(
            '''CREATE TABLE card_states
            (
                id TEXT PRIMARY KEY,
                player_card_0 INTEGER,
                player_card_1 INTEGER,
                board_card_0 INTEGER,
                board_card_1 INTEGER,
                board_card_2 INTEGER,
                board_card_3 INTEGER,
                board_card_4 INTEGER,
                n_players INTEGER,
                pot REAL,
                bet REAL,
                app REAL
            )'''
            )

    def insert_state_and_app_to_card_states(self, game_state, app):

        self.cursor.execute('INSERT INTO card_states (id,'
                            'player_card_0, player_card_1,'
                            'board_card_0, board_card_1, board_card_2,'
                            'board_card_3, board_card_4, n_players,'
                            'pot, bet, app) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                            (game_state.get_state_id(),
                             game_state.player_cards[0].code(),
                             game_state.player_cards[1].code(),
                             game_state.board_cards[0].code(),
                             game_state.board_cards[1].code(),
                             game_state.board_cards[2].code(),
                             game_state.board_cards[3].code(),
                             game_state.board_cards[4].code(),
                             game_state.n_players,
                             game_state.pot,
                             game_state.bet,
                             app))

    def drop_table_card_states(self):
        self.cursor.execute("DROP TABLE IF EXISTS card_states")
        print('DBConnector: card_states table dropped.')

    def get_all_tables(self):
        self.cursor.execute("""select * from sqlite_master
                                where type = 'table'""")
        tables = self.cursor.fetchall()
        return tables

    def __del__(self):
        self.connection.close()
