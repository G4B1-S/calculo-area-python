import math

# Paso 1: Solicitar al usuario que ingrese el radio del circulo


radio = float(input("Por favor, ingrese el radio del circulo: "))


# Paso 2: Calculamos el area del circulo utilizando la formula area = π * radio^2

area = math.pi * (radio**2)


# Paso 3: Mostrar al usuario el area calculada

print("el area del circulo con radio", radio, "es:", area )