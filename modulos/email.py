import smtplib
from email.message import EmailMessage

def enviar_email(dato):
    remitente = "mateo.lasso@correounivalle.edu.co"
    destinatarios = ["santiago.narvaez@correounivalle.edu.co", "dayron.ramirez@correounivalle.edu.co"]

    mensaje = str(dato)

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