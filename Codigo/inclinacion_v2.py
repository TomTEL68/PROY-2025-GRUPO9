import machine
import time
import math
from mpu6050 import MPU6050

# Configurar I2C
i2c = machine.I2C(0, scl=machine.Pin(21), sda=machine.Pin(20))

# Inicializar MPU6050
mpu = MPU6050(i2c)
mpu.wake()

# Configurar LED
led = machine.Pin(15, machine.Pin.OUT)

def calcular_inclinacion_x(ax, ay, az):
    # Calcula el ángulo de inclinación solo en el eje X en grados
    angulo_x = math.degrees(math.atan2(ay, az))  # Usamos el eje Y y Z para calcular X
    
    return angulo_x

def detectar_mala_postura(angulo_x):
    # Definir el rango correcto de inclinación en el eje X (en grados)
    rango_buena_postura_min = -110
    rango_buena_postura_max = -70
    
    # Detectar mala postura si está fuera del rango
    if angulo_x < rango_buena_postura_min or angulo_x > rango_buena_postura_max:
        return True   # Mala postura
    
    return False  # Buena postura

while True:
    # Leer acelerómetro
    ax, ay, az = mpu.read_accel_data()
    
    # Calcular inclinación solo en el eje X
    inclinacion_x = calcular_inclinacion_x(ax, ay, az)
    
    # Detección de mala postura
    mala_postura = detectar_mala_postura(inclinacion_x)
    
    if mala_postura:
        led.on()
        print("¡Mala postura detectada!")
    else:
        led.off()
    
    print("Inclinación X: {:.2f}°".format(inclinacion_x))
    print("-----------------------------")
    
    time.sleep(0.5)
