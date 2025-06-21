import urequests
import Wifi

# No se si era necesario pero quité estos datos por si acaso :)
BOT_TOKEN = "Bot Token"
CHAT_ID = "Chat ID"

def alerta_telegram(mensaje):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    datos = {
        "chat_id": CHAT_ID,
        "text": mensaje
    }

    try:
        r = urequests.post(url, json=datos)
        print("Mensaje enviado")
        r.close()
    except Exception as e:
        print("Error al enviar mensaje por Telegram:", e)
