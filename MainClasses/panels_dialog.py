from imports import *


class PanelsDialog(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Panels()
        self.ui.setupUi(self)
        self.connection = sqlite3.connect("room_db.db")
        self.cursor = self.connection.cursor()
        self.ui.btnCalc.clicked.connect(self.get_panels_amount)

    def get_panels_amount(self):
        panel_type = self.ui.typeCmbx.currentText()
        panel_params = self.cursor.execute("SELECT width, height FROM panels WHERE title = ?",
                                           (panel_type,)).fetchone()
        panel_width = panel_params[0]
        panel_height = panel_params[1]
        panel_square = panel_width * panel_height / 1000000

        working_surface_square = self.cursor.execute("""
                SELECT working_surface_square FROM rooms 
                WHERE id = (SELECT MAX(id) FROM rooms)
                """).fetchone()[0]

        result = math.ceil(working_surface_square / panel_square)
        self.cursor.execute("UPDATE rooms SET panels_amount = :pa WHERE id = (SELECT MAX(id) FROM rooms)",
                            {"pa": result})
        self.connection.commit()
        self.ui.panelsCntOutput.setText(str(result))
