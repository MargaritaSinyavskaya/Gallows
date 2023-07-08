import sys, random
import typing
from PyQt5 import QtCore

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton
)
from PyQt5.QtGui import QPainter, QFont, QPen
from PyQt5.QtCore import Qt

class Main_win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):    
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.show()
        self.setWindowTitle('Виселица')
        self.resize(400, 400)


        self.start_game = QPushButton('Начать игру')
        self.exit = QPushButton('Выход')

        self.Vline = QVBoxLayout()
        self.Vline.addWidget(self.start_game)
        self.Vline.addWidget(self.exit)        
        self.widget.setLayout(self.Vline)


class Hangman(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Виселица')
        self.setGeometry(100, 100, 500, 500)

        self.word = random.choice(['КОТ', 'СОБАКА', 'ПИТОН', 'ПРОГРАММИРОВАНИЕ', 'КОМПЬЮТЕР'])
        self.tries = 0
        self.max_tries = 8
        self.guessed_letters = []

        self.pause_button = QPushButton('Пауза')


        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 380, 30)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 20))

        self.button_layout = QVBoxLayout()

        s_letters = []
        for i in range(3):
            s_letters.append(QHBoxLayout())
            self.button_layout.addLayout(s_letters[i])

        x = 0
        i = 0
        for letter in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            button = QPushButton(letter, self)
            button.clicked.connect(lambda _, l=letter: self.check_letter(l))
            s_letters[i].addWidget(button)
            x += 1
            if x % 11 == 0:
                i += 1

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pause_button, Qt.AlignRight)
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
            painter.drawLine(250, 320, 10, 320) # draw the floor

        if self.tries >= 2:
            painter.drawLine(70, 320, 70, 40) # draw the main_line

        if self.tries >= 3:
            painter.drawLine(175, 40, 70, 40) # draw the hline

        if self.tries >= 4:
            painter.drawLine(175, 40, 175, 100) # draw the vline

        if self.tries >= 5:
            painter.drawEllipse(150, 100, 50, 50) # draw the head

        if self.tries >= 6:
            painter.drawLine(175, 150, 175, 250)  # draw the body

        if self.tries >= 7:
            painter.drawLine(175, 175, 150, 200)  # draw the left arm
            painter.drawLine(175, 175, 200, 200)  # draw the right arm

        if self.tries >= 8:
            painter.drawLine(175, 250, 150, 275)  # draw the left leg
            painter.drawLine(175, 250, 200, 275)  # draw the right leg

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
        print(text)
        print(self.word)
        print(self.guessed_letters)

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

class pause_win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pause_win = QWidget()
        self.setCentralWidget(self.pause_win)
        self.setWindowTitle('Пауза')
        self.resize(300, 300)
        self.menu_button = QPushButton('Главное меню')
        self.continue_button = QPushButton('Продолжить')
        self.surrender_button = QPushButton('Сдаться')
        self.main_pause = QVBoxLayout()
        self.main_pause_hlay = QHBoxLayout()
        self.main_pause.addWidget(self.menu_button, alignment = Qt.AlignCenter)
        self.main_pause.addWidget(self.continue_button, alignment = Qt.AlignCenter)
        self.main_pause.addWidget(self.surrender_button, alignment = Qt.AlignCenter)
        self.main_pause_hlay.addLayout(self.main_pause)
        self.pause_win.setLayout(self.main_pause_hlay)

        self.menu_button.clicked.connect(self.exit_in_lobby)
        self.continue_button.clicked.connect(self.continue_game_before_pause)
        self.surrender_button.clicked.connect(self.surrender)


    def exit_in_lobby(self):
        self.close()
        hangman.close()
        main.show()

    def continue_game_before_pause(self):
        self.close()

    def surrender(self):
        self.close()
        hangman.label.setText(hangman.word)

            
def open_game():
    hangman.show()
    hangman.tries = 0
    hangman.word = random.choice(['КОТ', 'СОБАКА', 'ПИТОН', 'ПРОГРАММИРОВАНИЕ', 'КОМПЬЮТЕР'])   
    hangman.guessed_letters = []
    hangman.update_label()
    main.close()
    

def pause():
    pause_window.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main_win()
    hangman = Hangman()
    pause_window = pause_win()

    hangman.pause_button.clicked.connect(pause)
    main.start_game.clicked.connect(open_game)
    
    sys.exit(app.exec_())