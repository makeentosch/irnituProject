from MainClasses.wallpaper_dialog import *
from MainClasses.paints_dialog import *
from MainClasses.panels_dialog import *
from MainClasses.plaster_dialog import *
from MainClasses.putty_dialog import *

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, "plugins", "platforms")
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.engine = create_engine("sqlite:///room_db.db", echo=True)
        self.ui.btnCalc.clicked.connect(self.calculate_square)

        self.ui.comboBox.currentIndexChanged.connect(self.check_choose)

    def calculate_square(self):
        room_length = float(self.ui.inputLength.text())
        room_width = float(self.ui.inputWidth.text())
        room_height = float(self.ui.inputHeight.text())
        doors_square = float(self.ui.doorInputWidth.text()) * float(self.ui.doorInputHeight.text()) * int(self.ui.doorsCount.text())
        windows_square = float(self.ui.windowInputWidth.text()) * float(self.ui.windowInputHeight.text()) * int(self.ui.windowsCount.text())

        result = 2 * (room_width + room_length) * room_height - doors_square - windows_square
        self.ui.outputSquare.setText(str(result))

        with Session(self.engine) as session:
            query = """
            INSERT INTO rooms (length, width, height, working_surface_square)
            VALUES (:l, :w, :h, :wss)
            """
            session.execute(text(query), {"l": room_length, "w": room_width, "h": room_height, "wss": result})
            session.commit()

    def check_choose(self):
        if self.ui.comboBox.currentText() == "Обои":
            wp_window = WallpaperDialog()
            wp_window.exec()
        elif self.ui.comboBox.currentText() == "Краска":
            wp_window = PaintsDialog()
            wp_window.exec()
        elif self.ui.comboBox.currentText() == "Панели":
            wp_window = PanelsDialog()
            wp_window.exec()
        elif self.ui.comboBox.currentText() == "Штукатурка":
            wp_window = PlasterDialog()
            wp_window.exec()
        elif self.ui.comboBox.currentText() == "Шпаклевка":
            wp_window = PuttyDialog()
            wp_window.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
