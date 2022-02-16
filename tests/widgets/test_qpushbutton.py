""" Unit test decpys.widgets.QPushButton.
"""



#built-in
from __future__ import annotations
from typing import Any, Callable

# pytest
import pytest

# setup
import define_pkg_path
from fixtures import init_qapp

# pyside
from PySide6.QtCore import Qt
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QPushButton as BaseQPushButton

# decpys
from decpys.widgets import QPushButton, qPushButton



######################
##      SETUP       ##
######################



value = 0

class Button(QPushButton):

    def __init__(self):
        super().__init__()

def onClick_slot():
    global value
    value += 1



##########################
##      UNIT TESTS      ##
##########################



def test_qpushbutton(init_qapp):
    """ Assert that a QPushButton registers as a type of its base class.
    """
    btn = QPushButton()
    assert isinstance(btn, BaseQPushButton), \
        "The derived QPushButton must register as type PySide6.QtWidgets.QPushButton."



def test_onClick(init_qapp):
    """ Assert that a QPushButton registers a click signal.
    """
    btn = Button()
    btn.onClick(onClick_slot)
    QTest.mouseClick(btn, Qt.LeftButton)
    assert value == 1, \
        "The Button must call its assigned slot when it is clicked."



def test_qpushbutton_function(init_qapp):
    """ Assert that a QPushButton is returned by the qPushButton() convenience function.
    """
    btn = qPushButton(text="original") \
            .onClick(onClick_slot)
    QTest.mouseClick(btn, Qt.LeftButton)
    assert btn.text() == "original", \
        "The QPushButton must have its text property set by qPushButton()."
    assert value == 2, \
        "The QPushButton must have the ability to be modified after it returns from qPushButton()."


