from base_modules.card import *


class GameState:
    def __init__(self):
        card_generation_mode = "none"
        self.player_cards = [Card(card_generation_mode),
                             Card(card_generation_mode)]
        self.board_cards = [Card(card_generation_mode),
                            Card(card_generation_mode),
                            Card(card_generation_mode),
                            Card(card_generation_mode),
                            Card(card_generation_mode)]
        self.n_players = 0
        self.pot = 0
        self.bet = 0

    def get_state_id(self):
        state_id = self.player_cards[0].code() + '_'
        state_id = state_id + self.player_cards[1].code() + '_'
        state_id = state_id + self.board_cards[0].code() + '_'
        state_id = state_id + self.board_cards[1].code() + '_'
        state_id = state_id + self.board_cards[2].code() + '_'
        state_id = state_id + self.board_cards[3].code() + '_'
        state_id = state_id + self.board_cards[4].code() + '_'
        state_id = state_id + str(self.n_players) + '_'
        state_id = state_id + str(self.pot) + '_'
        state_id = state_id + str(self.bet)

        return state_id

    def __str__(self):
        str_state = "Player cards:" + str(self.player_cards) + '\n'
        str_state = str_state + "Board cards:" + str(self.board_cards) + '\n'
        str_state = str_state + "N players:" + str(self.n_players) + '\n'
        str_state = str_state + "Pot:" + str(self.pot) + '\n'
        str_state = str_state + "Bet:" + str(self.bet)

        return str_state
