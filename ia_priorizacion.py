# ia_priorizacion.py

class IAPriorizacion:
    """
    Clase encargada de analizar la información de un Evento
    y sugerir una prioridad basada en reglas o un modelo.
    """
    def __init__(self):
        # Aquí se cargarán los modelos de Machine Learning en el futuro
        print("Módulo de IA para Priorización inicializado.")

    def sugerir_prioridad(self, evento):
        """
        Asigna una prioridad inicial basada en el título y la categoría del evento.
        
        Prioridad sugerida: 1 (Alta) a 10 (Baja).
        """
        prioridad_base = evento.prioridad  # Usamos la prioridad que ya tiene
        titulo = evento.titulo.lower()
        categoria = evento.categoria.lower()

        # Regla 1: Palabras clave críticas (Alta Prioridad)
        if "reunión" in titulo or "entregar" in titulo or "deadline" in titulo:
            prioridad_base = min(prioridad_base, 3) # Asigna prioridad 3 o menos (alta)

        # Regla 2: Categorías de baja prioridad
        if categoria == "ocio" or "gimnasio" in titulo or "descanso" in titulo:
            prioridad_base = max(prioridad_base, 7) # Asigna prioridad 7 o más (baja)

        # Regla 3: Si la categoría es "Importante" (que no existe aún, pero la IA la podría predecir)
        if categoria == "trabajo":
             prioridad_base = min(prioridad_base, 4)

        return prioridad_base