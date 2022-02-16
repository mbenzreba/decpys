""" Wrapper for PySide6.QtWidgets.QPushButton.
"""



# built-in
from __future__ import annotations
from typing import Any, Callable

# pyside
from PySide6.QtGui import (
    QIcon as BaseQIcon,
    QPixmap as BaseQPixmap
)
from PySide6.QtWidgets import QPushButton as BaseQPushButton

#decpys
from decpys.core import Alignment
from decpys.gui import QIcon



##################
##  EXTENSION   ##
##################



class QPushButton(BaseQPushButton):
    """ Simple push button.
    """



    def __init__(self):
        """ Returns a QPushButton.
        """
        super().__init__()



    def onClick(self, slot: Callable[..., Any]) -> QPushButton:
        """ Connects a click signal to the function `slot`.
        """
        self.clicked.connect(slot)
        return self



######################################
##      CONVENIENCE FUNCTION        ##
######################################



def qPushButton(text: str = None,
                icon: QIcon = None) -> QPushButton:
    """ Returns a QPushButton.

    * text (str): display text (mutually exclusive with `icon`)
    * icon (QIcon): display icon (mutually exclusive with `text`)
    """
    btn = QPushButton()

    if text:
        btn.setText(text)
    elif icon:
        btn.setIcon(icon)

    return btn
