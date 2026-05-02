from application.use_cases.task_service import TaskService

class ConsoleAdapter:
    """
    Adaptador de Entrada: Interactúa con el usuario a través de la consola
    y delega las acciones a los Casos de Uso.
    """
    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def iniciar(self):
        while True:
            print("\n--- GESTOR DE TAREAS ACADÉMICAS ---")
            print("1. Registrar nueva tarea")
            print("2. Listar todas las tareas")
            print("3. Listar tareas pendientes")
            print("4. Marcar tarea como completada")
            print("5. Eliminar tarea")
            print("6. Salir")
            
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                titulo = input("Ingresa el título de la tarea: ")
                try:
                    tarea = self.task_service.registrar_tarea(titulo)
                    print(f"✅ Tarea registrada. ID: {tarea.id}")
                except ValueError as e: # Captura la regla de negocio del Dominio
                    print(f"❌ {e}")

            elif opcion == "2":
                tareas = self.task_service.listar_todas()
                self._imprimir_tareas(tareas)

            elif opcion == "3":
                tareas = self.task_service.listar_pendientes()
                self._imprimir_tareas(tareas)

            elif opcion == "4":
                id_tarea = input("Ingresa el ID de la tarea a completar: ")
                if self.task_service.completar_tarea(id_tarea):
                    print("✅ Tarea marcada como completada.")
                else:
                    print("❌ Tarea no encontrada.")

            elif opcion == "5":
                id_tarea = input("Ingresa el ID de la tarea a eliminar: ")
                if self.task_service.eliminar_tarea(id_tarea):
                    print("✅ Tarea eliminada correctamente.")
                else:
                    print("❌ Tarea no encontrada.")

            elif opcion == "6":
                print("Saliendo del gestor... ¡Éxitos en tus estudios!")
                break
            else:
                print("❌ Opción no válida.")

    def _imprimir_tareas(self, tareas):
        if not tareas:
            print("No hay tareas para mostrar.")
        else:
            print("\nLista de tareas:")
            for t in tareas:
                print(t)