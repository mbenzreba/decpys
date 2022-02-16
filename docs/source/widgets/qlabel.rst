QLabel
=======

``from decpys.widgets import QLabel``

See the `official Qt documentation <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLabel.html>`_
for the widget this class wraps.


Convenience functions
---------------------

Use these convenience functions when you need to construct QLabel within your UI.

.. py:function:: qLabel(text = None,
    halign = None,
    valign = None)

    Returns a QLabel.

    :param text: Text label.
    :type text: str or None
    :param halign: Horizontal alignment.
    :type halign: Alignment or None
    :param valign: Vertical alignment
    :type valign: Alignment or None
    :rtype: QLabel


Methods
-------

.. py:class:: QLabel(text=None)

   Returns a QLabel wrapper for displaying text, movies, images, etc.

   :param text: Text label.
   :type kind: str or None
   :rtype: QLabel


.. py:method:: QLabel.alignment()

    Returns the alignment of this widget contained in a 2-element tuple, where the first 
    element of the tuple is the horizontal alignment and the second is the vertical alignment.

    :return: A two-element tuple of Alignments, in the form (horizontal, vertical).
    :rtype: Tuple[Alignment, Alignment]
    

.. py:method:: QLabel.setAlignment(alignment)

    Sets this label's alignment.

    :param alignment: Alignment enumeration.
    :type alignment: Alignment
    :return: This QLabel after the ``setAlignment()`` mutation has been applied.
    :rtype: QLabel


.. py:method:: QLabel.setText(text)

    Sets this label's text.

    :param text: Plain text that the label should display.
    :type text: str
    :return: This QLabel after the ``set_text`` mutation has been applied.
    :rtype: QLabel