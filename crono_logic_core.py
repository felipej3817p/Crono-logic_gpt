# crono_logic_core.py

import datetime as dt
import json 
import os   
# Asegúrate de que ia_priorizacion.py esté en la misma carpeta
from ia_priorizacion import IAPriorizacion 

class Evento:
    """Clase para representar un único evento o tarea en la agenda."""
    def __init__(self, titulo, fecha_hora, prioridad=5, categoria="Sin Asignar"):
        self.titulo = titulo
        # La fecha_hora puede ser un objeto datetime o un string ISO
        self.fecha_hora = fecha_hora 
        self.prioridad = prioridad
        self.categoria = categoria
        
    def __repr__(self):
        # Muestra la prioridad ajustada por la IA
        return f"Evento(Título='{self.titulo}', Fecha='{self.fecha_hora}', Prioridad={self.prioridad})"

    def to_dict(self):
        """Convierte el objeto Evento a un diccionario para poder guardarlo en JSON."""
        return {
            "titulo": self.titulo,
            # Convertimos el objeto datetime a un string ISO para guardarlo
            "fecha_hora": self.fecha_hora.isoformat() if isinstance(self.fecha_hora, dt.datetime) else self.fecha_hora,
            "prioridad": self.prioridad,
            "categoria": self.categoria
        }


class CronoLogicCore:
    """
    Clase principal para gestionar la agenda, la persistencia y la priorización de IA.
    """
    def __init__(self):
        self.agenda = []
        self.archivo_agenda = "agenda.json"
        # Inicializa la IA (no necesita clave por ahora, ya que es una simulación)
        self.ia_core = IAPriorizacion() 
        self.cargar_agenda() 
        print(f"[{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Crono-logic V2.0 inicializado. {len(self.agenda)} eventos cargados.")

    # --- MÉTODOS DE PERSISTENCIA ---
    def cargar_agenda(self):
        """Carga los eventos desde el archivo JSON si existe."""
        if os.path.exists(self.archivo_agenda):
            try:
                with open(self.archivo_agenda, 'r') as f:
                    datos = json.load(f)
                    self.agenda = []
                    for item in datos:
                        # Reconstruimos el objeto Evento: string ISO de vuelta a datetime
                        fecha = dt.datetime.fromisoformat(item["fecha_hora"])
                        evento = Evento(item["titulo"], fecha, item["prioridad"], item["categoria"])
                        self.agenda.append(evento)
                print(f"Agenda cargada exitosamente desde {self.archivo_agenda}.")
            except json.JSONDecodeError:
                print("Error: El archivo de agenda está corrupto.")

    def guardar_agenda(self):
        """Guarda la agenda actual en el archivo JSON."""
        datos_a_guardar = [evento.to_dict() for evento in self.agenda]
        with open(self.archivo_agenda, 'w') as f:
            # indent=4 es para que el archivo JSON sea fácil de leer
            json.dump(datos_a_guardar, f, indent=4) 
        print(f"Agenda guardada en {self.archivo_agenda}.")

    # --- MÉTODO DE INTEGRACIÓN DE IA ---
    def agregar_evento(self, evento: Evento):
        """Añade un nuevo objeto Evento y ajusta la prioridad con la IA."""
        
        # 1. Obtenemos la prioridad sugerida por la IA (simulación)
        prioridad_sugerida = self.ia_core.sugerir_prioridad(evento)
        
        # 2. Reemplazamos la prioridad del evento
        evento.prioridad = prioridad_sugerida
        print(f"IA ASIGNÓ prioridad {prioridad_sugerida} para '{evento.titulo}'.")

        # 3. Guardamos y persistimos
        self.agenda.append(evento)
        self.guardar_agenda() 
    
    def obtener_eventos_ordenados(self):
        """
        Retorna los eventos ordenados cronológicamente por fecha/hora.
        """
        # Ordenar la lista por la fecha y hora del evento
        self.agenda.sort(key=lambda evento: evento.fecha_hora)
        return self.agenda


# --- Ejemplo de Uso (Modificado para probar la IA) ---
if __name__ == "__main__":
    
    core = CronoLogicCore()
    
    # Solo agregamos eventos nuevos si la agenda estaba vacía
    if not core.agenda or len(core.agenda) < 2:
        print("\n--- Agenda vacía o con pocos eventos, agregando eventos para probar la IA ---")
        
        # Borramos la agenda para probar la IA desde cero cada vez
        core.agenda = []
        
        ahora = dt.datetime.now()
        
        # Eventos de prueba:
        evento1 = Evento("Reunión con el CEO para el reporte final", ahora + dt.timedelta(days=2), prioridad=10, categoria="Trabajo")
        evento2 = Evento("Ir al gimnasio y relajarme", ahora + dt.timedelta(hours=4), prioridad=10, categoria="Ocio")
        
        core.agregar_evento(evento1)
        core.agregar_evento(evento2)
    else:
        print("\n--- Agenda no vacía, usando eventos cargados ---")


    print("\n--- Eventos Actuales Ordenados Cronológicamente ---")
    eventos_ordenados = core.obtener_eventos_ordenados()
    for evento in eventos_ordenados:
        print(evento)