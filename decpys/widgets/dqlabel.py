""" Wrapper classfor PySide6.QtWidgets.QLabel.
"""



# built-in
from __future__ import annotations
from typing import Tuple

# base
from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt

# decpys
from decpys.core import Alignment



class DQLabel(QLabel):
    """ Used to show text, movies, pictures. etc. as a label.
    """



    def __init__(self, text: str = None):
        """ Returns a QLabel wrapper for displaying text, movies, images, etc.
        """
        super().__init__(text)



    def alignment(self) -> Tuple[Alignment, Alignment]:
        """ Returns the alignment of this widget contained in a 2-element tuple, where the first 
        element of the tuple is the horizontal alignment and the second is the vertical alignment.
        """
        return (Alignment.from_int(super().alignment() & Qt.AlignHorizontal_Mask), 
                Alignment.from_int(super().alignment() & Qt.AlignVertical_Mask))



    def setAlignment(self, alignment: Alignment) -> DQLabel:
        """ Sets this label's alignment.
        """
        super().setAlignment(Qt.Alignment(alignment.value))
        return self



    def setText(self, text: str) -> DQLabel:
        """ Sets this label's text.
        """
        super().setText(text)
        return self
    