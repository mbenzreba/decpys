"""
"""



# python
from __future__ import annotations
from typing import Any, Union, Callable, Tuple

# pyside
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QLayout,
    QWidget
)

from decpys.types import SignalType



##############################
##          LAYOUT          ##
##############################



class QLayoutCascader:
    """ Used to provide cascading property mutation in decpys layout initializer functions.
    """



    def __init__(self, layout: QLayout):
        """ Initializes the cascader to wrap `layout`.

        * layout (QLayout): the layout to call cascading functions against
        """
        self._layout = layout



    def getLayout(self) -> QLayout:
        """ Returns the layout.
        """
        return self._layout



    def setChildren(self, children: list[QWidget]) -> QWidgetCascader:
        """ Returns the layout cascader after setting its children.

        * children (list[QWidget]): widgets contained by the layout
        """
        if children:
            for child in children:
                self._layout.addWidget(child)
        return self



##############################
##          WIDGET          ##
##############################



class QWidgetCascader:
    """ Used to provide cascading property mutation in decpys widget initializer functions.
    """



    def __init__(self, widget: QWidget):
        """ Initializes this cascader to 'wrap' parameter `widget`.

        * widget (QWidget): the widget to call cascading functions against
        """
        self._widget = widget



    def getWidget(self):
        """ Returns the widget.
        """
        return self._widget



    def setAlignment(self, align: Qt.Alignment = None) -> QWidgetCascader:
        """ Returns the widget cascader after setting its alignment.

        * align (Qt.Alignment): horizontal and vertical bit flags optionally OR'd together
        """
        if align:
            self._widget.setAlignment(align)
        return self



    def setLayout(self, layout: QLayout = None) -> QWidgetCascader:
        """ Returns the widget cascader after setting its layout.

        * layout (QLayout): layout
        """
        if layout:
            self._widget.setLayout(layout)
        return self



    def setSlots(self, slots: list[Tuple[SignalType, Callable[..., Any]]]) -> QWidgetCascader:
        """ Returns the widget cascader after setting slots to its signals.

        * slots (list of (SignalType, Callable[..., Any]) tuples): a list of this widget's signals 
        and the corresponding slots to emit those signals to
        """
        if slots:
            for slot in slots:
                signal = slot[0]
                try:
                    if signal == SignalType.CLICKED:
                        self._widget.clicked.connect(slot[1])
                except TypeError:
                    pass
        return self



    def setText(self, text: str = None) -> QWidgetCascader:
        """ Returns the widget cascader after setting its display text.

        * text (str): display text
        """
        if text:
            self._widget.setText(text)
        return self

        

    def setTextOrIcon(self, value: Union[str, QIcon] = None) -> QWidgetCascader:
        """ Returns the widget cascader after setting its display text or icon.

        * value (str | QIcon): display of the widget
        """
        if value:
            if isinstance(value, str):
                self._widget.setText(value)
            elif isinstance(value, QIcon):
                self._widget.setIcon(value)
        return self



    


    
