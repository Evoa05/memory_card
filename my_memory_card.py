from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Игра жанра "приключения"', "Tomb Raider", "CS:GO", "Dota 2", "Minecraft"))
question_list.append(Question('Какого предмета не существует?', 'Рукоделие', 'Технология', 'Искуссктво', 'Музыка'))
question_list.append(Question('Какой пулей можно убить вампира?', 'Серебряной', 'Железной', 'Золотой', 'Медной'))
question_list.append(Question('Какго фильма не существует?', 'Истребители', 'Звонок', 'Форсаж', 'Астрал'))
question_list.append(Question('Работа сязаная с физ. силой', 'грузчик', 'программист', 'учитель', 'художник'))
question_list.append(Question('Приложение для создания музыки', 'FL studio', 'Steam', 'Mail.ru', 'VK'))
question_list.append(Question('Что относится к гуманитарным наукам?', 'Филология', 'Физика', 'Математика', 'Геометрия'))
question_list.append(Question('Кто Бог грома?', 'Тор', 'Локи', 'Бальдр', 'Видар'))
question_list.append(Question('Из чего делают бумагу?', 'из дерева', 'из травы', 'из земли', 'из листвы'))
question_list.append(Question('Какая пятая планета от солнца?', 'Юпитер', 'Сатурн', 'Меркурий', 'Венера'))

app = QApplication([])
 
'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса
 
RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# варианты ответов на вопросы
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
 # их позиционирование
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
 
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


# создаем горизовнтальные линии для размещения виджетов
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
# позиционируем наш виджет вопроса относительно центра
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox) # назначаем группу ответов на 2 гор. линию
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()

 
layout_line3.addStretch(1) # назначаем отступы для нашей кнопки справа и слева 
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой, растягиваем на 2 "столбца"
layout_line3.addStretch(1) # назначаем отступы для нашей кнопки справа и слева 
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout() # создаем центральную линия для того чтобы закрепить всю ранее созданную сетрку
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

# все виджеты расставлены и настоло время написать функции для взаимодествия
# ********************************************************

def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total, '\n-Правельных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')

def next_question():
          #задает следующий вопрос из списка
    window.total += 1 #Счётчик заданы вопросов
    print('Статистика\n-Всего вопросов:', window.total, '\n-Правельных ответов:', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question] # взяли вопрос
    ask(q) # спросили

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setWindowTitle('Memory Card')

window.setLayout(layout_card) # сделали родителем окно для главной вертикальной линии

btn_OK.clicked.connect(click_OK) # проверяем, что панель ответов показывается при нажатии на кнопку

window.total = 0
window.score = 0
next_question()

window.resize(250, 200)
window.show()
app.exec()