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
    align = None,
    layout = None)

    Returns a `QLabel <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLabel.html>`_.

    :param text: display text
    :type text: str
    :param align: horizontal and vertical alignment flags bitwise OR'd together
    :type align: `PySide6.QtCore.Qt.Alignment <https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html?highlight=alignment#PySide6.QtCore.PySide6.QtCore.Qt.AlignmentFlag>`_
    :param layout: layout containing the children of this widget
    :type layout: `QLayout <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLayout.html>`_


.. py:function:: qPushButton(
    display = None,
    layout = None)

    Returns a `QPushButton <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QPushButton.html>`_.

    :param display: display text/icon
    :type display: str | `PySide6.QtGui.QIcon <https://doc.qt.io/qtforpython/PySide6/QtGui/QIcon.html>`_
    :param layout: layout containing the children of this widget
    :type layout: `QLayout <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLayout.html>`_


.. py:function:: qVBoxLayout(
    children)

    Returns a `QVBoxLayout <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QVBoxLayout.html>`_.

    :param children: widgets placed inside this layout, order-sensitive
    :type children: `QWidget <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html>`_

