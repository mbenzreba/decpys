""" Defines pytest fixtures for use in pytest modules.
"""


import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="session")
def init_qapp():
    """ Yields a QApplication so that QWidgets can exist.
    """
    app = QApplication()
    yield app
    app.exit()

