""" Import names needed by tests run in tests/widgets.
"""


import sys, os


decpys_pkg = os.path.join("..", "decpys")
decpys_widgets_pkg = os.path.join("..", "decpys", "widgets")

sys.path.append(decpys_pkg)
sys.path.append(decpys_widgets_pkg)