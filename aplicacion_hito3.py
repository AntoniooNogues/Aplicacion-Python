from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
from bdd_futbol_emotion import *


class Ventana_BDD (QMainWindow):
    def __init__(self):
        super(Ventana_BDD, self).__init__()
        loadUi('Hito3.ui', self)
        self.Add.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.add))
        self.Buscar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.base_datos_2))
        self.Editar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.editar))
        self.Eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.eliminar))
        #Ver registros de base de datos
        self.refrescar_sql.clicked.connect(self.cargar_datos_sql) #Funciona
        #Ver registros de un producto mediante la inserccion de una id
        self.apply_edit.clicked.connect(self.buscar_producto)
        self.bt_guardar_add.clicked.connect(self.crear_nuevo)
        self.guardar_cambios.clicked.connect(self.modificar_producto)
        self.borrar.clicked.connect(self.borrar_registros_id)
        self.actualizar_tabla.clicked.connect(self.cargar_datos_sql_eliminar)
        self.bt_validar_id_eliminar.clicked.connect(self.elimar_producto_id)
        #ICONO y NOMBRE del programa.
        self.setWindowTitle("Antonio Nogues Gómez")
        icono = QIcon("Icono.png")
        self.setWindowIcon(icono)
    def cargar_datos_sql(self): #Funciona
        self.stackedWidget.setCurrentWidget(self.base_datos_2)
        lista_botas, columnas = extraer_datos()
        self.tablaproducto.setRowCount(len(lista_botas))
        for fila, botas in enumerate(lista_botas, start=0):
            for columna, campo_botas in enumerate(botas.values(), start=0):
                self.tablaproducto.setItem(fila, columna, QTableWidgetItem(str(campo_botas)))

        self.tablaproducto.resizeColumnsToContents()

    def cargar_datos_sql_eliminar(self): #Funciona
        self.stackedWidget.setCurrentWidget(self.eliminar)
        lista_botas, columnas = extraer_datos()
        self.tabla_sql_eliminar.setRowCount(len(lista_botas))
        for fila, botas in enumerate(lista_botas, start=0):
            for columna, campo_botas in enumerate(botas.values(), start=0):
                self.tabla_sql_eliminar.setItem(fila, columna, QTableWidgetItem(str(campo_botas)))

        self.tabla_sql_eliminar.resizeColumnsToContents()

    def crear_nuevo(self): #Funciona
        bota = dict()
        bota['nombre'] = self.input_nombre_add.text()
        bota['marca'] = self.input_marca_add.text()
        bota['imagen'] = self.input_imagen_add.text()
        bota['url'] = self.input_url_add.text()
        bota['precio'] = self.input_precio_add.text()
        bota['descripcion'] = self.input_descripcion_add.text()
        bota['tipo_suela'] = self.input_tipo_suela_add.text()
        if bota['nombre'] != " " and bota['marca'] != " " and bota['precio'] != " ":
            insertar_dato(bota)
            self.texto_validacion.setText("Producto Registrado")
        else:
            self.texto_validacion.setText("Error, el campo esta en blanco")

    def buscar_producto(self):
        id = self.input_id_edit.text()
        self.producto = extraer_datos_por_id(id)
        if self.producto:
            valores = list(self.producto.values())
            self.input_nombre_edit.setText(str(valores[1]))
            self.input_marca_edit.setText(str(valores[2]))
            self.input_imagen_edit.setText(str(valores[3]))
            self.input_url_edit.setText(str(valores[4]))
            self.input_precio_edit.setText(str(valores[5]))
            self.input_descripcion_edit.setText(str(valores[6]))
            self.input_tiposuela_edit.setText(str(valores[7]))
        else:
            self.mensaje.setText("No existe un producto con esta ID")
    def elimar_producto_id(self):
        id = self.id_eliminar.text()
        eliminacion_registro_id(id)
        self.texto_validacion_2.setText("Registro Eliminado con Exito")

    def modificar_producto(self):
        id = self.input_id_edit.text()
        nombre = self.input_nombre_edit.text()
        marca = self.input_marca_edit.text()
        imagen = self.input_imagen_edit.text()
        url = self.input_url_edit.text()
        precio = self.input_precio_edit.text()
        descripcion = self.input_descripcion_edit.text()
        tipo_suela = self.input_tiposuela_edit.text()
        accion = actualizar_producto(id, nombre, marca, imagen, url, precio, descripcion, tipo_suela)
        self.mensaje.setText("Producto Actualizado")

    def borrar_registros_id(self):
        self.input_id_edit.clear()
        self.input_nombre_edit.clear()
        self.input_marca_edit.clear()
        self.input_imagen_edit.clear()
        self.input_url_edit.clear()
        self.input_precio_edit.clear()
        self.input_descripcion_edit.clear()
        self.input_tiposuela_edit.clear()
        self.mensaje.clear()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana_principal = Ventana_BDD()
    ventana_principal.show()
    sys.exit(app.exec_())

