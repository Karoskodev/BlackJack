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
    high = ["J", "Q", "K"]
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

def main():
    """
    Function to run the game. 
    """

    print("Welcome to Blackjack!\n")

    for _ in range(2):
        dealing(player)
        dealing(dealer)

    game_over = False

    while not game_over:
        player_score = calculate_score(player)
        dealer_score = calculate_score(dealer)

        print(f"Your cards: {player}, score: {player_score}")
        print(f"Dealer's first card: {dealer[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game_over = True
        else:
            ask = input("Type 'y' to get another card, or 'n' to pass: ")

            if ask.lower() == "y":
                dealing(player)
            else:
                game_over = True
    
    while dealer_score < 17:
        dealing(dealer)
        dealer_score = calculate_score(dealer)


    print(f"Your final hand: {player}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")
    print(compare_score(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    player.clear()
    dealer.clear()
    main()
