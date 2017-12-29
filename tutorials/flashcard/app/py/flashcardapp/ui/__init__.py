from PyQt4 import QtGui
from PyQt4 import QtCore

from flashcardapp.deck import Deck
from flashcardapp.card import Card

deck_review_widget = QtGui.QWidget()

deck_review_widget.show()

mainLayout = QtGui.QVBoxLayout()
mainLayout.setAlignment(QtCore.Qt.AlignJustify)
deck_review_widget.setLayout(mainLayout)

card_view = QtGui.QLabel("Undefined deck")

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
