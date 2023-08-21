class Asientos:
    def __init__(self, color, registro, precio):
        self.color = color 
        self.registro = registro
        self.precio = precio
    
    def cambiarColor(self, ncolor):
        colores_validos = ["negro", "amarillo", "blanco", "rojo", "verde"]
        if ncolor.lower() in colores_validos:
            self.color = ncolor.lower()

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

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos  
        self.marca = marca
        self.motor = motor  
        self.registro = registro
        self.cantidadCreados = cantidadCreados

    def cantidadAsientos(self):
        numAsientos = 0
        for asiento in self.asientos:
            if asiento is not None:
                numAsientos += 1
        return numAsientos

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for asiento in self.asientos:
                if asiento is not None:
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto originales"
        else:
            return "Las piezas no son originales"


        