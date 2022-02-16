""" Implements PySide6.QtWidgets.QAbstractButton for use in a declarative UI design.
"""



# built-in
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

# pyside
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QAbstractButton as BaseQAbstractButton,
                               QWidget,
                               QPushButton)



class QAbstractButton(BaseQAbstractButton):
    """ Abstract base class for buttons.
    """



    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """ Returns an abstract button.
        """
        super().__init__(parent)



    @abstractmethod
    def setIcon(self, icon: QIcon) -> QAbstractButton:
        """ Set the icon of this button.
        """
        super().setIcon(icon)
        return self


    @abstractmethod
    def setText(self, text: str) -> QAbstractButton:
        """  Set the text of this button.
        """
        super().setText(text)
        return self
        

