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

def compare_score(player_score, dealer_score):
    """
    Compare scores of the player and dealer and return result
    """

    if player_score == dealer_score:
        return "It's a draw!"
    elif player_score == 21:
        return "You win with a Blackjack!"
    elif dealer_score == 21:
        return "Dealer wins with a Blackjack!"
    elif player_score > 21:
        return "You went over 21. You lose!"
    elif dealer_score > 21:
        return "Dealer went over 21. You win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "Dealer wins!"
