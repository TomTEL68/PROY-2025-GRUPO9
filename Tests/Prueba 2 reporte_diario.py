from tiempo import obtener_hora_simulada
import time

segundos_inicio_sistema = time.time()
hora_inicio_real = (9, 42, 0)

while True:
    hora_actual = obtener_hora_simulada(segundos_inicio_sistema, hora_inicio_real)
    
    if hora_actual == (9, 42, 5):
        print("listo capo")
        break  # Si quieres que el código se detenga

    time.sleep(1)  # Espera un segundo antes de volver a revisar
