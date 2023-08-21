class Asientos:
    def __init__(self, color, registro, precio):
        self.color = color 
        self.registro = registro
        self.precio = precio
    
    def cambiarColor(self, color):
        self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevo_registro):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo



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
        return len(self.asientos)

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            return
        