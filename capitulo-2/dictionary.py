rae ={}

rae['piza'] = 'Comida italiana'
rae['pasta'] = 'Comida deliciosa'

#print(rae)
a=rae.get('piza',None)
print(a)

rae.keys()
rae.values()
rae.items()

for key in rae.keys():
    print(key)

for value in rae.values():  
    print(value)

for key, value in rae.items():
    print(key, value)