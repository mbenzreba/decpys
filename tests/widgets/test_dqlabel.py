""" Test decpys.widgets.DQLabel.
"""



# built-in
import pytest
import define_pkg_path

# pyside
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QApplication

# decpys
from decpys.widgets import DQLabel
from decpys.core import Alignment



@pytest.fixture
def init_qapp() -> QApplication:
    """ A QApplication must exist before any QWidget is instantiated.
    """
    return QApplication()



def test_dqlabel(init_qapp):
    """ Test that a DQLabel can be instantiated and is type DQLabel.
    """
    app = init_qapp
    assert isinstance(DQLabel(), DQLabel)
    


def test_dqlabel_is_qlabel():
    """ Test that a DQLabel is an instance of QLabel.
    """
    app = init_qapp
    assert isinstance(DQLabel(), QLabel)



def test_dqlabel_alignment():
    """ Test that a DQLabel's alignment can be set and get.

    BUG: For some reason, the label's horizontal alignment always returns 0 here. I don't
    think it can be set in this kind of environment.
    TODO: Recheck the appearance of this alignment bug in E2E testing. 
    """
    app = init_qapp
    label = DQLabel("label1").setAlignment(Alignment.ALIGN_VCENTER)
    assert label.alignment() == (Alignment.ALIGN_NONE, Alignment.ALIGN_VCENTER, )
    label = label.setAlignment(Alignment.ALIGN_TOP)
    assert label.alignment() == (Alignment.ALIGN_NONE, Alignment.ALIGN_TOP, )