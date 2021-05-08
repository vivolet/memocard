#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QRadioButton, QGroupBox, QVBoxLayout, QButtonGroup
from random import shuffle, randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memo Card')
lb_question = QLabel('Самый простой вопрос. ОС от Microsoft?')
btn = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Windows')
rbtn_2 = QRadioButton('Android')
rbtn_3 = QRadioButton('Linux')
rbtn_4 = QRadioButton('MacOS')
AnswerGroupBox = QGroupBox('Результат теста')
btn_1 = QLabel('Правильно/Неправильно')
btn_2 = QLabel('Windows')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#создание виджетов главного окна
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(btn_1)
layout_ans4.addWidget(btn_2)
AnswerGroupBox.setLayout(layout_ans4)

#расположение виджетов по лэйаутам
layout_main = QVBoxLayout()
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnswerGroupBox.hide()
layoutH1.addWidget(lb_question, alignment = Qt.AlignCenter)
layoutH2.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn, alignment = Qt.AlignCenter)
layoutH2.addWidget(AnswerGroupBox, alignment = Qt.AlignCenter)
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

#обработка нажатий на переключатели
def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    btn.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if btn.text() == 'Ответить':
        show_result()
    else:
        show_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q):
    shuffle(answers)
    lb_question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    btn_2.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
def click_ok():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()
    
main_win.cur_question = -1
def next_question():
    main_win.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
    print('Всего:', main_win.total)
    print('Рейтинг:', (main_win.score/main_win.total) * 100)
def show_correct(res):
    btn_1.setText(res)
    show_result()
btn.clicked.connect(click_ok)
main_win.total = 0
main_win.score = 0
questions_list = []
q1 = Question('Устройство вывода звуковой информации','Колонки','Клавиатура','Монитор','Дисковод')
q2 = Question('Портативный компьютер','Ноутбук','Планшет','Смартфон','КПК')
q3 = Question('Сколько клавиш на клавиатуре?','104','112','103','106')
q4 = Question('Год создания компании Xiaomi','2010','2013','2008','2016')
q5 = Question('Марка смартфонов от Google','Pixel','Chromebook','Realme','Lumia')
q6 = Question('Дочерняя компания смартфонов от Huawei','Honor','OnePlus','Vivo','Xiaomi')
q7 = Question('Год выпуска iPhone 5','2012','2014','2015','2013')
q8 = Question('Назовите НЕ дочернюю компанию','Нет правильного ответа','Pocophone','OnePlus','Honor')
q9 = Question('Первый смартфон на Android от Samsung был выпущен в:','2009','2013','2011','2007')
q10 = Question('Первый процессор серии Apple Silicon:','M1','Pentium 4','Xeon E5','Ryzen 3')
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
questions_list.append(q5)
questions_list.append(q6)
questions_list.append(q7)
questions_list.append(q8)
questions_list.append(q9)
questions_list.append(q10)
#отображение окна приложения
main_win.setLayout(layout_main)
main_win.show()
app.exec_()