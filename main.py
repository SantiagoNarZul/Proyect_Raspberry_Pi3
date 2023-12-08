import RPi.GPIO as GPIO
import time
from datetime import datetime
from modulos import sensores_sala, sensor_habitacion, sensores_cocina, email

GPIO.setwarnings(False)
# Configura el modo de la GPIO
GPIO.setmode(GPIO.BCM)

#Banderas
alarma_on = 0

# Configura el número del pin GPIO que deseas usar
habilitador_alarma = 4
led_alarma = 20

#Configurar el pin 4 como entrada
GPIO.setup(habilitador_alarma, GPIO.IN)
# Configura el pin 20 como salida
GPIO.setup(led_alarma, GPIO.OUT)


while True:
    valor_habilitador_alarma = GPIO.input(habilitador_alarma)

    if (valor_habilitador_alarma == 1 and alarma_on == 0):
        alarma_on = 1
        email.enviar_email("Alarma Activa")
    elif (valor_habilitador_alarma == 0 and alarma_on == 1):
        alarma_on = 0
        GPIO.output(led_alarma, GPIO.LOW)
        email.enviar_email("Alarma Desactivada")

    if (alarma_on == 1):
        #Sensores generales sala
        valor_ventana_sala, valor_puerta = sensores_sala.lectura_sensores()
        #Sensor habitacion
        valor_ventana_habitacion = sensor_habitacion.lectura_sensores()
        #Sensor cocina
        valor_sensor_gas, valor_sensor_incendio = sensores_cocina.lectura_sensores()

        if valor_ventana_sala == 1 or valor_puerta == 1 or valor_ventana_habitacion == 1 or valor_sensor_gas == 1 or valor_sensor_incendio == 1:
            GPIO.output(led_alarma, GPIO.HIGH)
            # Crea un mensaje con los sensores activados
            sensores_activados = []
            if valor_ventana_sala == 1:
                sensores_activados.append("Sensor de Ventana Sala")
            if valor_puerta == 1:
                sensores_activados.append("Sensor de Puerta")
            if valor_ventana_habitacion == 1:
                sensores_activados.append("Sensor de Ventana Habitación")
            if valor_sensor_gas == 1:
                sensores_activados.append("Sensor de Gas")
            if valor_sensor_incendio  == 1:
                sensores_activados.append("Sensor de Incendio")
            mensaje = " y ".join(sensores_activados) + " activados - Alarma Raspberry Pi 3B"
            email.enviar_email(mensaje)

    elif (alarma_on == 0):
        GPIO.output(led_alarma, GPIO.LOW)