""" Unit test decpys.widgets.
"""



# python
import os

# package path
import define_pkg_path

# pytest
from fixtures import init_qapp

# pyside
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QPushButton
)

# decpys
from decpys.gui import (
    qIcon
)
from decpys.widgets import (
    qLabel,
    qPushButton
)



##########################################
##          UNIT TEST WIDGETS           ##
##########################################



def test_qlabel(init_qapp):
    """ Assert that `qLabel()` initializes and returns a `QLabel` appropriately.
    """
    label = qLabel(
        text="label",
        align=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
    )
    assert isinstance(label, QLabel), \
        "The value returned from qLabel() must be type Qt Label object."
    assert label.text() == "label", \
        "The label's text must be set within qLabel()."
    assert label.alignment() & Qt.AlignmentFlag.AlignHorizontal_Mask == Qt.AlignmentFlag.AlignRight, \
        "The label's horizontal alignment must be set within qLabel()."
    assert label.alignment() & Qt.AlignmentFlag.AlignVertical_Mask == Qt.AlignmentFlag.AlignVCenter, \
        "The label's vertical alignment must be properly set within qLabel()."



def test_qpushbutton(init_qapp):
    """ Assert that `qPushButton()` initializes and returns a `QPushButton` appropriately.
    """
    # button with text
    btn1 = qPushButton(display="button1")
    assert isinstance(btn1, QPushButton), \
        "The value returned from qPushButton() must be of type QPushButton."
    assert btn1.text() == "button1", \
        "The button's text must be set within qPushButton()."

    # button with icon
    btn2 = qPushButton(
        display=qIcon(
            os.path.join(".", "tests", "icons", "check-underline.png")
        )
    )
    assert isinstance(btn2, QPushButton), \
        "The value returned from qPushButton() must be type QPushButton."
    assert btn2.icon() != None, \
        "The button's icon must be set within qPushButton()"