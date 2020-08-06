#código que permite o cofre enviar um alerta para o proprietário caso uma pessoa não reconhecida tente abrir o cofre ou algum movimento anormal for detectado

import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_alert(path_to_image, movement):
    #emails a serem utilizados
    email_user = 'usuario@gmail.com'
    email_password = 'senha'
    email_send = 'usuario2@gmail.com'

    #assunto do email
    subject = ''
    body = ''

    # parametro movement = 0, alerta pra pessoa não reconhecida
    # parametro movement = 1, movimento anormal detectado
    if movement is 0:
        subject = 'Alerta! Tentativa de acesso ao cofre nao autorizada.'
        body = 'Esta tentativa de acesso está em : {} '.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    elif movement is 1:
        subject = 'Alerta!Movimento anormal detectado pelo cofre.'
        body = 'O cofre detectou movimento anormal em: {}\n Foto tirada abaixo:.'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

    #Formulação do email
    msg = MIMEMultipart()
    msg['De'] = email_user
    msg['Para'] = email_send
    msg['Assunto'] = subject

    #Anexar ao corpo do email
    msg.attach(MIMEText(body, 'plain'))

    #Carrega e abre uma imagem
    filename = path_to_image
    attachment = open(filename, 'rb')

    #Anexa a imagem ao email como anexo
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)

    #Anexa o email e informações do servidor de email do remetente como anexo
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    #Manda o email
    server.sendmail(email_user, email_send, text)
    server.quit()