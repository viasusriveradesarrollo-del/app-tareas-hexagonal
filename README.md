# Gestor de Tareas Académicas - Arquitectura Hexagonal 🏛️

Este proyecto es una aplicación de consola para la gestión de tareas académicas, desarrollada aplicando los principios de la **Arquitectura Hexagonal** (también conocida como Puertos y Adaptadores). 

## Descripción del Problema
La aplicación permite a los usuarios registrar, consultar, completar y listar tareas pendientes de forma estructurada. Su propósito principal es evidenciar la separación de responsabilidades entre la lógica de negocio (el dominio) y la infraestructura (interfaz de usuario y almacenamiento), logrando un sistema con un alto nivel de desacoplamiento.

## Estructura del Proyecto
El código está organizado estrictamente en tres capas para aislar el dominio de los detalles técnicos:

* **`domain/`**: Es el corazón del software. Contiene la entidad `Tarea` y las reglas de negocio (por ejemplo, evitar que se registren tareas sin título). No tiene dependencias externas.
* **`application/`**: Contiene los **Casos de Uso** (`TaskService`) que orquestan las acciones del usuario, y los **Puertos** (`TaskRepository`), que son las interfaces o contratos que definen cómo se comunica el sistema con el exterior[cite: 1].
* **`infrastructure/`**: Contiene los **Adaptadores**[cite: 1]. Aquí se implementan los detalles técnicos:
  * `MemoryTaskRepository`: Adaptador de salida para persistencia básica en memoria[cite: 1].
  * `ConsoleAdapter`: Adaptador de entrada funcional a través de una Interfaz de Línea de Comandos (CLI)[cite: 1].

## Tecnologías Usadas
* **Lenguaje:** Python 3.x[cite: 1]
* **Librerías estándar:** `uuid` (para identificar tareas de forma única) y `abc` (para definir los puertos mediante clases abstractas).

## Instrucciones de Ejecución
Sigue estos pasos para ejecutar el proyecto en tu máquina local[cite: 1]:

1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Clona este repositorio en tu equipo:
   ```bash
   git clone [https://github.com/viasusriveradesarrollo-del/app-tareas-hexagonal.git](https://github.com/viasusriveradesarrollo-del/app-tareas-hexagonal.git)
