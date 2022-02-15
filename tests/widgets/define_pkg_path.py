""" Import names needed by tests run in tests/widgets.
"""


import sys, os


decpys_pkg = os.path.join("..", "decpys")
decpys_core_pkg = os.path.join("..", "decpys", "core")
decpys_gui_pkg = os.path.join("..", "decpys", "gui")
decpys_widgets_pkg = os.path.join("..", "decpys", "widgets")

sys.path.append(decpys_pkg)
sys.path.append(decpys_core_pkg)
sys.path.append(decpys_gui_pkg)
sys.path.append(decpys_widgets_pkg)