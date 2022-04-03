""" Defines convenience functions for designing UIs in a programmatically declarative manner.
"""



# python
from typing import Tuple, Union, Callable, Any

# pyside
from PySide6.QtCore import (
    Qt, 
    QObject
)
from PySide6.QtGui import (
    QIcon
)
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel, QLayout,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget
)

# decpys
from decpys.cascade import (
    QLayoutCascader,
    QWidgetCascader
)
from decpys.types import SignalType



##################################
##          WIDGETS             ##
##################################



def qHBoxLayout(
        children: list[QWidget]
    ) -> QHBoxLayout:
    """ Returns a QHBoxLayout.

    * children (list[QWidget]): widgets placed inside this layout, order-sensitive
    """
    layout = QLayoutCascader(QHBoxLayout())
    return layout.setChildren(children) \
                 .getLayout()



def qLabel(
        text: str = None,
        align: Qt.Alignment = None,
        layout: QLayout = None
    ) -> QLabel:
    """ Returns a QLabel.

    * text (str): text the label displays
    * align (Qt.Alignment): alignment flags
    * layout (QLayout): layout containing children of this widget
    """
    label = QWidgetCascader(QLabel())
    return label.setText(text) \
                .setAlignment(align) \
                .setLayout(layout) \
                .getWidget()



def qMainWindow(
        title: str,
        centralWidget: QWidget
    ) -> QMainWindow:
    """ Returns a QMainWindow.

    * centralWidget (QWidget): the central widget of this window
    """
    window = QMainWindow()
    window.setWindowTitle(title)
    window.setCentralWidget(centralWidget)
    return window



def qPushButton(
        display: Union[str, QIcon] = None,
        slots: list[Tuple[SignalType, Callable[..., Any]]] = None,
        layout: QLayout = None,
    ) -> QPushButton:
    """ Returns a QPushButton.

    * display (str | QIcon): text or icon to display on button
    * slots (list of (SignalType, Callable[..., Any]) tuples): a list of this widget's signals 
    and the corresponding slots to emit those signals to
    * layout (QLayout): layout containing children of this widget
    """
    btn = QWidgetCascader(QPushButton())
    return btn.setTextOrIcon(display) \
              .setSlots(slots) \
              .setLayout(layout) \
              .getWidget()



def qRadioButton(
        display: Union[str, QIcon] = None,
        slots: list[Tuple[SignalType, Callable[..., Any]]] = None
    ) -> QRadioButton:
    """ Returns a `QRadioButton`.

    * display (str | QIcon): text or icon to display on button
    * slots (list of (SignalType, Callable[..., Any]) tuples): a list of this widget's signals 
    and the corresponding slots to emit those signals to
    """
    btn = QWidgetCascader(QRadioButton())
    return btn.setTextOrIcon(display) \
              .setSlots(slots) \
              .getWidget()
              


def qVBoxLayout(
        children: list[QWidget]
    ) -> QVBoxLayout:
    """ Returns a QVBoxLayout.

    * children (list[QWidget]): widgets placed inside this layout, order-sensitive
    """
    layout = QLayoutCascader(QVBoxLayout())
    return layout.setChildren(children) \
                 .getLayout()



def qWidget(
        layout: QLayout
    ) -> QWidget:
    """ Returns a QWidget.

    * layout (QLayout): layout containing children of this widget
    """
    widget = QWidget()
    widget.setLayout(layout)
    return widget


