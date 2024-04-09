def error_numero(mensaje):
  while True:
    try:
      opcion = int(input(mensaje))
    except ValueError:
      print("\nUsted no ingreso una opcion valida, Por Favor vuelva a intentar")
    else:
      return opcion
    
def limiteAnio():
  if anio in range(0,2024):
      print("se agrego")
  else:
      while error < 1:
        print("El año del libro debe ser menor a 2023 debe ser numero")
        anio = error_numero("Ingrese año del libro: ")
        if anio in range(0,2024):
          error = error +1 
      print("se agrego")
      
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
