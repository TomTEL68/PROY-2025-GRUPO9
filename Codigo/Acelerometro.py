from machine import ADC, Pin
import time

# Configura ADCs
x_pin = ADC(26)  # GP26
y_pin = ADC(27)  # GP27
z_pin = ADC(28)  # GP28

# Filtro: promedio de 20 muestras
def leer_filtrado(adc, muestras=20):
    total = 0
    for _ in range(muestras):
        total += adc.read_u16()
        time.sleep_ms(2)  # Pequeño delay para evitar ruido inmediato
    return total / muestras

while True:
    x = leer_filtrado(x_pin)
    y = leer_filtrado(y_pin)
    z = leer_filtrado(z_pin)
    
    print("X:", x, " Y:", y, " Z:", z)
    time.sleep(1)
