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


if __name__ == '__main__':
    from flashcardapp.card import Card

    deck = Deck("Test1")
    
    for front, back in [('a', 'A'), ('and', 'AND'), ('can', 'CAN')]:
        card = Card(front, back)
        deck.add_card(card)
    
    for card in deck.cards:
        print(card)
