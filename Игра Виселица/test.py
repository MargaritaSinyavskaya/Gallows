from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap
import random 
import sys

app = QApplication([])
window = QWidget()
window.show()
window.setWindowTitle('Виселица')
window.resize(900, 600)

start_button = QPushButton('Новая игра')
start_button.setFixedSize(200, 50)
exit_button = QPushButton('Выход')
exit_button.setFixedSize(200, 50)
continue_button = QPushButton('Продолжить')
continue_button.setFixedSize(200, 50)
highscore_button = QPushButton('Рекорды')
highscore_button.setFixedSize(200, 50)
achievement_button = QPushButton('Достижения')
achievement_button.setFixedSize(200, 50)

h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
h_line4 = QHBoxLayout()
h_line5 = QHBoxLayout()
v_line1 = QVBoxLayout()
h_line1.addWidget(start_button, alignment = Qt.AlignRight)
h_line2.addWidget(continue_button, alignment = Qt.AlignRight)
h_line3.addWidget(highscore_button, alignment = Qt.AlignRight)
h_line4.addWidget(achievement_button, alignment = Qt.AlignRight)
h_line5.addWidget(exit_button, alignment = Qt.AlignRight)
v_line1.addLayout(h_line1)
v_line1.addLayout(h_line2)
v_line1.addLayout(h_line3)
v_line1.addLayout(h_line4)
v_line1.addLayout(h_line5)
window.setLayout(v_line1)

window2 = QWidget()
window2.setWindowTitle('Виселица')
window2.resize(900, 600)

main_layout = QVBoxLayout()
right_layout = QVBoxLayout()
top_layout = QHBoxLayout()
alphabet_layout = QVBoxLayout()
words_layout = QVBoxLayout()
input_layout = QVBoxLayout()
pause_layout = QVBoxLayout()

right_layout.addLayout(pause_layout)
right_layout.addLayout(words_layout)
right_layout.addLayout(alphabet_layout)
right_layout.addLayout(input_layout)
top_layout.addLayout(right_layout)
main_layout.addLayout(top_layout)
window2.setLayout(main_layout)

word = random.choice(['кот', 'собака', 'ноутбук', 'телефон', 'игра', 'еда'])
tries = 0
max_tries = 6
guessed_letters = []

word_label = QLabel(word)
words_layout.addWidget(word_label, alignment = Qt.AlignRight)
font = word_label.font()
font.setPointSize(20)
word_label.setFont(font)

def check_win(self):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def check_lose(self):
    return tries >= max_tries

def update_word_label(self):
    text = ''
    for letter in word:
        if letter in guessed_letters:
            text += letter
        else:
            text += ' __ '
    word_label.setText(text)

def check_letter(self):
        if letter in guessed_letters:
            QMessageBox.warning('Предупреждение', 'Вы уже вводили эту букву!')
            return

        if letter in word:
            guessed_letters.append(letter)
            update_word_label()
            if check_win():
                QMessageBox.information('Победа!', 'Вы выиграли!')
                close()
        else:
            tries += 1
            if check_lose():
                QMessageBox.warning('Поражение', 'Вы проиграли!')
                close()

def letter_clicked(self):
    sender = self.sender()
    sender.setEnabled(False)
    check_letter(window2)

s_letters = []
for i in range(3):
    s_letters.append(QHBoxLayout())
    alphabet_layout.addLayout(s_letters[i])

x = 0
i = 0
for letter in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
    button = QPushButton(letter)
    s_letters[i].addWidget(button)
    x += 1
    if x % 11 == 0:
        i += 1
    button.setFixedSize(70, 70)
    button.clicked.connect(letter_clicked)

input_label = QLabel('Введите букву:')
input_layout.addWidget(input_label)
inputt = QLineEdit()
inputt.returnPressed.connect(check_letter)
input_layout.addWidget(inputt)

pause_button = QPushButton('▐▐')
pause_button.setFixedSize(40, 40)
pause_layout.addWidget(pause_button, alignment = Qt.AlignRight)

pause_win = QWidget()
pause_win.setWindowTitle('Пауза')
pause_win.resize(300, 300)
pause_win.hide()

menu_button = QPushButton('Главное меню')
continue_button2 = QPushButton('Продолжить')
surrender_button = QPushButton('Сдаться')

mein_pause_vlayout = QVBoxLayout()
mein_pause_hlayout = QHBoxLayout()
mein_pause_vlayout.addWidget(menu_button, alignment = Qt.AlignCenter)
mein_pause_vlayout.addWidget(continue_button2, alignment = Qt.AlignCenter)
mein_pause_vlayout.addWidget(surrender_button, alignment = Qt.AlignCenter)
mein_pause_hlayout.addLayout(mein_pause_vlayout)
pause_win.setLayout(mein_pause_hlayout)

def new_game():
    update_word_label(window2)
    window.hide()
    window2.show()

def pause_game():
    pause_win.show()

def exit_in_lobby():
    pause_win.hide()
    window2.hide()
    window.show()

def continue_game_before_pause():
    pause_win.hide()

def surrender():
    pause_win.hide()
    word_label.setText(word)

start_button.clicked.connect(new_game)
exit_button.clicked.connect(window.close)
pause_button.clicked.connect(pause_game)
menu_button.clicked.connect(exit_in_lobby)
continue_button2.clicked.connect(continue_game_before_pause)
surrender_button.clicked.connect(surrender)

app.exec_()