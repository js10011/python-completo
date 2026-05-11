import pickle

# Objeto para serialização
student_info = {
    'name': 'John Doe',
    'age': 20,
    'status': 'student'
}

# Serialização do objeto
with open('student_info.pkl', 'wb') as f:
    pickle.dump(student_info, f)

# Desserialização do objeto
with open('student_info.pkl', 'rb') as f:
    loaded_student_info = pickle.load(f)

print(loaded_student_info)