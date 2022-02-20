Widgets
=======

``from decpys.widgets import *``

Defines widgets for display in a Qt application.

See the `official Qt documentation <https://doc.qt.io/qtforpython/PySide6/QtWidgets/index.html>`_
for an index of all widgets this package wraps.



Initializer Functions
---------------------

Use these initialization functions to create and return the widgets your UI needs.


.. py:function:: qLabel(
    text = None,
    align = None)

    Returns a `QLabel <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLabel.html>`_.

    :param text: display text
    :type text: str
    :param align: horizontal and vertical alignment flags bitwise OR'd together
    :type align: `PySide6.QtCore.Qt.Alignment <https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html?highlight=alignment#PySide6.QtCore.PySide6.QtCore.Qt.AlignmentFlag>`_


.. py:function:: qPushButton(
    display = None)

    Returns a `QPushButton <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QPushButton.html>`_.

    :param display: display text/icon
    :type display: str | `PySide6.QtGui.QIcon <https://doc.qt.io/qtforpython/PySide6/QtGui/QIcon.html>`_


