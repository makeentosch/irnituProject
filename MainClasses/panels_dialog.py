from imports import *


class PanelsDialog(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Panels()
        self.ui.setupUi(self)
        self.engine = create_engine("sqlite:///room_db.db", echo=True)