import pytest
from PyQt5.QtWidgets import QApplication #redundant
from PyQt5 import QtCore
from pytestqt.qt_compat import qt_api
from Leksecreator import MathExerciseGenerator

@pytest.fixture
def app(qtbot):
	"""
	Fixture for creating the application instance and setting up qtbot.
	qtbot is a pytest-qt fixture that provides methods to control the GUI.
	"""
	test_app = MathExerciseGenerator()
	qtbot.addWidget(test_app)
	return test_app

def test_class_paths(app, qtbot):

	# Simulate selecting 0NUSF from the dropdown
	# 0NUSF being the default value necessitates an extra value change
	app.selectKlasse.setCurrentIndex(app.selectKlasse.findText("0NUSG"))
	app.selectKlasse.setCurrentIndex(app.selectKlasse.findText("0NUSF"))
	# 0NUSF expected path
	# WARNING - fixed path
	expected_pathF = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSF 2023/IndividuellF"
	# expected path == displayed path
	assert app.PWDdisplay.text() == expected_pathF

	# Testing expected path for 0NUSG
	# Simulating with clicks
	qtbot.mouseClick(app.selectKlasse, QtCore.Qt.LeftButton)
	qtbot.keyClicks(app.selectKlasse, "0NUSG")
	qtbot.keyPress(app.selectKlasse, QtCore.Qt.Key_Enter)
	app.selectKlasse.setCurrentIndex(app.selectKlasse.findText("0NUSG"))
	# WARNING - fixed path
	expected_pathG = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSG 2023/IndividuellG"
	assert app.PWDdisplay.text() == expected_pathG
	
	# Testing expected path for 0NUSI
	# Simulating with clicks
	qtbot.mouseClick(app.selectKlasse, QtCore.Qt.LeftButton)
	qtbot.keyClicks(app.selectKlasse, "0NUSI")
	qtbot.keyPress(app.selectKlasse, QtCore.Qt.Key_Enter)
	app.selectKlasse.setCurrentIndex(app.selectKlasse.findText("0NUSI"))
	# WARNING - fixed path
	expected_pathI = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSI 2023/Individuell"
	assert app.PWDdisplay.text() == expected_pathI

def test_search(app, qtbot, mocker):
	# Setup 0NUSG
	# Real path irrelevant
	app.klassenPWD = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSF 2023/IndividuellF"
	# Er denne riktig satt opp? Hva gjør qt_api?
	app.fileDisplay = qt_api.QtWidgets.QListWidget() # Forstå denne.
	qtbot.addWidget(app.fileDisplay)

	# Setting up Mock os.listdir and os.path.isfile
	mocker.patch('os.listdir', return_value=["testfil.txt", "enTilTest.xlsx", "dummyfil.d"])
	mocker.patch('os.path.isfile', return_value=True)

	# Test: File found
	app.searchForFiles('entil')
	assert 'enTilTest.xlsx' in [app.fileDisplay.item(i).text() for i in range(app.fileDisplay.count())]

	# Test: File not found
	app.searchForFiles('detteErIkkeEnFil')
	assert app.fileDisplay.count() == 0 # Expecting no files found

	# Test for å sjekke udefinert app.klassenPWD?