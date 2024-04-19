from imports import *


class WallpaperDialog(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Wallpapers()
        self.ui.setupUi(self)
        self.engine = create_engine("sqlite:///room_db.db", echo=True)

        self.ui.btnCalc.clicked.connect(self.get_roll_amount)
        self.ui.btnCalc.clicked.connect(self.get_glue_weight)

    def get_roll_amount(self):
        width = float(self.ui.inputWidth.text())
        height = float(self.ui.inputHeight.text())
        rapport = float(self.ui.inputRapport.text())
        reserve = float(self.ui.inputReserve.text())
        with Session(self.engine) as session:
            room_square = session.execute(text("""SELECT working_surface_square FROM rooms ORDER BY id DESC""")).first()[0]
            rolls_amount = math.ceil(room_square / (width + height + rapport + reserve))
            query = """
            INSERT INTO wallpapers (width, height, rapport, reserve)
            VALUES (:w, :h, :rap, :res)
            """
            session.execute(text(query), {"w": width, "h": height, "rap": rapport, "res": reserve})
            session.execute(text("UPDATE rooms SET rolls_amount = :ra WHERE id = (SELECT MAX(id) FROM rooms)"), {"ra": rolls_amount})
            session.commit()

        self.ui.outputWpCount.setText(str(rolls_amount))

    def get_glue_weight(self):
        wp_type = self.ui.comboBox.currentText()
        with Session(self.engine) as session:
            rolls_cnt = session.execute(text("SELECT rolls_amount FROM rooms ORDER BY id DESC")).first()[0]
            query = """
            SELECT wallpapers.id, glues.weight FROM glues 
            JOIN wallpapers ON wallpapers.glue_id = glues.id
            ORDER BY wallpapers.id DESC
            """
            glue_weight_common = session.execute(text(query)).first()[1]
            session.execute(text("""UPDATE rooms SET glue_weight = :w WHERE id = (SELECT MAX(id) FROM rooms)"""),
                            {"w": glue_weight_common})
            session.commit()
            self.ui.outputGlueCount.setText(str(glue_weight_common))