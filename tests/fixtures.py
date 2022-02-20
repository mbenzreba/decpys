""" Defines pytest fixtures for use in pytest modules.
"""



# pytest
import pytest

# pyside
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication



@pytest.fixture(scope="session")
def init_qapp():
    """ Yields a QApplication so that QWidgets can exist.
    """
    app = QApplication()
    yield app
    app.exit()



@pytest.fixture(scope="session")
def init_qguiapp():
    """ Yields a QGuiApplication so that graphical Qt components can exist.
    """
    guiapp = QGuiApplication()
    yield guiapp
    guiapp.exit()

