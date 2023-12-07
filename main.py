import RPi.GPIO as GPIO
import time
from email.message import EmailMessage
import smtplib
from datetime import datetime

GPIO.setwarnings(False)
# Configura el modo de la GPIO
GPIO.setmode(GPIO.BCM)

# Configura el número del pin GPIO que deseas usar
led_pin = 18

# Configura el pin como salida
GPIO.setup(led_pin, GPIO.OUT)

# Enviar correo desde raspberry
remitente = "mateo.lasso@correounivalle.edu.co"
destinatarios = ["santiago.narvaez@correounivalle.edu.co", "dayron.ramirez@correounivalle.edu.co"]

mensaje = "Hola desde Raspberry Pi 3B"

for destinatario in destinatarios:
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Alarma Raspberry:"
    email.set_content(mensaje)
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente, "pexb kpdq wnbu rayr")

    smtp.sendmail(remitente, destinatario, email.as_string())

    smtp.quit()


while True:
    # Enciende el LED
    print("Led encendido")
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(1)  # Espera 1 segundo

    # Apaga el LED
    print("Led apagado")
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(1)  # Espera 1 segundo
