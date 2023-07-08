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
#главное меню
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
        
#окно игры
    class game_window(QMainWindow):
        def __init__(self):
            super().__init__()
            self.widget = QWidget()
            self.widget.setWindowTitle('Виселица')
            self.widget.resize(700, 700)
            self.widget.show()

            self.lb_man = QLabel()
            

            self.main_layout = QVBoxLayout()
            self.right_layout = QVBoxLayout()
            self.top_layout = QHBoxLayout()
            self.alphabet_layout = QVBoxLayout()
            self.right_layout.addLayout(self.alphabet_layout)
            self.top_layout.addWidget(self.lb_man)
            self.top_layout.addLayout(self.right_layout)
            
            self.main_layout.addLayout(self.top_layout)
            
            self.label = QLabel(self)
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

            self.pixmap = QPixmap(500,500)
            self.pixmap.fill(QColor('white'))
            

            self.painter = QPainter(self.pixmap)

            self.painter.setRenderHint(QPainter.Antialiasing)
            self.painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
            self.painter.setBrush(Qt.NoBrush)

            


        def check_letter(self, letter):
            if letter in self.guessed_letters:
                return

            self.guessed_letters.append(letter)

            if letter not in self.word:
                self.tries += 1
                if self.tries >= 1:
                    self.painter.drawLine(50, 350, 150, 350)

                if self.tries >= 2:
                    self.painter.drawLine(100, 350, 100, 50)

                if self.tries >= 3:
                    self.painter.drawLine(100, 50, 200, 50)

                if self.tries >= 4:
                    self.painter.drawLine(200, 50, 200, 100)

                if self.tries >= 5:
                    self.painter.drawEllipse(175, 100, 50, 50)

                if self.tries >= 6:
                    self.painter.drawLine(200, 150, 200, 250)
                    self.painter.drawLine(200, 250, 175, 300)
                    self.painter.drawLine(200, 250, 225, 300)
                print(self.tries)

            self.update_label()
            

            if self.check_win():
                self.label.setText('Вы выиграли!')
                self.disable_buttons()

            if self.check_lose():
                self.label.setText('Вы проиграли!')
                self.disable_buttons()
            
            self.update()
            self.lb_man.setPixmap(self.pixmap)

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
        self.widget.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_Window()
    sys.exit(app.exec_())