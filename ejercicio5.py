
import os 
path = os.path.abspath('.') 

#for f in os.scandir(path):
 #   print(f,"=>",f.path)
  #  print(f.is_dir())

def funcionListaCarpeta(path):
    listaCarpeta = []
    for f in os.scandir(path):
       if f.is_dir():
           funcionListaCarpeta(f.path)
       else: 
           listaCarpeta.append(f.path)
    
    print(listaCarpeta)

funcionListaCarpeta(path)