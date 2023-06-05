import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
         2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

player = []

dealer = []

def dealing (who):
    """
    Deal a card to the player/dealer and remove that card from deck
    """
    card = random.choice(deck)
    who.append(card)
    deck.remove(card)


def calculate_score(cards):
    """
    Takes a list of cards and returns the score calculated from the cards
    """
    score = 0
    high = ["j", "Q", "K"]
    for card in cards:
        if card in range(1, 11):
            score += card
        elif card in high:
            score += 10
        else:
            if score > 11:
                score += 1
            else:
                score += 11
    return score

