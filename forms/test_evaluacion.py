import pandas as pd
import pytest
from LogicaEvaluacion import generar_letras_aleatorias, actualizar_lista_en_csv, mostrar_letras_cada_10_segundos

def test_generar_letras_aleatorias():
    letras_aleatorias = generar_letras_aleatorias()
    assert len(letras_aleatorias) == 10
    # Puedes agregar más aserciones según tus requisitos

def test_actualizar_lista_en_csv(tmp_path):
    letras = ['a', 'b', 'c']
    csv_file = tmp_path / "C:/Users/diego/OneDrive/Documentos/GitHub/HablaMano/common_letter.csv"
    actualizar_lista_en_csv(letras, str(csv_file))

    df = pd.read_csv(str(csv_file)) 
    assert len(df) == 1
    assert df['letras'].iloc[0] == 'a,b,c'

def test_mostrar_letras_cada_10_segundos(capsys, monkeypatch):
    letras = ['a', 'b', 'c']
    monkeypatch.setattr('builtins.input', lambda _: 'exit')  # Simula la entrada del usuario

    mostrar_letras_cada_10_segundos(letras)

    captured = capsys.readouterr()
    assert 'a\nb\nc\ntimeout:#\n' == captured.out