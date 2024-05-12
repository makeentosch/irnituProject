from imports import *


class PaintsDialog(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Paints()
        self.ui.setupUi(self)
        self.connection = sqlite3.connect("room_db.db")
        self.cursor = self.connection.cursor()

        self.ui.btnCalc.clicked.connect(self.get_paints_weight)

    def get_paints_weight(self):
        paints_type = self.ui.typeCmbx.currentText()
        room_square = self.cursor.execute("SELECT working_surface_square FROM rooms ORDER BY id DESC").fetchone()[0]

        paints_weight = self.cursor.execute("SELECT weight FROM paints WHERE title = (?)",
                                            (paints_type,)).fetchone()[0]
        result = room_square / paints_weight * 1000
        result = round(result, 2)
        self.cursor.execute("UPDATE rooms SET paints_weight = :res WHERE id = (SELECT MAX(id) FROM rooms)",
                            {"res": result})
        self.connection.commit()
        self.ui.outputPaintsWeight.setText(str(result))
