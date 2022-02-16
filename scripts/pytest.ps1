# This script is needed to run pytests due to QApplication singleton bug.
# The QApplication cannot be torn down effectively after each test module is run in pytest, so a
# RuntimeError is thrown as soon as the second script is reached and attempts instantiation of a
# new application.

pytest tests/core/test_qt.py
pytest tests/gui/test_qicon.py
pytest tests/widgets/test_qabstractbutton.py
pytest tests/widgets/test_qlabel.py
pytest tests/widgets/test_qpushbutton.py