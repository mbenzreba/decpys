QIcon
=======

``from decpys.gui import QIcon``

See the `official Qt documentation <https://doc.qt.io/qtforpython/PySide6/QtGui/QIcon.html>`_
for the GUI asset this class extends.


Methods
-------

.. py:class:: QIcon(self, iconFile=None)

   Returns a QIcon for use in graphical Qt applications.

   Note that the complete path to the icon file image does not need to be passed during ``QIcon``
   construction. ``QIcon`` keeps an internal list of directories to search for an icon file.
   Currently, these directories are ``.`` and ``./icons``, where the current working directory
   is the directory from which the python interpreter is executed.

   :param iconFile: Name of icon image file.
   :type iconFile: str or None
   :rtype: QIcon


.. py:method:: QIcon.isValid(self)

    Returns True if the icon is associated with a valid icon file, pixmap, etc.

    :return: True if the QIcon called has an associated graphic, False otherwise.
    :rtype: Boolean
    