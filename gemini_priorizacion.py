# gemini_priorizacion.py
# (Version Final Operativa sin dependencia externa)

class IAPriorizacion:
    """
    Clase de Priorización basada en reglas para la V2.0.
    """
    def __init__(self):
        print("Módulo de IA para Priorización V2.0 (Reglas Operativas) inicializado.")

    def sugerir_prioridad(self, evento):
        """
        Asigna una prioridad basada en reglas de palabras clave y categoría.
        Prioridad 1 (Máxima) a 10 (Mínima).
        """
        prioridad_base = evento.prioridad
        titulo = evento.titulo.lower()
        categoria = evento.categoria.lower()
        
        # Regla 1: Asignar MÁXIMA prioridad (número bajo) a Trabajo/Cosas Importantes
        if "reunión" in titulo or "reporte" in titulo or categoria == "trabajo":
            prioridad_base = min(prioridad_base, 3) 

        # Regla 2: Asignar MÍNIMA prioridad (número alto) a Ocio
        if "gimnasio" in titulo or "relajarme" in titulo or categoria == "ocio":
            prioridad_base = max(prioridad_base, 8) 

        # Regla 3: Si es una entrega, es crítica.
        if "entregar" in titulo:
            prioridad_base = min(prioridad_base, 1) 

        return prioridad_base