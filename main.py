from PyQt6.QtCore import QPropertyAnimation
from PyQt6 import QtCore as qtc
from PyQt6 import QtWidgets as qtw
from UI.UI_base import Ui_MainWindow
from back_end.arduino_serial import arduinoSerial


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.page_widgets.setCurrentWidget(self.serial_page)
        self.slide_menu.setMaximumWidth(0)
        self.serial = start_serial(self.serial_out, self.save)
        self.scrollArea.setVerticalScrollBar(self.verticalScrollBar)

        self.btn_menu.clicked.connect(lambda: self.toggleMenu(48))  # slide menu
        self.btn_serial.clicked.connect(self.go_to_serial)
        self.btn_database.clicked.connect(self.go_to_database)
        self.serialInput.returnPressed.connect(self.get_text)

    def go_to_serial(self):
        self.page_widgets.setCurrentWidget(self.serial_page)
        self.highlight_button()

    def go_to_database(self):
        self.page_widgets.setCurrentWidget(self.database_page)
        self.highlight_button()

    def get_text(self):
        self.serial.enviar_serial(self.serialInput.text())
        self.serialInput.setText('')

    def serial_out(self, entrada):
        texto = entrada + '\n' + self.serialOutput.text()
        self.serialOutput.setText(texto)

    def save(self, texto):
        print(f'Saving: {texto}')

    def highlight_button(self):
        self.btn_serial.setAutoFillBackground(False)
        self.btn_database.setAutoFillBackground(False)

        page = self.page_widgets.currentWidget().objectName()
        if page == 'serial_page':
            self.btn_serial.setAutoFillBackground(True)
        if page == 'database_page':
            self.btn_database.setAutoFillBackground(True)

    def toggleMenu(self, maxWidth):
        width = self.slide_menu.width()
        standard = 0  # minimum width
        widthExtended = standard

        if width == standard:
            widthExtended = maxWidth

        # ANIMATION
        self.animation = QPropertyAnimation(self.slide_menu, b"maximumWidth")
        self.animation.setDuration(150)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.start()

        self.highlight_button()


if __name__ == '__main__':
    import sys

    app = qtw.QApplication([])

    MainWindow = MainWindow()
    MainWindow.show()

    sys.exit(app.exec())