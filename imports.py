import os
import sys
import math
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from GeneratedClasses.wallpaper import Ui_Wallpapers
from GeneratedClasses.mainwindow import Ui_MainWindow
from GeneratedClasses.paints import Ui_Paints
from GeneratedClasses.panels import Ui_Panels
from GeneratedClasses.plaster import Ui_Plaster
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import sqlite3
