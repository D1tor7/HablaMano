#form_master.py
import tkinter as tk
from tkinter.font import BOLD
import subprocess
import LogicaEvaluacion
import random
class MasterPanel:
    def __init__(self, usuario_actual):
        self.ventana = tk.Tk()
        self.ventana.title("MasterPanel")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)

        # Agregar una etiqueta para mostrar el nombre del usuario en la esquina
        label_usuario = tk.Label(self.ventana, text=f"Usuario: {usuario_actual}", font=("Times", 12, BOLD), bg="#fcfcfc", fg="#666a88")
        label_usuario.place(x=w - 10, y=10, anchor="ne")

        # Agregar un botón "Evaluar Letras"
        self.boton_evaluar_letras = tk.Button(self.ventana, text="Evaluar Letras", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=self.mostrar_botones)
        self.boton_evaluar_letras.place(x=50, y=50, width=200, height=50)

        # Agregar una etiqueta para mostrar las letras aleatorias
        self.etiqueta_letras_aleatorias = tk.Label(self.ventana, text="", font=("Times", 12), bg="#fcfcfc", fg="#000")
        self.etiqueta_letras_aleatorias.place(x=50, y=160)

    def mostrar_botones(self):
        # Eliminar el botón "Evaluar Letras"
        self.boton_evaluar_letras.destroy()

        # Agregar dos nuevos botones: "Letras con Movimiento" y "Letras sin Movimiento"
        boton_letras_con_movimiento = tk.Button(self.ventana, text="Letras con Movimiento", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff")
        boton_letras_con_movimiento.place(x=50, y=50, width=200, height=50)

        # Agregar un botón "Letras sin Movimiento" que abre el archivo .py y muestra las letras aleatorias
        boton_letras_sin_movimiento = tk.Button(self.ventana, text="Letras sin Movimiento", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=self.mostrar_letras_aleatorias)
        boton_letras_sin_movimiento.place(x=50, y=110, width=200, height=50)

    def abrir_archivo_py(self):
        ruta_archivo_py = r"C:/Users/diego/OneDrive/Documentos/GitHub/HablaMano/Letras/LetrasSinMovimiento/ProyectoMediaPipe_SinMovimiento.py"
        subprocess.Popen(["python", ruta_archivo_py])

    def limpiar_canvas(self):
        # Destruir todos los widgets en el canvas
        for widget in self.ventana.winfo_children():
            if isinstance(widget, tk.Widget) and widget.winfo_class() != "Label":
                widget.destroy()

    def mostrar_letras_aleatorias(self):
        try:
            # Limpiar los botones antes de mostrar las letras
            self.limpiar_canvas()

            # Obtener las letras aleatorias del módulo LogicaEvaluacion
            self.letras_actuales = LogicaEvaluacion.generar_letras_aleatorias()

            # Iniciar el ciclo de cambio de letras cada 10 segundos
            self.cambiar_letras_cada_10_segundos()

            # Abrir el archivo ProyectoMediaPipe_SinMovimiento.py
            self.abrir_archivo_py()

        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir durante la ejecución
            print(f"Error al mostrar letras aleatorias: {e}")

    def cambiar_letras_cada_10_segundos(self):
        if self.letras_actuales:
            # Obtener la próxima letra de la lista
            letra_actual = self.letras_actuales.pop(0)

            # Actualizar la etiqueta con la nueva letra
            self.etiqueta_letras_aleatorias.config(text=f"Letra Actual: {letra_actual}")

            # Programar la llamada recursiva para dentro de 10 segundos
            self.ventana.after(1000, self.cambiar_letras_cada_10_segundos)
        else:
            # Cuando se acaban las letras, imprimir "timeout"
            self.etiqueta_letras_aleatorias.config(text="timeout:#")


if __name__ == "__main__":
    usuario_actual = "root"  # Debes definir el nombre de usuario actual aquí
    master_panel = MasterPanel(usuario_actual)
    master_panel.ventana.mainloop()