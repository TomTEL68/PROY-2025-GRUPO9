import urequests

try:
    r = urequests.get("http://clients3.google.com/generate_204")
    print("Conexión OK")
except Exception as e:
    print("Error de conexión:", e)
