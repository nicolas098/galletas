class SistemaExpertoHorno:
    def __init__(self):
        # Reglas del sistema experto (niveles cromáticos y acciones)
        self.reglas = {
            'cruda': 'alta',
            'semicruda': 'moderada',
            'dorada': 'baja'
        }

    def evaluar_cromatico(self, nivel_cromatico):
        """Evalúa el nivel cromático y retorna la acción (temperatura) adecuada."""
        if nivel_cromatico >= 0 and nivel_cromatico <= 4:
            return self.reglas['cruda']  # Nivel cromático crudo
        elif nivel_cromatico > 4 and nivel_cromatico <= 8:
            return self.reglas['semicruda']  # Nivel cromático semicrudo
        elif nivel_cromatico > 8 and nivel_cromatico <= 10:
            return self.reglas['dorada']  # Nivel cromático dorado
        else:
            return "Nivel cromático fuera de rango"

    def obtener_temperatura(self, accion):
        """Convierte la acción (etiqueta de temperatura) en grados Celsius."""
        temperaturas = {
            'alta': 30,       # Temperatura alta
            'moderada': 20,   # Temperatura moderada
            'baja': 10        # Temperatura baja
        }
        return temperaturas.get(accion, 'Desconocido')

# Crear instancia del sistema experto
horno = SistemaExpertoHorno()

# Definir casos de prueba
niveles_cromaticos = [2, 6, 9]

# Evaluar niveles cromáticos y determinar temperatura
for nivel in niveles_cromaticos:
    accion = horno.evaluar_cromatico(nivel)
    temperatura = horno.obtener_temperatura(accion)
    print(f"Nivel cromático: {nivel} -> Acción: {accion} -> Temperatura del horno: {temperatura}°C")
