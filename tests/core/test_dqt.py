""" Test the decpys.core.dqt module.
"""



# built-in
import pytest
import define_pkg_path

# pyside
from PySide6.QtCore import Qt

# decpys
from decpys.core import Alignment



#########################
#       Alignment       #
#########################



def test_alignment():
    """ Assert that an alignment setting registers as an Alignment object.
    """
    alignment = Alignment.ALIGN_BOTTOM
    assert isinstance(alignment, Alignment), \
            "Initialized object is not of type Alignment"


def test_alignment_from_int():
    """ Assert that an Alignment can be made from an integer value.
    """
    alignment = Alignment.fromInt(1)
    assert isinstance(alignment, Alignment), \
            "Object converted from integer is not of type Alignment."
    assert alignment == Alignment.ALIGN_LEFT, \
            "Object converted from integer is not the correct Alignment value."


def test_alignment_from_pyside():
    """ Assert that an Alignment can be made from corresponding PySide6.QtCore.Qt.AlignmentFlag 
    values.
    """
    alignment = Alignment.fromPyside(Qt.AlignmentFlag.AlignBottom)
    assert isinstance(alignment, Alignment), \
            "Object converted from PySide is not of type Alignment."
    assert alignment == Alignment.ALIGN_BOTTOM, \
            "Object converted from PySide is not the correct Alignment value."


def test_alignment_to_pyside():
    """ Assert that an Alignment can be converted to its corresponding PySide6.QtCore.Qt.AlignmentFlag
    value.
    """
    alignment = Alignment.toPyside(Alignment.ALIGN_LEFT)
    assert isinstance(alignment, Qt.AlignmentFlag), \
            "Object converted to Qt is not of type AlignmentFlag."
    assert alignment == Qt.AlignmentFlag.AlignLeft, \
            "Object converted to Qt is not the correct AlignmentFlag value."