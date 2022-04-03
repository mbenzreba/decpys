# Standards for the `decpys` library

The way development is set up for `decpys` widgets right now (with the use of a cascader to streamline
initialization), a lot of duplication of comments and cascader method calls occurs. These snippets
here maintain a standard that all widgets should assume for their implementation and documentation.


## Documentation

For widgets that inherit from **`QWidget`**:

```python
def qThing(
        title: str = None,
        text: str = None,
        display: Union[str, QIcon] = None,
        align: Qt.Alignment = None,
        slots: list[Tuple[SignalType, Callable[..., Any]]] = None,
        layout: QLayout = None
    ) -> QThing:
    """ Returns a `QThing`.

    * title (str): display caption for windows
    * text (str): display text
    * display (str | QIcon): text or icon to display on button
    * align (Qt.Alignment): alignment flags
    * slots (list of (SignalType, Callable[..., Any]) tuples): a list of this widget's signals 
    and the corresponding slots to emit those signals to
    * layout (QLayout): layout containing children of this widget
    """
    widget = QWidgetCascader(QThing())
    return widget.setTitle(title)           \
                 .setText(text)             \
                 .setTextOrIcon(display)    \
                 .setAlignment(align)       \
                 .setSlots(slots)           \
                 .setLayout(layout)         \
                 .getWidget()
```

And their matching RST documentation:

```
.. py:function:: qThing(
    title: str = None,
    text: str = None,
    display = None,
    align = None,
    slots = None,
    layout = None)

    Returns a `QThing <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QThing.html>`_.

    :param title: display caption for windows
    :type title: str
    :param text: display text
    :type text: str
    :param display: display text/icon
    :type display: str | `QIcon <https://doc.qt.io/qtforpython/PySide6/QtGui/QIcon.html>`_
    :param align: horizontal and vertical alignment flags bitwise OR'd together
    :type align: `PySide6.QtCore.Qt.Alignment <https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html?highlight=alignment#PySide6.QtCore.PySide6.QtCore.Qt.AlignmentFlag>`_
    :param slots: a list of this widget's signals and the corresponding slots to emit those signals to
    :type slots: list[Tuple[SignalType, Callable[..., Any]]]
    :param layout: layout containing the children of this widget
    :type layout: `QLayout <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLayout.html>`_
```

For widgets that inherit from **`QLayout`**:

```python
def qThing(
        children: list[QWidget]
    ) -> QThing:
    """ Returns a `QThing`.

    * children (list[QWidget]): widgets placed inside this layout, order-sensitive
    """
    layout = QLayoutCascader(QThing())
    return layout.setChildren(children)     \
                 .getLayout()
```

And their matching RST documentation:

```
.. py:function:: qThing(
    children)

    Returns a `QThing <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QThing.html>`_.

    :param children: widgets placed inside this layout, order-sensitive
    :type children: list[`QWidget <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html>`_]
```




