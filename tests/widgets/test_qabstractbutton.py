""" Unit test decpys.widgets.QAbstractButton.
"""



# built-in
from __future__ import annotations
from typing import Optional
import pytest
import define_pkg_path

# pyside
from PySide6.QtWidgets import QApplication, QWidget

# decpys
from decpys.gui import QIcon
from decpys.widgets import QAbstractButton



##########################
## Classes and wrappers ##
##########################



class Button(QAbstractButton):
    """ Simple button class derived from `QAbstractButton`.
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

    def setIcon(self, icon: QIcon) -> Button:
        return super().setIcon(icon)

    def setText(self, text: str) -> Button:
        return super().setText(text)

def button(text: str = None, icon: QIcon = None):
    btn = Button()
    if text:
        btn.setText(text)
    elif icon:
        btn.setIcon(icon)
    return btn



#####################
##      TESTS      ##
#####################



@pytest.fixture(scope="module")
def init_qapp():
    app = QApplication()
    yield app


def test_qabstractbutton(init_qapp):
    """ Assert that a QAbstractButton can be initialized.
    """
    btn = QAbstractButton()
    assert isinstance(btn, QAbstractButton), \
            "The button must register as a QAbstractButton type object."


def test_button_is_qabstractbutton(init_qapp):
    """ Assert that a Button (derived from QAbstractButton) registers as its basetype.
    """
    btn = Button()
    assert isinstance(btn, Button), \
            "The button must register as type Button."
    assert isinstance(btn, QAbstractButton), \
            "The button must register as type of its superclass QAbstractButton."


def test_button_text(init_qapp):
    """ Assert that a Button can have its text mutated and accessed.
    """
    btn = button(text="button")
    assert isinstance(btn, Button), \
            "The button() method must return the instance of the widget."
    assert btn.text() == "button", \
            "The button() method must set the text of the widget it is given."
    btn = button(text="original").setText("mutated")
    assert btn.text() == "mutated", \
            "The setText() method must return an instance of the widget after it has been mutated."


def test_button_icon(init_qapp):
    """ Assert that a Button (derived from QAbstractButton) can have its icon mutated and accessed.
    """
    btn = button(icon=QIcon("tests\\gui\\icons\\check-underline.png"))
    assert btn.icon(), \
            "The button() method must set the Button's icon."

