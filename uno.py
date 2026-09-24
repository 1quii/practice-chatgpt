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

#Ejercicio 5
for i in range(1, 11):
    print(i)

#Ejercicio 6
def energetic_energy(mass, velocity):
    return (mass * velocity**2) / 2

m1,m2,m3,m4,m5=input("Ingrese 5 masas separadas por comas: ").split(",")
v1,v2,v3,v4,v5=input("Ingrese 5 velocidades separadas por comas: ").split(",")

masses = [float(m1), float(m2), float(m3), float(m4), float(m5)]
velocities = [float(v1), float(v2), float(v3), float(v4), float(v5)]

for i in range(5):
    energy = energetic_energy(masses[i], velocities[i])
    print(f"La energía cinética del objeto {i+1} es: {energy}")

#Ejercicio 7

