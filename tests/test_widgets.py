""" Unit test decpys.widgets.
"""



# python
import os

# package path
import define_pkg_path

# pytest
from fixtures import init_qapp

# pyside
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

# decpys
from decpys.gui import (
    qIcon
)
from decpys.types import (
    onClick
)
from decpys.widgets import (
    qLabel,
    qMainWindow,
    qPushButton,
    qVBoxLayout,
    qWidget
)



##########################################
##          UNIT TEST WIDGETS           ##
##########################################


##  -------------------------
##  QLabel


def test_qlabel(init_qapp):
    """ Assert that `qLabel()` initializes and returns a `QLabel` appropriately.
    """
    label = qLabel(
        text="label",
        align=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
    )
    assert isinstance(label, QLabel), \
        "The value returned from qLabel() must be type Qt Label object."
    assert label.text() == "label", \
        "The label's text must be set within qLabel()."
    assert label.alignment() & Qt.AlignmentFlag.AlignHorizontal_Mask == Qt.AlignmentFlag.AlignRight, \
        "The label's horizontal alignment must be set within qLabel()."
    assert label.alignment() & Qt.AlignmentFlag.AlignVertical_Mask == Qt.AlignmentFlag.AlignVCenter, \
        "The label's vertical alignment must be properly set within qLabel()."



##  -------------------------
##  QMainWindow


def test_qmainwindow(init_qapp):
    """ Assert that `qMainWindow()` initializes and returns a `QMainWindow` appropriately.
    """
    window = qMainWindow(
        title="window",
        centralWidget = qLabel(
            text = "window label",
            align = Qt.AlignmentFlag.AlignCenter
        )
    )
    assert isinstance(window, QMainWindow), \
        "The value returned from qMainWindow() must be type QMainWindow."
    assert window.centralWidget() != 0, \
        "The main window's central widget must be set from within qMainWindow()."



##  -------------------------
##  QPushButton


qPushButtonValue = 0
def incrementQPushButtonValue():
    global qPushButtonValue
    qPushButtonValue += 1


def test_qpushbutton(init_qapp):
    """ Assert that `qPushButton()` initializes and returns a `QPushButton` appropriately.
    """
    # button with text
    btn1 = qPushButton(display="button1")
    assert isinstance(btn1, QPushButton), \
        "The value returned from qPushButton() must be of type QPushButton."
    assert btn1.text() == "button1", \
        "The button's text must be set within qPushButton()."

    # button with icon
    btn2 = qPushButton(
        display=qIcon(
            os.path.join(".", "tests", "icons", "check-underline.png")
        )
    )
    assert isinstance(btn2, QPushButton), \
        "The value returned from qPushButton() must be type QPushButton."
    assert btn2.icon() != None, \
        "The button's icon must be set within qPushButton()"


def test_qpushbutton_onClick(init_qapp):
    """
    """
    btn = qPushButton(
        display = "clickHandler",
        slots = [
            (onClick(), incrementQPushButtonValue)
        ]
    )
    btn.click()
    assert qPushButtonValue == 1, \
        "The global value must be incremented after the button is clicked."



##  -------------------------
##  QVBoxLayout


def test_qvboxlayout(init_qapp):
    """ Assert that `qVBoxLayout()` initializes and returns a QVBoxLayout.
    """
    layout = qVBoxLayout(
        children = [
            qLabel("label")
        ]
    )
    assert isinstance(layout, QVBoxLayout), \
        "The value returned from qVBoxLayout() must be type QVBoxLayout."
    assert layout.count() == 1, \
        "The layout's children widgets must be added inside qVBoxLayout()."



##  -------------------------
##  QWidget


def test_qwidget(init_qapp):
    """ Assert that `qWidget()` initializes and returns a QWidget.
    """
    widget = qWidget(
        layout = qVBoxLayout(
            children = [
                qLabel(
                    text = "label"
                )
            ]
        )
    )
    assert isinstance(widget, QWidget), \
        "The value returned from qWidget() must be type QWidget."
    assert len(widget.children()) == 2, \
        "The widget's children widgets must be transferred to the widget after configuring the layout."

