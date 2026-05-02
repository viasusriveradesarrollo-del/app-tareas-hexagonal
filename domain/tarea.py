import uuid

class Tarea:
    def __init__(self, titulo: str, id: str = None, completada: bool = False):
        # Regla de negocio: No se deben registrar tareas con título vacío
        if not titulo or not titulo.strip():
            raise ValueError("Error: El título de la tarea no puede estar vacío.")
        
        # Las tareas se identifican por un id único
        self.id = id if id else str(uuid.uuid4())
        self.titulo = titulo.strip()
        self.completada = completada

    def completar(self):
        # Regla de negocio: Una tarea completada debe cambiar su estado
        self.completada = True

    # Este método solo es para que se imprima bonito en consola después
    def __str__(self):
        estado = "[X]" if self.completada else "[ ]"
        return f"{estado} {self.titulo} (ID: {self.id})"