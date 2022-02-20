""" Defines convenience functions for designing UIs in a programmatically declarative manner.
"""



# python
from typing import Union

# pyside
from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QIcon
)
from PySide6.QtWidgets import (
    QLabel,
    QPushButton
)



##################################
##          WIDGETS             ##
##################################



def qLabel(text: str = None,
        align: Qt.Alignment = None):
    """ Returns a QLabel.

    * text (str): text the label displays
    * align (Qt.Alignment): alignment flags
    """
    label = QLabel()

    if text:
        label.setText(text)

    if align:
        label.setAlignment(align)

    return label



def qPushButton(display: Union[str, QIcon] = None) -> QPushButton:
    """ Returns a QPushButton.

    * display (str | QIcon): text or icon to display on button
    """
    btn = QPushButton()

    if isinstance(display, str):
        btn.setText(display)
    elif isinstance(display, QIcon):
        btn.setIcon(display)

    return btn

