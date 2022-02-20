""" Defines convenience functions for designing UIs in a programmatically declarative manner.
"""



# python
from typing import Union

# pyside
from PySide6.QtCore import (
    Qt, 
    QObject
)
from PySide6.QtGui import (
    QIcon
)
from PySide6.QtWidgets import (
    QLabel, QLayout,
    QPushButton,
    QVBoxLayout,
    QWidget
)



##################################
##          WIDGETS             ##
##################################



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
    label = QLabel()

    if text:
        label.setText(text)

    if align:
        label.setAlignment(align)

    if layout:
        label.setLayout(layout)

    return label



def qPushButton(
        display: Union[str, QIcon] = None,
        layout: QLayout = None,
    ) -> QPushButton:
    """ Returns a QPushButton.

    * display (str | QIcon): text or icon to display on button
    * layout (QLayout): layout containing children of this widget
    """
    btn = QPushButton()

    if isinstance(display, str):
        btn.setText(display)
    elif isinstance(display, QIcon):
        btn.setIcon(display)

    if layout:
        btn.setLayout(layout)
    
    return btn



def qVBoxLayout(
        children: list[QWidget]
    ) -> QVBoxLayout:
    """ Returns a QVBoxLayout.

    * children (list[QWidget]): widgets placed inside this layout, order-sensitive
    """
    layout = QVBoxLayout()

    for child in children:
        layout.addWidget(child)

    return layout



def qWidget(
        layout: QLayout
    ) -> QWidget:
    """ Returns a QWidget.

    * layout (QLayout): layout containing children of this widget
    """
    widget = QWidget()
    widget.setLayout(layout)
    return widget


