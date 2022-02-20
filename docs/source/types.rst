Types
=====

``from decpys.types import *``

Defines types needed by the package to make sure the declarative programming paradigm can work 
within Python.


Signals
-------

Signals and slots are how the Qt framework registers basic events. Widgets can define and emit
their own signals, while slots are those functions that are hooked up to listen for certain signals
and react appropriately. `Qt provides a good introduction to their "signals and slots" system if
you are still unsure how they might work <https://doc.qt.io/qt-5/signalsandslots.html>`_.

In ``decpys``, common Qt signals are defined in their own enum called ``SignalType``. Functions
like ``onClick()`` or ``onPress()`` are later defined to return a particular ``SignalType`` value
so that the syntax to the UI designer is as clean and familiar as possible.

Take, for example:

.. code-block:: python

    someWidget(
        slots = [
            (onClick(), doSomethingAfterClick)
        ]
    )

``someWidget`` is passed a list of tuples to its keyword argument ``slots``, where the first
element of the tuple is a function that returns a ``SignalType``, and the second element of the
tuple is the name of a callable function.


.. py:class:: SignalType

    Inherits from python's built-in `Enum <https://docs.python.org/3/library/enum.html#enum.Enum>`_ 
    type. Enumerates names for signals that Qt objects can emit.

    .. py:attribute:: CLICKED
        
        Named value for the common Qt signal ``clicked``.


.. py:function:: onClick()

    Returns ``SignalType.CLICKED``.

    :rtype: SignalType
