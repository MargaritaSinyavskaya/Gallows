#импорт нужных библиотек и модулей
import sys, random
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton
)
from PyQt5.QtGui import QPainter, QFont, QPen
from PyQt5.QtCore import Qt
#создание главного меню
class Main_win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    #создание UI - интерфейса пользователя
    def initUI(self):    
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.show()
        self.setWindowTitle('Виселица')
        self.resize(400, 400)

        self.start_label = QLabel()
        self.start_label.setText('Добро пожаловать в игру!')
        self.start_label.setFont(QFont('Arial', 20))

        self.start_game = QPushButton('Начать игру')
        self.start_game.setFixedSize(200, 50)
        self.exit = QPushButton('Выход')
        self.exit.setFixedSize(200, 50)

        self.Vline = QVBoxLayout()
        self.Vline.addWidget(self.start_label, alignment = Qt.AlignCenter)
        self.Vline.addWidget(self.start_game, alignment = Qt.AlignCenter)
        self.Vline.addWidget(self.exit, alignment = Qt.AlignCenter)        
        self.widget.setLayout(self.Vline)
#создаем окно игры
class Hangman(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Виселица')
        self.setGeometry(300, 250, 500, 500)
        #выбираем главное слово и задаем параметры
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
        self.btn_list = list()

        s_letters = []
        for i in range(3):
            s_letters.append(QHBoxLayout())
            self.button_layout.addLayout(s_letters[i])
        #заполнение списков буквами в три ряда
        x = 0
        i = 0
        for letter in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            self.button = QPushButton(letter, self)
            self.button.clicked.connect(lambda _, l=letter: self.check_letter(l))
            s_letters[i].addWidget(self.button)
            self.btn_list.append(self.button)
            x += 1
            if x % 11 == 0:
                i += 1
            self.button.setFixedSize(100, 50)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pause_button, Qt.AlignRight)
        self.layout.addWidget(self.label)
        self.layout.addLayout(self.button_layout)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
    #ирсование человека
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.setBrush(Qt.NoBrush)

        if self.tries >= 1:
            painter.drawLine(250, 320, 10, 320) # рисуем основание

        if self.tries >= 2:
            painter.drawLine(70, 320, 70, 40) # рисуем колонну

        if self.tries >= 3:
            painter.drawLine(175, 40, 70, 40) # рисуем балку

        if self.tries >= 4:
            painter.drawLine(175, 40, 175, 100) # рисуем веревку

        if self.tries >= 5:
            painter.drawEllipse(150, 100, 50, 50) # рисуем голову

        if self.tries >= 6:
            painter.drawLine(175, 150, 175, 250)  # рисуем тело

        if self.tries >= 7:
            painter.drawLine(175, 175, 150, 200)  # рисуем левую руку
            painter.drawLine(175, 175, 200, 200)  # рисуем правую руку

        if self.tries >= 8:
            painter.drawLine(175, 250, 150, 275)  # рисуем левую ногу
            painter.drawLine(175, 250, 200, 275)  # рисуем правую ногу
    #проверяем буквы в слове
    def check_letter(self, letter):
        sender_button = app.sender()
        sender_button.setEnabled(False)
        if letter in self.guessed_letters:
            return

        self.guessed_letters.append(letter)

        if letter not in self.word:
            self.tries += 1

        self.update_label()

        if self.check_win():
            game.stop_game()
            print('Конец игры.')
            print('Вы выиграли!')
            endwin.text_label.setText('Вы выиграли!')
            endwin.end_win.show()

        if self.check_lose():
            game.stop_game()
            print('Конец игры.')
            print('Вы проиграли!')
            endwin.text_label.setText('Вы проиграли!')
            endwin.end_win.show()

        self.update()

    def update_label(self):
        text = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                text += letter
            else:
                text += ' _ '
        self.label.setText(text)

    def check_win(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def check_lose(self):
        return self.tries >= self.max_tries

    def disable_buttons(self):
        for self.button in self.button_layout.children():
            self.button.setEnabled(False)
#окно паузы
class pause_win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pause_win = QWidget()
        self.setCentralWidget(self.pause_win)
        self.setWindowTitle('Пауза')
        self.resize(300, 300)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
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
        game.stop_game()
        print('Конец игры.')
        print('Слово: ' + hangman.word)
        endwin.text_label.setText('Слово: ' + hangman.word)
        endwin.end_win.show()

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(16)  # Обновлять экран каждые 16 миллисекунд

    def update_game(self):
        # Обновление игрового экрана
        pass

    def stop_game(self):
        self.timer.stop()
#конечное меню
class EndGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.end_win = QWidget()
        self.end_win.resize(300, 300)
        self.end_win.setWindowTitle('Конец игры')
        self.text_label = QLabel()
        self.text_label.setFont(QFont('Arial', 15))

        self.end_button = QPushButton('Главное меню')
        self.end_button.setFixedSize(200, 50)

        self.main_layout = QVBoxLayout()
        self.text_layout = QVBoxLayout()
        self.text_layout.addWidget(self.text_label, alignment=Qt.AlignCenter)
        self.text_layout.addWidget(self.end_button, alignment=Qt.AlignCenter)
        self.main_layout.addLayout(self.text_layout)
        self.end_win.setLayout(self.main_layout)
        self.end_win.setWindowModality(QtCore.Qt.ApplicationModal)

def open_game():
    hangman.show()
    hangman.tries = 0
    hangman.word = random.choice(['КОТ', 'СОБАКА', 'ПИТОН', 'ПРОГРАММИРОВАНИЕ', 'КОМПЬЮТЕР'])   
    hangman.guessed_letters = []

    for btn in hangman.btn_list:
        btn.setEnabled(True)

    hangman.update_label()
    main.close()

def pause():
    pause_window.show()

def exit_in_lobby2():
    endwin.end_win.hide()
    hangman.close()
    main.show()

#основная часть программы
app = QApplication(sys.argv)
main = Main_win()
hangman = Hangman()
pause_window = pause_win()
game = Game()
endwin = EndGame()

hangman.pause_button.clicked.connect(pause)
main.start_game.clicked.connect(open_game)
main.exit.clicked.connect(main.close)
endwin.end_button.clicked.connect(exit_in_lobby2)
    
app.exec_()