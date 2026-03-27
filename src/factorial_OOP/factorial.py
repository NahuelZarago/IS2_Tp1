#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 


# Función para procesar la entrada y calcular factoriales
def procesar_y_calcular(entrada):
    """
    Analiza la entrada (número o rango) y calcula los factoriales correspondientes.
    """
    try:
        if "-" in entrada:
            # Dividir la cadena por el guion
            partes = entrada.split("-")
            
            # Caso: "-10" (desde 1 hasta 10)
            if partes[0] == "":
                inicio, fin = 1, int(partes[1])
            # Caso: "40-" (desde 40 hasta 60)
            elif partes[1] == "":
                inicio, fin = int(partes[0]), 60
            # Caso: "4-8" (desde 4 hasta 8)
            else:
                inicio, fin = int(partes[0]), int(partes[1])
        else:
            # Caso: número único
            inicio = fin = int(entrada)

        # Validar que el inicio no sea mayor al fin
        if inicio > fin:
            print(f"Error: El inicio ({inicio}) no puede ser mayor al fin ({fin}).")
            return

        # Calcular y mostrar resultados
        for n in range(inicio, fin + 1):
            print(f"Factorial de {n}! es {factorial(n)}")

    except ValueError:
        print(f"Error: '{entrada}' no es un formato válido (use números o rangos como 4-8).")

#Lógica Principal

# 1. Si se omite el argumento, solicitarlo manualmente
if len(sys.argv) < 2:
    argumento = input("No se detectó argumento. Ingrese número o rango (ej. 4-8, -10, 40-): ")
else:
    argumento = sys.argv[1]

# 2. Procesar el argumento (ya sea de sys.argv o input)
procesar_y_calcular(argumento)
