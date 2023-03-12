### Minisistema
roles=['admin','vendedor','inventario']
productos = ['galletas','bebidas','embutidos']
sistema={
    "nombre":"tienda",
    "usuarios":[
        {
            'name':" ",
            'password':" ",
            'rol':" " ##vendedor ,administrador ,inventario
        }
    ],
    "sedes":[{
        "nombreSede":"",
        "ubicacion":""
    }],
    "productos":[
    {
        "nombre":"", ## galletas, bebidas, embutidos
        "precio":"",
        "stock":""
    }]
}
##### funciones
## karen vera
def agregarUsuario():
    nameUsuario=input("ingrese el nombre de usuario")
    password=input("ingrese su password")

    while True:
        rol=input("ingrese su rol")
        if rol in roles:
            break
        else:
            print("ingrese un rol correcto",roles)
        
    dictUser={
        'name':nameUsuario,
        'password':password,
        'rol':rol
    }
    sistema['usuarios'].append(dictUser)
###
def eliminarUsuario():
    usuarioPorEliminar=input("ingrese usuario por eliminar")
    for i,valor in enumerate(sistema['usuarios']):
        if valor['name']==usuarioPorEliminar:
                ## ingresar password para verificar que es correcto
                sistema['usuarios'].remove(i)
    ## remove
    pass
###
def obtenerRol(usuario):
    rol=""
    for i,valor in enumerate(sistema["usuarios"]):
        if valor['name']==usuario:
            rol=valor['rol']
    return rol
####
def agregarSedes():
    usuario=input("ingresa usuario")
    rol=obtenerRol(usuario)
    if rol=='admin':
        sede=input("ingrese sede")
        ubicacion=input("ingrese ubicacion")
        dictSede={
            'sede':sede,
            'ubicacion':ubicacion
        }
        sistema["sedes"].append(dictSede)
    else:
        print("no es un rol permitido")
###
def verSedes():
    pass
#####
def tipo_precio(nomProducto):
    if nomProducto == productos[0]:
        precio = 20 
      
    elif nomProducto == productos[1]:
        precio = 30
      
    elif nomProducto == productos[2]:
        precio = 50 
        
    return precio 

def tipo_stock(nome):
    if nome == productos[0]:
        
        stock = False
    elif nome == productos[1]:
      
        stock = True
    elif nome == productos[2]:
       
        stock = True 
    return stock

def agregarProductos():
    while True: 
      nomProducto = input("Ingrese el nombre del producto: ")
      if nomProducto in productos:
          break
      else: print("ingrese un prodcuto correcto",productos)
     
    precio = tipo_precio(nomProducto)
    stock = tipo_stock(nomProducto)
    dictProducto={
            'nombre':nomProducto,
            'precio':precio,
            'stock': stock
        }
    sistema["productos"].append(dictProducto)
#####
def cambiarStock():
    while True: 
      nam = input("Ingrese el nombre del producto a cambiar stock: ")
      
      if nam in productos:
          break
      else: print("ingrese un prodcuto correcto",productos)
    
    precio = tipo_precio(nam)
    stock = not tipo_stock(nam)
    dictProducto={
            'nombre':nam,
            'precio':precio,
            'stock': stock
        }
    sistema["productos"].append(dictProducto)


    

agregarUsuario()
agregarSedes()
agregarProductos()
cambiarStock()
print(sistema)