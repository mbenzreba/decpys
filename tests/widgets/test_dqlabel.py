""" Test decpys.widgets.DQLabel.
"""


import define_pkg_path
from PySide6.QtWidgets import QLabel
from decpys.widgets import DQLabel


def test_dqlabel():
    assert isinstance(DQLabel(), DQLabel)
    assert isinstance(DQLabel(), QLabel)