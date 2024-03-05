import pytest
from PyQt5.QtWidgets import QApplication #redundant
from PyQt5 import QtCore
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

def test_class_pats(app, qtbot):
	"""
	Test that the correct path is displayed when "0NUS*" is chosen.
	"""
	# Simulate selecting 0NUSF from the dropdown
	# 0NUSF being the default value necessitates an extra value change
	app.selectKlasse.setCurrentIndex(app.selectKlasse.findText("0NUSG"))
	app.selectKlasse.setCurrentIndex(app.selectKlasse.findText("0NUSF"))
	# 0NUSF expected path
	expected_pathF = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSF 2023/IndividuellF"
	# expected path == displayed path
	assert app.PWDdisplay.text() == expected_pathF

	qtbot.mouseClick(app.selectKlasse, QtCore.Qt.LeftButton)
	qtbot.keyClicks(app.selectKlasse, "0NUSG")
	qtbot.keyPress(app.selectKlasse, QtCore.Qt.Key_Enter)
	app.selectKlasse.setCurrentIndex(app.selectKlasse.findText("0NUSG"))
	expected_pathG = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSG 2023/IndividuellG"
	assert app.PWDdisplay.text() == expected_pathG
	
	qtbot.mouseClick(app.selectKlasse, QtCore.Qt.LeftButton)
	qtbot.keyClicks(app.selectKlasse, "0NUSI")
	qtbot.keyPress(app.selectKlasse, QtCore.Qt.Key_Enter)
	app.selectKlasse.setCurrentIndex(app.selectKlasse.findText("0NUSI"))
	expected_pathI = "C:/Users/andran0803/OneDrive - Osloskolen/_Skole/Matematikk/Resultater/Lekser 0NUSI 2023/Individuell"
	assert app.PWDdisplay.text() == expected_pathI
	
	