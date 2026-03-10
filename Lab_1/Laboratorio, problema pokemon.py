nombre = input("Ingrese su nombre: ")
nombre = str(nombre)

if any(char.isdigit() for char in nombre):
    print("Error: el nombre no puede contener números")
    exit()  

#---------------------------------------------------------------
edad = input("Ingrese su edad: ")
edad = int(edad)

#-----Funcion para verificar edad------------------------------

if edad < 10 or edad > 150:
    print("Error: edad inválida, debe estar entre 10 y 150")
    exit()  # detiene el programa
    

#-------------------------------------------------------------

peso = input("Ingrese su peso(kg): ")
peso = float(peso)

altura = input("Ingrese su altura(m): ")
altura = float(altura)

#-------Funcion calculo de IMC-------------------------------

def masacorporal(kg,h):
    imc = kg/(h*h)
    if imc < 18.5:
        print("Su categoria segun su IMC es bajo peso")
    if imc >= 18.5 and imc <= 24.9:
        print("Su categoria segun su IMC es peso normal")
    if imc >= 25 and imc <= 29.9:
        print("Su categoria segun su IMC es sobrepeso")
    if imc >= 30:
        print("Su categoria segun su IMC es obesidad")


print(masacorporal(peso,altura))





