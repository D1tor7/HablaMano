import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel
from forms.form_register import RegistrationScreen  # Importa la clase de registro
import csv

class App:
    def __init__(self):
        # Crear un diccionario de usuarios y contraseñas válidos
        self.usuarios_validos = {"root": "1234"}

        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesión")
        self.ventana.geometry("800x500")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)
        
        
        logo=utl.leer_imagen("./imagenes/logo.png",(200,200))
        
        #frame_logo
        frame_logo=tk.Frame(self.ventana,bd=0,width=300,relief=tk.SOLID,padx=10,pady=10,bg="#3a7ff6")
        frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        label=tk.Label(frame_logo,image=logo,bg="#3a7ff6")
        label.place(x=0,y=0,relwidth=1,relheight=1)
        
        #frame_form
        frame_form=tk.Frame(self.ventana,bd=0,relief=tk.SOLID,bg="#fcfcfc")
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frameform
        
        #frame_form_top
        frame_form_top=tk.Frame(frame_form,bd=0,height=50,relief=tk.SOLID,bg="black")
        frame_form_top.pack(side="top",fill=tk.X)
        title=tk.Label(frame_form_top,text="Inicio de sesion",font=("Times",30),fg="#666a88",bg="#fcfcfc",pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top
        
        #frame_form_fill
        frame_form_fill=tk.Frame(frame_form,bd=0,height=50,relief=tk.SOLID,bg="#fcfcfc")
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)
        
        etiqueta_usuario=tk.Label(frame_form_fill,text="Usuario",font=("Times",14),fg="#666a88",bg="#fcfcfc",anchor="w")
        etiqueta_usuario.pack(fill=tk.X,padx=20,pady=5)
        self.usuario=ttk.Entry(frame_form_fill,font=("Times",14))
        self.usuario.pack(fill=tk.X,padx=20,pady=10)
        
        etiqueta_password=tk.Label(frame_form_fill,text="Contraseña",font=("Times",14),fg="#666a88",bg="#fcfcfc",anchor="w")
        etiqueta_password.pack(fill=tk.X,padx=20,pady=5)
        self.password=ttk.Entry(frame_form_fill,font=("Times",14))
        self.password.pack(fill=tk.X,padx=20,pady=10)
        self.password.config(show="*")
        
        inicio=tk.Button(frame_form_fill,text="Iniciar Sesion",font=("Times",15,BOLD),bg="#3a7ff6",bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X,padx=20,pady=20)
        inicio.bind("<Return>",(lambda event:self.verificar()))
        
        # Agregar el botón "Registrarse"
        registrarse = tk.Button(frame_form_fill, text="Registrarse", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=self.abrir_registro)
        registrarse.pack(fill=tk.X, padx=20, pady=20)
    
    def abrir_registro(self):
        # Abrir la pantalla de registro
        self.ventana_registro = tk.Toplevel(self.ventana)
        RegistrationScreen(self.ventana_registro)
        
    def verificar(self):
        user = self.usuario.get()
        password = self.password.get()
        
        # Verifica las credenciales con los registros del archivo CSV
        with open('registros.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['usuario'] == user and row['contrasena'] == password:
                    self.ventana.destroy()
                    MasterPanel(user)  # Pasar el nombre de usuario a MasterPanel
                    return
        
        # Si no se encontró coincidencia, muestra un mensaje de error
        messagebox.showerror(message="La contraseña o el usuario ingresado son incorrectos", title="Mensaje")

