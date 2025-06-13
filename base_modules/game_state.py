class GameState:
    def __init__(self):
        self.player_cards = [None, None]
        self.board_cards = [None, None, None, None, None]
        self.n_players = None
        self.pot = None
        self.bet = None

    def __str__(self):
        str_state = "Player cards:" + str(self.player_cards) + '\n'
        str_state = str_state + "Board cards:" + str(self.board_cards) + '\n'
        str_state = str_state + "N players:" + str(self.n_players) + '\n'
        str_state = str_state + "Pot:" + str(self.pot) + '\n'
        str_state = str_state + "Bet:" + str(self.bet)

        return str_state
