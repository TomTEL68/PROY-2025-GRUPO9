import machine
import time
import math
from mpu6050 import MPU6050
from mensaje_bot import alerta_telegram
from tiempo import obtener_hora_simulada

# Configurar I2C
i2c = machine.I2C(0, scl=machine.Pin(21), sda=machine.Pin(20))

# Inicializar MPU6050
mpu = MPU6050(i2c)
mpu.wake()

# Configurar BUZZER
buzzer = machine.Pin(15, machine.Pin.OUT)

def Sonido_buzzer(tiempo=0.5):
    buzzer.value(1)
    time.sleep(tiempo)
    buzzer.value(0)

def calcular_inclinacion_x(ax, ay, az):
    angulo_x = math.degrees(math.atan2(ay, az))  # Usamos el eje Y y Z para calcular X
    return angulo_x

def detectar_mala_postura(angulo_x):
    rango_buena_postura_min = 70
    rango_buena_postura_max = 110
    return angulo_x < rango_buena_postura_min or angulo_x > rango_buena_postura_max

# ⏰ Temporizador para evitar enviar mensajes seguidos
tiempo_ultimo_envio = 0
intervalo_envio = 2  

#Variables del temporizador que detecta la mala postura
contador_mala_postura = 0 
en_mala_postura = False
tiempo_inicio_mala_postura = None
tiempo_espera_alerta = 1.5
tiempo_en_mala_postura = 0

#Variables para detectar la hora actual
segundos_inicio_sistema = time.time()
hora_inicio_real = (0, 0, 0)

# Variables para el envio del reporte
reporte_enviado = False
while True:
    try:
        ax, ay, az = mpu.read_accel_data()

        if ax == 0 and ay == 0 and az == 0:
            print("Lecturas inválidas del MPU6050 (0, 0, 0). Reiniciando sensor...")
            mpu = MPU6050(i2c)
            mpu.wake()
            continue

    except Exception as e:
        print("Error leyendo del MPU6050:", e)
        try:
            mpu = MPU6050(i2c)
            mpu.wake()
            print("MPU6050 reiniciado.")
        except Exception as e2:
            print("Fallo al reiniciar el MPU6050:", e2)
        continue  

    inclinacion_x = calcular_inclinacion_x(ax, ay, az)
    mala_postura = detectar_mala_postura(inclinacion_x)

    if mala_postura:
        if not en_mala_postura:
            tiempo_inicio_mala_postura = time.time()
            en_mala_postura = True
        else:
            duracion = time.time() - tiempo_inicio_mala_postura
            if duracion >= tiempo_espera_alerta:
                buzzer.value(1) 
                time.sleep(0.5)
                buzzer.value(0)
                print("¡Mala postura mantenida por {} segundos! Conteo: {}".format(int(duracion), contador_mala_postura))

                
    else:
        if en_mala_postura:
            duracion_total = time.time() - tiempo_inicio_mala_postura
            if duracion_total >= tiempo_espera_alerta:
                tiempo_en_mala_postura += duracion_total
                contador_mala_postura += 1
                #print("Fin de mala postura. Duró {:.1f} segundos".format(duracion_total))
        en_mala_postura = False
        tiempo_inicio_mala_postura = None
        buzzer.value(0)

    print("Inclinación X: {:.2f}°".format(inclinacion_x))
    
    print("-----------------------------")
#----------------------------------------------------------------
          #CODIGO DEL REPORTE DIARIO
    hora_actual = obtener_hora_simulada(segundos_inicio_sistema, hora_inicio_real)

    if hora_actual == (0, 2, 0) and not reporte_enviado: # Aquí puedes cambiar según cuanto tiempo quieres que te envíe el reporte desde que se conectó el proyecto. SOLO CAMBIA LA PARTE DE (0, 2, 0) donde el primero son las horas, despues lo minutos y por ultimo los segundos.
        tiempo_minutos = int(tiempo_en_mala_postura // 60) #Nosotros lo tenemos en 2 [min] para que la presenteción sea más rápida, pero un temporizador de 5, 9, o 12 [hrs] debería ser suficiente (esto es generoso ya que la bateria deberia durar unas 20 [hrs] minimo)
        tiempo_segundos = int(tiempo_en_mala_postura % 60)
        mensaje_de_reporte = f"""Aqui tienes tu reporte diario:
- Numero de malas posturas en total: {contador_mala_postura}
- Tiempo total en malas posturas: {tiempo_minutos} minutos y {tiempo_segundos} segundos"""
        print("Tu reporte está listo")
        try:
            alerta_telegram(mensaje_de_reporte)
            reporte_enviado = True
            tiempo_ultimo_envio = time.time()
            
        except Exception as e:
            print("Error al enviar mensaje por Telegram:", e)
            
        print(mensaje_de_reporte)
        
    time.sleep(0.5)  
    