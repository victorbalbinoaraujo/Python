def value_of_card(card):
    if card in ['J', 'Q', 'K']: return 10
    if card == 'A': return 1
    return int(card)

def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two): return card_one
    if value_of_card(card_two) > value_of_card(card_one): return card_two
    return card_one, card_two

def value_of_ace(card_one, card_two):
    return 1 if value_of_card(card_one) + value_of_card(card_two) >= 11 else 11

def is_blackjack(card_one, card_two):
    return ((value_of_card(card_one) == 1 and value_of_card(card_two) == 10) or (value_of_card(card_one) == 10 and value_of_card(card_two) == 1))
    
def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    return value_of_card(card_one) + value_of_card(card_two) in [9, 10, 11]
