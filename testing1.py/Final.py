import sys
libros=[ [6,"Sistemas",[["Jorge" ,"Diaz"],["Pedro", "Lopez"]],2007,"Terror",200,"Exito"],
          [3,"El libro de Frozen",[["Leo" ,"Juarez"]],2000,"Infantil",10,"Exito"],
         [1903421872,"El libro de la selva", [["Nicolas Leo" ,"Messi"]],2000,"Infantil",345,"Exito"],
       [1920123814,"Sismo",[["Leo" ,"Juarez"]],1998,"Suspenso",56,"Elcano"]]

generos= ["Terror","Accion","Drama","Ficcion","Fantasia","Historico","Politico","Infantil","Suspenso"]

#----------------------------------------------------------------------------------------





def error_numero(mensaje):
  while True:
    try:
      opcion = int(input(mensaje))
    except ValueError:
      print("\nUsted no ingreso una opcion valida, Por Favor vuelva a intentar")
    else:
      return opcion
      
#----------------------------------------------------------------------------------------





def menu():
  print("""
  Si desea dar de alta un libro ingrese 1
  Si desea dar de baja un libro ingrese 2
  Si buscar un libro ingrese 3
  Si desea modificar un libro ingrese 4
  Si desea ver un listado ingrese 5
  Si deseas ver todos los libros en stock ingrese 6
  Si deseas cerrar el programa ingrese 0
  """)
  
  opcion = error_numero("\nIngrese la opcion deseada de forma numerica: ")
  
  if  opcion == 1:
    alta()
  
  elif opcion == 2:
    baja()
  
  elif opcion == 3 :
    buscar_titulo()

  elif opcion == 4 :
    modificar()

  elif opcion == 5 :
    listados()
  
  elif opcion == 6:
    print(libros)#(== end")
    mas_opciones()

  elif opcion == 0:
    sys.exit()

  else:
    print("\nPor favor ingrese una opcion valida\n")
    menu()
    
#-----------------------------------------------------------------------------------------





def alta(): 
  altaisbn = error_numero("\nIngresar ISBN del libro que desee dar de alta: ")
  i=0
  error = 0
  libro_existente = False
  
  while i < len(libros):
    if altaisbn == libros[i][0]: 
      print("\n¡Ese ISBN ya pertenece a un libro existente!, Por favor ingrese el ISBN correcto\n") 
      alta()
      libro_existente = True
    i=i+1
    
  if libro_existente == False :
    print("""\n¡Ese ISBN no esta registrado!
    Ingrese los siguientes datos: \n""")
    libro_nuevo = []
    autores = []
    editoriales = []
    
    libro_nuevo.append(altaisbn)
    
    titulo = input("Ingrese el titulo del libro: ")
    libro_nuevo.append(titulo)
    
    cuantos_autores = error_numero("\n¿Cuantos autores desea agregrar 1,2 o 3? ")#no funciona
    while cuantos_autores not in range(1,4): 
      cuantos_autores = error_numero("\n¿Cuantos autores desea agregrar 1,2 o 3? ")
    if cuantos_autores >= 1:
      nombre_autor = input("Ingrese el/los nombre/s del primer autor: ")
      apellido_autor = input("Ingrese el/los apellido/s del primer autor: ")
      autores.append([nombre_autor,apellido_autor])
    if cuantos_autores >= 2:
      nombre_autor2 = input("Ingrese el/los nombre/s del primer autor: ")
      apellido_autor2 = input("Ingrese el/los apellido/s del primer autor: ")
      autores.append([nombre_autor2,apellido_autor2])
    if cuantos_autores >= 3:
      nombre_autor3 = input("Ingrese el/los nombre/s del primer autor: ")
      apellido_autor3 = input("Ingrese el/los apellido/s del primer autor: ")
      autores.append([nombre_autor3,apellido_autor3])
    libro_nuevo.append(autores)
    
    anio = error_numero("Ingrese año del libro: ")
    if anio in range(0,2024):
      libro_nuevo.append(anio)
    else:
      while error < 1:
        print("El año del libro debe ser menor a 2023 debe ser numero")
        anio = error_numero("Ingrese año del libro: ")
        if anio in range(0,2024):
          error = error +1 
      libro_nuevo.append(anio)
      
    genero = input("Ingrese genero del libro: ")
    while genero.lower().capitalize() not in generos:
      print("El genero que ingreso no existe")
      genero = input("Ingrese genero del libro: ") 
    libro_nuevo.append(genero.capitalize())
    
    paginas = error_numero("Ingrese cantidad de paginas que tiene el libro: ")
#    if paginas <= 0:
#      print("debe ser mayor a 1")
    libro_nuevo.append(paginas)
    
    cuantas_editoriales= error_numero("\n¿Cuantas editoriales desea agregrar 1 o 2? ")
    while cuantas_editoriales not in range(1,3):
      cuantas_editoriales = error_numero("\n¿Cuantas editoriales desea agregrar 1 o 2? ") 
    if cuantas_editoriales <= 1:
      editorial_1 = input("Ingrese la primera editorial: ")
      editoriales.append(editorial_1)
    elif cuantas_editoriales <= 2:
      editorial_2 = input("Ingrese la segunda editorial: ")
      editoriales.append(editorial_2)
    libro_nuevo.append(editoriales)    
    
    print("\n¡El libro cargado: ",libro_nuevo,"fue cargado con exito!") 
    libros.append(libro_nuevo) 
    mas_opciones() 

#----------------------------------------------------------------------------------------




  
def baja():
  bajaisbn = error_numero("\nIngresar ISBN del libro que desee dar de baja: ")
  i=0
  libro_borrado = False
    
  while i < len(libros):
    if bajaisbn == libros[i][0]:
      titulo = libros[i][1]
      del libros[i]
      libro_borrado = True
    i=i+1
    
  if libro_borrado:#ver libro borrado
    print ("\nEl libro",format(titulo),"fue dado de baja con exito")
    mas_opciones()
  else:
    print ("\nEl libro que se solicito dar de baja no existe\n")
    baja()

#----------------------------------------------------------------------------------------




  
def buscar_titulo():
  i = 0
  hay_libro = False
  libro_encontrado = []
  buscar = input("\nIngrese el titulo del libro que desee buscar: ")
  
  while i < len(libros):
    if buscar.lower() in libros[i][1].lower():
      libro_encontrado.append(libros[i])
      hay_libro = True
    i=i+1
    
  if hay_libro:
    print("\nEl libro que busca es:",libro_encontrado)
    mas_opciones()
  else:
    print("\nEl libro que desea buscar no esta registrado en la biblioteca\n")
    buscar_titulo()

#----------------------------------------------------------------------------------------





def modificar():
  isbn_solicitado = error_numero("\nIngrese el ISBN del libro que deseea modificar: ")
  i = 0
  error = 0
  libro_modificado = []
  autores = []
  editoriales = []
  modificado = False
    
  while i < len(libros):
    if isbn_solicitado == libros[i][0]:
      libro_modificado.append(isbn_solicitado)
      titulo = libros[i][1]
      print("\n¿El libro que desea modificar es",format(titulo),"?")
      desea_modificar = input("Ingrese si o no: ")
      if desea_modificar.lower() == "si":
        titulo = input("Ingrese el titulo del libro: ")
        libro_modificado.append(titulo)
      
        cuantos_autores = error_numero("\n¿Cuantos autores desea agregrar 1,2 o 3?")
        while cuantos_autores not in range(1,4):
          cuantos_autores= error_numero("\n¿Cuantos autores desea agregrar 1,2 o 3? ") 
        if cuantos_autores >= 1:
          nombre_autor = input("Ingrese el/los nombre/s del primer autor: ")
          apellido_autor = input("Ingrese el/los apellido/s del primer autor: ")
          autores.append([nombre_autor,apellido_autor])
        if cuantos_autores >= 2:
          nombre_autor2 = input("Ingrese el/los nombre/s del primer autor: ")
          apellido_autor2 = input("Ingrese el/los apellido/s del primer autor: ")
          autores.append([nombre_autor2,apellido_autor2])
        if cuantos_autores >= 3:
          nombre_autor3 = input("Ingrese el/los nombre/s del primer autor: ")
          apellido_autor3 = input("Ingrese el/los apellido/s del primer autor: ")
          autores.append([nombre_autor3,apellido_autor3])
        libro_modificado.append(autores)
    
      
        anio = error_numero("Ingrese año del libro: ")
        if anio in range(0,2024):
          libro_modificado.append(anio)
        else:
          while error < 1:
            print("El año del libro debe ser menor a 2023 debe ser numero")
            anio = error_numero("Ingrese año del libro: ")
            if anio in range(0,2024):
              error = error +1 
          libro_modificado.append(anio)
          
        genero = input("Ingrese genero del libro: ")
        while genero.lower().capitalize() not in generos:
          print("El genero que ingreso no existe")
          genero = input("Ingrese genero del libro: ") 
        libro_modificado.append(genero.capitalize())
        
        paginas = error_numero("Ingrese cantidad de paginas que tiene el libro: ")
        libro_modificado.append(paginas)
        
        cuantas_editoriales= error_numero("\n¿Cuantas editoriales desea agregrar 1 o 2? ")
        while cuantas_editoriales not in range(1,3):
          cuantas_editoriales = error_numero("\n¿Cuantas editoriales desea agregrar 1 o 2? ") 
        if cuantas_editoriales <= 1:
          editorial_1 = input("Ingrese la primera editorial: ")
          editoriales.append(editorial_1)
        elif cuantas_editoriales <= 2:
          editorial_2 = input("Ingrese la segunda editorial: ")
          editoriales.append(editorial_2)
        libro_modificado.append(editoriales)
        
        print("\nEl libro ",libro_modificado," fue cargado con exito")
        del libros[i] 
        libros.insert(i, libro_modificado)
        mas_opciones()
        modificado = True 
      else:
        modificar()
    i = i + 1
    
  if modificado == False :
    print("\nEl ISBN solicitado no esta registrado!, Por favor ingrese el ISBN correcto\n")
    modificar()

#----------------------------------------------------------------------------------------





def listados():
  opcion_listado = error_numero("""
  Si desea ver listados de libros existentes ingrese 1
  Si desea ver listado de Autores existentes ingrese 2
  Si desea ver listado de libros del mismo Genero ingrese 3
  Si desea ver listado de libros del mismo Autor ingrese 4
  Si desea ver listado de libros del misma editorial ingrese 5
  Si desea ver listado de libros de una editorial en un rango de años ingrese 6
  Si desea ver listado de autores de la misma editorial ingrese 7
  Si desea ver listado de libros editados el mismo año ingrese 8
  Si desea ver listado de libros de autores cuyo apellido empiezen con una letra determinada ingrese 9
  Si desea ver listado de libros cuyo titulo empieze con una palabra determinada 0
  
  Ingrese la opcion deseada: """)#ver si quiere salir del sistema

  listado = []
  if opcion_listado == 1:
    for x in libros:
      if x not in listado:
        listado.append(x[opcion_listado])
        
  if opcion_listado == 2:
    i = 0
    while i < len(libros):
      for x in libros[i][2]:
        if x not in listado:
          listado.append(x)
      i = i + 1 
 
  if opcion_listado == 3 :
    genero = input("\n¿Que genero desea buscar?: ")
    i=0
    for x in libros:
      if genero.lower() == libros[i][4].lower() :
        listado.append(x)
      i = i + 1
      
  elif opcion_listado == 4:#ver que pueda buscar por apellido no funciona
    nombre_autor = input("\nIngrese el/los nombre/s del autor que desea buscar: ")
    apellido_autor = input("\nIngrese el/los apellido/s del autor que desea buscar: ")
    
    for x in libros:
      i=0
      while i < len(x[2]):
        if nombre_autor.lower() == x[2][i][0].lower() and apellido_autor.lower() == x[2][i][1].lower():
          listado.append(x)
        i = i + 1
        
  elif opcion_listado == 5: 
    editorial = input("\n¿Que editorial desea buscar?: ")
    i=0
    for x in libros:
      if editorial.lower() == libros[i][6].lower() :
        listado.append(x)
      i = i + 1
      
  elif opcion_listado == 6:
    editorial = input("\n¿Que editorial desea buscar?: ")
    primer_anio = error_numero("\nIngrese de forma numerica desde que año desea buscar: ")
    segundo_anio = error_numero("Ingrese de forma numerica hasta que año desea buscar: ")
    i=0
    for x in libros:
      if editorial.lower() == libros[i][6].lower() :
        if x[3] in range(primer_anio,segundo_anio+1):
          listado.append(x)
      i = i + 1
  
  elif opcion_listado == 7: 
    editorial = input("\n¿Los autores de que editorial desea buscar?: ")
    i=0
    for x in libros:
      if editorial.lower() == libros[i][6].lower() :
          listado.append(x[2])
      i = i + 1
      
  elif opcion_listado == 8: 
    anio_edicion = error_numero("\nIngrese de forma numerica que año desea buscar: ")
    i=0
    titulo = libros[i][1]
    for x in libros:
      if x[3] in range(anio_edicion,anio_edicion+1):
          listado.append(x)
      i = i + 1
      
  elif opcion_listado == 9: #no funciona
    print("a")
  elif opcion_listado == 0:   
    primer_palabra = input("\nIngrese la  palabra de los libros que desea ver: ")
    i=0
    for x in libros:
      if primer_palabra.lower().strip() in x[1].lower().split(" "):
          listado.append(x)
      i = i + 1
        
  if listado == []:
    print("\nEl listado que busca no se ha encontrado")
  else:
    print("\nEl listado que busca es:\n", listado)
  error = 0 
  while error < 1:
    desea_listado = input("\n¿Desea buscar otro listado?")
    if desea_listado.lower() == "si":
      listados()
    elif desea_listado.lower() == "no":
      mas_opciones()
      
#---------------------------------------------------------------------------------------





def mas_opciones():
  otra_operacion = input("\n¿Desea realizar otra operacion?, Ingrese si o no: ")
  if otra_operacion.lower() == "si": 
    menu()
  else:
    print("\n¡Muchas Gracias por su visita a la biblioteca!\n")
    sys.exit()