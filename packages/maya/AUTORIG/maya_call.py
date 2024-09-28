import os
from PySide2 import QtWidgets, QtCore
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

class SimpleWindow(QtWidgets.QWidget):
    def __init__(self):
        super(SimpleWindow, self).__init__()

        self.setWindowTitle("Simple PySide2 Window")

        # Create layout
        layout = QtWidgets.QVBoxLayout()

        # Create buttons
        self.load_position_button = QtWidgets.QPushButton("Load Position")
        self.run_script_button = QtWidgets.QPushButton("Run Script")
        self.selector_button = QtWidgets.QPushButton("Selector")

        # Add buttons to layout
        layout.addWidget(self.load_position_button)
        layout.addWidget(self.run_script_button)
        layout.addWidget(self.selector_button)

        # Set layout for the main window
        self.setLayout(layout)

        # Connect buttons to functions
        self.load_position_button.clicked.connect(self.load_position)
        self.run_script_button.clicked.connect(self.run_script)
        self.selector_button.clicked.connect(self.selector_script)

    def load_position(self):
        cmds.file('E:\Git___\zarco-pipeline\packages\maya\AUTORIG\characterTuners12.ma', i=True, force=True)

    def run_script(self):
        cmds.file(r"E:\Git___\zarco-pipeline\packages\maya\AUTORIG\AutoRig.mel", i=True, force=True)

    def selector_script(self):
        print("Close button clicked")
        cmds.file(r"E:\Git___\zarco-pipeline\packages\maya\AUTORIG\selectorInterface5.mel", i=True, force=True)

def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

def run():
    parent = get_maya_main_window()
    render_window = SimpleWindow()
    render_window.setParent(parent, QtCore.Qt.Window)
    render_window.show()

