# programar para convertir una cantidad a grados centigrados a su equivalencio en Farenheit y Kelvin

# input
c = int(input("digite el valor de c: "))

# processing 
F = ( c * 1.8 +32)
K = ( c + 273.15)

# ouput
print("---------------------------")
print("--------RESULTADOS---------")
print("---------------------------")
print(" la conversion en Farenhell en " + str (F))
print(" la conversion de Kelvin es " + str (K))