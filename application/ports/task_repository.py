from abc import ABC, abstractmethod
from typing import List
from domain.tarea import Tarea

class TaskRepository(ABC):
    """
    Puerto de salida: Define el contrato para el almacenamiento de tareas.
    La aplicación no sabe si esto será en memoria, JSON, o SQL.
    """
    
    @abstractmethod
    def guardar(self, tarea: Tarea) -> None:
        pass

    @abstractmethod
    def obtener_todas(self) -> List[Tarea]:
        pass

    @abstractmethod
    def obtener_por_id(self, id: str) -> Tarea:
        pass

    @abstractmethod
    def eliminar(self, id: str) -> None:
        pass