# For es para listas, tuplas y diccionarios.


dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

# Ejemplo de FOR con listas.
for x in dias:
    print(x)
print("----o----")

# Ejemplo de FOR con BREAK. 
for x in dias:
    print(x)
    if x == "viernes":
        break
print("----o----")

# Ejemplo FOR con excepcion.
for x in dias:
    if x == "viernes":
        break
    print(x)

print("----o----")

# Ejemplo FOR de repeticion.
numero = 10
for x in range(numero):
    print("hola")
else:
    print("fin del ejemplo")

