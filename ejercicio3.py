
def mayor(a,b):
    ms = "El numero mayor es "

    if(a>b):
        print(ms, a)
    elif (a==b):
        print("Los numeros son iguales. Ingrese otros.")
        return 0
    else: 
        print(ms, b)
    
    return 1 

if __name__ == '__main__':  
   n1 = int(input("Ingrese el primer numero: "))
   n2 = int(input("Ingrese el segudo numero: "))

   mayor(n1,n2)
   
