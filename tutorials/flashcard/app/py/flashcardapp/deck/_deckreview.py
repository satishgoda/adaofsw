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
    def current_card(self):
        return self.deck.cards[self.current_index]

    @property
    def next_card(self):
        return self._card_adjoining(1)
    
    @property
    def previous_card(self):
        return self._card_adjoining(-1)
