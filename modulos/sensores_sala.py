import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# Configura el modo de la GPIO
GPIO.setmode(GPIO.BCM)

sensor_ventana_sala = 23
sensor_puerta_principal = 25

GPIO.setup(sensor_ventana_sala, GPIO.IN)
GPIO.setup(sensor_puerta_principal, GPIO.IN)

def lectura_sensores():

    valor_sensor_ventana = GPIO.input(sensor_ventana_sala)
    valor_sensor_puerta_principal = GPIO.input(sensor_puerta_principal)

    return valor_sensor_ventana, valor_sensor_puerta_principal