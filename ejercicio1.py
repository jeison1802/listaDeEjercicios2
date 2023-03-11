

# Pregunta 1
# Realizar un Menú Iterativo que tenga las siguientes opciones (Solo poner
# el número de la pregunta)



lista = [2,3,4,5,8,14,15,17,19,20,22,25,24]
lista1 = [["Jeison",13],["Miguel",20],["Mareano",23],["Abigail",18]]

def menu1(): 
   for i in range(4):
      for j in range(4):
           print(" * ",end=" ")
      print("\n")    
   return 1
 
def menu2():
    print("Los multiplos de 2 en la lista son: ")
    for c in lista:      
        if(c%2==0):
            print(c)
    return 1

def menu3():
    print("Los mayores de edad son : ")
    s = 0
    for c in lista1:
      s = s + 1  
      if c[1]>=18:
          if s == len(lista1):
            print(c[0]) 
          else :
            print(c[0],end=", ") 
      
    return 1      


n = int(input("Ingrese un numero: \n Opciones \n 1: Dibuja un cuadrado\n 2: Muestro los multiplos de 2 de una lista \n 3: Imprime a los mayores de edad \n "))
if(n==1):
    menu1()
elif(n==2):
    menu2()
elif(n==3):
    menu3()
