
def primo(numero):
  es_primo=True
  if numero == 1:
     return False
  for num in range(2, numero):
     if numero % num == 0:
         es_primo=False
  if es_primo:
        return True
  else: return False


def evaluar():
    lista = []
    for i in range(1,10**5,100):
       if primo(i):
         lista.append(i)
    print(lista)
        
   
evaluar()      
       