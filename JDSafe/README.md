# JDSafe - Sistema de Gestión e Interfaz de Seguridad

¡Bienvenido al repositorio de **JDSafe**! Este es un programa interactivo basado en consola diseñado para gestionar la logística, el registro de usuarios (clientes e instructores), el control de vehículos y la programación de citas para módulos de seguridad y asistencia.

## 📋 Descripción General

El script principal expone una interfaz de menú numérico robusta que guía al usuario a través de las diferentes operaciones del sistema. Cuenta con control de flujo continuo y manejo de excepciones para asegurar una experiencia de usuario estable ante entradas no válidas.

## 🚀 Funcionalidades Principales

El menú interactivo permite acceder a las siguientes opciones:

1. **Programar citas:** Programación y asignación de franjas horarias.
2. **Asistencias y observaciones:** Registro y seguimiento del cumplimiento y bitácoras operativas.
3. **Registrar clientes:** Módulo para dar de alta nuevos usuarios en el sistema.
4. **Registrar instructor:** Registro del personal técnico o de instrucción.
5. **Registrar vehículo:** Gestión y control de la flota vehicular asignada.
6. **Consultar citas agendadas:** Vista general de los compromisos programados.
7. **Consultar historial del cliente:** Trazabilidad completa de las interacciones y registros de cada cliente.
0. **Salir del programa:** Finaliza de manera segura la ejecución del sistema.

## 🛠️ Tecnologías Utilizadas

* **Python 3.x**
* Control de flujo iterativo (`while True`)
* Estructuras condicionales anidadas (`if-elif-else`)
* Manejo de excepciones robusto (`try-except-else`)

## 💻 Requisitos e Instalación

Para ejecutar este script, solo necesitas tener instalado Python en tu entorno local.

1. Clona este repositorio o descarga el archivo fuente.
2. Abre una terminal en la ruta del archivo.
3. Ejecuta el siguiente comando:

```bash
python3 menu.py
```

## 🛡️ Manejo de Errores

El sistema implementa bloques `try-except` para capturar:
* `TypeError`: Previene fallos cuando se ingresan tipos de datos incompatibles.
* `Exception`: Captura genérica de cualquier error inesperado para evitar cierres abruptos del programa, imprimiendo el mensaje de error correspondiente.