""" Defines decpys.gui.QIcon.
"""



# built-in
import os

# pyside
from PySide6.QtGui import QIcon as BaseQIcon



class QIcon(BaseQIcon):
    """ Used in conjunction with a widget to display a scalable icon.
    """



    # Paths to search for when setting an icon
    _iconFilePaths = [
        (".", ),
        ("icons", )
    ]



    def __init__(self, iconFile: str = None):
        """ Returns a QIcon for use in graphical Qt applications.
        """
        self._isValid = False

        if iconFile:
            pathToIcon = QIcon._findPathToIconFile(iconFile)
            if pathToIcon:
                super().__init__(pathToIcon)
                self._isValid = True
            else:
                super().__init__()


    def isValid(self):
        """ Returns True if the icon is associated with a valid icon file, pixmap, etc.
        """
        return self._isValid



    @staticmethod
    def _findPathToIconFile(iconFile: str) -> str:
        """ Returns the path to `iconFile` if it exists, None otherwise.
        """
        for path in QIcon._iconFilePaths:
            pathToIconFile = os.path.join(*path, iconFile)
            if os.path.exists(pathToIconFile):
                return pathToIconFile
        return None







