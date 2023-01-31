from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel



app = QApplication([])
window = QWidget()
window.setWindowTitle('Program language')
window.resize(400, 300)

#1 шаг. Создать 6 надписей с названиями языков программирования
laybel1 = QLabel('PHP Code')
laybel2=QLabel('Javascript')
laybel3=QLabel('Python')
laybel4=QLabel('Pascal')
laybel5=QLabel('Java')
laybel6=QLabel('C#')

#2 шаг. Создать 4 направляющие: 3 горизонтальные и 1 вертикальную
layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

#3 шаг. Привязать 6 объектов к горизонтальным направляющим
layoutH1.addWidget(laybel1, alignment=Qt.AlignCenter)
layoutH1.addWidget(laybel2, alignment=Qt.AlignCenter)
layoutH2.addWidget(laybel3, alignment=Qt.AlignCenter)
layoutH2.addWidget(laybel4, alignment=Qt.AlignCenter)
layoutH3.addWidget(laybel5, alignment=Qt.AlignCenter)
layoutH3.addWidget(laybel6, alignment=Qt.AlignCenter)

#4 шаг. Привязать горизонтальные направляющие к вертикальной направляющей
layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
window.setLayout(layoutV)

window.show()
app.exec_()

# Последний шаг. Создать 4 направляющие: 3 горизонтальные и 1 вертикальную
