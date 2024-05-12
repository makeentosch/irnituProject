from MainClasses.wallpaper_dialog import *
from MainClasses.paints_dialog import *
from MainClasses.panels_dialog import *
from MainClasses.plaster_dialog import *

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, "plugins", "platforms")
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCalc.clicked.connect(self.calculate_working_surface_square)
        self.ui.comboBox.currentIndexChanged.connect(self.check_choose)

        self.connection = sqlite3.connect("room_db.db")
        self.cursor = self.connection.cursor()

    def calculate_working_surface_square(self):
        room_length = float(self.ui.inputLength.text())
        room_width = float(self.ui.inputWidth.text())
        room_height = float(self.ui.inputHeight.text())

        # Обработка данных о двери
        door_type = self.ui.doorCmbx.currentText()
        door_params = self.cursor.execute("""SELECT width, height FROM doors WHERE title = (?)""",
                                          (door_type,)).fetchone()
        door_width = door_params[0]
        door_height = door_params[1]
        doors_count = int(self.ui.doorsCount.text())

        # Обработка данных об окне
        window_type = self.ui.windowCmbx.currentText()
        window_params = self.cursor.execute("""SELECT width, height FROM windows WHERE title = (?)""",
                                            (window_type,)).fetchone()
        window_width = window_params[0]
        window_height = window_params[1]
        windows_count = int(self.ui.windowsCount.text())

        doors_square = door_width * door_height * doors_count / 1000000
        windows_square = window_width * window_height * windows_count / 1000000

        result = 2 * (room_width + room_length) * room_height - doors_square - windows_square
        result = round(result, 2)
        self.ui.outputSquare.setText(str(result) + " кв. м")

        query = """
        INSERT INTO rooms (length, width, height, working_surface_square, doors_amount, windows_amount)
        VALUES (:l, :w, :h, :wss, :da, :wa)
        """
        self.cursor.execute(query, {"l": room_length, "w": room_width, "h": room_height,
                                    "wss": result, "da": doors_count, "wa": windows_count})
        self.connection.commit()

        return result

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
