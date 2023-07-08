import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QLineEdit, QMessageBox, QMainWindow
)
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt
import random, sys

class Hangman(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Виселица')

        self.word = random.choice(['кот', 'собака', 'питон', 'программирование', 'компьютер'])
        self.tries = 0
        self.max_tries = 6
        self.guessed_letters = []

        self.word_label = QLabel(self.word, self)
        self.word_label.setGeometry(10, 10, 280, 30)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 50, 280, 200)
        self.image_label.setPixmap(QPixmap('images/hangman0.png'))

        self.letters_layout = QHBoxLayout()
        self.letters = []
        for letter in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            button = QPushButton(letter, self)
            button.clicked.connect(self.letter_clicked)
            self.letters_layout.addWidget(button)
            self.letters.append(button)

        self.input_layout = QVBoxLayout()
        self.input_label = QLabel('Введите букву:', self)
        self.input_layout.addWidget(self.input_label)
        self.input = QLineEdit(self)
        self.input.returnPressed.connect(self.check_letter)
        self.input_layout.addWidget(self.input)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.word_label)
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addLayout(self.letters_layout)
        self.main_layout.addLayout(self.input_layout)

        self.setLayout(self.main_layout)

    def letter_clicked(self):
        sender = self.sender()
        sender.setEnabled(False)
        self.check_letter()

    def check_letter(self):
        letter = self.input.text().lower()
        self.input.clear()

        if letter in self.guessed_letters:
            QMessageBox.warning(self, 'Предупреждение', 'Вы уже вводили эту букву!')
            return

        if letter in self.word:
            self.guessed_letters.append(letter)
            self.update_word_label()
            if self.check_win():
                QMessageBox.information(self, 'Победа!', 'Вы выиграли!')
                self.close()
        else:
            self.tries += 1
            self.update_image_label()
            if self.check_lose():
                QMessageBox.warning(self, 'Поражение', 'Вы проиграли!')
                self.close()

    def update_word_label(self):
        text = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                text += letter
            else:
                text += '_'
        self.word_label.setText(text)

    def update_image_label(self):
        self.image_label.setPixmap(QPixmap(f'images/hangman{self.tries}.png'))

    def check_win(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def check_lose(self):
        return self.tries >= self.max_tries

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hangman = Hangman()
    hangman.show()
    sys.exit(app.exec_())





'''

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QTimer

class StickFigureWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(50)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2))
        painter.drawLine(50, 50, 50, 100)  # draw the body
        painter.drawLine(50, 75, 30, 60)  # draw the left arm
        painter.drawLine(50, 75, 70, 60)  # draw the right arm
        painter.drawLine(50, 100, 30, 120)  # draw the left leg
        painter.drawLine(50, 100, 70, 120)  # draw the right leg
        painter.drawEllipse(30, 10, 40, 40) # draw the head

widget = StickFigureWidget()
widget.show()
window = QMainWindow()
window.show()
window.resize(300, 300)
window.setCentralWidget(widget)'''    

#right_layout.addWidget() добавить виджет
right_layout.addLayout(alphabet_layout)
top_layout.addWidget(stickman)
top_layout.addLayout(right_layout)
#top_layout.addWidget()
main_layout.addLayout(top_layout)
#main_layout.addWidget()
game_window.setLayout(main_layout)

s_letters = []
for i in range(3):
    s_letters.append(QHBoxLayout())
    alphabet_layout.addLayout(s_letters[i])

#создание объектов окна 
x = 0
i = 0
letters = QButtonGroup()
for letter in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
    button = QPushButton(letter)
    s_letters[i].addWidget(button)
    letters.addButton(button)
    x += 1
    if x % 11 == 0:
        i += 1