""" Test decpys.widgets.DQLabel.
"""


import define_pkg_path
from decpys.widgets import DQLabel


def test_dqlabel():
    assert isinstance(DQLabel(), DQLabel)