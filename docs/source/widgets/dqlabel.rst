DQLabel
=======

``from decpys.widgets import DQLabel``

See the `official Qt documentation <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLabel.html>`_
for the widget this class wraps.


Methods
-------

.. py:class:: DQLabel(text=None)

   Returns a QLabel wrapper for displaying text, movies, images, etc.

   :param text: Text label.
   :type kind: str or None
   :rtype: DQLabel


.. py:method:: DQLabel.set_alignment(alignment)

    Sets this label's alignment using alignment flags from ``PySide6``.

    :param alignment: Qt Alignment flags in a single integer.
    :type alignment: int
    :return: This DQLabel after the ``set_alignment`` mutation has been applied.
    :rtype: DQLabel


.. py:method:: DQLabel.set_text(text)

    Sets this label's text.

    :param text: Plain text that the label should display.
    :type text: str
    :return: This DQLabel after the ``set_text`` mutation has been applied.
    :rtype: DQLabel