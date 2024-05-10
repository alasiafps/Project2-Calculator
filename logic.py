from PyQt6.QtWidgets import *
from gui import *
import math


class Logic(QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calculate_area_button.clicked.connect(lambda: self.calcular())

    def calcular(self) -> None:
        """
        Reads input from input box, uses it to calculate the area
        It then sets the output label to the calculated area.
        Also reads exceptions and handles them
        :return: None
        """
        try:
            if self.rect_radio.isChecked():
                length = float(self.length_input.text())
                width = float(self.width_input.text())
                area_rect = length * width
                self.output_label.setText(f'{area_rect}')
            elif self.circle_radio.isChecked():
                radius = float(self.radius_input.text())
                area_radius = math.pi * (radius ** 2)
                self.output_label.setText(f'{area_radius:.5}')
        except Exception:
            self.output_label.setText('Error')