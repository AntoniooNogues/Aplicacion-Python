from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
from bdd_futbol_emotion import *


class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('Hito3.ui', self)
        self.Add.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.add))
        self.Buscar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.sql))
        self.Editar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.editar))
        self.Eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.eliminar))
        self.guardar.clicked.connect(self.crear_nuevo())

    def cargar_datos_sql(self):
        self.stacked.Widget.setCurrentWidget(self.tabla)
        lista_botas, columnas = extraer_datos()
        self.tableWidget.setRowCount(len(lista_botas))
        for fila, botas in enumerate(lista_botas, start=0):
            for columnas, campos in enumerate(botas.values(), start=0):
                self.tableWidget.setItem(fila, columnas, QTableWidgetItem(str(campos)))
        self.tableWidget.resizeColumnsToContens()

    def crear_nuevo(self):
        bota_nueva = dict()
        bota_nueva['nombre'] = self.input_nombre.text()
        bota_nueva['marca'] = self.input_marca.text()
        bota_nueva['imagen'] = self.input_imagen.text()
        bota_nueva['url'] = self.input_url.text()
        bota_nueva['precio'] = self.input_precio.text()
        bota_nueva['descripcion'] = self.input_descripcion.text()
        bota_nueva['tipo_suela'] = self.input_tipo_suela.text()
        insertar_registro_diccionario(bota_nueva)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec_())


