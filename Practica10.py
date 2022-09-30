# Cadenas en Python 

nombre = "David"
edad = 22
nombres = """ David 
Mica
Luci
Juli"""

# Trabajar con una cadema.
for x in nombre:
    print(x)

print(len(nombre))
print(nombre * 3)



# Cortar cadena. 
print(nombre[0:2])


# Cadenas y sus metodos: upper(). lower(). replace(). format()
print(nombre.upper())
print(nombre.replace("D", "w"))
print(nombre.format(edad))