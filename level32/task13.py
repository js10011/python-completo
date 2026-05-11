import csv

# Definimos o nome do arquivo com o qual vamos trabalhar
filename = 'students.csv'

# Criamos uma lista vazia para armazenar informações sobre os estudantes
students = []

# Leitura de dados dos estudantes do arquivo CSV
with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
    # Criamos um objeto csvreader para ler linhas do arquivo
    csvreader = csv.reader(csvfile)
    # Percorremos cada linha do arquivo
    for row in csvreader:
        # Verificamos se a linha tem exatamente 3 elementos (nome, idade, curso)
        if len(row) == 3:
            # Adicionamos os dados do estudante na lista em forma de dicionário
            students.append({
                'name': row[0],
                'age': row[1],
                'course': row[2]
            })

# Exemplo de adição de um novo estudante
students.append({'name': 'John Doe', 'age': '22', 'course': 'Physics'})

# Gravação dos dados atualizados dos estudantes no arquivo CSV
with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
    # Criamos um objeto csvwriter para gravar linhas no arquivo
    csvwriter = csv.writer(csvfile)
    # Gravamos os dados de cada estudante no arquivo
    for student in students:
        csvwriter.writerow([student['name'], student['age'], student['course']])