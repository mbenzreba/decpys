""" Mimics the `PySide6.QtCore.Qt` namespace that defines miscellaneous values for Qt GUI
configuration.
"""



# built-in
from __future__ import annotations
from enum import Enum

# pyside
from PySide6.QtCore import Qt



class Alignment(Enum):
    """ Enumerates acceptable alignment values for Qt widgets and layouts.
    """


    @staticmethod
    def fromInt(value: int) -> Alignment:
        """ Returns the `Alignment` that corresponds to `value`.
        """
        conversion_dict = {
            0x0001  : Alignment.ALIGN_LEFT,
            0x0002  : Alignment.ALIGN_RIGHT,
            0x0004  : Alignment.ALIGN_HCENTER,
            0x0008  : Alignment.ALIGN_JUSTIFY,

            0x0020  : Alignment.ALIGN_TOP,
            0x0040  : Alignment.ALIGN_BOTTOM,
            0x0080  : Alignment.ALIGN_VCENTER,
            0x0100  : Alignment.ALIGN_BASELINE,

            0x0104  : Alignment.ALIGN_CENTER,

            0x0000  : Alignment.ALIGN_NONE
        }
        return conversion_dict[int(value)]



    @staticmethod
    def fromPyside(flag: Qt.Alignment) -> Alignment:
        """ Returns the `Alignment` for `flag`.
        """
        conversion_dict = {
            Qt.AlignLeft        : Alignment.ALIGN_LEFT,
            Qt.AlignRight       : Alignment.ALIGN_RIGHT,
            Qt.AlignHCenter     : Alignment.ALIGN_HCENTER,
            Qt.AlignJustify     : Alignment.ALIGN_JUSTIFY,

            Qt.AlignTop         : Alignment.ALIGN_TOP,
            Qt.AlignBottom      : Alignment.ALIGN_BOTTOM,
            Qt.AlignVCenter     : Alignment.ALIGN_VCENTER,
            Qt.AlignBaseline    : Alignment.ALIGN_BASELINE,

            Qt.AlignCenter      : Alignment.ALIGN_CENTER
        }
        return conversion_dict[flag]



    @staticmethod
    def toPyside(flag: Alignment) -> Qt.Alignment:
        """ Returns the PySide6 Qt object representation for `flag`. 
        """
        conversion_dict = {
            Alignment.ALIGN_LEFT      : Qt.AlignLeft,
            Alignment.ALIGN_RIGHT     : Qt.AlignRight,
            Alignment.ALIGN_HCENTER   : Qt.AlignHCenter,
            Alignment.ALIGN_JUSTIFY   : Qt.AlignJustify,

            Alignment.ALIGN_TOP       : Qt.AlignTop,
            Alignment.ALIGN_BOTTOM    : Qt.AlignBottom,
            Alignment.ALIGN_VCENTER   : Qt.AlignVCenter,
            Alignment.ALIGN_BASELINE  : Qt.AlignBaseline,

            Alignment.ALIGN_CENTER    : Qt.AlignCenter
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
