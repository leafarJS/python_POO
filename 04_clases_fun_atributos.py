#Funciones para atributos

class Persona:
  #atributos
  edad = 45
  nombre = "Jorge"
  pais = "Ucrania"


#crear objeto
doctor = Persona()


#llamar a los atributos 
print(f"La edad es: {doctor.edad} años")
print("El nombre del doctor es:", getattr(doctor, "nombre")) 

#Preguntar si tenemos ese atributo dentro la clase 
print("¿Conocemos la edad del doctor?", hasattr(doctor, "edad"))
print("¿Conocemos el apellido del doctor?", hasattr(doctor, "apellido"))

#cambiar el valor del atributo del objeto
print(doctor.nombre)
setattr(doctor,'nombre', 'Rafael')
print(doctor.nombre)

#eleminar un atributo 
print(doctor.pais)
delattr(Persona, 'pais')
print(doctor.pais)
