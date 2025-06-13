from base_modules.card import *


class GameState:
    def __init__(self):
        self.player_cards = set()
        self.flop_board_cards = set()
        self.tern_board_card = set()
        self.river_board_card = set()
        self.n_players = 0
        self.pot = 0
        self.bet = 0

    def set_n_players(self, n_players):
        if type(n_players) == int and n_players >= 2:
            self.n_players = n_players

    def add_player_card(self, player_card):
        if type(player_card) == Card and len(self.player_cards)<2:
            self.player_cards.add(player_card)

    def add_flop_board_cards(self, flop_board_cards):
        if type(flop_board_cards) == Card and len(self.flop_board_cards)<3:
            self.flop_board_cards.add(flop_board_cards)

    def add_tern_board_card(self, tern_board_card):
        if type(tern_board_card) == Card and len(self.tern_board_card)<1:
            self.tern_board_card.add(tern_board_card)

    def add_river_board_card(self, river_board_card):
        if type(river_board_card) == Card and len(self.river_board_card)<1:
            self.river_board_card.add(river_board_card)

    def __str__(self):
        str_state = "Player cards:" + str(self.player_cards) + '\n'
        str_state = str_state + "Board cards:" + str(self.flop_board_cards) + '\n'
        str_state = str_state + str(self.tern_board_card) + '\n'
        str_state = str_state + str(self.river_board_card) + '\n'
        str_state = str_state + "N players:" + str(self.n_players) + '\n'
        str_state = str_state + "Pot:" + str(self.pot) + '\n'
        str_state = str_state + "Bet:" + str(self.bet)

        return str_state
