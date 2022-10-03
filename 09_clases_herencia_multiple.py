#herencia multiple

class Telefono:
  def __init__(self):
    pass 
  
  def llamar(self):
    print('llamando...')
    
  def ocupado(self):
    print('ocupado...')
    
class Camara:
  def __init__(self):
    pass 
  
  def fotografia(self):
    print('tomar fotografia...')
    
class Reproduccion:
  def __init__(self):
    pass 
  
  def reproductor_musica(self):
    print('reproducción musica...')
    
  def reproducir_video(self):
    print('reproducción video...')
    

class SmartPhone(Telefono, Camara, Reproduccion):
  #destructor
  def __del__(self): # se utiliza para no utilizar los recursos que no estan siendo utilizados 
    print('Telefono apagado')
    

iphone_10 = SmartPhone()
#print(dir(iphone_10))
print(iphone_10.fotografia())
print(iphone_10.llamar())
#print(iphone_10.ocupado())
print(iphone_10.reproductor_musica())