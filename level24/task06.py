import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações
smtp_server = 'smtp.example.com'
smtp_port = 587
username = 'your_email@example.com'
password = 'your_password'
from_email = 'your_email@example.com'
to_email = 'recipient@example.com'
subject = 'Assunto do email'
body = 'Este é o corpo do email'

# Criação da mensagem
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Conexão com o servidor SMTP e envio do email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Estabelece uma conexão TLS
    server.login(username, password)
    server.sendmail(from_email, to_email, msg.as_string())
    print("Email enviado com sucesso")
except Exception as e:
    print(f"Erro ao enviar o email: {e}")
finally:
    server.quit()