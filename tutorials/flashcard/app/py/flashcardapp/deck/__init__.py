class Deck(object):
    def __init__(self, name):
        self._name = name
        self._cards = []
    
    @property
    def name(self):
        return self._name
        
    @property
    def cards(self):
        return self._cards
    
    def add_card(self, card):
        self.cards.append(card)


class DeckReview(object):
    """
    Encapsulate a session where a Deck of cards is being reviewed.
    
    The state consists of the current card being displayed
    
    Clients can request for the next and previous card in the deck
    """
    
    def __init__(self, deck):
        self._deck = deck
        self._current_index = 0
    
    @property
    def deck(self):
        return self._deck
    
    @property
    def current_index(self):
        return self._current_index
    
    @property
    def number_of_cards(self):
        return len(self.deck.cards)
    
    def _card_adjoining(self, direction):
        self._current_index += direction        
        next_index = self.current_index%self.number_of_cards
        return self.deck.cards[next_index]

    
    @property
    def next_card(self):
        return self._card_adjoining(1)
    
    @property
    def previous_card(self):
        return self._card_adjoining(-1)


if __name__ == '__main__':
    from flashcardapp.card import Card

    deck = Deck("Test1")
    
    for front, back in [('a', 'A'), ('and', 'AND'), ('can', 'CAN')]:
        card = Card(front, back)
        deck.add_card(card)
    
    for card in deck.cards:
        print(card)
    
    print("\n\nLet us now review a deck of cards\n\n")
    
    review = DeckReview(deck)

    print(review.deck.cards[review.current_index])
    for index in range(10):
        print(review.next_card)
