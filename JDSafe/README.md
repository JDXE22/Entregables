# JDSafe - Sistema de Gestión e Interfaz de Seguridad

¡Bienvenido al repositorio de **JDSafe**! Este es un programa interactivo basado en consola diseñado para gestionar la logística, el registro de usuarios (clientes e instructores), el control de vehículos y la programación de citas para módulos de seguridad y asistencia.

## 📋 Descripción General

El script principal (`menu.py`) expone una interfaz de menú numérico robusta que guía al usuario a través de las diferentes operaciones del sistema. Cuenta con control de flujo continuo y manejo de excepciones para asegurar una experiencia de usuario estable ante entradas no válidas.

## 🚀 Funcionalidades Principales

El menú interactivo permite acceder a las siguientes opciones:

1. **Programar citas:** Programación y asignación de franjas horarias.
2. **Asistencias y observaciones:** Registro y seguimiento del cumplimiento y bitácoras operativas.
3. **Registrar clientes:** Módulo para dar de alta nuevos usuarios en el sistema.
4. **Registrar instructor:** Registro del personal técnico o de instrucción.
5. **Registrar vehículo:** Gestión y control de la flota vehicular asignada.
6. **Consultar citas agendadas por fecha:** Vista general de los compromisos programados en una fecha específica.
7. **Consultar historial del cliente:** Trazabilidad completa de las interacciones y registros de cada cliente.
8. **Consultar horarios disponibles:** Visualización de horarios libres para agendar citas.
0. **Salir del programa:** Finaliza de manera segura la ejecución del sistema.

## 🛠️ Tecnologías Utilizadas

* **Python 3.x**
* Módulos personalizados para funcionalidades específicas:
  - `interfaces`: Contiene las funcionalidades principales del sistema (citas, clientes, instructores, vehículos, horarios, asistencias).
  - `helpers`: Proporciona funciones auxiliares como manejo de archivos y validaciones.
* Control de flujo iterativo (`while True`) para mantener el menú activo.
* Estructuras condicionales anidadas (`if-elif-else`) para la lógica del menú.
* Manejo de excepciones robusto (`try-except-else`) para capturar errores y prevenir fallos.

## 📂 Estructura del Proyecto

```
JDSafe/
├── menu.py          # Script principal del programa
├── README.md        # Documentación del proyecto
├── helpers/         # Funciones auxiliares
│   ├── funciones_txt.py
│   ├── validaciones.py
├── interfaces/      # Funcionalidades principales del sistema
│   ├── asistencias.py
│   ├── citas.py
│   ├── clientes.py
│   ├── horarios.py
│   ├── instructores.py
│   ├── vehiculos.py
└── data/            # Archivos de datos generados por el sistema (citas, clientes, etc.)
```

## 💻 Requisitos e Instalación

Para ejecutar este script, solo necesitas tener instalado Python en tu entorno local.

1. Clona este repositorio o descarga el archivo fuente.
2. Asegúrate de que la carpeta `data/` exista en el directorio raíz del proyecto. Si no existe, créala manualmente.
3. Abre una terminal en la ruta del archivo.
4. Ejecuta el siguiente comando:

```bash
python3 menu.py
```

Si el comando anterior no funciona debido a problemas de configuración del entorno, prueba con:

```bash
python3 -m menu
```

> **Nota:** Asegúrate de que el archivo `menu.py` esté en el directorio raíz del proyecto o en el `PYTHONPATH`.

## 🛡️ Manejo de Errores

El sistema implementa bloques `try-except` para capturar y manejar errores de manera eficiente:

* **`ValueError`**: Maneja entradas no válidas, como caracteres en lugar de números.
* **`TypeError`**: Previene fallos cuando se ingresan tipos de datos incompatibles.
* **`Exception`**: Captura genérica de cualquier error inesperado para evitar cierres abruptos del programa. El mensaje de error correspondiente se imprime en la consola para facilitar la depuración.

> **Nota:** Se recomienda revisar los mensajes de error en la consola para identificar posibles problemas en la ejecución.

## 📜 Detalles Adicionales

### Módulos Personalizados

1. **`helpers/funciones_txt.py`**: Maneja la lectura, escritura y actualización de archivos de texto utilizados como base de datos.
2. **`helpers/validaciones.py`**: Contiene funciones para validar la disponibilidad de instructores, vehículos y citas.
3. **`interfaces/`**: Contiene las funcionalidades principales del sistema:
   - `citas.py`: Permite agendar y consultar citas.
   - `clientes.py`: Maneja el registro de clientes.
   - `instructores.py`: Maneja el registro de instructores.
   - `vehiculos.py`: Permite registrar vehículos.
   - `horarios.py`: Muestra horarios disponibles.
   - `asistencias.py`: Registra y consulta asistencias y observaciones.

### Archivos de Datos

Los datos generados por el sistema se almacenan en archivos de texto dentro de la carpeta `data/`. Estos archivos incluyen:
- `clientes.txt`: Información de los clientes registrados.
- `instructores.txt`: Información de los instructores registrados.
- `vehiculos.txt`: Información de los vehículos registrados.
- `citas_clientes.txt`: Información de las citas programadas.
- `asistencias.txt`: Registro de asistencias y observaciones.

¡Gracias por usar **JDSafe**! Si tienes alguna pregunta o sugerencia, no dudes en contactarnos.