import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# Configura el modo de la GPIO
GPIO.setmode(GPIO.BCM)

sensor_gas = 8
sensor_incendio = 7

GPIO.setup(sensor_gas, GPIO.IN)
GPIO.setup(sensor_incendio, GPIO.IN)

def lectura_sensores():

    valor_sensor_gas = GPIO.input(sensor_gas)
    valor_sensor_incendio = GPIO.input(sensor_incendio)

    return valor_sensor_gas, valor_sensor_incendio