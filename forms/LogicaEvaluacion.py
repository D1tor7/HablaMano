# LogicaEvaluacion.py
import random
import time

def generar_letras_aleatorias():
    letras = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in ['j', 's', 'ñ', 'z']]
    letras_aleatorias = random.sample(letras, 10)
    random.shuffle(letras_aleatorias)
    return letras_aleatorias

def mostrar_letras_cada_10_segundos(letras):
    for letra in letras:
        print(letra)
        time.sleep(1)  # Pausa la ejecución durante 10 segundos

    print("timeout:#")  # Cuando se acaban las letras, imprime timeout

if __name__ == "__main__":
    letras_aleatorias = generar_letras_aleatorias()
    mostrar_letras_cada_10_segundos(letras_aleatorias)