from PyQt4 import QtGui

app = QtGui.QApplication([])
main_win = QtGui.QMainWindow()
frame = QtGui.QFrame(main_win)
main_win.setCentralWidget(frame)
grid_layout = QtGui.QGridLayout(frame)

text_editor = QtGui.QTextEdit()
text_editor.setText("This is a simple PyQt app that includes "
                    "a main window, a grid layout, and a text "
                    "editor widget.\n\n"
                    "It is constructed entirely from code.")
grid_layout.addWidget(text_editor)
main_win.show()
# Need the following statement if running as a script
app.exec_()
