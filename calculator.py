"""
/***************************************************************************
Name                 : PyQt Desktop Calculator
Description          : Desktop calculator application.
Date                 : 11/July/2021
copyright            : (C) 2021 by Joseph Kariuki
email                : joehene@gmail.com
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import sys
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QGridLayout
)

__version__ = '0.1'
__author__ = 'Joseph Kariuki'


class MyCalculator(QMainWindow):
    """
    Main window containing the controls for the calculator.
    """

    def __init__(self, parent=None):
        """
        View initializer.
        """
        super().__init__(parent)
        # Windows properties
        self.setWindowTitle('Desktop Calculator')
        self.setFixedSize(400, 400)

        self._createButtons()

    def _create_buttons(self):
        """
        Create buttons.
        """
        pass


def main():
    """
    Main function of the application.
    """
    pycalc = QApplication(sys.argv)
    view = MyCalculator()
    view.show()
    sys.exit(pycalc.exec())


if __name__ == '__main__':
    main()
