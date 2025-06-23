# PROY-2025-GRUPO9


Repositorio del grupo 9 para el proyecto del ramo *Proyecto Inicial* – 2025.

## 👥 Integrantes del grupo

| Nombre y Apellido | Usuario GitHub | Correo USM               | Rol          |
| ----------------- | -------------- | ------------------------ | ------------ |
| TOMAS CARVAJAL    | @TomTEL68      | tcarvajalm@usm.cl        | 202530010-9  |
| ZINEDINE ARJEL    | @Zizager       | zarjel@usm.cl            | 202530015-k  |
| CARLOS PEÑA Y LILLO | @Carlos200717| cpenaylilloc@usm.cl      | 20253004-4   |
| CARLO MAGNO       | @Cmagno69      | cmagno@usm.cl            | 202530016-8  |
| SCARLETT MEDINA   | @scarlett999   | smedinab@usm.cl          | 202530043-5  |
---

## 📝 Descripción breve del proyecto

Nuestro proyecto consiste en el desarrollo de un corrector de postura utilizando la Raspberry Pi Pico W.El
dispositivo estará diseñado para monitorear la posición de la espalda del usuario en tiempo real mediante sensores,y alertará
 al usuario para que corriga y logre una posición adecuada,con el fin de prevenir molestias físicas.

---

## 🎯 Objetivos

- Objetivo general:
  - Desarrollar un dipositivo pequeño y portatil que ayude a mejorar la postura de una persona enviando alertas caundo detecte que este encorvada o adoptando una mala postura.
- Objetivos específicos:
  - Desarrollar el sistema de detección de postura mediante sensores, que identifiquen cuando la persona adopta una mala postura.
  - Programar una alerta automática que se active cuando la persona esta en una mala postura durante una X cantidad de tiempo.
  - Crear un prototipo funcional del dispositivo a desarrollar que sea pequeño, liviano y cómodo de llevar.
  - Optimizar el consumo de energía del dispositivo para garantizar una autonomía minima sin la necesidad de recargarlo frecuentemente.
---

## 🧩 Alcance del proyecto

> El proyecto busca mejorar la postura de los profesores y estudiantes que pasan mucho tiempo en escritorios, aunque puede ser usado por todas las personas que lo necesiten. Algunas limitaciones del proyecto es que no podrá utilizarse al momento de dormir por no ser lo suficiente mente resistente pata soportar nuestro peso. Algunas mejoras a futuro son una aplicación que muestre como va tu postura a lo largo del día y una función que te ayude con la postura de algunos ejercicios.

---

## 🛠️ Tecnologías y herramientas utilizadas

- Lenguaje(s) de programación:
  - Micropython 
- Microcontroladores
  - Raspberry Pi Pico W 2
- Sensores
  - MPU6050
- Actuadores
  - Buzzer
- Fuente de alimentación
   - Power bank 5V
---

## 🗂️ Estructura del repositorio

```
/PROY-2025-GRUPOX
│
├── docs/               # Documentación general y reportes
├── src/                # Código fuente del proyecto
├── tests/              # Casos de prueba
├── assets/             # Imagenés, diagramas, etc.
└── README.md           # Este archivo
```

---

## 🧪 Metodología

> *Describir la metodología de desarrollo del proyecto (ágil, en cascada, prototipado, etc.). También puedes incluir el flujo de trabajo con Git (feature branches, pull requests, etc.).*

---

## 📝 Instrucciones de uso
Preparación
 
 Paso 1:
 
  - Instalar micropython en la Raspberry Pi Pico 2 w 
 
 Paso 2:
 
  - Descargar el editor de codigo Thonny

 Paso 3:
 
  - Copia los archivos y librerías en una carpeta o arrastralos directamente a Thonny

Bot de Telegram:
 - Abre Telegram.

 - Busca y abre el bot @BotFather.

 - Escribe /start y luego /newbot.

 - Sigue las instrucciones para:

   - Darle un nombre (ej: MiPrimerBot)

   - Crear un usuario (ej: miprimermibot_bot)

  - El bot te dará un TOKEN, algo como:

    > 123456789:ABCdefGhIjk-LMnopQRstUVwxyz123456789

Chat ID del bot:

- Envía un mensaje cualquiera a tu bot
- Ahora en tu navegador copia este link y reemplaza el token en el lugar correspondiente:

  > https://api.telegram.org/botTU_TOKEN_AQUÍ/getUpdates

  * Coloca tu token donde dice "TU_TOKEN_AQUÍ"

- Luego aparecerá un monton de información, pero habra un apartado que dice "Chat:" y cerca de ahí encontrarás algo que dice "id", ese será tu chat id así que deberás reemplazarlo en la parte correspondiente del codigo "mensaje_bot.py"
 
Conexión:

> Guiate con la datasheet y el pinout que se encuentran en la sección "assets"

  MPU6050
 | Pin GPIO (Raspberry)  | Posición física (Raspberry) | En MPU6050  |
 | --------------------- | --------------------------- | ----------- |
 |         GND           |              38             |      GND    |
 |       3V3(OUT)        |              36             |      VCC    |
 |         GP21          |              27             |      SCL    |
 |         GP20          |              26             |      SDA    |

  Buzzer Activo ("2 patas")
 | Pin GPIO (Rasperry) | Posición física (Raspberry) |  En Buzzer  |
 | ------------------- | --------------------------- | ----------- |
 |        GP15         |              20             |  Pata larga | 
 |        GND          |              18             |  Pata corta |

Ahora si quieres que la raspberry funcione sin la necesidad de tu computador debes hacer lo siguiente:
 - Primero: Sube el archivo main.py y las librerias a la raspberry
 - Segundo: Obten una power bank de 5V

Eso es todo lo que hay que hacer para que la raspberry funcione de manera autonoma.

Consideraciones:
 - La raspberry Pi Pico 2 w funciona solo con una banda de 2.4 GHz, una banda de 5 GHz no funciona, al menos en este modelo. (Para el caso del wifi)
 - El proyecto actualmente no tiene un reloj sincronizado a tiempo real, si no que está hecho para que envie el reporte despues de cierta cantidad de horas desde que se encendió, este tiempo se puede cambiar en la sección de reporte diario en "inclinacion_v2.py".
---
## 🖥️ Documentos y Presentaciones
[Presentacion 1](https://docs.google.com/presentation/d/1vpTP30czPQ5rnJlemLcHhbLzSoCb2XOXyMoU7RWRpfY/edit?slide=id.g27b320635fe_0_0#slide=id.g27b320635fe_0_0)

---
## 📅 Cronograma de trabajo


[Carta Gantt](https://docs.google.com/spreadsheets/d/1owv-qJoIXr2M_csk8ziTQ3kosMEWWK-S/edit?usp=sharing&ouid=104960101161963807007&rtpof=true&sd=true)

---

## 📚 Bibliografía

[Enlace](https://google.com)

---

## 📌 Notas adicionales

> *Espacio para dejar cualquier comentario útil, como pendientes, acuerdos del grupo, consideraciones especiales, etc.*
