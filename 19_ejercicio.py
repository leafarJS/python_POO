#TODO: Ejercicio 1

class Empleado:
  def __init__(self, nombre, edad, legajo, sueldo):
    self.nombre = nombre
    self.edad = edad
    self.legajo = legajo
    self.sueldo = sueldo
    
  def calcular_sueldo(self, descuento, bonos):
    return self.sueldo - descuento + bonos
  
class Agente_ventas(Empleado):
  def __init__(self, nombre, edad, legajo, sueldo, mostrador):
    self.numero_mostrador = mostrador
    #cuando se tiene dos constructures y se tiene herencia
    super().__init__(nombre, edad, legajo, sueldo)
    
  
class Tripulante(Empleado):
  #cuando no tiene constructor y heredad directamente del padre
   
  def mostrar_renovacion_licencia(self):
    if self.edad > 50:
      print("Renueva licencia cada año")
    else:
      print("Renueva cada 6 meses")
  
  
  
  
  
  
vendedor = Agente_ventas("jorge", 45, 4375374, 25000, 4)
print(vendedor.nombre)
calculo = vendedor.calcular_sueldo(5000, 1000)
print(calculo)


piloto_senior = Tripulante("Rafael", 35, 4375375, 45000)
print(piloto_senior.nombre) 
print(piloto_senior.mostrar_renovacion_licencia())

print("============================================")

#TODO: Ejercicio 2

class Carrera:
  def __init__(self, nombre):
    self.nombre = nombre
    #oculatar el atributo para que utilizen el metodo para su llenado
    self.__materia = {}
    
  
  def agregar_materias(self, materia, codigo):
    self.__materia[codigo] = materia
    

class Materia:
  def __init__(self, nombre, profesor, fecha):
    self.nombre = nombre
    self.profesor = profesor
    # !no puede ser anterior a 2006
    self.fecha_inicio = fecha
   
   #decorador creando una propiedad a partir de un atributo 
  @property 
  def fecha_inicio(self):
    return self._fecha_inicio #atributo privado
  
  @fecha_inicio.setter
  def fecha_inicio(self,fecha):
    if fecha < 2006:
      self._fecha_inicio = 2006
    else:
      self._fecha_inicio = fecha


especialidad = Carrera("Ingenieria")
algebra = Materia("Algebra", "Al jaruismi", 2010)
fisica = Materia("Fisica", "Einstein", 2006)
quimica = Materia("Quimica", "Heisenberg", 2003)


#especialidad.materia.append((101, algebra))
#especialidad.materia.append((103, fisica))
#print(len(especialidad.materia))

especialidad.agregar_materias(algebra, 101)
#print(especialidad.materia) //se oculto el atributo

print(algebra.fecha_inicio)
print(fisica.fecha_inicio)
print(quimica.fecha_inicio)

# ! no recomendable
""" especialidad.agregar_materias(algebra, 101)
print(len(especialidad.materia))

copia = especialidad.materia
print(type(copia))
copia[102] = fisica
print(len(copia))
print(especialidad.materia) """

print("============================================")

#TODO: Ejercicio 3 sobre escritura de metodos

class Ejecutivo:
  def __init__(self, nombre, legajo, sueldo):
    self.nombre = nombre
    self.legajo = legajo
    self.sueldo = sueldo
    
  def calcular_sueldo(self, descuento):
    return self.sueldo - descuento
  
class Gerente(Ejecutivo):
  #asignar un valor para evitar la sobre carga
  def calcular_sueldo(self, descuento, bonificacion=0):
    return self.sueldo - descuento + bonificacion
  
subgerente = Ejecutivo("Rafael", 1002, 25000)
gerente = Gerente("Jorge", 1001, 45000)

print(subgerente.calcular_sueldo(2500))
print(gerente.calcular_sueldo(2500, 4000))