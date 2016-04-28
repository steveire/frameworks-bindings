#!/usr/bin/env python
#-*- coding: utf-8 -*-

import signal
import sys


sys.path.append(sys.argv[1])

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from PyKF5 import KItemModels
from PyKF5 import KWidgetsAddons

class TodoWidget(QtWidgets.QWidget):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)

		self.stringListModel = QtCore.QStringListModel();

		self.doneSelectionModel = QtCore.QItemSelectionModel()
		self.doneSelectionModel.setModel(self.stringListModel)

		self.checkableProxy = KItemModels.KCheckableProxyModel()
		self.checkableProxy.setSourceModel(self.stringListModel)
		self.checkableProxy.setSelectionModel(self.doneSelectionModel)

		mainlayout = QtWidgets.QHBoxLayout(self)

		todoLayout = QtWidgets.QVBoxLayout(self)
		mainlayout.addLayout(todoLayout)

		todoLayout.addWidget(QtWidgets.QLabel("TODO list"))

		addLayout = QtWidgets.QHBoxLayout(self)
		todoLayout.addLayout(addLayout)
		self.addLineEdit = QtWidgets.QLineEdit()
		addLayout.addWidget(self.addLineEdit)
		self.addButton = QtWidgets.QPushButton("Add")
		addLayout.addWidget(self.addButton)
		self.addButton.clicked.connect(self.add_todo)
		self.addLineEdit.returnPressed.connect(self.add_todo)

		self.stringsView = QtWidgets.QTreeView()
		self.stringsView.header().hide()
		self.stringsView.setModel(self.checkableProxy)
		self.stringsView.setSelectionMode(QtWidgets.QTreeView.ExtendedSelection)
		todoLayout.addWidget(self.stringsView)

		self.selectionProxy = KItemModels.KSelectionProxyModel()
		self.selectionProxy.setSourceModel(self.stringListModel)
		self.selectionProxy.setSelectionModel(self.doneSelectionModel)

		l = QtWidgets.QVBoxLayout(self)
		mainlayout.addLayout(l)

		l.addWidget(QtWidgets.QLabel("DONE list"))

		self.selectionView = QtWidgets.QTreeView()
		self.selectionView.header().hide()
		self.selectionView.setModel(self.selectionProxy)
		l.addWidget(self.selectionView)

		statusLayout = QtWidgets.QHBoxLayout(self)
		l.addLayout(statusLayout)

		self.ratingWidget = KWidgetsAddons.KLed()
		statusLayout.addWidget(self.ratingWidget)

		self.statusText = QtWidgets.QLabel("Status: Ok")
		statusLayout.addWidget(self.statusText)

	def add_todo(self):
		rc = self.stringListModel.rowCount()
		self.stringListModel.insertRow(rc)
		self.stringListModel.setData(self.stringListModel.index(rc, 0), self.addLineEdit.text())
		self.addLineEdit.clear()

app = QtWidgets.QApplication(sys.argv)

todoWidget = TodoWidget()
todoWidget.resize(600, 400)

todoWidget.show()

def sigint_handler(*args):
    QtWidgets.QApplication.quit()

signal.signal(signal.SIGINT, sigint_handler)

timer = QtCore.QTimer()
timer.start(16)
timer.timeout.connect(lambda: None)

app.exec_()
