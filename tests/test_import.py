""" Ensure that all imports work as intended from outside package development.
"""


# add package to path
import sys, os
decpys_pkg = os.path.join("..", "decpys")
decpys_widgets_pkg = os.path.join("..", "decpys", "widgets")

sys.path.append(decpys_pkg)
sys.path.append(decpys_widgets_pkg)


# test imports

# simple import
import decpys
import decpys.widgets

# module attribute import
from decpys.widgets import DQLabel

# all import
from decpys.widgets import *