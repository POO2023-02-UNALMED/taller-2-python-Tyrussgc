class Asiento:
    def __init__(self, color, registro, precio):
        self.color = color 
        self.registro = registro
        self.precio = precio
    
    def cambiarColor(self, ncolor):
        colores_validos = ["negro", "amarillo", "blanco", "rojo", "verde"]
        if ncolor in colores_validos:
            self.color = ncolor

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevo_registro):
        self.registro = nuevo_registro

    def asignarTipo(self, ntipo):
        if ntipo.lower() == "electrico" or ntipo.lower() == "gasolina":
            self.tipo = ntipo 




        