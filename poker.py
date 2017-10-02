#this is some of the work that I have done in python
def makedeck():
    lst = []
    suits = ['Spade','Clover','Diamond','Heart']
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    for suit in suits:
        for rank in ranks:
            tup = (suit,rank);
            lst.append(tup)
    return lst

import random        
def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

maker = makedeck()
print(shuffleDeck(maker))
    
def deal(numofHands,maxCards,deck,hands):
    hands = []
    deck = shuffleDeck(makedeck())
    decklen = len(deck)
    for han in range(numofHands):
        numofCards = 0
        hand = []
        while(numofCards != maxCards):
            numofCards = numofCards + 1
            hand.append(deck[decklen - 1])
            decklen = decklen - 1
        hands.append(hand)
    return hands           
print("\n")
print("\n")
print("\n")
decka = shuffleDeck(makedeck())
hand = []
dealer = deal(4,5,decka,hand)
print(dealer)

#discard a card from a hand
import random
def Discard(numofCards, pile):
    hand = []
    pile = []
    deck = shuffleDeck(makedeck())
    for card in deck:
        hand.append(card)
    numtoDiscard = random.randint(0,numofCards)
    for discard in len(numtoDiscard):
        pile.append(hand[discard])
        hand.pop()
    return pile

cool = []
print(Discard(6,cool))
        
    
    
    


