"""
comentario multilinea
"""

#comentario lineal

"""
Python es sensible a maúsculas y minúsculas

Las variables no pueden comenzar con números
"""

#No es necesario especificar el tipo de dato
numero = 5

#Si ponemos algo entre comillas, lo interpreta como texto y no como variable
print ("numero")

#Mandamos como parámetro el valor de una variable
print (numero)

# ctrl + D nos permitira cambiar una palabra que seleccionemos en todo el código

decimal = 2.5
print ("decimal o flotante")
print (decimal)

numero = numero + 6

print ("Suma de enteros")
print (numero)

#Podemos sumar enteros y flotantes sin ningún problema
suma = numero + decimal
print ("Suma de entero y flotante")
print (suma)

#Simplificación de operación suma
suma += 1

#Division entre variables
suma /= decimal
print ("Division de variables")
print (suma)
#Toda división se convierte en float

#Multiplicación
mult = suma *2
print ("Multiplicacion", mult)
#Cada print será un salto de línea, coma nos dará espacio

#Potencias
potencia = 2**3 #2 al cubo
print ("Potencia del numero 2:", potencia)

#Modulo
#es el residuo de una división
modulo = 13%2
print ("Modulo (residuo de la division):", modulo)
#   / = division, % = módulo

"""
Tipo de dato de texto
"""

queso = "oaxaca"
print (queso)

#para definir el contenido de nuestro texto podemos usar comillas, y dentro
#usar una comilla sin problema
quesero = "Echame un queso 'oaxaca' por favor"

#pero si deseamos imprimir comillas, tendremos que usar comilla simple 
#para que no haya problemas de interpretacion
quesero2 = 'Esta mas rico el "quesillo". baboso.'

print(quesero)
print(quesero2)

formato = """           

                        esto es un texto.
    que         respeta
           los           espacios 
                jajaja"""

print (formato)
