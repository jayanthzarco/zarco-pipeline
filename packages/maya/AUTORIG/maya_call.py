import os
from PySide2.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget
import maya.cmds as cmds

class SimpleWindow(QWidget):
    def __init__(self):
        super(SimpleWindow, self).__init__()

        self.setWindowTitle("Simple PySide2 Window")

        # Create layout
        layout = QVBoxLayout()

        # Create buttons
        self.load_position_button = QPushButton("Load Position")
        self.run_script_button = QPushButton("Run Script")
        self.selector_button = QPushButton("Selector")

        # Add buttons to layout
        layout.addWidget(self.load_position_button)
        layout.addWidget(self.run_script_button)
        layout.addWidget(self.selector_button)

        # Set layout for the main window
        self.setLayout(layout)

        # Connect buttons to functions
        self.load_position_button.clicked.connect(self.load_position)
        self.run_script_button.clicked.connect(self.run_script)
        self.close_button.clicked.connect(self.selector_script)

    def load_position(self):
        cmds.file('E:\Git___\zarco-pipeline\packages\maya\AUTORIG\characterTuners12.ma', i=True, force=True)

    def run_script(self):
        cmds.file(r"E:\Git___\zarco-pipeline\packages\maya\AUTORIG\AutoRig.mel", i=True, force=True)

    def selector_script(self):
        print("Close button clicked")
        cmds.file(r"E:\Git___\zarco-pipeline\packages\maya\AUTORIG\selectorInterface5.mel", i=True, force=True)

def run():
    global window
    window = SimpleWindow()
    window.show()

