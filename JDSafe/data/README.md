# JDSafe - Sistema de Gestión e Interfaz de Seguridad

¡Bienvenido al repositorio de **JDSafe**! Este es un programa interactivo basado en consola diseñado para gestionar la logística, el registro de usuarios (clientes e instructores), el control de vehículos y la programación de citas para módulos de seguridad y asistencia.

## 📋 Descripción General

El script principal (`menu.py`) expone una interfaz de menú numérico robusta que guía al usuario a través de las diferentes operaciones del sistema. Cuenta con control de flujo continuo, loops de validación específicos por sección para evitar reescritura de datos, y manejo de excepciones para asegurar una experiencia de usuario sumamente estable ante entradas no válidas o colisiones en la programación.

## 🚀 Funcionalidades Principales

El menú interactivo permite acceder a las siguientes operaciones, las cuales han sido optimizadas para mejorar la experiencia de usuario (UX) y la consistencia de los datos:

1. **Programar citas (Agendamiento Inteligente):**
   - **Menús Numéricos e Indexados:** Se eliminó la digitación manual de horarios e instructores. Los instructores aptos y los bloques de horarios se seleccionan mediante un número de opción para evitar errores de tipeo.
   - **Filtro Dinámico:** Al agendar, el sistema detecta la categoría de vehículo elegida (Moto o Carro) y lista únicamente a los instructores calificados con esa especialidad.
   - **Validación de Fechas Futuras:** El sistema rechaza fechas en el pasado y notifica al usuario en sitio.
   - **Loop de Reintento Específico:** En caso de que el instructor o el vehículo ya estén ocupados en la fecha/hora seleccionada, el flujo solo vuelve a solicitar la fecha y bloque de horario, sin forzar a reiniciar todo el formulario de inscripción del cliente.
   - **Código Único de Cita:** Genera de forma automática un código de cita de 3 dígitos (del 100 al 999) garantizando la no duplicidad.

2. **Asistencias y observaciones (Enlace de Registros):**
   - El registro de asistencias busca y valida la cita programada mediante su código único de 3 dígitos.
   - Si la cita existe, el sistema **autocompleta la fecha** directamente desde la base de datos de citas, eliminando la redundancia y solicitando únicamente la observación al instructor.
   - Almacena el historial como cadena formateada (`str`) para mantener una persistencia compatible al 100% con los intérpretes de texto.

3. **Registrar clientes:** Módulo para dar de alta nuevos usuarios con validación estricta de formato y longitud de documentos de identidad (6 a 10 dígitos) y nombres.
4. **Registrar instructor:** Registro del personal docente verificando especialidades y disponibilidad.
5. **Registrar vehículo:** Gestión del parque vehicular (Moto/Carro) validando formatos sintácticos de placa (Carro: `ABC123` / Moto: `ABC12D`).
6. **Consultar citas agendadas por fecha:** Muestra el listado estructurado de citas de una fecha con su código, instructor, tipo de vehículo y hora.
7. **Consultar historial del cliente:** Trazabilidad completa de las citas de un cliente mediante su documento.
8. **Consultar horarios disponibles (Vista de Estado):** Presenta los 9 bloques del día con su indicador dinámico de disponibilidad: `[LIBRE]` u `[OCUPADO]`.
9. **Salir del programa:** Cierre seguro y liberación de la ejecución.

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- Módulos personalizados para funcionalidades específicas:
  - `interfaces`: Contiene las funcionalidades del sistema (citas, clientes, instructores, vehículos, horarios, asistencias).
  - `helpers`: Proporciona funciones auxiliares como manejo de archivos (`funciones_txt.py`) y validaciones lógicas (`validaciones.py`).
- Control de flujo secuencial y modular con loops independientes en pantallas clave.
- Serialización segura y robusta a archivos de texto plano mediante `ast.literal_eval`.

## 📂 Estructura del Proyecto

```
JDSafe/
├── menu.py          # Script principal del programa (Menú e Integración)
├── helpers/         # Funciones auxiliares y lógica del negocio
│   ├── funciones_txt.py  # Lectura, escritura y cálculo de almacenamiento
│   └── validaciones.py   # Validaciones de especialidades, colisiones y existencia
├── interfaces/      # Interfaces de interacción por consola
│   ├── asistencias.py
│   ├── citas.py
│   ├── clientes.py
│   ├── horarios.py
│   ├── instructores.py
│   └── vehiculos.py
└── data/            # Archivos de persistencia generados por el sistema
    ├── README.md         # Documentación del proyecto
    ├── clientes.txt      # Clientes registrados
    ├── instructores.txt  # Instructores disponibles
    ├── vehiculos.txt     # Vehículos registrados
    ├── citas_clientes.txt# Citas agendadas
    └── asistencias.txt   # Historial de observaciones y asistencias
```

## 💻 Requisitos e Instalación

Para ejecutar este programa localmente:

1. Asegúrate de tener instalado Python en tu entorno.
2. Abre una terminal en la raíz del proyecto.
3. Ejecuta el archivo principal:

```bash
python menu.py
```

o

```bash
python3 -m menu
```

## 🛡️ Manejo de Errores y Robustez

El sistema implementa validaciones estrictas y capturas de excepciones en cada pantalla:

- **`ValueError`**: Captura caracteres no válidos donde se esperan enteros (menús, bloque de horarios, documentos).
- **`AttributeError` / `TypeError`**: Prevención de fallos durante la manipulación de arreglos y diccionarios cargados desde los archivos.
- **Control de Duplicidades**: Verificación en tiempo real leyendo directamente del almacenamiento físico en cada registro para evitar registros idénticos simultáneos.
