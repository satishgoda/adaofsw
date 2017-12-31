from _deck import Deck
from _deckreview import DeckReview


if __name__ == '__main__':
    from flashcardapp import fetch_demo_cards

    deck = Deck("Test1")
    
    for card in fetch_demo_cards():
        deck.add_card(card)
    
    for card in deck.cards:
        print(card)
    
    print("\n\nLet us now review a deck of cards\n\n")
    
    review = DeckReview(deck)

    print(review.current_card)
    for index in range(10):
        print(review.next_card)
        
    
    print("\n\nLet us now review a deck of cards (in reverse)\n\n")
    
    review = DeckReview(deck)

    print(review.current_card)
    for index in range(10):
        print(review.previous_card)
