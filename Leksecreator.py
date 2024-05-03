from operator import le
import sys
import os, shutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QListWidget
#For a PyQt application specifically, PyQt doesn't have a built-in mechanism for enforcing a single instance. However, you can achieve this behavior by other means, such as:
#Using a Mutex or a Lock File: Create a lock file or a mutex when the application starts. If the file or mutex already exists, it indicates the application is running, and you can either focus the existing window or exit the new instance.

class MathExerciseGenerator(QWidget):

	#Lager én instance av appen??
	def __init__(self):
		super().__init__() # Henter ting fra super-klassen (hva da?)
		self.klassen = ""
		# Initieres med path til 0NUSF (midlertidig)
		self.klassenPWD = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSF 2023/IndividuellF"
		# Result from file search
		self.foundFiles = ['test']
		# Rename files preview
		self.renameFiles = [] # Trenger denne å initialiseres? Sannsynligvis ja, pga den skal brukes til copy-and-rename etterpå
		self.initUI()
	
	# Creating the UI
	def initUI(self):
		#Overskriften til programmet
		self.setWindowTitle('Math Exercise Generator')
		# Definerer plassering og størrelse på vinduet (Ambisjon: dynamisk størrelse)
		# (plasseringX, plasseringY, størrelseX, størrelseY)
		self.setGeometry(300, 100, 1000, 500)

		# Horisontal layout inndeling
		mainLayout = QHBoxLayout()  

		# Vertikal layout inndeling for venstre side
		leftLayout = QVBoxLayout()


			# # Ikke behov på nåværende tidspunkt
		# #label for input
		# self.nameLabel = QLabel('Student Name:')
		# leftLayout.addWidget(self.nameLabel)
		# #input-felt
		# self.nameInput = QLineEdit()
		# leftLayout.addWidget(self.nameInput)


		# Søkefelt for filer
		# #Fase 1: finn filer å modifisere - Fase 2: Lag/Bruk en database
		#label for søkefelt
		self.searchStringLabel = QLabel('Search string:')
		leftLayout.addWidget(self.searchStringLabel)
		#søkefelt
		self.searchStringInput = QLineEdit()
		# Kobler søkefeltet til searchForFiles
		self.searchStringInput.textChanged.connect(self.searchForFiles)
		leftLayout.addWidget(self.searchStringInput)
		# (Copy and) Replace with label
		self.replaceWithLabel = QLabel('Replace search string with:')
		leftLayout.addChildWidget(self.replaceWithLabel)
		# (Copy and) Replacement string
		self.replaceWithField = QLineEdit()
		leftLayout.addWidget(self.replaceWithField)
		# Connecting replaceWithField to output
		self.replaceWithField.textChanged.connect(self.copyAndRenameFiles)



		# display PWD - debug, showing the path for the files for this class
		self.PWDdisplay = QLabel(self.klassenPWD)
		leftLayout.addWidget(self.PWDdisplay)
		# Just the text urging the user to select a class
		self.chooseKlasseLabel = QLabel('Choose class:')
		leftLayout.addWidget(self.chooseKlasseLabel)
		# Boks for å velge klasse -> Vurderes endret til radio-buttons
		self.selectKlasse = QComboBox()
		self.selectKlasse.addItems(['0NUSF', '0NUSG', '0NUSI'])
		# Could the signal send class name rather than index?
		self.selectKlasse.currentIndexChanged.connect(self.getClassPWD)
		leftLayout.addWidget(self.selectKlasse)

		# Lag-oppgaver knapp. Foreløpig bare et skall
		self.generateButton = QPushButton('Generate Exercise')
		self.generateButton.clicked.connect(self.generateExercise)
		leftLayout.addWidget(self.generateButton)



		# Høyre side av layouten i appen
		rightLayout = QVBoxLayout()

		# Label for found files
		self.searchResultLabel = QLabel("Files found: ")
		rightLayout.addWidget(self.searchResultLabel)

		# Boks til filnavn
		self.fileDisplay = QListWidget()
		rightLayout.addWidget(self.fileDisplay)
		self.fileDisplay.addItem("test")

		# Til høyre for høyre
		rightmostLayout = QVBoxLayout()
		# preview label
		self.renamePreviewLabel = QLabel("Rename preview: ")
		rightmostLayout.addWidget(self.renamePreviewLabel)
		# Box for file preview
		self.filePreview = QListWidget()
		rightmostLayout.addWidget(self.filePreview)

		# Add both left and right and rightmost layouts to the main layout
		mainLayout.addLayout(leftLayout)
		mainLayout.addLayout(rightLayout)
		mainLayout.addLayout(rightmostLayout)
		#mainLayout.addWidget(self.fileDisplay)  # Add the file display list to the main layout

		# initierer(?) layouten
		self.setLayout(mainLayout)
	
	# Tomt skall - ikke utarbeidet
	def generateExercise(self):
		student_name = self.nameInput.text()
		current_level = self.levelSelect.currentText()
		# Placeholder for generating exercise logic
		print(f"Generating exercise for {student_name}, Level {current_level}")

	# Henter pathen til de respektive klassene. 
	# #Skal senere erstattes med en database for de respektive klassene
	def getClassPWD(self, index): # index trengs ikke skrives, for den brukes ikke 
		# Could the function receive the class name rather than the index?
		self.klassen = self.selectKlasse.currentText()
		if self.klassen == "0NUSF":
			self.klassenPWD = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSF 2023/IndividuellF"
		elif self.klassen == "0NUSG":
			self.klassenPWD = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSG 2023/IndividuellG"
		elif self.klassen == "0NUSI":
			self.klassenPWD = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSI 2023/Individuell"
		else:
			self.klassenPWD = "Annen klasse"
		# Setting the class name as the content of the dropdown for choosing class(?)
		self.PWDdisplay.setText(self.klassenPWD)
		
	# Finner filene som matcher 
	def searchForFiles(self, searchString):
		os.system('cls') # Bare for windows (trengs den for UI-en, eller bare for powershell?)
		# print("Search string:", searchString) # Bare for powershell
		searchString = searchString.lower()
		self.fileDisplay.clear()
		self.foundFiles = ['test']
		files = [f for f in os.listdir(self.klassenPWD) if os.path.isfile(os.path.join(self.klassenPWD, f))]
		# files = [f for f in os.listdir(self.klassenPWD)] #debug, slett

		# Filter files based on search string
		self.foundFiles = [f for f in files if searchString in f.lower()]

		# Update QListWidget with found files
		for file in self.foundFiles:
			self.fileDisplay.addItem(file)

		# Optional: print to console (or use logging instead in real applications)
		print("Found files:", self.foundFiles)

		# for file in files: # kan jeg ta for-løkka rett inn i list-comprehension delen?
		# 	if (file.lower().find(searchString) != -1):
		# 		#print(file)
		# 		self.foundFiles.append(file)
		# print(self.foundFiles)
		
	def copyAndRenameFiles(self, renameString):
		os.system('cls') # clear powershell for each change to remaned files
		self.renameFiles = [] # Must reset for each change.
		self.filePreview.clear() # Must clear field for each change
		for file in self.foundFiles:
			self.renameFiles = self.renameFiles + [file.replace(self.searchStringInput.text(), renameString)]
			print(self.searchStringInput.text()) # funker
			print("Rename string: ", renameString)
			print(file.replace(self.searchStringInput.text(), renameString))
		for file in self.renameFiles:
			self.filePreview.addItem(file)



if __name__ == '__main__':
	app = QApplication(sys.argv) # Hva gjør denne?
	ex = MathExerciseGenerator() # Lager en instance av MathExerciseGenerator
	ex.show() #Viser programmet?
	sys.exit(app.exec_()) # Avslutter programmet? Lytter til diverse close-window kommandoer?
