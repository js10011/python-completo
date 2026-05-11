import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Dados para conexão com o servidor de e-mail
SMTP_SERVER = 'smtp.example.com'          # Endereço do servidor SMTP
SMTP_PORT = 587                            # Porta SMTP
EMAIL_ADDRESS = 'youremail@example.com'    # Seu endereço de e-mail
EMAIL_PASSWORD = 'yourpassword'            # Senha da sua conta de e-mail
TO_EMAIL = 'recipient@example.com'         # Endereço do destinatário

# Função para enviar e-mail
def send_email():
    try:
        # Criação da mensagem de e-mail
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = TO_EMAIL
        message['Subject'] = 'Lembrete do relatório semanal'

        # Texto da mensagem
        body = 'Hora de enviar o relatório semanal'
        message.attach(MIMEText(body, 'plain'))

        # Conexão com o servidor e envio do e-mail
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Conexão segura
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(message)
        server.quit()

        print("Mensagem enviada com sucesso")
    except Exception as e:
        print(f"Falha ao enviar mensagem: {e}")

# Configuração do agendamento: envio do e-mail toda semana na segunda-feira às 10:00
schedule.every().monday.at("10:00").do(send_email)

# Loop principal para executar tarefas agendadas
while True:
    schedule.run_pending()  # Verifica e executa tarefas agendadas para o horário atual
    time.sleep(60)  # Pausa de 60 segundos para reduzir carga do processador