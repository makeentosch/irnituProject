from imports import *


class WallpaperDialog(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Wallpapers()
        self.ui.setupUi(self)
        self.connection = sqlite3.connect("room_db.db")
        self.cursor = self.connection.cursor()

        self.ui.btnCalc.clicked.connect(self.get_roll_amount)
        self.ui.btnCalc.clicked.connect(self.get_glue_weight)

    def get_roll_amount(self):
        width = float(self.ui.inputWidth.text())
        length = float(self.ui.inputLength.text())
        rapport = float(self.ui.inputRapport.text())
        reserve = float(self.ui.inputReserve.text())
        wp_square = width * length  # раппорт и запас никак не используются

        self.cursor.execute("""INSERT INTO wallpapers (width, length, rapport, reserve) VALUES (:w, :l, :rap, :res)""",
                            {"w": width, "l": length, "rap": rapport, "res": reserve})

        working_surface_square = self.cursor.execute("""
        SELECT working_surface_square FROM rooms 
        WHERE id = (SELECT MAX(id) FROM rooms)
        """).fetchone()[0]

        rolls_amount = math.ceil(float(working_surface_square) / wp_square)
        self.cursor.execute("""UPDATE rooms SET rolls_amount = :ra WHERE id = (SELECT MAX(id) FROM rooms)""",
                            {"ra": rolls_amount})

        self.ui.outputWpCount.setText(str(rolls_amount))
        self.connection.commit()

    def get_glue_weight(self):
        wp_type = self.ui.comboBox.currentText()
        glue_id = self.cursor.execute("""SELECT id FROM glues WHERE wp_name = (?)""", (wp_type,)).fetchone()[0]

        self.cursor.execute("""UPDATE wallpapers SET glue_id = :gid WHERE id = (SELECT MAX(id) FROM wallpapers)""",
                            {"gid": glue_id})

        room_square = self.cursor.execute("""SELECT working_surface_square FROM rooms ORDER BY id DESC""").fetchone()[0]

        query = """
        SELECT glues.weight 
        FROM glues 
        JOIN wallpapers ON wallpapers.glue_id = glues.id 
        WHERE wallpapers.id = (SELECT MAX(id) FROM wallpapers) 
        """
        glue_weight = self.cursor.execute(query).fetchone()[0]
        result = room_square * glue_weight
        result = round(result, 2)
        self.cursor.execute("""UPDATE rooms SET glue_weight = :res WHERE id = (SELECT MAX(id) FROM rooms)""",
                            {"res": result})
        self.connection.commit()
        self.ui.outputGlueCount.setText(str(result))
