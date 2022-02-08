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


.. py:method:: DQLabel.alignment()

    Returns the alignment of this widget contained in a 2-element tuple, where the first 
    element of the tuple is the horizontal alignment and the second is the vertical alignment.

    :return: A two-element tuple of Alignments, in the form (horizontal, vertical).
    :rtype: Tuple[Alignment, Alignment]
    

.. py:method:: DQLabel.setAlignment(alignment)

    Sets this label's alignment.

    :param alignment: Alignment enumeration.
    :type alignment: Alignment
    :return: This DQLabel after the ``setAlignment()`` mutation has been applied.
    :rtype: DQLabel


.. py:method:: DQLabel.setText(text)

    Sets this label's text.

    :param text: Plain text that the label should display.
    :type text: str
    :return: This DQLabel after the ``set_text`` mutation has been applied.
    :rtype: DQLabel