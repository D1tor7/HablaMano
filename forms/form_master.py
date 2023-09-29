import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
import subprocess

class MasterPanel:
    def __init__(self, usuario_actual):
        self.ventana = tk.Tk()
        self.ventana.title("MasterPanel")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)

        # Agregar una etiqueta para mostrar el nombre del usuario en la esquina
        label_usuario = tk.Label(self.ventana, text=f"Usuario: {usuario_actual}", font=("Times", 12, BOLD), bg="#fcfcfc", fg="#666a88", anchor="nw")
        label_usuario.pack(side="left", padx=10, pady=10)

        # Agregar un botón "Evaluar Letras"
        self.boton_evaluar_letras = tk.Button(self.ventana, text="Evaluar Letras", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=self.mostrar_botones)
        self.boton_evaluar_letras.place(x=50, y=50, width=200, height=50)

    def mostrar_botones(self):
        # Eliminar el botón "Evaluar Letras"
        self.boton_evaluar_letras.destroy()

        # Agregar dos nuevos botones: "Letras con Movimiento" y "Letras sin Movimiento"
        boton_letras_con_movimiento = tk.Button(self.ventana, text="Letras con Movimiento", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff")
        boton_letras_con_movimiento.place(x=50, y=50, width=200, height=50)

        # Agregar un botón "Letras sin Movimiento" que abre el archivo .py
        boton_letras_sin_movimiento = tk.Button(self.ventana, text="Letras sin Movimiento", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=self.abrir_archivo_py)
        boton_letras_sin_movimiento.place(x=50, y=110, width=200, height=50)
        
    def abrir_archivo_py(self):
        ruta_archivo_py = r"C:/Users/diego/OneDrive/Documentos/GitHub/HablaMano/Letras/LetrasSinMovimiento/ProyectoMediaPipe_SinMovimiento.py"
        subprocess.Popen(["python", ruta_archivo_py])

if __name__ == "__main__":
    usuario_actual = "root"  # Debes definir el nombre de usuario actual aquí
    master_panel = MasterPanel(usuario_actual)
    master_panel.ventana.mainloop()