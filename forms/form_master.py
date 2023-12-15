# form_master.py

import tkinter as tk
from tkinter.font import BOLD
from PIL import Image, ImageTk
import subprocess
import random
import pandas as pd


class MasterPanel:
    def __init__(self, usuario_actual):
        self.ventana = tk.Tk()
        self.ventana.title("MasterPanel")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        self.datos = pd.read_csv('common_letter.csv')
        self.letras_columna = self.datos['letras'].apply(lambda x: x.split(','))
        self.contador_actual = None

        self.estado_mensaje = tk.StringVar()
        self.color_mensaje = tk.StringVar()


        # Configurar las etiquetas a la izquierda
        self.etiqueta_letra_actual = tk.Label(self.ventana, text="", font=("Times", 20, BOLD), bg="#fcfcfc", fg="#666a88", anchor="w")
        self.etiqueta_letra_actual.place(x=10, y=h // 2, anchor="w")

        self.etiqueta_mensaje = tk.Label(self.ventana, text="", font=("Times", 16), bg="#fcfcfc", fg="#666a88", anchor="w")
        self.etiqueta_mensaje.place(x=10, y=h // 2 + 50, anchor="w")

        self.etiqueta_resultado = tk.Label(self.ventana, image=None, bg="#fcfcfc")
        self.etiqueta_resultado.place(x=10, y=h // 2 + 100, anchor="w")

        label_usuario = tk.Label(self.ventana, text=f"Usuario: {usuario_actual}", font=("Times", 12, BOLD), bg="#fcfcfc", fg="#666a88", anchor="w")
        label_usuario.place(x=10, y=10, anchor="w")

        self.boton_evaluar_letras = tk.Button(self.ventana, text="Evaluar Letras", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=lambda: self.limpiar_pantalla(self.mostrar_botones))
        self.boton_evaluar_letras.place(x=10, y=50, width=200, height=50)

        self.puntaje = 0
        self.letras_totales = 0  # Variable para contar el total de letras
        self.imagen_actual = None

       
        self.etiqueta_contador = tk.Label(self.ventana, text="", font=("Times", 12), bg="#fcfcfc", fg="#666a88", anchor="w")
        self.etiqueta_contador.place(x=10, y=230, anchor="w")

    def limpiar_pantalla(self, siguiente_funcion):
        # Destruir todos los widgets en la ventana excepto la etiqueta de letras actuales
        for widget in self.ventana.winfo_children():
            if isinstance(widget, tk.Widget) and widget.winfo_class() != "Label" and widget != self.etiqueta_letra_actual:
                widget.destroy()

        # Llamar a la función siguiente
        siguiente_funcion()

    def mostrar_botones(self):
        boton_letras_con_movimiento = tk.Button(self.ventana, text="Letras con Movimiento", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=lambda: self.limpiar_pantalla(self.abrir_archivo_py_M))
        boton_letras_con_movimiento.place(x=10, y=50, width=200, height=50)

        boton_letras_sin_movimiento = tk.Button(
            self.ventana, text="Letras sin Movimiento", font=("Times", 15, BOLD),
            bg="#3a7ff6", bd=0, fg="#fff", command=lambda: [self.abrir_archivo_py_M(), self.mostrar_letras_sin_movimiento(), self.limpiar_canvas(), self.abrir_archivo_logic()]
        )

        boton_letras_sin_movimiento.place(x=10, y=110, width=200, height=50)

    def abrir_archivo_logic(self):
        ruta_logica_archivo_py = r"C:/Users/diego/OneDrive/Documentos/GitHub/HablaMano/forms/LogicaEvaluacion.py"
        subprocess.Popen(["python", ruta_logica_archivo_py])

    def abrir_archivo_py_M(self):
        ruta_archivo_py = r"C:/Users/diego/OneDrive/Documentos/GitHub/HablaMano/Letras/LetrasSinMovimiento/ProyectoMediaPipe_SinMovimiento.py"
        subprocess.Popen(["python", ruta_archivo_py])

    def mostrar_letras_sin_movimiento(self):
        # Obtener la letra más común dinámicamente
        self.etiqueta_letra_mas_comun = tk.Label(self.ventana, text="", font=("Times", 12), bg="#fcfcfc", fg="#666a88", anchor="w")
        self.etiqueta_letra_mas_comun.place(x=10, y=170, anchor="w")

        self.etiqueta_lista_letras = tk.Label(self.ventana, text="", font=("Times", 12), bg="#fcfcfc", fg="#666a88", anchor="w")
        self.etiqueta_lista_letras.place(x=10, y=200, anchor="w")

        self.actualizar_letra_mas_comun()

        self.mostrar_siguiente_letra(self.letras_columna.iloc[0], 0)

    def actualizar_letra_mas_comun(self):
        # Leer el archivo CSV nuevamente para obtener la letra más común
        datos_actualizados = pd.read_csv('common_letter.csv')
        letra_mas_comun = datos_actualizados['Most Common Letter'].iloc[0]
        self.etiqueta_letra_mas_comun.config(text=f"Letra más común: {letra_mas_comun}")
        self.ventana.after(3000, self.actualizar_letra_mas_comun)

    def mostrar_siguiente_letra(self, lista_letras, indice):
        self.detener_contador_actual()  # Detener el contador actual antes de iniciar uno nuevo

        self.contador_segundos = 10  # Establecer el tiempo de espera en segundos
        self.actualizar_contador()
        if indice < len(lista_letras):
            letra_actual = lista_letras[indice]

            self.etiqueta_letra_actual.config(text=f"Letra actual: {letra_actual}")

            # Iniciar el contador antes de verificar la letra
            self.ventana.after(1000, lambda: self.actualizar_contador())
            self.ventana.after(10000, lambda: self.verificar_letra(lista_letras, letra_actual, indice))
        else:
            self.ventana.after(10000, self.limpiar_etiquetas)
    
    def actualizar_contador(self):
        if self.contador_segundos > 0:
            self.etiqueta_contador.config(text=f"Tiempo restante: {self.contador_segundos} segundos")
            self.contador_segundos -= 0.5
            self.contador_actual = self.ventana.after(1000, self.actualizar_contador)  # Actualizar cada 1 segundo
        else:
            self.etiqueta_contador.config(text="")
            self.detener_contador_actual()
    
    def detener_contador_actual(self):
        if self.contador_actual is not None:
            self.ventana.after_cancel(self.contador_actual)
            self.contador_actual = None


    def verificar_letra(self, lista_letras, letra_actual, indice):
        if letra_actual.lower() == self.etiqueta_letra_mas_comun.cget("text").split(":")[1].strip().lower():
            self.etiqueta_mensaje.config(text="Correcto", fg="green")
            self.puntaje += 10  # Sumar 10 puntos por respuesta correcta
        else:
            self.etiqueta_mensaje.config(text="Incorrecto", fg="red")

        # Elimina el uso de imágenes
        # self.etiqueta_resultado.config(image=self.imagen_actual)

        self.etiqueta_letra_actual.lift()
        self.etiqueta_mensaje.lift()

        self.ventana.update_idletasks()

        self.ventana.after(2000, self.limpiar_mensaje_imagen)

        self.letras_totales += 1  # Incrementar el total de letras

        if self.letras_totales == len(lista_letras):  # Verificar si se ha llegado al final de la lista de letras
            self.ventana.after(4000, self.mostrar_puntuacion)
        else:
            self.ventana.after(4000, lambda: self.mostrar_siguiente_letra(lista_letras, indice + 1))

    def mostrar_puntuacion(self):
        mensaje_puntuacion = f"Puntuación total: {self.puntaje}"
        self.etiqueta_mensaje.config(text=mensaje_puntuacion, fg="blue")
        self.ventana.after(10000, self.limpiar_mensaje_imagen)
        self.ventana.after(10000, self.limpiar_etiquetas)

    def limpiar_etiquetas(self):
        self.etiqueta_letra_actual.config(text="")
        self.etiqueta_mensaje.config(text="")
        # Elimina el uso de la etiqueta de resultado y la imagen
        # self.etiqueta_resultado.config(image=None)
        self.limpiar_imagen()

    def limpiar_mensaje_imagen(self):
        self.etiqueta_mensaje.config(text="")
        self.etiqueta_resultado.config(image=None)

    def limpiar_imagen(self):
        if self.imagen_actual is not None:
            self.etiqueta_resultado.config(image=None)
            self.imagen_actual = None  # Restablecer la referencia de la imagen actual


if __name__ == "__main__":
    usuario_actual = "root"
    master_panel = MasterPanel(usuario_actual)
    master_panel.ventana.mainloop()