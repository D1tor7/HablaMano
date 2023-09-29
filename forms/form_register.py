import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import csv
from tkinter import ttk, messagebox

class RegistrationScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro")
        self.root.geometry("800x500")
        self.root.resizable(width=0, height=0)
        
        # Crear los campos de registro
        self.etiqueta_usuario = tk.Label(root, text="Usuario", font=("Times", 14))
        self.etiqueta_usuario.pack(pady=10)
        self.usuario = ttk.Entry(root, font=("Times", 14))
        self.usuario.pack(pady=10)
        
        self.etiqueta_correo = tk.Label(root, text="Correo", font=("Times", 14))
        self.etiqueta_correo.pack(pady=10)
        self.correo = ttk.Entry(root, font=("Times", 14))
        self.correo.pack(pady=10)
        
        self.etiqueta_password = tk.Label(root, text="Contraseña", font=("Times", 14))
        self.etiqueta_password.pack(pady=10)
        self.password = ttk.Entry(root, font=("Times", 14))
        self.password.pack(pady=10)
        self.password.config(show="*")
        
        self.etiqueta_confirmacion = tk.Label(root, text="Confirmación de Contraseña", font=("Times", 14))
        self.etiqueta_confirmacion.pack(pady=10)
        self.confirmacion = ttk.Entry(root, font=("Times", 14))
        self.confirmacion.pack(pady=10)
        self.confirmacion.config(show="*")
        
        self.registrar = tk.Button(root, text="Registrar", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=self.guardar_registro)
        self.registrar.pack(pady=20)

    def guardar_registro(self):
        usuario = self.usuario.get()
        contrasena = self.password.get()
        correo = self.correo.get()
        confirmacion = self.confirmacion.get()

        if contrasena != confirmacion:
            messagebox.showerror(message="Las contraseñas no coinciden.", title="Error")
            return

        # Abre el archivo CSV en modo de escritura
        with open('registros.csv', mode='a', newline='') as file:
            writer = csv.writer(file)

            # Escribe la información del usuario en el archivo CSV
            writer.writerow([usuario, contrasena, correo])

        messagebox.showinfo(message="Registro exitoso.", title="Éxito")
