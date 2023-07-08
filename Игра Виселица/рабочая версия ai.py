import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QVBoxLayout, QHBoxLayout, QLabel, QPushButton)
from PyQt5.QtGui import QPainter, QFont, QPen, QColor
from PyQt5.QtCore import Qt

class Hangman(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Виселица')
        self.setGeometry(100, 100, 400, 400)

        self.word = 'компьютер'
        self.tries = 0
        self.max_tries = 6
        self.guessed_letters = []

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 380, 30)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 20))

        self.button_layout = QHBoxLayout()
        for letter in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            button = QPushButton(letter, self)
            button.clicked.connect(lambda _, l=letter: self.check_letter(l))
            self.button_layout.addWidget(button)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addLayout(self.button_layout)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.setBrush(Qt.NoBrush)

        if self.tries >= 1:
            painter.drawLine(50, 350, 150, 350)

        if self.tries >= 2:
            painter.drawLine(100, 350, 100, 50)

        if self.tries >= 3:
            painter.drawLine(100, 50, 200, 50)

        if self.tries >= 4:
            painter.drawLine(200, 50, 200, 100)

        if self.tries >= 5:
            painter.drawEllipse(175, 100, 50, 50)

        if self.tries >= 6:
            painter.drawLine(200, 150, 200, 250)
            painter.drawLine(200, 250, 175, 300)
            painter.drawLine(200, 250, 225, 300)

    def check_letter(self, letter):
        if letter in self.guessed_letters:
            return

        self.guessed_letters.append(letter)

        if letter not in self.word:
            self.tries += 1

        self.update_label()

        if self.check_win():
            self.label.setText('Вы выиграли!')
            self.disable_buttons()

        if self.check_lose():
            self.label.setText('Вы проиграли!')
            self.disable_buttons()

        self.update()

    def update_label(self):
        text = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                text += letter
            else:
                text += '_'
        self.label.setText(text)

    def check_win(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def check_lose(self):
        return self.tries >= self.max_tries

    def disable_buttons(self):
        for button in self.button_layout.children():
            button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hangman = Hangman()
    hangman.show()
    sys.exit(app.exec_())