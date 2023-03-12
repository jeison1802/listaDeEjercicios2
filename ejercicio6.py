# Ejercicio 6: Para ingresar a un evento 

def main():
   
    name = input("Ingrese su nombre: ")
    age = int(input("Ingrese su edad: "))
    reserva = input("Tiene invitación?: Si o No: ")

    if evaluar_edad(age) == True:
        print("Su ingreso es permitido")
        tiene_reserva(reserva)
        eres_amigo(name)
    else: print("No puede entrar!. Gracias")

def evaluar_edad(ed):
    if ed>=18 and ed<40: 
        return True
    else:
        return False

def tiene_reserva(reser):
    if reser =="Si":
        print("Puedes acceder al bar libre")
    else: 
        print("Tiene que pagar, pero si eres amigo hay promociones:")
       

def eres_amigo(nombre):
    if nombre == "Juancho":
        print("Por ser Juancho TIENES ingreso libre. Se celebra a los Juanchos")
    elif nombre == "Ezequiel":
         print("Puede entrar, pero pagas el doble ")
   
    
main()
