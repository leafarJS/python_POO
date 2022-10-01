#clases y objetos
class Persona:
  doctor = "Jorge"


print(Persona.doctor)
  
class Jugadores_A:
  player_1 = "cr7"
  player_2 = "ronaldhiño"
  
print(Jugadores_A.player_1)

class Jugadores_B:
  player_3 = "Ronaldo"
  player_1 = "Pele"     
  

print(Jugadores_B.player_1)

class Equipos:
  equipo_1 = "Barcelona"
  equipo_2 = "Real Madrid"


print(Equipos.equipo_1)

#Clase
class Nombre:
  #pass es para hacer un parentesis en la clase
  pass


#objeto
jorge = Nombre()
zamira = Nombre()

#crear atributos para el objeto
#objeto.atributo = valor 
jorge.edad = 45
jorge.sexo = "Masculino"
jorge.pais = "Bolivia"

zamira.edad = 19
zamira.sexo = "Femenino"
zamira.pais = "Bolivia"


print(jorge.edad)
print(zamira.pais)