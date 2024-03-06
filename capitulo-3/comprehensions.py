import random

lista_de_numeros = list(range(1, 100))

print(lista_de_numeros)

pares = [numero for numero in lista_de_numeros if numero % 2 == 0]
print(pares)

#Diccionario Comprehension

student_uid = [1, 2, 3]
students = ['Juan', 'Jose', 'Ricardo']
students_with_uid = {uid: student for uid, student in zip(student_uid, students)}
print(students_with_uid)

#Set Comprehension
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1,3))

print(random_numbers)