import pandas as pd
import random
import time

def generar_letras_aleatorias():
    letras = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in ['j', 's', 'ñ', 'z']]
    letras_aleatorias = random.sample(letras, 10)
    random.shuffle(letras_aleatorias)
    return letras_aleatorias

def actualizar_lista_en_csv(letras):
    try:
        # Cargar el archivo CSV
        ruta_csv = "common_letter.csv"
        df = pd.read_csv(ruta_csv)

        # Borrar y renovar la columna "c"
        df["letras"] = [",".join(map(str, letras))]

        # Guardar el DataFrame de nuevo en el archivo CSV
        df.to_csv(ruta_csv, index=False)

    except Exception as e:
        print(f"Error al actualizar la lista en el archivo CSV: {e}")

def mostrar_letras_cada_10_segundos(letras):
    for letra in letras:
        print(letra)
        time.sleep(1)  # Pausa la ejecución durante 1 segundo

    # Cuando se acaban las letras, imprimir timeout
    print("timeout:#")

if __name__ == "__main__":
    letras_aleatorias = generar_letras_aleatorias()
    actualizar_lista_en_csv(letras_aleatorias)
    mostrar_letras_cada_10_segundos(letras_aleatorias)