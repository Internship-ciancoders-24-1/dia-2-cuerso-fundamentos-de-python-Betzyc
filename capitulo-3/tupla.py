#Las tuplas no se pueden modificar
a = 1,2,3
a = (1,2,3)
print(type(a))

print(a[0])
print(a[1])
print(a[2])

print(a.index(1))   #Devuelve el indice del valor
print(a.count(2))   #Devuelve la cantidad de veces que aparece el valor



#Los set, no tienen orden por ende no usan index
a=set([1,2,3])
b={3,4,5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))



