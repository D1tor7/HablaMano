# test_form_master.py
import pytest
from form_master import MasterPanel
import tkinter as tk

@pytest.fixture
def master_panel():
    usuario_actual = "test_user"
    return MasterPanel(usuario_actual)

def test_contador_actual(master_panel):
    master_panel.contador_segundos = 5
    master_panel.actualizar_contador()
    assert master_panel.etiqueta_contador.cget("text") == "Tiempo restante: 5 segundos"

def test_detener_contador_actual(master_panel):
    master_panel.contador_segundos = 5
    master_panel.actualizar_contador()
    master_panel.detener_contador_actual()
    assert "Tiempo restante: 5" in master_panel.etiqueta_contador.cget("text")

def test_verificar_letra_correcta(master_panel):
    master_panel.etiqueta_mensaje = tk.Label(master_panel.ventana, text="", font=("Times", 12), bg="#fcfcfc", fg="#666a88", anchor="w")
    master_panel.etiqueta_mensaje.place(x=10, y=200, anchor="w")
    master_panel.etiqueta_letra_mas_comun = tk.Label(master_panel.ventana, text="", font=("Times", 12), bg="#fcfcfc", fg="#666a88", anchor="w")
    master_panel.etiqueta_letra_mas_comun.place(x=10, y=170, anchor="w")
    master_panel.etiqueta_letra_mas_comun.config(text="Letra más común: A")
    master_panel.verificar_letra(['A'], 'A', 0)
    assert master_panel.puntaje == 10
    assert master_panel.etiqueta_mensaje.cget("text") == "Correcto"

def test_verificar_letra_incorrecta(master_panel):
    master_panel.etiqueta_mensaje = tk.Label(master_panel.ventana, text="", font=("Times", 12), bg="#fcfcfc", fg="#666a88", anchor="w")
    master_panel.etiqueta_mensaje.place(x=10, y=200, anchor="w")
    master_panel.etiqueta_letra_mas_comun = tk.Label(master_panel.ventana, text="", font=("Times", 12), bg="#fcfcfc", fg="#666a88", anchor="w")
    master_panel.etiqueta_letra_mas_comun.place(x=10, y=170, anchor="w")
    master_panel.etiqueta_letra_mas_comun.config(text="Letra más común: A")
    master_panel.verificar_letra(['B'], 'B', 0)
    assert master_panel.puntaje == 0
    assert master_panel.etiqueta_mensaje.cget("text") == "Incorrecto"

def test_mostrar_puntuacion(master_panel):
    master_panel.puntaje = 20
    master_panel.mostrar_puntuacion()
    assert master_panel.etiqueta_mensaje.cget("text") == "Puntuación total: 20"
