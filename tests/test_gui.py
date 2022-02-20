""" Unit test decpys.gui.
"""



# python
import os

# package path
import define_pkg_path

# pytest
from fixtures import init_qguiapp

# pyside
from PySide6.QtGui import (
    QIcon
)

# decpys
from decpys.gui import (
    qIcon
)



##################
##  UNIT TESTS  ##
##################



def test_qicon(init_qguiapp):
    """ Assert that qIcon() initializes and returns a proper QIcon.
    """
    icon = qIcon(os.path.join(".", "tests", "icons", "check-underline.png"))
    assert isinstance(icon, QIcon), \
        "qIcon() must return an object of type QIcon."
    assert not icon.isNull(), \
        "The icon must not register as null when initialized with a valid file."
