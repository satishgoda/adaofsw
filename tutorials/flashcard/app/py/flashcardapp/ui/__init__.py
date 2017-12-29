from PyQt4 import QtGui
from PyQt4 import QtCore

from flashcardapp.deck import Deck, DeckReview
from flashcardapp.card import Card

deck_review_widget = QtGui.QWidget()

deck_review_widget.show()

mainLayout = QtGui.QVBoxLayout()
mainLayout.setAlignment(QtCore.Qt.AlignJustify)
deck_review_widget.setLayout(mainLayout)

deck = Deck("Test1")

for front, back in [('a', 'A'), ('and', 'AND'), ('can', 'CAN')]:
    card = Card(front, back)
    deck.add_card(card)

review = DeckReview(deck)

card_view = QtGui.QLabel(review.current_card.front)

font = card_view.font()
font.setPointSize(60)
font.setWeight(72)
card_view.setFont(font)

mainLayout.addWidget(card_view)

buttons_widget = QtGui.QWidget()
mainLayout.addWidget(buttons_widget)

buttonsLayout = QtGui.QHBoxLayout()
buttons_widget.setLayout(buttonsLayout)

prev_button = QtGui.QPushButton("prev")
next_button = QtGui.QPushButton("next")

buttonsLayout.addWidget(prev_button)
buttonsLayout.addWidget(next_button)

def next_card():
    card = review.next_card
    card_view.setText(card.front)

def prev_card():
    card = review.previous_card
    card_view.setText(card.front)

prev_button.clicked.connect(prev_card)
next_button.clicked.connect(next_card)

deck_review_widget.adjustSize()
