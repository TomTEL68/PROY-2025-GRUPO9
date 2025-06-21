import machine
import time
import math
from mpu6050 import MPU6050
from mensaje_bot import alerta_telegram

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
    rango_buena_postura_min = -110
    rango_buena_postura_max = -70
    return angulo_x < rango_buena_postura_min or angulo_x > rango_buena_postura_max

def contador_malas_postura():
    contador_mala_postura = 0
    
# ⏰ Temporizador para evitar enviar mensajes seguidos
tiempo_ultimo_envio = 0
intervalo_envio = 60  # en segundos

while True:
    try:
        ax, ay, az = mpu.read_accel_data()

        # chequea si el mpu6050 da grados en 0 y reinicia sensor
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
        Sonido_buzzer(0.5)
        time.sleep(2)
        print("¡Mala postura detectada!")
        contador_mala_postura += 1
        
        tiempo_actual = time.time()
        if tiempo_actual - tiempo_ultimo_envio > intervalo_envio:
            try:
                alerta_telegram("Tienes una mala postura")
                tiempo_ultimo_envio = tiempo_actual
            except Exception as e:
                print("Error al enviar mensaje por Telegram:", e)

    else:
        buzzer.value(0)

    print("Inclinación X: {:.2f}°".format(inclinacion_x))
    print("-----------------------------")
    time.sleep(0.5)
 