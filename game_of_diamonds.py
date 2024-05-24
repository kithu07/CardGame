import random

FACE_VALUE = {'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}
diamond_cards = [card for card in FACE_VALUE]
player_cards = [card for card in FACE_VALUE]
computer_cards = [card for card in FACE_VALUE]
score_list = []

def auction(diamond_cards: list[str]) -> tuple[list[str], str]:
    auction_card = random.choice(diamond_cards)
    diamond_cards.remove(auction_card)
    return diamond_cards, auction_card

def computer_bidding(diamond_card:str, computer_cards: list[str]) -> tuple[list[str], str]:
    #computer_bid = random.choice(computer_cards)
    computer_bid = diamond_card
    computer_cards.remove(computer_bid)
    return computer_cards, computer_bid

def player_bidding(diamond_card: str, player_cards: list[str]) -> tuple[list[str], str]:
    print("Choose a card to bid from", player_cards)
    player_bid = input("Enter your bidding card name")
    if player_bid not in player_cards:
        player_bid = input("enter valid choice")
    player_cards.remove(player_bid)
    return player_cards, player_bid

# print(auction(diamond_cards))
# print(computer_bidding('9', computer_cards))
# print(player_bidding('9', player_cards))

def game(diamond_cards: list[str], computer_cards: list[str], player_cards: list[str]):
    while diamond_cards != []:
        diamond_cards, diamond_card = auction(diamond_cards)
        print("Bid for", diamond_card)
        computer_cards, computer_bid = computer_bidding(diamond_card, computer_cards)
        player_cards, player_bid = player_bidding(diamond_card, player_cards)
        print("\nCards bid are:", computer_bid, player_bid)
        round_points = points_calc(computer_bid, player_bid, diamond_card)
        print("Computer scored:", round_points[0], "and Player scored", round_points[1], '\n')
        score_list.append(round_points)
    display_victory(score_list)

def points_calc(computer_bid: str, player_bid: str, diamond_card: str) -> list[int, int]:
    if FACE_VALUE[computer_bid] > FACE_VALUE[player_bid]:
        return [FACE_VALUE[diamond_card], 0]
    elif FACE_VALUE[player_bid] > FACE_VALUE[computer_bid]:
        return [0, FACE_VALUE[diamond_card]]
    else:
        return [FACE_VALUE[diamond_card]/2] * 2
    
# print(points_calc('9', '10', 'Q'))
# print(points_calc('K', '10', 'Q'))
# print(points_calc('10', '10', 'Q'))

def display_victory(score_list: list[list[int, int]]) -> None:
    comp_total, player_total = 0, 0
    for comp_score, player_score in score_list:
        comp_total += comp_score
        player_total += player_score
    print("The total score:\nComputer:", comp_total,"\tPlayer:", player_total)
    if comp_total > player_total:
        print("Computer has won")
    elif player_total > comp_total:
        print("Player has won")
    else: 
        print("Draw match")

#display_victory([[0, 12], [0, 13], [0, 2], [0, 11], [5, 0], [10, 0], [4, 0], [3.0, 3.0], [1, 0], [3, 0], [0, 7], [8, 0], [4.5, 4.5]])
game(diamond_cards, computer_cards, player_cards)