import time

def obtener_hora_simulada(segundo_inicio_sistema, hora_inicio):
    delta = time.time() - segundo_inicio_sistema
    total_segundos = hora_inicio[0]*3600 + hora_inicio[1]*60 + hora_inicio[2] + int(delta)
    h = (total_segundos // 3600) % 24
    total_segundos %= 3600
    m = total_segundos // 60
    s = total_segundos % 60
    return (h, m, s)
