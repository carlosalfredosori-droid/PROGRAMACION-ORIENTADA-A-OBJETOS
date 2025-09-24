# Elavoracion de una calculadora basica 
def calculadora():
    while True:
        print("\n--- Calculadora ---")
        print("1. Suma")
        print("2. Multiplicacion")
        print("3. División")
        print("4. Resta")
        print("5. Salir")
        
        opcion = input("Ingrese la opción deseada: ")
        
        # Validar si la opción es un número y si está en el rango
        if opcion.isdigit():
            opcion = int(opcion)
            
            if opcion == 5:
                print("¡Gracias por usar la calculadora! Saliendo...")
                break  # Sale del bucle
            # opereaciones logicos 
            if opcion >= 1 and opcion <= 5:
                try:
                    num1 = float(input("Ingrese el primer numero: "))
                    num2 = float(input("Ingrese el segundo numero: "))
                    
                    if opcion == 1:
                        print(f"{num1} + {num2} = {num1 + num2}")
                    elif opcion == 2:
                        print(f"{num1} * {num2} = {num1 * num2}")
                    elif opcion == 3:
                        if num2 != 0:
                            print(f"{num1} / {num2} = {num1 / num2}")
                        else:
                            print("¡Error! No se puede dividir por cero.")
                    elif opcion == 4:
                        print(f"{num1} - {num2} = {num1 - num2}")
                        #en caso de no poner los datos corretos 
                except ValueError:
                    print("¡Entrada no válida! Por favor, ingrese solo numeros.")
            else:
                print("Opción no válida. Por favor, elija una opción del 1 al 5.")
        else:
            print("Entrada no válida. Por favor, ingrese un numero.")

calculadora()