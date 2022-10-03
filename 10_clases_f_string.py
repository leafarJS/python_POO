#f-string
curso = 'python'
print('tutoriales de % s'%curso)

nombre = 'jorge'
edad = 45

print('hola soy, % s y tengo % s años'%(nombre, edad))

print('que tal soy {} y mi edad es de {} años'.format(nombre, edad))

print(f"tengo {edad} años y mi nombre es {nombre}")


class Estudiante:
  def __init__(self, nombre, apellido, curso):
    self.nombre = nombre
    self.apellido = apellido
    self.curso = curso
  
  #representación de una cadena o de un objeto| 
  # solo imprime el resultado como una cadena 
    """  def __str__(self):
    return f"Mi nombre es {self.nombre}, el apellido que me fue heredado es {self.apellido}, y tengo conocimiento {self.curso} del lenguaje python" """
  #para representar los atributos
  def __repr__(self):
    return f"Mi nombre es {self.nombre}, el apellido que me fue heredado es {self.apellido}, y tengo conocimiento {self.curso} del lenguaje python"

new_student = Estudiante('jorge', 'callejo', 'intermedio')
print(f"{new_student !r}")
