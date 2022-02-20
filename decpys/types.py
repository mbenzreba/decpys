""" Defines types needed by decpys to use Qt in a declarative manner.
"""



# python
from enum import Enum



class SignalType(Enum):
    """ Enumerates Qt signal names so that all signals are in one easily-accessible place. It is
    still up to initializer functions to implement these signals in a consistent manner.
    """
    CLICKED = 1


def onClick() -> SignalType:
    """
    """
    return SignalType.CLICKED