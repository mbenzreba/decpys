""" Mimics the `PySide6.QtCore.Qt` namespace that defines miscellaneous values for Qt GUI
configuration.
"""



# built-in
from __future__ import annotations
from enum import Enum

# pyside
from PySide6.QtCore import Qt



class AlignmentFlag(Enum):
    """ Enumerates acceptable alignment values for Qt widgets and layouts.
    """


    def from_int(value: int) -> AlignmentFlag:
        """ Returns the `AlignmentFlag` that corresponds to `value`.
        """
        conversion_dict = {
            0x0001  : AlignmentFlag.ALIGN_LEFT,
            0x0002  : AlignmentFlag.ALIGN_RIGHT,
            0x0004  : AlignmentFlag.ALIGN_HCENTER,
            0x0008  : AlignmentFlag.ALIGN_JUSTIFY,

            0x0020  : AlignmentFlag.ALIGN_TOP,
            0x0040  : AlignmentFlag.ALIGN_BOTTOM,
            0x0080  : AlignmentFlag.ALIGN_VCENTER,
            0x0100  : AlignmentFlag.ALIGN_BASELINE,

            0x0104  : AlignmentFlag.ALIGN_CENTER,

            0x0000  : AlignmentFlag.ALIGN_NONE
        }
        return conversion_dict[int(value)]



    def from_pyside(flag: Qt.AlignmentFlag) -> AlignmentFlag:
        """ Returns the `AlignmentFlag` for `flag`.
        """
        conversion_dict = {
            Qt.AlignLeft        : AlignmentFlag.ALIGN_LEFT,
            Qt.AlignRight       : AlignmentFlag.ALIGN_RIGHT,
            Qt.AlignHCenter     : AlignmentFlag.ALIGN_HCENTER,
            Qt.AlignJustify     : AlignmentFlag.ALIGN_JUSTIFY,

            Qt.AlignTop         : AlignmentFlag.ALIGN_TOP,
            Qt.AlignBottom      : AlignmentFlag.ALIGN_BOTTOM,
            Qt.AlignVCenter     : AlignmentFlag.ALIGN_VCENTER,
            Qt.AlignBaseline    : AlignmentFlag.ALIGN_BASELINE,

            Qt.AlignCenter      : AlignmentFlag.ALIGN_CENTER
        }
        return conversion_dict[flag]



    def to_pyside(flag: AlignmentFlag) -> Qt.AlignmentFlag:
        """ Returns the PySide6 Qt object representation for `flag`. 
        """
        conversion_dict = {
            AlignmentFlag.ALIGN_LEFT      : Qt.AlignLeft,
            AlignmentFlag.ALIGN_RIGHT     : Qt.AlignRight,
            AlignmentFlag.ALIGN_HCENTER   : Qt.AlignHCenter,
            AlignmentFlag.ALIGN_JUSTIFY   : Qt.AlignJustify,

            AlignmentFlag.ALIGN_TOP       : Qt.AlignTop,
            AlignmentFlag.ALIGN_BOTTOM    : Qt.AlignBottom,
            AlignmentFlag.ALIGN_VCENTER   : Qt.AlignVCenter,
            AlignmentFlag.ALIGN_BASELINE  : Qt.AlignBaseline,

            AlignmentFlag.ALIGN_CENTER    : Qt.AlignCenter
        }
        return conversion_dict[flag]



    # values

    # horizontal
    ALIGN_LEFT      = Qt.AlignLeft
    ALIGN_RIGHT     = Qt.AlignRight
    ALIGN_HCENTER   = Qt.AlignHCenter
    ALIGN_JUSTIFY   = Qt.AlignJustify

    # vertical
    ALIGN_TOP       = Qt.AlignTop
    ALIGN_BOTTOM    = Qt.AlignBottom
    ALIGN_VCENTER   = Qt.AlignVCenter
    ALIGN_BASELINE  = Qt.AlignBaseline

    # horizontal & vertical
    ALIGN_CENTER    = Qt.AlignCenter

    # error
    ALIGN_NONE      = 0
