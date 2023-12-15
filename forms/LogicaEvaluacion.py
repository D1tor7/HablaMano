import pandas as pd
import random
import time

def generar_letras_aleatorias():
    letras_permitidas = ['A', 'C', 'U', 'V', 'Y', 'L', 'O', 'W', 'X', 'I']
    letras_aleatorias = random.sample(letras_permitidas, 10)
    random.shuffle(letras_aleatorias)
    return letras_aleatorias

def actualizar_lista_en_csv(letras, ruta_csv):  
    try:
        df = pd.read_csv(ruta_csv)
        df["letras"] = [",".join(map(str, letras))]
        df.to_csv(ruta_csv, index=False)
    except Exception as e:
        print(f"Error al actualizar la lista en el archivo CSV: {e}")

def mostrar_letras_cada_10_segundos(letras):
    for letra in letras:
        print(letra)
        time.sleep(1)

    print("timeout:#")

if __name__ == "__main__":
    letras_aleatorias = generar_letras_aleatorias()
    actualizar_lista_en_csv(letras_aleatorias, "common_letter.csv")
    mostrar_letras_cada_10_segundos(letras_aleatorias)