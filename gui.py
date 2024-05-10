from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator) -> None:
        """
        This function creates the gui and makes the buttons work. It reads what button was
        pushed and sends it to the screen
        :param Calculator:
        :return: None
        """
        Calculator.setObjectName("Calculator")
        Calculator.resize(600, 630)  # Extended width
        Calculator.setMinimumSize(QtCore.QSize(600, 630))
        Calculator.setMaximumSize(QtCore.QSize(600, 630))
        self.centralwidget = QtWidgets.QWidget(parent=Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.output_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(10, 10, 381, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.output_label.setFont(font)
        self.output_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.output_label.setLineWidth(2)
        self.output_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.output_label.setObjectName("output_label")
        self.intButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pos_or_neg())
        self.intButton.setGeometry(QtCore.QRect(10, 130, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.intButton.setFont(font)
        self.intButton.setObjectName("intButton")
        self.cButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("C"))
        self.cButton.setGeometry(QtCore.QRect(110, 130, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.deleteButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.delete())
        self.deleteButton.setGeometry(QtCore.QRect(200, 130, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.divideButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("/"))
        self.divideButton.setGeometry(QtCore.QRect(300, 130, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.multiplyButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(300, 220, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.nineButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("9"))
        self.nineButton.setGeometry(QtCore.QRect(200, 220, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.sevenButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 220, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("8"))
        self.eightButton.setGeometry(QtCore.QRect(110, 220, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.minusButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("-"))
        self.minusButton.setGeometry(QtCore.QRect(300, 310, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.sixButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("6"))
        self.sixButton.setGeometry(QtCore.QRect(200, 310, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.fourButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 310, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("5"))
        self.fiveButton.setGeometry(QtCore.QRect(110, 310, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.additionButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("+"))
        self.additionButton.setGeometry(QtCore.QRect(300, 400, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.additionButton.setFont(font)
        self.additionButton.setObjectName("additionButton")
        self.threeButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("3"))
        self.threeButton.setGeometry(QtCore.QRect(200, 400, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.oneButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 400, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("2"))
        self.twoButton.setGeometry(QtCore.QRect(110, 400, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.computeButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.math())
        self.computeButton.setGeometry(QtCore.QRect(300, 490, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.computeButton.setFont(font)
        self.computeButton.setObjectName("computeButton")
        self.periodButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.dot_it())
        self.periodButton.setGeometry(QtCore.QRect(200, 490, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.periodButton.setFont(font)
        self.periodButton.setObjectName("periodButton")
        self.halloButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.halloButton.setGeometry(QtCore.QRect(10, 490, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.halloButton.setFont(font)
        self.halloButton.setObjectName("halloButton")
        self.zeroButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.pressed_button("0"))
        self.zeroButton.setGeometry(QtCore.QRect(110, 490, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        # Add radio buttons for shape selection
        self.rect_radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.rect_radio.setGeometry(QtCore.QRect(420, 150, 120, 30))
        self.rect_radio.setObjectName("rect_radio")
        self.rect_radio.setText("Rectangle")
        self.rect_radio.toggled.connect(self.toggle_rectangle)
        self.circle_radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.circle_radio.setGeometry(QtCore.QRect(420, 190, 120, 30))
        self.circle_radio.setObjectName("circle_radio")
        self.circle_radio.setText("Circle")
        self.circle_radio.toggled.connect(self.toggle_circle)
        # Length and Width input fields
        self.length_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.length_label.setGeometry(QtCore.QRect(420, 240, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.length_label.setFont(font)
        self.length_label.setObjectName("length_label")
        self.width_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.width_label.setGeometry(QtCore.QRect(420, 280, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.width_label.setFont(font)
        self.width_label.setObjectName("width_label")
        self.length_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.length_input.setGeometry(QtCore.QRect(500, 240, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.length_input.setFont(font)
        self.length_input.setObjectName("length_input")
        self.width_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.width_input.setGeometry(QtCore.QRect(500, 280, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.width_input.setFont(font)
        self.width_input.setObjectName("width_input")
        # Radius input field
        self.radius_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.radius_label.setGeometry(QtCore.QRect(420, 330, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radius_label.setFont(font)
        self.radius_label.setObjectName("radius_label")
        self.radius_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.radius_input.setGeometry(QtCore.QRect(500, 330, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radius_input.setFont(font)
        self.radius_input.setObjectName("radius_input")
        self.radius_label.hide()
        self.radius_input.hide()

        # Calculate Area button
        self.calculate_area_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.calculate_area())
        self.calculate_area_button.setGeometry(QtCore.QRect(420, 380, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculate_area_button.setFont(font)
        self.calculate_area_button.setObjectName("calculate_area_button")
        self.calculate_area_button.setText("Calculate Area")

        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 409, 21))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)
        self.length_label.setHidden(True)
        self.width_label.setHidden(True)
        self.length_input.setHidden(True)
        self.width_input.setHidden(True)
        self.calculate_area_button.setHidden(True)


    def toggle_rectangle(self, checked) -> None:
        """
        This function controls the gui for the rectangle labels and inputs
        :param checked:
        :return: None
        """
        if checked:
            self.length_label.show()
            self.length_input.show()
            self.width_label.show()
            self.width_input.show()
            self.radius_label.hide()
            self.radius_input.hide()
            self.calculate_area_button.show()

    def toggle_circle(self, checked) -> None:
        """
        This function controls the attributes for if the circle button gets clicked
        :param checked:
        :return: None
        """
        if checked:
            self.length_label.hide()
            self.length_input.hide()
            self.width_label.hide()
            self.width_input.hide()
            self.radius_label.show()
            self.radius_input.show()
            self.calculate_area_button.show()

    def pressed_button(self, pressed) -> None:
        """
        Function will take the buttons the user presses and inputs them. It makes sure that
        if zero is already inputted, it clears it so there's not a zero at the start of the string.
        it also checks to see if C was pushed to clear the current label.
        :param pressed: button pushed
        :return: None
        """
        if pressed == "C":
            self.output_label.setText('0')
        else:
            if self.output_label.text() == "0":
                self.output_label.setText("")
            self.output_label.setText(f'{self.output_label.text()}{pressed}')

    def delete(self) -> None:
        """
        deletes the last character in the label
        :return: None
        """
        screen = self.output_label.text()
        screen = screen[:-1]
        self.output_label.setText(screen)

    def math(self) -> None:
        """
        This is the function that does the math. I learned that eval() takes a string and does all the math for you,
        so no logic is necessary.
        :return: None
        """
        screen = self.output_label.text()
        try:
            ans = eval(screen)
            self.output_label.setText(str(ans))
        except:
            self.output_label.setText("ERROR")

    def pos_or_neg(self) -> None:
        """
        Function that changes the current number on the screen to negative if positive, or positive if negative.
        :return: None
        """
        screen = self.output_label.text()
        if "-" in screen:
            self.output_label.setText(screen.replace(("-"), ""))
        else:
            self.output_label.setText(f'-{screen}')

    def dot_it(self) -> None:
        """
        adds a .
        :return: None
        """
        screen = self.output_label.text()
        if screen[-1] == ".":
            pass
        else:
            self.output_label.setText(f'{screen}.')

    def calculate_area(self) -> None:
        """
        This function
        :return:
        """
        if self.rect_radio.isChecked():
            length = float(self.length_input.text())
            width = float(self.width_input.text())
            area = length * width
            self.output_label.setText(str(area))
        elif self.circle_radio.isChecked():
            radius = float(self.radius_input.text())
            area = 3.14 * (radius ** 2)
            self.output_label.setText(str(area))

    def retranslateUi(self, Calculator) -> None:
        """
        This function helps set up the rest of the GUi.
        :param Calculator:
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "MainWindow"))
        self.output_label.setText(_translate("Calculator", "0"))
        self.intButton.setText(_translate("Calculator", "+/-"))
        self.cButton.setText(_translate("Calculator", "C"))
        self.deleteButton.setText(_translate("Calculator", "DEL"))
        self.divideButton.setText(_translate("Calculator", "/"))
        self.multiplyButton.setText(_translate("Calculator", "x"))
        self.nineButton.setText(_translate("Calculator", "9"))
        self.sevenButton.setText(_translate("Calculator", "7"))
        self.eightButton.setText(_translate("Calculator", "8"))
        self.minusButton.setText(_translate("Calculator", "-"))
        self.sixButton.setText(_translate("Calculator", "6"))
        self.fourButton.setText(_translate("Calculator", "4"))
        self.fiveButton.setText(_translate("Calculator", "5"))
        self.additionButton.setText(_translate("Calculator", "+"))
        self.threeButton.setText(_translate("Calculator", "3"))
        self.oneButton.setText(_translate("Calculator", "1"))
        self.twoButton.setText(_translate("Calculator", "2"))
        self.computeButton.setText(_translate("Calculator", "="))
        self.periodButton.setText(_translate("Calculator", "."))
        self.halloButton.setText(_translate("Calculator", ":3"))
        self.zeroButton.setText(_translate("Calculator", "0"))
        self.rect_radio.setText(_translate("Calculator", "Rectangle"))
        self.circle_radio.setText(_translate("Calculator", "Circle"))
        self.length_label.setText(_translate("Calculator", "Length:"))
        self.width_label.setText(_translate("Calculator", "Width:"))
        self.radius_label.setText(_translate("Calculator", "Radius:"))
        self.calculate_area_button.setText(_translate("Calculator", "Calculate Area"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec())