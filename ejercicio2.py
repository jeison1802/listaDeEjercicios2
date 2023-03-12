categoria_libros = ["Drama","Romantico","Terror","Fantasía"]
usuarios = ["Luis","Arturo","Miguel","Julio"]

Biblioteca = {
    'categoria':"", 
    'nombres_autores':[{
        'libros':"",
        'autores':""
    }],
    'estado':" ",
    'usuarios':" "
}

def agregarCategoria():

    while True:
        categoria=input("Ingrese la categoría del libro: ")
        if categoria in categoria_libros:
            break
        else:
            print("ingrese la categoría correcta",categoria_libros)
    
    dictCategoria={
        'categoria':categoria
    }
    Biblioteca['categoria'].append(dictCategoria)
   
###

def mas_datos():
    autor = input("Ingrese un autor: ")
    libro = input("Ingrese un libro: ")
     
    dictAutores={
        'libros':libro,
        'autores':autor,
    }
    Biblioteca['nombres_autores'].append(dictAutores)

def estado():
    est = input("Ingrese el estado del libro (prestado: Si, No prestado: No)")
    if est == "si":
        c = True
    else:  c = False
    dictEstado={
        'estado': c
    }
    Biblioteca['estado'].append(dictEstado)



def agregarUsuario():
    while True:
        usue=input("Ingrese un usuario: ")
        if usue in usuarios:
            break
        else:
            print("ingrese un usuario correcto",usuarios)
   
    dictUsers={
        'usuarios':usue,
    }
    Biblioteca['usuarios'].append(dictUsers)
#####
def cambiarEstado():
    while True: 
      nam = input("Ingrese el nombre del libro que quiere cambiar estado: ")
      
      if nam == Biblioteca["nombres_autores"[0]]:
          not Biblioteca["estado"]
          break 
      else: 
        print("ingrese un libro que se añadió anteriormente")
        break
    
    


    
agregarCategoria()
mas_datos()
estado()
agregarUsuario()
cambiarEstado()
print(Biblioteca)