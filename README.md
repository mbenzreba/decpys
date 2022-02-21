# Declarative PySide6

`decpys` (or **Dec**-larative **PyS**-ide) is a Python library that acts as a thin wrapper around
the original [PySide6](https://pypi.org/project/PySide6/) to enable super-fast GUI prototyping
using modern declarative UI techniques completely within Python. `decpys` is licensed under 
[GPLv2](./LICENSE.txt).



## Installation

`decpys` is available through PyPI. From the command-line, simply:

```
pip install decpys
```



## Design

`decpys` is inspired by UI frameworks like React and Flutter. `decpys` extends the popular 
`PySide6` Qt library so that Qt widgets can be used in a intuitive, concise manner to build out
declarative-style UI blocks completely within python.

Normally, Qt is used to build UIs in an imperative manner. This means that each widget and its
properties must be set, step-by-step. This might look familiar to you:

```python
window = QMainWindow()
widget = QWidget()
label = QLabel()
label.setText("a label")
layout = QVBoxLayout()
layout.addWidget(label)
widget.setLayout(layout)
window.setCentralWidget(widget)
window.setWindowTitle("a window")
```

It's cumbersome. Qt introduced [QML](https://doc.qt.io/qt-5/qtqml-index.html "a primer on QML in C++")
a while back, but that introduces a new syntax and file format to learn. Tools also have to be made
in IDEs/editors to give users the speed they seek developing.

Let's take a look at the last example, this time written using `decpys`:

```python
window = qMainWindow(
    title="a window",
    centralWidget=qWidget(
        layout=qVBoxLayout(
            children=[
                qLabel(
                    text="a label"
                )
            ]
        )
    )
)
```

Indents lend themselves well to visualizing widget hierarchy. Python's keyword arguments (and many 
IDEs' support for type hinting) help the user find relevant properties. If you've ever used a
declarative-UI framework, you know the benefits it brings to productivity and readable code.

See the [ClickableButton example](https://github.com/mbenzreba/decpys/blob/master/examples/ClickableButton/main.py) 
for a more involved look at how `decpys` can be used.