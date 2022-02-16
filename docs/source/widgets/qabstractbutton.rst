QAbstractButton
===============

``from decpys.widgets import QAbstractButton``

See the `official Qt documentation <https://doc.qt.io/qtforpython/PySide6/QtWidgets/QAbstractButton.html>`_
for the widget this class wraps.


Methods
-------

.. py:class:: QAbstractButton(parent=None)

   Returns an abstract button. Instead of initializing this directly, ``QAbstractButton`` should
   be subclassed.

   :param parent: Parent widget to this button.
   :type parent: QWidget


.. py:method:: QAbstractButton.setIcon(icon)
    :abstractmethod:

    Set the icon of this button.

    :param icon: The icon to set this button's display to.
    :type icon: QIcon
    :return: This button, after the mutation has been processed.
    :rtype: QAbstractButton


.. py:method:: QAbstractButton.setText(text)

    Set the text of this button.

    :param text: The text to set this button's label to.
    :type text: str
    :return: This button, after the mutation has been processed.
    :rtype: QAbstractButton
    