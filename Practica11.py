# Como usar tuplas.
nombres = ("David", "Micaela", "lucia", "julieta" )
numeros = (1, 2, 3, 4, 5)
valor = (True, False, True)
comvinados = ( "David", 2, 4, True, False)

#Acceder a elementos de una tupla. 
#print(nombres[1])



#Actualizar una tupla
#x = list(nombres)
#x[1] = "Cristina"
#nombres = tuple(x)

#print(nombres)

#x = list(comvinados)
#x[3] = "Cristina"
#comvinados = tuple(x)

#print(comvinados)

#Desempaquetar una tupla.
#(uno, dos, tres, cuatro, cinco) = numeros
#print(uno)



#Metodos de una tupla count(), index()
print(numeros.count(2))
print(numeros.index(5))