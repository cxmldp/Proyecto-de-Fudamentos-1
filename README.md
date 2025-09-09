# Sistema Experto de Diagnóstico Médico

## Descripción
Este es un sistema educativo de diagnóstico médico desarrollado en Python que utiliza únicamente condicionales para identificar posibles enfermedades basándose en síntomas ingresados por el usuario.

## Características
- ✅ **Solo condicionales**: Cumple con el requisito del proyecto
- ✅ **Validación robusta**: Minimiza errores del usuario
- ✅ **Interfaz amigable**: Mensajes claros y profesionales
- ✅ **20 enfermedades**: Cubre una amplia gama de condiciones médicas
- ✅ **Manejo de errores**: Respuestas apropiadas para casos no encontrados

## Instalación y Uso

### Requisitos
- Python 3.6 o superior

### Ejecución
```bash
python diagnostico_medico.py
```

## Funcionalidades de Validación

El sistema incluye múltiples validaciones para minimizar errores:

1. **Validación de entrada vacía**: No permite síntomas vacíos
2. **Validación de longitud**: Síntomas entre 2-50 caracteres
3. **Validación de tipo**: Solo acepta texto, no números
4. **Validación de contenido**: Debe contener al menos una letra
5. **Validación de caracteres especiales**: Rechaza símbolos problemáticos (@, #, $, etc.)
6. **Normalización robusta**: Convierte todo a minúsculas y elimina espacios extra
7. **Búsqueda flexible**: Reconoce variaciones y sinónimos de síntomas
8. **Manejo de tildes**: Acepta tanto "escalofríos" como "escalofrios"

## Enfermedades Soportadas

El sistema puede identificar las siguientes condiciones:

1. **COVID-19**: fiebre, tos, dificultad para respirar
2. **Meningitis**: dolor de cabeza, rigidez en el cuello, fiebre
3. **Gastroenteritis**: náuseas, vómitos, dolor abdominal
4. **Resfriado común**: dolor de garganta, tos, congestión nasal
5. **Sarampión**: fiebre, sarpullido, ojos rojos
6. **Ataque al corazón**: dolor de pecho, dificultad para respirar, sudoración excesiva
7. **Hepatitis**: dolor abdominal, ictericia, fatiga
8. **Reacción alérgica**: picazón, erupción, hinchazón
9. **Infección de oído**: dolor de oído, drenaje del oído, pérdida de audición
10. **Gripe**: fiebre, escalofríos, dolor muscular
11. **Problema cardíaco**: dolor en el pecho, mareos, palpitaciones
12. **Trastorno metabólico**: pérdida de apetito, pérdida de peso, fatiga extrema
13. **Problema nervioso/muscular**: dolor de espalda, dolor en las piernas, entumecimiento
14. **Derrame cerebral**: pérdida de memoria, confusión, dificultad para hablar
15. **Hipotiroidismo**: fatiga, depresión, aumento de peso
16. **Diabetes**: sed excesiva, frecuencia urinaria, visión borrosa
17. **Tuberculosis**: tos persistente, pérdida de peso, sudores nocturnos
18. **Artritis**: dolor articular, rigidez, hinchazón
19. **Anemia**: fatiga extrema, falta de aliento, dolor en el pecho
20. **Infección ocular/glaucoma**: visión borrosa, dolor ocular, enrojecimiento

## Ejemplo de Uso

### Ejemplo 1: COVID-19
```
Ingresa tu síntoma #1: FIEBRE
Ingresa tu síntoma #2: tos
Ingresa tu síntoma #3: DIFICULTAD PARA RESPIRAR

Diagnóstico: Podría ser COVID-19. Por favor, consulta a un médico.
```

### Ejemplo 2: Gripe
```
Ingresa tu síntoma #1: ESCALOFRÍOS
Ingresa tu síntoma #2: fiebre
Ingresa tu síntoma #3: dolor muscular

Diagnóstico: Podría ser una gripe. Descansa, mantente hidratado y consulta a un médico si los síntomas persisten.
```

### Ejemplo 3: Anemia
```
Ingresa tu síntoma #1: FATIGA EXTREMA
Ingresa tu síntoma #2: FALTA DE ALIENTO
Ingresa tu síntoma #3: DOLOR en el pecho

Diagnóstico: Podría ser anemia. Por favor, realiza un examen de sangre.
```

## Notas Importantes

⚠️ **ADVERTENCIA**: Este es un sistema educativo únicamente. No debe utilizarse para diagnósticos médicos reales. Siempre consulte a un médico profesional.

## Estructura del Código

- `main()`: Función principal que maneja la interfaz de usuario
- `realizar_diagnostico()`: Función que contiene toda la lógica de diagnóstico usando condicionales
- Validaciones integradas para minimizar errores del usuario

## Tecnologías Utilizadas

- **Python 3.x**
- **Solo condicionales** (if/elif/else)
- **Validación de entrada**
- **Manejo de strings**

## Autores

- Camilo Delgado
- Tania Guerra
- Angel Mendoza

Proyecto desarrollado para Fundamentos de Programación
