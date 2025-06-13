import itertools
import copy
from db_generator.db_connector import *
from base_modules.game_state import *


db_connector = DBConnector()


def get_card_deck():
    deck = set()
    for suit, value in itertools.product(set(Suit), set(Value)):
        deck.add(Card(suit.value * value.value))

    return deck


def generate_all_situations():

    # базовая колода для ситуации
    base_deck = get_card_deck()

    # базовая ситуация
    base_situation = GameState()

    # перебор всех возможных ситуаций (8*52*51/(2*1)*50*49*48/(3*2*1)*47*46 = 449.516.121.600) штук
    counter = 0
    for n_players in range(2, 10):

        # создаём копию базовых колоды
        deck = copy.deepcopy(base_deck)

        for p1, p2 in itertools.combinations(base_deck, 2):
            # удаляем из копии колоды использованные карты
            deck = deck.difference({p1, p2})

            for b1, b2, b3 in itertools.combinations(base_deck, 3):
                # удаляем из копии колоды использованные карты
                deck = deck.difference({b1, b2, b3})

                for b4 in itertools.combinations(base_deck, 1):

                    # удаляем из копии колоды использованные карты
                    deck = deck.difference({b4})

                    for b5 in itertools.combinations(base_deck, 1):

                        # удаляем из копии колоды использованные карты
                        deck = deck.difference({b5})

                        # создаём копии базовых колоды и ситуации
                        situation = copy.deepcopy(base_situation)

                        # дополняем ситуацию картами и количеством игроков из текущей итерации
                        situation.add_player_card(p1)
                        situation.add_player_card(p2)
                        situation.add_flop_board_cards(b1)
                        situation.add_flop_board_cards(b2)
                        situation.add_flop_board_cards(b3)
                        situation.add_tern_board_card(b4)
                        situation.add_river_board_card(b5)
                        situation.set_n_players(n_players)

                        # отображаем прогресс в %
                        counter += 1
                        if counter % 10000000 == 0:
                            print(float(int(counter*1000/4495161216)/1000), '%')
