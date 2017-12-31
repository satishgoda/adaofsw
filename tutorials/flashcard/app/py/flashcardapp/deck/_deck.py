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
