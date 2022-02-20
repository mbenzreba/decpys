# This script is needed to run pytests due to QApplication singleton bug.
# The QApplication cannot be torn down effectively after each test module is run in pytest, so a
# RuntimeError is thrown as soon as the second script is reached and attempts instantiation of a
# new application.

pytest tests/test_gui.py
pytest tests/test_widgets.py