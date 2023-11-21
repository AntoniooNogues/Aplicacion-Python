from Hito3_ui import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QMaiWindow
from bdd_futbol_emotion import *
class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super(VentanaPrincipal,self).__init__()
        loadUi("Hito3.ui", self)
        self.Add.clicked.connect(lambda: self.stackedWidget(self.add))
        self.Buscar.clicked.connect(lambda: self.stackedWidget(self.sql))
        self.Editar.clicked.connect(lambda: self.stackedWidget(self.editar))
        self.Eliminar.clicked.connect(lambda: self.stackedWidget(self.eliminar))

    def cargar_datos_sql(self):
        self.stacked.Widget.setCurrentWidget(self.sql)
        lista_botas, columnas = extraer_datos()
        self.tableWidget.setRowCount(len(lista_botas))
        for fila, botas in enumerate(lista_botas, start=0):
            for columnas, campos in enumerate(botas.values(), start=0):
                self.tableWidget.setItem(fila, columnas, QTableWidgetItem(str(campos)))
        self.tableWidget.resizeColumnsToContens()
    def crear_nuevo(self):
        bota_nueva = dict()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


