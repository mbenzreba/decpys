""" Import names needed by tests run in tests/gui.
"""



# built-in
import sys, os



#####################
#       SCRIPT      #
#####################



# paths to decpys packages and subpackages
decpys_pkg = os.path.join("..", "decpys")
decpys_core_pkg = os.path.join("..", "decpys", "core")
decpys_gui_pkg = os.path.join("..", "decpys", "gui")
decpys_widgets_pkg = os.path.join("..", "decpys", "widgets")

# append paths to system environment
sys.path.append(decpys_pkg)
sys.path.append(decpys_core_pkg)
sys.path.append(decpys_gui_pkg)
sys.path.append(decpys_widgets_pkg)