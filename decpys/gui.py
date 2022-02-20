""" Defines convenience functions for implementing graphical components in a Qt UI.
"""



# pyside
from PySide6.QtGui import (
    QIcon
)



##########################
##      GRAPHICS        ##
##########################



def qIcon(icon: str):
    """ Returns a QIcon.

    * icon (str): icon file name
    """
    return QIcon(icon)