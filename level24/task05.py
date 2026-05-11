import poplib
from email.parser import BytesParser
from email.policy import default

# Servidor POP3 e credenciais
POP3_SERVER = 'pop.example.com'
POP3_PORT = 110
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Conexão ao servidor POP3 e autenticação
mailbox = poplib.POP3(POP3_SERVER, POP3_PORT)
mailbox.user(USERNAME)
mailbox.pass_(PASSWORD)

# Obtenção da lista de e-mails
num_messages = len(mailbox.list()[1])

# Se houver e-mails, obtém o conteúdo do último
if num_messages > 0:
    response, lines, octets = mailbox.retr(num_messages)
    message_content = b'\r\n'.join(lines)

    # Parsing do e-mail
    message = BytesParser(policy=default).parsebytes(message_content)
    
    # Exibição do conteúdo do último e-mail
    print(f"Subject: {message['subject']}")
    print(f"From: {message['from']}")
    print(f"To: {message['to']}")
    print(f"Date: {message['date']}")
    print("\nBody:\n")
    if message.is_multipart():
        for part in message.iter_parts():
            if part.get_content_type() == "text/plain":
                print(part.get_payload(decode=True).decode(part.get_content_charset()))
    else:
        print(message.get_payload(decode=True).decode(message.get_content_charset()))

# Fechamento da conexão
mailbox.quit()