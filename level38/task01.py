import logging

# Configuração do logging
logging.basicConfig(filename='program_log.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Gravação de mensagens no arquivo de log
logging.info('Programa iniciado')
logging.info('Processo em execução')
logging.info('Programa finalizado')