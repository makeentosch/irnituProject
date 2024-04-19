from imports import *


class PaintsDialog(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Paints()
        self.ui.setupUi(self)
        self.engine = create_engine("sqlite:///room_db.db", echo=True)