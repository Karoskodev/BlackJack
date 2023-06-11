import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
        2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
        2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
        2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

player = []

dealer = []


def dealing(who):
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

    for _ in range(2):
        dealing(player)
        dealing(dealer)

    game_over = False

    while not game_over:
        player_score = calculate_score(player)
        dealer_score = calculate_score(dealer)

        print(f"\nYour cards:")
        for x in player:
            print(f"{x},", end=" ")
        print(f"\nscore: {player_score}")

        print(f"\nDealer's first card: \n{dealer[0]}\n")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game_over = True
        else:
            try:
                ask = input("Type 'y' to get another card, or 'n' to pass: ")

                if ask.lower() == "y":
                    dealing(player)
                elif ask.lower() == "n":
                    game_over = True
                else:
                    raise ValueError
                    (f"I am sorry but {ask} is not a valid selection")
            except ValueError:
                print("Invalid input. Please enter 'y' or 'n'")

    while dealer_score < 17:
        dealing(dealer)
        dealer_score = calculate_score(dealer)

    print(f"\nYour final hand:")
    for x in player:
        print(f"{x},", end=" ")
    print(f"\nfinal score: {player_score}")

    print(f"\nDealer's final hand:")
    for x in dealer:
        print(f"{x},", end=" ")
    print(f"\nfinal score: {dealer_score}\n")
    print(compare_score(player_score, dealer_score))


print("Welcome to Blackjack!")


while True:
    try:
        question = input("\nDo you want to start a new game ?
                         Type 'y' for yes or 'n' for no: ")
        if question.lower() == 'y':
            if len(deck) < 26:
                deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
                        2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
                        2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
                        2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
            player.clear()
            dealer.clear()
            main()
        elif question.lower() == 'n':
            break
        else:
            raise ValueError
            (f"I am sorry but {question} is not a valid selection")

    except ValueError:
        print("I am sorry that input is invalid. Please enter 'y' or 'n'")
