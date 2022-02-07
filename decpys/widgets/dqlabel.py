""" Wrapper classfor PySide6.QtWidgets.QLabel.
"""


from __future__ import annotations
from PySide6.QtWidgets import QLabel


class DQLabel(QLabel):


    def __init__(self, text: str = None):
        """ Returns a QLabel wrapper for displaying text, movies, images, etc.
        """
        if text:
            super(text)
        else:
            super()


    def set_alignment(self, alignment: int) -> DQLabel:
        """ Sets this label's alignment using alignment flags from PySide6.
        """
        self.setAlignment(alignment)
        return self


    def set_text(self, text: str) -> DQLabel:
        """ Sets this label's text.
        """
        self.setText(text)
        return self