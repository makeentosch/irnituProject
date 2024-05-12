from imports import *


class PlasterDialog(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Plaster()
        self.ui.setupUi(self)
        self.connection = sqlite3.connect("room_db.db")
        self.cursor = self.connection.cursor()
        self.ui.btnCalc.clicked.connect(self.get_plaster_amount)

    def get_plaster_amount(self):
        plaster_type = self.ui.typeCmbx.currentText()
        layer_width = float(self.ui.inputLayerWidth.text())
        working_surface_square = self.cursor.execute("""
                        SELECT working_surface_square FROM rooms 
                        WHERE id = (SELECT MAX(id) FROM rooms)
                        """).fetchone()[0]

        if plaster_type == "Гипсовая":
            consumption = 0.98
        else:
            consumption = 1.48
        result = working_surface_square * consumption * layer_width
        result = round(result, 2)
        self.cursor.execute("UPDATE rooms SET plaster_amount = :pa WHERE id = (SELECT MAX(id) FROM rooms)",
                            {"pa": result})
        self.connection.commit()
        self.ui.outputPlasterCount.setText(str(result))