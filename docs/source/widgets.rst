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


.. py:function:: qMainWindow(
    title,
    centralWidget)

    Returns a `QMainWindow <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMainWindow.html>`_.

    :param title: window title
    :type title: str
    :param centralWidget: the central widget of this window
    :type centralWidget: `QWidget <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html>`_


.. py:function:: qPushButton(
    display = None,
    slots = None,
    layout = None)

    Returns a `QPushButton <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QPushButton.html>`_.

    :param display: display text/icon
    :type display: str | `QIcon <https://doc.qt.io/qtforpython/PySide6/QtGui/QIcon.html>`_
    :param slots: a list of this widget's signals and the corresponding slots to emit those signals to
    :type slots: list[Tuple[SignalType, Callable[..., Any]]]
    :param layout: layout containing the children of this widget
    :type layout: `QLayout <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLayout.html>`_


.. py:function:: qVBoxLayout(
    children)

    Returns a `QVBoxLayout <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QVBoxLayout.html>`_.

    :param children: widgets placed inside this layout, order-sensitive
    :type children: list[`QWidget <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html>`_]


.. py:function:: qWidget(
    layout)

    Returns a `QWidget <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html>`_.

    :param layout: layout containing the children of this widget
    :type layout: `QLayout <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLayout.html>`_
