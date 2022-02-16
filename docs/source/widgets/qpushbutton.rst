QPushButton
============

``from decpys.widgets import QPushButton``

See the `official Qt documentation <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QPushButton.html>`_
for the functionality this class wraps.


Convenience functions
---------------------

``from decpys.widgets import qPushButton``

Use these convenience functions when you need to construct Classname within your UI.

.. py:function:: qPushButton(text: str = None, icon: QIcon = None)

    Returns an initialized ``QPushButton``.

    :param text: display text (mutually exclusive with parameter ``icon``)
    :type text: str or None
    :param icon: display icon (mutually exclusive with parameter ``text``)
    :type icon: QIcon or None
    :return: A ``QPushButton`` with initialized properties.
    :rtype: QPushButton


Methods
-------

.. py:method:: QPushButton.onClick(self, slot: Callable[..., Any])

    Hooks this widget's ``click`` signal to the ``slot``, a function of any type signature. When 
    the widget receives a click, ``slot`` will be called.

    :param slot: function to call when this widget is clicked
    :type slot: Callable
    :return: The current instance of ``QPushButton`` after the ``click`` slot is set.
    :rtype: QPushButton

