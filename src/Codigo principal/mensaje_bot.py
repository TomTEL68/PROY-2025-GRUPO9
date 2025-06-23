import urequests
import Wifi

BOT_TOKEN = "8195083435:AAFsIF97ztL0mvbJSz6O6BNGgjR2S31fClw"
CHAT_ID = "-4807170489"

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
