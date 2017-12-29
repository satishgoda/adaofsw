class Card(object):
    def __init__(self, front, back):
        self._front = front
        self._back = back
    
    def __repr__(self):
        return str(self.__class__) + "[{0} - {1}]".format(self.front, self.back)
    
    @property
    def front(self):
        return self._front
        
    @property
    def back(self):
        return self._back

        
if __name__ == '__main__':
    card = Card('front', 'back')
    print(card)
    
    for front, back in [('a', 'A'), ('and', 'AND'), ('can', 'CAN')]:
        card = Card(front, back)
        print(card)
