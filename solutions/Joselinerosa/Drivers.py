class CarnetPuntos:
  def __init__(self):
    self.conductores = {}
    self.puntos_count =  {i: 0 for i in range(16)}

def nuevo(self, dni):
  if dni in self.drivers:
    raise ValueError("Duplicate conductors")
  self.drivers[dni] = 15
  self.points_count[15] += 1

  def quitar(self, dni, puntos):
    if dni not in self.drivers:
      raise ValueError("Non existent driver")
    puntos_actuales = self.puntos_count[dni] 

    #fix this and finish

    def consultar(self, dni):
      if dni not in self.drivers:
        raise ValueError("Conductor inexistente")
      return self.drivers[dni]
    

    def cuantos_con_puntos(puntos):
      if puntos < 0 or puntos > 15:
        raise ValueError ("Puntos no validos")
      return self.points_count[puntos]
