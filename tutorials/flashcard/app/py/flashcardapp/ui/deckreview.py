from PyQt4 import QtGui
from PyQt4 import QtCore


class DeckReviewWidget(QtGui.QWidget):
    def __init__(self, review_model):
        QtGui.QWidget.__init__(self)
        self._review_model = review_model
        
        self._setupUI()
        self._setupSignals()
    
        self._initialize()
    
    @property
    def review_model(self):
        return self._review_model
    
    def _setupUI(self):
        self._mainLayout = QtGui.QVBoxLayout()
        self._mainLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self._mainLayout)
        
        self._cardView = QtGui.QLabel("N/A")
        font = self._cardView.font()
        font.setPointSize(60)
        font.setWeight(72)
        self._cardView.setFont(font)

        self._mainLayout.addWidget(self._cardView)
        
        self._buttonsWidget = QtGui.QWidget()
        self._mainLayout.addWidget(self._buttonsWidget)
        
        self._buttonsLayout = QtGui.QHBoxLayout()
        self._buttonsLayout.setAlignment(QtCore.Qt.AlignCenter)
        self._buttonsWidget.setLayout(self._buttonsLayout)
        
        self._prevButton = QtGui.QPushButton("prev")
        self._nextButton = QtGui.QPushButton("next")
        
        self._buttonsLayout.addWidget(self._prevButton)
        self._buttonsLayout.addWidget(self._nextButton)

    def _setupSignals(self):
        self._prevButton.clicked.connect(self._prev_card)
        self._nextButton.clicked.connect(self._next_card)

    def update_cardView(self, card):
        self._cardView.setText(card.front)

    def _prev_card(self):
        card = self.review_model.previous_card
        self.update_cardView(card)

    def _next_card(self):
        card = self.review_model.next_card
        self.update_cardView(card)

    def _initialize(self):
        card = self.review_model.current_card
        self.update_cardView(card)


if __name__ == '__main__':
    from flashcardapp import Deck, DeckReview, fetch_demo_cards

    deck = Deck("Test1")

    for card in fetch_demo_cards():
        deck.add_card(card)

    review_model = DeckReview(deck)

    drw = DeckReviewWidget(review_model)
    drw.show()
