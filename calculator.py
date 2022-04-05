"""
/***************************************************************************
Name                 : PyQt Desktop Calculator
Description          : Desktop calculator application.
Date                 : 11/July/2021
copyright            : (C) 2021 by Joseph Kariuki
email                : contact@josephkariuki.com
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


class MyCalculatorUI(QMainWindow):
    """
    Main window containing the controls for the calculator.
    """

    def __init__(self, parent=None):
        """
        View initializer.
        """
        super().__init__(parent)
        # Windows properties
        self.setWindowTitle('My Desktop Calculator')
        self.setFixedSize(500, 500)
        # Set the widgets
        self.vbox_layout = QVBoxLayout()
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.vbox_layout)
        # Creating the user interface controls
        self._init_ui()
        self._create_buttons()

    def _init_ui(self):
        """
        Create the display controls.
        """
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Calculations appear here')
        # Set geometry and alignment
        self.line_edit.setFixedHeight(30)
        self.line_edit.setAlignment(Qt.AlignRight)
        # Set to read only. User cannot type and erase.
        self.line_edit.setReadOnly(True)
        self.vbox_layout.addWidget(self.line_edit)

    def _create_buttons(self):
        """
        Create the buttons for calculator.
        """
        # Create a dictionary to store the buttons
        self.buttons = {}
        button_layout = QGridLayout()
        # Button text mapped to location in the grid layout.
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3), 'C': (0, 4),
            # 'Cos': (0, 5),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3), '(': (1, 4),
            # 'Tan': (1, 5),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3), ')': (2, 4),
            # 'Sin': (2, 5),
            '0': (3, 0), '00': (3, 1), '.': (3, 2), '+': (3, 3), '=': (3, 4),
            # 'Rad': (3, 5),
        }
        # Add buttons to the grid
        for button_text, location in buttons.items():
            self.buttons[button_text] = QPushButton(button_text)
            self.buttons[button_text].setFixedSize(45, 45)
            # Add buttons in their respective grid locations (row, column)
            button_layout.addWidget(
                self.buttons[button_text], location[0], location[1]
            )
        # Add the grid layout to the main layout
        self.vbox_layout.addLayout(button_layout)

    def set_line_edit_text(self, btn_text):
        """
        Set the text of the clicked button.
        :param btn_text: The text of the button that has been clicked.
        :type btn_text: str
        """
        self.line_edit.setText(btn_text)
        self.line_edit.setFocus()

    def line_edit_text(self):
        """
        Gets the text that is shown in the line edit.
        """
        return self.line_edit.text()

    def clear_line_edit(self):
        """
        Clears the text displayed in the line edit.
        """
        self.set_line_edit_text('')


class MyCalcController:
    """
    Contains logic that links the model/data to the view / calculator user
    interface.
    """

    def __init__(self, data, calc_ui):
        """
        Class initializer.
        """
        self._data = data
        self._calc_ui = calc_ui
        self._connect_signals()

    def _output(self):
        """
        Calculate the result.
        """
        result = self._data(
            result=self._calc_ui.line_edit_text()
        )
        self._calc_ui.set_line_edit_text(result)

    def _controller(self, exp):
        """
        Controller logic.
        :param exp: Expression
        :type exp: str
        """
        if self._calc_ui.line_edit_text() == ERROR_MSG:
            self._calc_ui.clear_line_edit()

        expression = self._calc_ui.line_edit_text() + exp
        self._calc_ui.set_line_edit_text(expression)

    def _connect_signals(self):
        """
        Connects the signals to slots.
        """
        for button_text, button in self._calc_ui.buttons.items():
            if button_text not in {'=', 'C'}:
                button.clicked.connect(
                    partial(self._controller, button_text)
                )
            # TODO: Add logic for angle calculations
            if button_text in {'Cos', 'Tan', 'Sin', 'Rad'}:
                button.setEnabled(False)

        self._calc_ui.buttons['C'].clicked.connect(
            self._calc_ui.clear_line_edit
        )
        self._calc_ui.buttons['='].clicked.connect(self._output)
        self._calc_ui.line_edit.returnPressed.connect(self._output)


ERROR_MSG = 'ERROR'  # Global variable for storing all type of errors


# Implementing the model
def evaluate_result(result):
    """
    Evaluate a result.
    """
    try:
        result = str(eval(result, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result


def main():
    """
    Main function of the application.
    """
    my_calc = QApplication(sys.argv)
    # Calculator user interface (View)
    view = MyCalculatorUI()
    view.show()
    # The model
    model = evaluate_result
    # Controller
    MyCalcController(data=model, calc_ui=view)
    # Executing the main loop of the calculator
    sys.exit(my_calc.exec())


if __name__ == '__main__':
    main()
