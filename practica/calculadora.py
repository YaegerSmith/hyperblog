print("Calculadora que suma, resta, multiplica y divide")

print("Menú de opciones.")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion = float(input("Ingrese la opción deseada: "))
if opcion == 1:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("La suma es: ", num1 + num2)
elif opcion == 2:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("La resta es: ", num1 - num2)
elif opcion == 3:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("La multiplicación es: ", num1 * num2)
    
elif opcion == 4:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("La división es: ", num1 / num2)
    
else:
    print("Opción no válida")