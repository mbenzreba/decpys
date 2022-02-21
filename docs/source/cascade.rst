Cascaders
=========

``from decpys.cascade import *``

Defines classes needed to simplify widget instantiation in ``decpys.widgets``.

The cascaders listed here can be extended in applications to provide even more helper methods that
streamline the creation of custom widgets using initializer functions.


Layout Cascader
---------------

.. py:class:: QLayoutCascader(layout)

    Initializes a cascader to wrap the layout parameter.

    :param layout: the layout to call cascading functions against.
    :type layout: `QLayout <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLayout.html>`_


    .. py:method:: getLayout()

        Returns the layout managed by this cascader.

        :rtype: `QLayout <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLayout.html>`_

    .. py:method:: setChildren(children)

        Returns the layout cascader after setting its children.

        :param children: widgets to be contained by the layout
        :type children: list[list of `QWidget <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html>`_]
        :rtype: QLayoutCascader



Widget Cascader
---------------


.. py:class:: QWidgetCascader(widget)

    Initializes a cascader to wrap the widget parameter.

    :param widget: the widget to call cascading functions against
    :type widget: `QWidget <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html>`_


    .. py:method:: getWidget()

        Returns the widget managed by this cascader.

        :rtype: `QWidget <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html>`_

    .. py:method::setAlignment(align)

        Returns the widget cascader after setting its alignment.

        :param align: horizontal and vertical bit flags OR'd together
        :type align: `Qt.Alignment <https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html?highlight=alignment#PySide6.QtCore.PySide6.QtCore.Qt.AlignmentFlag>`_
        :rtype: QWidgetCascader

    .. py:method:: setLayout(layout)

        Returns the widget cascader after settings its layout.

        :param layout: layout
        :type layout: `QLayout <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLayout.html>`_
        :rtype: QWidgetCascader

    .. py:method::setSlots(slots)

        Returns the widget cascader after setting slots to its signals.

        :param slots: a list of this widget's signals and the corresponding slots to emit those 
        signals to
        :type slot: list[Tuple[SignalType, Callable[..., Any]]]
        :rtype: QWidgetCascader

    .. py:method:: setText(text)

        Returns the widget cascader after settings its display text.

        :param text: display text
        :type text: str
        :rtype: QWidgetCascader

    .. py:method:: setTextOrIcon(value)

        Returns the widget cascader after setting its display text or icon.

        :param value: display of the widget
        :type value: str | str | `QIcon <https://doc.qt.io/qtforpython/PySide6/QtGui/QIcon.html>`_
        :rtype: QWidgetCascader

    
