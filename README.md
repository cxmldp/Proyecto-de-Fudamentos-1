# 🏥 Sistema de Gestión Hospitalaria y Diagnóstico Médico

## 📋 Descripción

Sistema integral de gestión hospitalaria desarrollado en Python que combina:

1. **Sistema Experto de Diagnóstico Médico** (Entrega 1) - Utiliza únicamente condicionales para identificar 20 posibles enfermedades
2. **Sistema de Gestión de Pacientes** (Entrega 2) - Permite registrar, editar y consultar información de pacientes con persistencia de datos

---

## ✨ Características Principales

### 🔬 Sistema de Diagnóstico (Entrega 1)
- ✅ **Solo condicionales**: Implementación usando if/elif/else exclusivamente
- ✅ **20 enfermedades**: Cubre una amplia gama de condiciones médicas
- ✅ **Validación robusta**: 6 tipos de validaciones para minimizar errores
- ✅ **Búsqueda flexible**: Reconoce variaciones y sinónimos de síntomas
- ✅ **Manejo de tildes**: Acepta síntomas con o sin acentos

### 👥 Sistema de Gestión de Pacientes (Entrega 2)
- ✅ **Registro de pacientes**: Datos personales completos
- ✅ **Edición de información**: Actualización individual o completa
- ✅ **Historial médico**: Enfermedades, tratamientos y alergias
- ✅ **Persistencia de datos**: Almacenamiento en archivos de texto
- ✅ **Búsqueda flexible**: Por ID o nombre de paciente
- ✅ **Integración completa**: El diagnóstico se guarda automáticamente en el historial

---

## 🚀 Instalación y Uso

### Requisitos
- Python 3.6 o superior
- Sistema operativo: Windows, Linux o macOS

### Ejecución

```bash
python diagnostico_medico.py
```

### Menú Principal

```
====================================================
    SISTEMA DE GESTIÓN HOSPITALARIA
    Y DIAGNÓSTICO MÉDICO
====================================================

📋 MENÚ PRINCIPAL
----------------------------------------------------
1. Realizar diagnóstico médico (Entrega 1)
2. Agregar nuevo paciente
3. Editar información de paciente
4. Consultar paciente y gestionar historial
0. Salir del sistema
----------------------------------------------------
```

---

## 🛠️ Funcionalidades Detalladas

### 1️⃣ Realizar Diagnóstico Médico

Sistema de diagnóstico basado en síntomas que utiliza **únicamente condicionales**.

**Validaciones implementadas:**
1. ❌ Entrada vacía no permitida
2. ❌ Longitud: 2-50 caracteres
3. ❌ Solo texto (no números puros)
4. ❌ Debe contener al menos una letra
5. ❌ Sin caracteres especiales problemáticos
6. ✅ Normalización automática (minúsculas, espacios)

**Ejemplo de uso:**
```
Ingresa tu síntoma #1: FIEBRE
Ingresa tu síntoma #2: tos
Ingresa tu síntoma #3: DIFICULTAD PARA RESPIRAR

Diagnóstico: Podría ser COVID-19. Por favor, consulta a un médico.
```

### 2️⃣ Agregar Nuevo Paciente

Registro completo de pacientes con validación de datos:

**Información requerida:**
- Número de identificación (único)
- Nombre completo (mínimo 3 caracteres)
- Fecha de nacimiento (DD/MM/AAAA)
- Género (M/F/Otro)
- Celular de contacto
- Fecha de registro (automática)

**Ejemplo:**
```
Número de identificación: 12345678
Nombre completo: Juan Pérez
Fecha de nacimiento: 15/05/1990
Género (M/F/Otro): M
Celular de contacto: 3001234567

✅ Paciente agregado exitosamente!
```

### 3️⃣ Editar Información de Paciente

Búsqueda por ID o nombre y edición selectiva o completa:

**Opciones de edición:**
1. Nombre completo
2. Fecha de nacimiento
3. Género
4. Celular de contacto
5. Editar todo
0. Cancelar

### 4️⃣ Consultar Paciente y Gestionar Historial

Visualización completa de información y gestión de historial médico:

**Información mostrada:**
- 📋 Datos personales del paciente
- 🦠 Enfermedades diagnosticadas (con síntomas y fechas)
- 💊 Tratamientos recetados (medicamentos y dosis)
- ⚠️ Alergias registradas (alérgenos y síntomas)

**Submenú de gestión:**
- 5. Agregar una enfermedad (con diagnóstico automático)
- 6. Agregar un tratamiento
- 7. Agregar una alergia
- 0. Volver al menú principal

---

## 🦠 Enfermedades Diagnosticables

El sistema puede identificar 20 condiciones médicas:

| # | Enfermedad | Síntomas Clave |
|---|------------|----------------|
| 1 | **COVID-19** | fiebre, tos, dificultad para respirar |
| 2 | **Meningitis** | dolor de cabeza, rigidez en el cuello, fiebre |
| 3 | **Gastroenteritis** | náuseas, vómitos, dolor abdominal |
| 4 | **Resfriado común** | dolor de garganta, tos, congestión nasal |
| 5 | **Sarampión** | fiebre, sarpullido, ojos rojos |
| 6 | **Ataque al corazón** | dolor de pecho, dificultad para respirar, sudoración excesiva |
| 7 | **Hepatitis** | dolor abdominal, ictericia, fatiga |
| 8 | **Reacción alérgica** | picazón, erupción, hinchazón |
| 9 | **Infección de oído** | dolor de oído, drenaje del oído, pérdida de audición |
| 10 | **Gripe** | fiebre, escalofríos, dolor muscular |
| 11 | **Problema cardíaco** | dolor en el pecho, mareos, palpitaciones |
| 12 | **Trastorno metabólico** | pérdida de apetito, pérdida de peso, fatiga extrema |
| 13 | **Problema nervioso/muscular** | dolor de espalda, dolor en las piernas, entumecimiento |
| 14 | **Derrame cerebral** | pérdida de memoria, confusión, dificultad para hablar |
| 15 | **Hipotiroidismo** | fatiga, depresión, aumento de peso |
| 16 | **Diabetes** | sed excesiva, frecuencia urinaria, visión borrosa |
| 17 | **Tuberculosis** | tos persistente, pérdida de peso, sudores nocturnos |
| 18 | **Artritis** | dolor articular, rigidez, hinchazón |
| 19 | **Anemia** | fatiga extrema, falta de aliento, dolor en el pecho |
| 20 | **Infección ocular/glaucoma** | visión borrosa, dolor ocular, enrojecimiento |

---

## 📁 Estructura del Proyecto

```
proyecto-fundamentos/
│
├── diagnostico_medico.py    # Código principal del sistema
├── pacientes.txt             # Base de datos de pacientes (generado)
├── historial_medico.txt      # Historial médico (generado)
├── README.md                 # Este archivo
└── .gitignore                # Archivos excluidos de Git
```

### 📊 Formato de Archivos de Datos

**pacientes.txt:**
```
ID|Nombre Completo|Fecha Nacimiento|Género|Celular|Fecha Registro
```

**historial_medico.txt:**
```
ID|tipo|dato1|dato2|fecha
```
Tipos: `enfermedad`, `tratamiento`, `alergia`

---

## 💻 Estructura del Código

### Funciones Principales

#### 🔹 Persistencia de Datos
- `cargar_pacientes()` - Carga pacientes desde archivo
- `guardar_pacientes()` - Guarda pacientes en archivo
- `cargar_historial_medico()` - Carga historial desde archivo
- `guardar_historial_medico()` - Guarda historial en archivo

#### 🔹 Gestión de Pacientes
- `agregar_paciente()` - Registra nuevo paciente
- `editar_paciente()` - Modifica información de paciente
- `buscar_paciente()` - Busca por ID o nombre
- `consultar_paciente()` - Muestra información completa

#### 🔹 Historial Médico
- `agregar_enfermedad()` - Registra diagnóstico
- `agregar_tratamiento()` - Registra tratamiento
- `agregar_alergia()` - Registra alergia

#### 🔹 Diagnóstico (Entrega 1)
- `diagnostico_sintomas()` - Interfaz de diagnóstico original
- `realizar_diagnostico()` - **Lógica de diagnóstico usando SOLO condicionales**

#### 🔹 Sistema
- `main()` - Menú principal integrado

---

## 🎯 Ejemplos de Uso Completos

### Ejemplo 1: Diagnóstico y Registro en Historial

```
1. Seleccionar opción 4 (Consultar paciente)
2. Ingresar ID del paciente
3. Seleccionar opción 5 (Agregar enfermedad)
4. Ingresar los síntomas:
   - Síntoma #1: fiebre
   - Síntoma #2: escalofríos
   - Síntoma #3: dolor muscular

Resultado:
Diagnóstico: Podría ser una gripe. Descansa, mantente hidratado y consulta a un médico si los síntomas persisten.
✅ Enfermedad agregada al historial del paciente.
```

### Ejemplo 2: Agregar Tratamiento

```
1. Consultar paciente (opción 4)
2. Seleccionar opción 6 (Agregar tratamiento)
3. Ingresar:
   - Medicamentos: Paracetamol, Ibuprofeno
   - Dosis: 500mg cada 8 horas, 400mg cada 6 horas

✅ Tratamiento agregado al historial del paciente.
```

---

## ⚠️ Notas Importantes

### Advertencia Médica
> **⚠️ IMPORTANTE**: Este es un sistema **educativo** únicamente desarrollado como proyecto académico. **NO debe utilizarse para diagnósticos médicos reales**. Siempre consulte a un médico profesional calificado.

### Privacidad de Datos
- Los archivos `pacientes.txt` y `historial_medico.txt` contienen información sensible
- Estos archivos están excluidos del repositorio Git por seguridad
- En un entorno real, se deberían implementar medidas adicionales de seguridad

---

## 🛡️ Seguridad y Privacidad

Los siguientes archivos están excluidos del control de versiones:
- `pacientes.txt` - Datos personales
- `historial_medico.txt` - Información médica sensible
- `*.pyc`, `__pycache__/` - Archivos de Python compilados

---

## 🔧 Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **Paradigma**: Programación estructurada
- **Estructuras de control**: if/elif/else (condicionales)
- **Estructuras de datos**: Diccionarios, listas
- **Persistencia**: Archivos de texto plano
- **Módulos estándar**: `os`, `datetime`

### Conceptos Aplicados
- ✅ Condicionales anidados
- ✅ Validación de entrada de usuario
- ✅ Manejo de archivos (lectura/escritura)
- ✅ Estructuras de datos complejas
- ✅ Funciones y modularización
- ✅ Manejo de excepciones
- ✅ Normalización de datos

---

## 👥 Autores

- **Camilo Delgado** - [@cxmldp](https://github.com/cxmldp)
- **Tania Guerra**
- **Angel Mendoza**

---

## 📚 Proyecto Académico

**Curso**: Fundamentos de Programación  
**Institución**: [Tu institución]  
**Año**: 2025  

### Entregas
- ✅ **Entrega 1**: Sistema de diagnóstico médico usando condicionales
- ✅ **Entrega 2**: Sistema de gestión de pacientes con persistencia

---

## 📝 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

## 🤝 Contribuciones

Este es un proyecto académico. Si deseas contribuir o reportar problemas, por favor contacta a los autores.

---

## 📞 Contacto

Para preguntas o sugerencias sobre el proyecto, contactar a:
- GitHub: [@cxmldp](https://github.com/cxmldp)
- Repositorio: [Proyecto-de-Fudamentos-1](https://github.com/cxmldp/Proyecto-de-Fudamentos-1)

---

**¡Gracias por visitar nuestro proyecto! 🙌**
