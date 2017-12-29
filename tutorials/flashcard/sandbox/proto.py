deck = "a and can down".split(" ")

from PyQt4 import QtGui
from PyQt4 import QtCore

prevb = QtGui.QPushButton("prev")
nextb = QtGui.QPushButton("next")

prevb.show()
nextb.show()

card = QtGui.QWidget()
card.show()

cardLay = QtGui.QVBoxLayout()
card.setLayout(cardLay)

cardDisplay = QtGui.QLabel(deck[0])

cardLay.addWidget(cardDisplay)

font = cardDisplay.font()
font.pointSize()
font.setPointSize(60)
cardDisplay.setFont(font)
font.setWeight(72)
cardDisplay.setFont(font)

cardLay.alignment()
cardLay.setAlignment(QtCore.Qt.AlignJustify)

##

# card.deleteLater()
# cardDisplay = QtGui.QLabel("<h1>{0}</h1>".format(deck[0]))

# cardDisplay.text()
# cardDisplay.setText('a')
# 
# font = cardDisplay.font()
# font.weight()
# font.setWeight(72)
# cardDisplay.setFont(font)
# 
# font.pointSize()
# font.setPointSize(30)
# 
# cardDisplay.setFont(font)

# def nextCard():
#     card_cur = cardDisplay.text()
#     card_index = (deck.index(card_cur)+1)%len(deck)
#     cardDisplay.setText(deck[card_index])
#     
# nextb.clicked.connect(nextCard)
# 
# def prevCard():
#     card_cur = cardDisplay.text()
#     card_index = (deck.index(card_cur)-1)%len(deck)
#     cardDisplay.setText(deck[card_index])
#     
# prevb.clicked.connect(prevCard)

prevb.clicked.disconnect(prevCard)
nextb.clicked.disconnect(nextCard)

def deck_card_adjoining(current, direction):
    card_index = (deck.index(current)+direction)%len(deck)
    return deck[card_index]

def nextCard():
    card_cur = cardDisplay.text()
    card_next = deck_card_adjoining(card_cur, 1)
    cardDisplay.setText(card_next)
    
nextb.clicked.connect(nextCard)

def prevCard():
    card_cur = cardDisplay.text()
    card_prev = deck_card_adjoining(card_cur, -1)
    cardDisplay.setText(card_prev)
    
prevb.clicked.connect(prevCard)
