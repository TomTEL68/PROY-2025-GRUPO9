import network
import time

ssid = "Matta_543_2.4G"
password = "Casucha99#"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print("Conectando a red Wi-Fi...")
    wlan.connect(ssid, password)
    timeout = 15
    while not wlan.isconnected() and timeout > 0:
        time.sleep(1)
        timeout -= 1

if wlan.isconnected():
    print("Conectado:", wlan.ifconfig())
else:
    print("No se pudo conectar al Wi-Fi")