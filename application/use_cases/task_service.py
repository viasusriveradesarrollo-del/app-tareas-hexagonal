from typing import List
from domain.tarea import Tarea
from application.ports.task_repository import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository):
        # Inyección de dependencias: Le pasamos el puerto, no una base de datos real
        self.repository = repository

    def registrar_tarea(self, titulo: str) -> Tarea:
        tarea = Tarea(titulo=titulo)
        self.repository.guardar(tarea)
        return tarea

    def listar_todas(self) -> List[Tarea]:
        return self.repository.obtener_todas()

    def listar_pendientes(self) -> List[Tarea]:
        todas = self.repository.obtener_todas()
        return [t for t in todas if not t.completada]

    def completar_tarea(self, id: str) -> bool:
        tarea = self.repository.obtener_por_id(id)
        if tarea:
            tarea.completar()
            self.repository.guardar(tarea)  # Actualiza la tarea guardada
            return True
        return False

    def eliminar_tarea(self, id: str) -> bool:
        tarea = self.repository.obtener_por_id(id)
        if tarea:
            self.repository.eliminar(id)
            return True
        return False