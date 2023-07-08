from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QMessageBox,
    QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QPainter, QPen, QFont, QPixmap, QColor
from PyQt5.QtCore import Qt
import sys, random


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.start_button = QPushButton('Новая игра')
        self.continue_button = QPushButton('Продолжить')
        self.highscore_button = QPushButton('Рекорды')
        self.achievement_button = QPushButton('Достижения')
        self.exit_button = QPushButton('Выход')
        self.widget = QWidget()
        self.widget.show()
        self.widget.setWindowTitle('Виселица')
        self.widget.resize(500,500)

        self.v_line1 = QVBoxLayout()
        self.v_line1.addWidget(self.start_button)
        self.v_line1.addWidget(self.continue_button)
        self.v_line1.addWidget(self.highscore_button)
        self.v_line1.addWidget(self.achievement_button)
        self.v_line1.addWidget(self.exit_button)
        self.widget.setLayout(self.v_line1)

        self.start_button.clicked.connect(self.open_game_window)
        

    class game_window(QMainWindow):
        def __init__(self):
            super().__init__()
            self.lb_man = QLabel()
            
            self.widget = QWidget()
            self.widget.setWindowTitle('Виселица')
            self.widget.resize(700, 700)
            self.widget.show()

            self.main_layout = QVBoxLayout()
            self.right_layout = QVBoxLayout()
            self.top_layout = QHBoxLayout()
            self.alphabet_layout = QVBoxLayout()
            #right_layout.addWidget() добавить виджет
            self.right_layout.addLayout(self.alphabet_layout, Qt.AlignBottom)
            #top_layout.addWidget(stickman)
            self.top_layout.addLayout(self.right_layout)
            self.top_layout.addWidget(self.lb_man)
            self.main_layout.addLayout(self.top_layout)
            #main_layout.addWidget()
            
            self.label = QLabel(self)
            #self.label.setGeometry(10, 10, 380, 30)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setFont(QFont('Arial', 20))
            self.main_layout.addWidget(self.label)
            
            self.widget.setLayout(self.main_layout)

            self.word = random.choice(['кот', 'собака', 'питон', 'программирование', 'компьютер'])
            self.tries = 0
            self.max_tries = 6
            self.guessed_letters = []

           
            
            self.s_letters = []
            for i in range(3):
                self.s_letters.append(QHBoxLayout())
                self.alphabet_layout.addLayout(self.s_letters[i])

            self.button_layout = QHBoxLayout()
            x = 0
            i = 0
            for letter in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
                button = QPushButton(letter, self)
                button.setFixedSize(70, 70)
                button.clicked.connect(lambda _, l=letter: self.check_letter(l))
                self.s_letters[i].addWidget(button)

                x += 1
                if x % 11 == 0:
                    i += 1  


        def paintEvent(self, event):
            self.pixmap = QPixmap(500,500)
            self.pixmap.fill(QColor('white'))
            self.lb_man.setPixmap(self.pixmap)
            painter = QPainter(self.lb_man)
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

            painter.end()

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


    def open_game_window(self):
        self.window = self.game_window()
        self.window.show()
        self.widget.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_Window()
    sys.exit(app.exec_())