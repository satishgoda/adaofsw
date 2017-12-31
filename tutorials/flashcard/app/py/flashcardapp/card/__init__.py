from _card import Card


def fetch_demo_cards():
    card_items = [('a', 'A'), ('and', 'AND'), ('can', 'CAN'), 
                  ('down','DOWN'), ('egg','EGG'), ('up','UP'), 
                  ('here','HERE'),
                  ]

    for front, back in card_items:
        card = Card(front, back)
        yield card


def test():
    from flashcardapp import Card
    
    card = Card('front', 'back')
    print(card)
    
    for card in fetch_demo_cards():
        print(card)


if __name__ == '__main__':
    test()
    