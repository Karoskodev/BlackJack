import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
         2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

player = []

dealer = []

def dealing (who):
    """
    Deal a card to the player/dealer and remove that card from cards
    """
    card = random.choice(cards)
    who.append(card)
    cards.remove(card)