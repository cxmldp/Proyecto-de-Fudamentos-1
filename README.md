# Sistema de Gestión Hospitalaria y Diagnóstico Médico 🏥

Proyecto desarrollado para la asignatura de Fundamentos de Programación. Este sistema permite gestionar pacientes, historiales médicos y realizar diagnósticos preliminares.

---

## 🚀 Novedades de la Tercera Entrega (GUI)

Esta versión implementa una **Interfaz Gráfica de Usuario (GUI)** completa usando `tkinter`, reemplazando la consola de texto.

### ✨ Características Principales
*   **Interfaz Visual**: Ventanas amigables, botones y formularios intuitivos.
*   **Gestión de Pacientes**: 
    *   Registro completo con Nombres, Apellidos, Documento, Correo y Celular.
    *   Validaciones estrictas (formato de correo, celular de 10 dígitos).
    *   Cálculo automático de la **Edad** y **Fecha de Registro**.
*   **Historial Médico Independiente**:
    *   Permite agregar **Enfermedades**, **Tratamientos** y **Alergias** de forma independiente.
    *   Integración del **Sistema de Diagnóstico** (Entrega 1) dentro de la interfaz visual.
*   **Persistencia**: Todos los datos se guardan automáticamente en archivos locales (`.txt`).

---

## 📋 Requisitos Previos

*   Python 3.x instalado en el sistema.
*   No requiere librerías externas (usa `tkinter` nativo).

---

## 🛠️ Cómo Ejecutar

1.  Clona o descarga este repositorio.
2.  Abre una terminal en la carpeta del proyecto.
3.  Ejecuta el siguiente comando:

```bash
python diagnostico_medico.py
```

4.  ¡Listo! Se abrirá la ventana del sistema.

---

## 🧪 Guía de Uso Rápida

1.  **Agregar Paciente**: Desde el menú principal, ingresa los datos del paciente. El sistema validará que el correo y celular sean correctos.
2.  **Consultar**: Busca un paciente por su documento de identidad.
3.  **Historial**: En la vista de detalle, usa los botones para agregar registros médicos.
    *   *Tip*: Al agregar una enfermedad, ingresa 3 síntomas para recibir un diagnóstico automático.
4.  **Listar**: Visualiza la tabla completa de pacientes registrados.

---

## 📂 Estructura del Proyecto

*   `diagnostico_medico.py`: Código fuente principal (contiene toda la lógica y la interfaz).
*   `pacientes.txt`: Base de datos local de pacientes (se crea automáticamente).
*   `historial_medico.txt`: Base de datos local de historiales (se crea automáticamente).

---

**Autor:** Estudiante  
**Fecha:** 2025
