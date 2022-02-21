""" An example decpys app showcasing development from v0.1.
"""



# path
# The following import is needed so that the decpys package can be used locally, without the need
# for a pip install.
import decpys_path

# pyside
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QLabel, QMainWindow
)

# decpys
from decpys.types import onClick
from decpys.widgets import (
    qLabel,
    qMainWindow,
    qPushButton,
    qVBoxLayout,
    qWidget
)



###################################################################################################
##  EXAMPLE APP:                                                                                ###
##  A clickable button and an accompanying label that tracks how many times the button has      ###
##  been clicked.                                                                               ###
###################################################################################################




# This global variable will keep track of how many times the button has been clicked.
number = 0

# This function will later be tied to the button by matching a signal to a slot in our UI code.
def incrementNumber():
    global number   # use the global number value that we instantiated before
    global window   # use the global window value that holds our UI
    number += 1

    # Find the label within the window. It's the only label within the app, so a name isn't needed.
    # In future versions we might see more sophisticated ways of looking up widgets in our UI.
    label: QLabel = window.findChild(QLabel, None, Qt.FindChildrenRecursively)

    # After finding the label, reset its label to a new string, based on the value of the global
    # variable number.
    label.setText(f'You have clicked the button {number} times.')




# All that was setup. The real app starts here.
# decpys is meant to be used in conjunction with PySide6. For that reason, we still need to import 
# PySide6 (check out the import statements at the top of this module). Start a QApplication: an 
# instance of QApplication must exist before any widgets can be instantiated.
app = QApplication()


# Now for our UI code.
# decpys is inspired by frameworks like React and Flutter. Imperative-style programming is
# non-intuitive and can be cumbersome to write. decpys provides a library of functions that
# does all the Qt widget instantiation for us, so that we can focus on writing our UI code in
# an intuitive and readable way.
window = qMainWindow(                                                       # start a QMainWindow
    title="ClickableButton Example",                                        # set the window title
    centralWidget=qWidget(                                                  # start a QWidget
        layout=qVBoxLayout(                                                 # start a QVBoxLayout
            children=[                                                      # start a list of children widgets
                qLabel(                                                     # start a QLabel
                    text=f"You have clicked the button {number} times.",    # set the label's text
                    align=Qt.AlignCenter                                    # set the label's alignment
                ),                                                          # close the QLabel, making it the layout's 1st child
                qPushButton(                                                # start a QPushButton
                    display="Click me!",                                    # set the button's text
                    slots=[                                                 # start a list of signals and slots
                        (onClick(), incrementNumber)                        # tie incrementNumber() to this button's clicked signal
                    ]                                                       # close the list of signals and slots
                )                                                           # close the QPushButton, making it the layout's 2nd child
            ]                                                               # close the list of children widgets for the layout
        )                                                                   # close the layout, making it the QWidget's layout
    )                                                                       # close the QWidget, making it the window's central widget
)                                                                           # close the QMainWindow and set it to the global window


window.show()   # show the window so that it is visible
app.exec()      # execute the main app loop