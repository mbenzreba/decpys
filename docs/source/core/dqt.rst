Qt
===

``from decpys.core import *``

See the `official Qt documentation <https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html>`_
for the functionality this submodule mimics.


Alignment
---------

.. py:class:: Alignment

    Enumerates alignments that can be used in widgets' ``alignment``, ``setAlignment``, and other
    related methods.

    Enumerated values:

    * ALIGN_LEFT
    * ALIGN_RIGHT
    * ALIGN_HCENTER
    * ALIGN_JUSTIFY
    * ALIGN_TOP
    * ALIGN_BOTTOM
    * ALIGN_VCENTER
    * ALIGN_BASELINE
    * ALIGN_CENTER
    * ALIGN_NONE

.. py:method:: Alignment.fromInt(value)
    :staticmethod:

    Returns the ``Alignment`` that corresponds to ``value``.

    :param value: Integer value representing a single ``Alignment`` flag (enumerated above).
    :param kind: int
    :return: The ``Alignment`` that corresponds to ``value``, or ``Alignment.ALIGN_NONE`` if the
        value could not be matched, or if the value is a combination of flags.
    :rtype: Alignment

.. py:method:: Alignment.fromPyside(flag)
    :staticmethod:

    Returns the ``decpys`` implementation for a ``Qt.Alignment`` object.

    :param flag: A flag used by the Qt toolkit to determine widget/layout alignment.
    :param kind: Qt.Alignment
    :return: The ``Alignment`` that corresponds to ``flag``.
    :rtype: Alignment

.. py:method:: Alignment.toPyside(flag)
    :staticmethod:

    Returns the PySide6 Qt object representation for ``flag``.

    :param flag: An ``Alignment``.
    :param kind: Alignment
    :return: The original ``Qt.Alignment`` object that ``Alignment`` extends.
    :rtype: PySide6.QtCore.Qt.Alignment



