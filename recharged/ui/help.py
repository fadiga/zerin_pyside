#!/usr/bin/env python
# encoding=utf-8
# maintainer: fad

import os
from PySide import QtGui, QtCore
import PySide.QtWebKit


class HTMLEditor(QtGui.QDialog):

    def __init__(self, parent = None):
        super(HTMLEditor, self).__init__(parent)

        self.setWindowTitle(u"Aide")
        view = PySide.QtWebKit.QWebView(parent)

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        view.load(QtCore.QUrl("file://%s" % os.path.join(ROOT_DIR, 'help.html')))
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(view)