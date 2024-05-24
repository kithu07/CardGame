import random
FACE_VALUE = {'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2':2, 'A': 1}
auction_cards = [card for card in FACE_VALUE]
player_cards = [card for card in FACE_VALUE]
computer_cards = [card for card in FACE_VALUE]


def auction(auction_cards: list[str]) -> tuple[list[str], str]:
    auctioned_card = random.choice(auction_cards)
    # print(f"auctioned card: {auctioned_card}")
    auction_cards.remove(auctioned_card)
    return auction_cards, auctioned_card

# print(auction(auction_cards))

def player_bidding(player_cards: list[str], diamond_card: str) -> tuple[list[str], str]:
    print("Your cards are:", player_cards)
    player_bid = input("Enter your bid from above card list")
    if player_bid not in player_cards:
        return player_cards, input("Enter your bid again from remaining cards")
    player_cards.remove(player_bid)
    return player_cards, player_bid

# print(player_bidding(player_cards,'9'))

def computer_bidding(computer_cards: list[str], diamond_card: str) -> tuple[list[str], str]:
    #computer_bid = random.choice(computer_cards)
    computer_bid = diamond_card
    print(f"Computer bids: {computer_bid}")
    computer_cards.remove(computer_bid)
    return computer_cards, computer_bid

# print(computer_bidding(computer_cards, '9'))
# arguments of game() -> player_bid: str, computer_bid: str, auctioned_card: str
def game( player_cards, computer_cards):
    game_over = False
    computer_score, player_score = 0, 0
    while not(game_over):
        auctioned_card = auction(auction_cards)[1]
        print(f"auctioned card: {auctioned_card}")
        player_cards, player_bid = player_bidding(player_cards, auctioned_card)
        computer_cards, computer_bid = computer_bidding(computer_cards, auctioned_card)
        print("-----------------------------------------------------")

        if FACE_VALUE[computer_bid] > FACE_VALUE[player_bid]:
            computer_score += FACE_VALUE[auctioned_card]

        elif FACE_VALUE[player_bid] == FACE_VALUE[computer_bid]:
            computer_score += FACE_VALUE[auctioned_card]/2 
            player_score += FACE_VALUE[auctioned_card]/2
        
        else:
            player_score += FACE_VALUE[auctioned_card]

        if len(computer_cards) == 0 and len(player_cards) == 0:
            game_over = True
    
    return (f"computer score: {computer_score}, player score: {player_score}")


print(game(player_cards, computer_cards))

        






