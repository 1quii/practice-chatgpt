# Ejercicio 1
nombre ="Me llamo Antonio"
edad="Tengo 30 años"
altura="Mido 1.60 metros"

print(nombre)
print(edad) 
print(altura)

# Ejercicio 2
masa=75
velocidad=20

Ec= (masa * velocidad**2) / 2
print("La energia cinetica es:", Ec)

# Ejercicio 3
nota=float(input("Ingrese la nota del estudiante: "))
if nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")

#Ejercicio 4
nota1=int(input("Ingrese una nota: "))
nota2=int(input("Ingrese otra nota: "))
nota3=int(input("Ingrese una tercera nota: "))
promedio=(nota1 + nota2 + nota3) / 3
if promedio >= 9:
    print("Excelente")
elif promedio >= 7 and promedio < 9:
    print("Notable")
elif promedio >= 5 and promedio < 7:
    print("Aprobado")
else:
    print("Suspenso")
