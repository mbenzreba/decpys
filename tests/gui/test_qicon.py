""" Unit testing decpys.gui.QIcon.
"""



# test
import pytest
from fixtures import init_qguiapp
import define_pkg_path

# pyside
from PySide6.QtGui import (QIcon as BaseQIcon,
                           QGuiApplication)

# decpys
from decpys.gui import QIcon



def test_qicon(init_qguiapp):
    """ Assert that a QIcon can be instantiated and registers as relevant types.
    """
    icon = QIcon()
    assert isinstance(icon, BaseQIcon), \
            "The icon is not an object of type PySide6.QtGui.QIcon."
    assert isinstance(icon, QIcon), \
            "The icon is not an object of type decpys.gui.QIcon"


def test_qicon_isValid(init_qguiapp):
    """ Assert that an icon initialized with an existing icon file is valid. Assert that, if the
    icon file used to instantiate the icon does not exist, than the icon is not valid.
    """
    icon = QIcon("tests\\gui\\icons\\check-underline.png")
    badIcon = QIcon("stinky-icon.png")
    assert icon.isValid(), \
            "Icon should have a valid icon file associated with it."
    assert not badIcon.isValid(), \
            "Icon should not have a valid icon file associated with it."