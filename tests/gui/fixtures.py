""" Fixtures needed by tests in tests/gui.
"""



# pytest
import pytest

# pyside
from PySide6.QtGui import QGuiApplication



@pytest.fixture(scope="session")
def init_qguiapp():
    """ Initialize the Qt application so that GUI objcts can exist.
    """
    app = QGuiApplication()
    yield app