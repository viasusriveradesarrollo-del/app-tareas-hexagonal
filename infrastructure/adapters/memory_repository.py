from typing import List, Dict
from application.ports.task_repository import TaskRepository
from domain.tarea import Tarea

class MemoryTaskRepository(TaskRepository):
    """
    Adaptador de Salida: Implementa el contrato TaskRepository.
    Guarda los datos en un diccionario en memoria RAM.
    """
    def __init__(self):
        # Usamos un diccionario para buscar rápido por ID
        self._tareas: Dict[str, Tarea] = {}

    def guardar(self, tarea: Tarea) -> None:
        self._tareas[tarea.id] = tarea

    def obtener_todas(self) -> List[Tarea]:
        return list(self._tareas.values())

    def obtener_por_id(self, id: str) -> Tarea:
        return self._tareas.get(id)

    def eliminar(self, id: str) -> None:
        if id in self._tareas:
            del self._tareas[id]