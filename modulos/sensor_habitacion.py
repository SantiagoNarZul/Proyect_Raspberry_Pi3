import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# Configura el modo de la GPIO
GPIO.setmode(GPIO.BCM)

sensor_ventana_habitacion = 24

GPIO.setup(sensor_ventana_habitacion, GPIO.IN)

def lectura_sensores():

    valor_sensor_ventana_habitacion = GPIO.input(sensor_ventana_habitacion)

    return valor_sensor_ventana_habitacion