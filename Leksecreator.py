import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
#For a PyQt application specifically, PyQt doesn't have a built-in mechanism for enforcing a single instance. However, you can achieve this behavior by other means, such as:
#Using a Mutex or a Lock File: Create a lock file or a mutex when the application starts. If the file or mutex already exists, it indicates the application is running, and you can either focus the existing window or exit the new instance.

class MathExerciseGenerator(QWidget):


	def __init__(self):
		super().__init__() # Henter ting fra super-klassen (hva da?)
		self.klassen = ""
		self.klassenPWD = ""
		self.initUI()
	
	def initUI(self):
		self.setWindowTitle('Math Exercise Generator')
		self.setGeometry(100, 100, 600, 500)

		layout = QVBoxLayout()

		self.nameLabel = QLabel('Student Name:')
		layout.addWidget(self.nameLabel)

		self.nameInput = QLineEdit()
		layout.addWidget(self.nameInput)

		# display PWD
		self.PWDdisplay = QLabel(self.klassenPWD)
		layout.addWidget(self.PWDdisplay)
		self.levelLabel = QLabel('Choose class:')
		layout.addWidget(self.levelLabel)

		self.selectKlasse = QComboBox()
		self.selectKlasse.addItems(['0NUSF', '0NUSG', '0NUSI'])
		self.selectKlasse.currentIndexChanged.connect(self.getClassPWD)
		layout.addWidget(self.selectKlasse)

		self.generateButton = QPushButton('Generate Exercise')
		self.generateButton.clicked.connect(self.generateExercise)
		layout.addWidget(self.generateButton)

		self.setLayout(layout)
	
	def generateExercise(self):
		student_name = self.nameInput.text()
		current_level = self.levelSelect.currentText()
		# Placeholder for generating exercise logic
		print(f"Generating exercise for {student_name}, Level {current_level}")

	def getClassPWD(self, index):
		self.klassen = self.selectKlasse.currentText()
		if self.klassen == "0NUSF":
			self.klassenPWD = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSF 2023/IndividuellF"
		elif self.klassen == "0NUSG":
			self.klassenPWD = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSG 2023/IndividuellG"
		elif self.klassen == "0NUSI":
			self.klassenPWD = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSI 2023/Individuell"
		else:
			self.klassenPWD = "Annen klasse"
		self.PWDdisplay.setText(self.klassenPWD)
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MathExerciseGenerator()
	ex.show()
	sys.exit(app.exec_())
