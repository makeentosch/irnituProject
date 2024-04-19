from imports import *


class PuttyDialog(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Putty()
        self.ui.setupUi(self)
        self.engine = create_engine("sqlite:///room_db.db", echo=True)