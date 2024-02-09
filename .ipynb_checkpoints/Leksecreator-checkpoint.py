import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox

class MathExerciseGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Math Exercise Generator')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.nameLabel = QLabel('Student Name:')
        layout.addWidget(self.nameLabel)

        self.nameInput = QLineEdit()
        layout.addWidget(self.nameInput)

        self.levelLabel = QLabel('Current Level:')
        layout.addWidget(self.levelLabel)

        self.levelSelect = QComboBox()
        self.levelSelect.addItems(['1', '2', '3', '4', '5'])
        layout.addWidget(self.levelSelect)

        self.generateButton = QPushButton('Generate Exercise')
        self.generateButton.clicked.connect(self.generateExercise)
        layout.addWidget(self.generateButton)

        self.setLayout(layout)
    
    def generateExercise(self):
        student_name = self.nameInput.text()
        current_level = self.levelSelect.currentText()
        # Placeholder for generating exercise logic
        print(f"Generating exercise for {student_name}, Level {current_level}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MathExerciseGenerator()
    ex.show()
    sys.exit(app.exec_())
