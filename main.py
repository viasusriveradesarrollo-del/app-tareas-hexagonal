from infrastructure.adapters.memory_repository import MemoryTaskRepository
from application.use_cases.task_service import TaskService
from infrastructure.adapters.console_adapter import ConsoleAdapter

def main():
    # 1. Instanciamos el adaptador de salida (Persistencia en memoria)
    repository = MemoryTaskRepository()
    
    # 2. Instanciamos el caso de uso inyectando el repositorio
    # (¡El servicio no sabe que es memoria, solo sabe que cumple el contrato!)
    task_service = TaskService(repository)
    
    # 3. Instanciamos el adaptador de entrada (Consola CLI) inyectando el servicio
    app = ConsoleAdapter(task_service)
    
    # 4. Arrancamos la aplicación
    app.iniciar()

if __name__ == "__main__":
    main()