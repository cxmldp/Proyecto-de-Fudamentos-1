"""
Sistema Experto de Diagnóstico Médico
Proyecto de Fundamentos de Programación
Autor: Estudiante
"""

import os
from datetime import datetime

# ==================== FUNCIONES DE PERSISTENCIA ====================

def cargar_pacientes():
    """Carga los pacientes desde el archivo pacientes.txt"""
    pacientes = {}
    if os.path.exists("pacientes.txt"):
        try:
            with open("pacientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        datos = linea.split("|")
                        if len(datos) == 6:
                            num_id = datos[0]
                            pacientes[num_id] = {
                                "nombre_completo": datos[1],
                                "fecha_nacimiento": datos[2],
                                "genero": datos[3],
                                "celular_contacto": datos[4],
                                "fecha_registro": datos[5]
                            }
        except Exception as e:
            print(f"Error al cargar pacientes: {e}")
    return pacientes


def guardar_pacientes(pacientes):
    """Guarda los pacientes en el archivo pacientes.txt"""
    try:
        with open("pacientes.txt", "w", encoding="utf-8") as archivo:
            for num_id, datos in pacientes.items():
                linea = f"{num_id}|{datos['nombre_completo']}|{datos['fecha_nacimiento']}|{datos['genero']}|{datos['celular_contacto']}|{datos['fecha_registro']}\n"
                archivo.write(linea)
    except Exception as e:
        print(f"Error al guardar pacientes: {e}")


def cargar_historial_medico():
    """Carga el historial médico desde historial_medico.txt"""
    historial = {}
    if os.path.exists("historial_medico.txt"):
        try:
            with open("historial_medico.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        datos = linea.split("|")
                        if len(datos) >= 3:
                            num_id = datos[0]
                            tipo = datos[1]  # enfermedad, tratamiento, alergia
                            
                            if num_id not in historial:
                                historial[num_id] = {
                                    "enfermedades": [],
                                    "tratamientos": [],
                                    "alergias": []
                                }
                            
                            if tipo == "enfermedad" and len(datos) == 5:
                                historial[num_id]["enfermedades"].append({
                                    "sintomas": datos[2],
                                    "nombre_enfermedad": datos[3],
                                    "fecha_registro": datos[4]
                                })
                            elif tipo == "tratamiento" and len(datos) == 5:
                                historial[num_id]["tratamientos"].append({
                                    "medicamentos": datos[2],
                                    "dosis": datos[3],
                                    "fecha_registro": datos[4]
                                })
                            elif tipo == "alergia" and len(datos) == 5:
                                historial[num_id]["alergias"].append({
                                    "alergeno": datos[2],
                                    "sintomas": datos[3],
                                    "fecha_registro": datos[4]
                                })
        except Exception as e:
            print(f"Error al cargar historial médico: {e}")
    return historial


def guardar_historial_medico(historial):
    """Guarda el historial médico en historial_medico.txt"""
    try:
        with open("historial_medico.txt", "w", encoding="utf-8") as archivo:
            for num_id, datos in historial.items():
                # Guardar enfermedades
                for enfermedad in datos.get("enfermedades", []):
                    linea = f"{num_id}|enfermedad|{enfermedad['sintomas']}|{enfermedad['nombre_enfermedad']}|{enfermedad['fecha_registro']}\n"
                    archivo.write(linea)
                
                # Guardar tratamientos
                for tratamiento in datos.get("tratamientos", []):
                    linea = f"{num_id}|tratamiento|{tratamiento['medicamentos']}|{tratamiento['dosis']}|{tratamiento['fecha_registro']}\n"
                    archivo.write(linea)
                
                # Guardar alergias
                for alergia in datos.get("alergias", []):
                    linea = f"{num_id}|alergia|{alergia['alergeno']}|{alergia['sintomas']}|{alergia['fecha_registro']}\n"
                    archivo.write(linea)
    except Exception as e:
        print(f"Error al guardar historial médico: {e}")


# ==================== FUNCIONES DE GESTIÓN DE PACIENTES ====================

def agregar_paciente(pacientes):
    """Menú 2: Agregar un nuevo paciente"""
    print("\n" + "=" * 60)
    print("    AGREGAR NUEVO PACIENTE")
    print("=" * 60)
    
    # Solicitar número de identificación
    while True:
        num_id = input("\nNúmero de identificación: ").strip()
        if not num_id:
            print("❌ El número de identificación no puede estar vacío.")
            continue
        if num_id in pacientes:
            print("❌ Ya existe un paciente con este número de identificación.")
            continue
        break
    
    # Solicitar nombre completo
    while True:
        nombre = input("Nombre completo: ").strip()
        if not nombre:
            print("❌ El nombre no puede estar vacío.")
            continue
        if len(nombre) < 3:
            print("❌ El nombre debe tener al menos 3 caracteres.")
            continue
        break
    
    # Solicitar fecha de nacimiento
    while True:
        fecha_nac = input("Fecha de nacimiento (DD/MM/AAAA): ").strip()
        if not fecha_nac:
            print("❌ La fecha de nacimiento no puede estar vacía.")
            continue
        # Validación básica de formato
        if len(fecha_nac.split("/")) != 3:
            print("❌ Formato incorrecto. Usa DD/MM/AAAA")
            continue
        break
    
    # Solicitar género
    while True:
        genero = input("Género (M/F/Otro): ").strip().upper()
        if genero not in ["M", "F", "OTRO"]:
            print("❌ Género inválido. Usa M, F o Otro.")
            continue
        break
    
    # Solicitar celular de contacto
    while True:
        celular = input("Celular de contacto: ").strip()
        if not celular:
            print("❌ El celular no puede estar vacío.")
            continue
        break
    
    # Fecha de registro automática
    fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Agregar paciente
    pacientes[num_id] = {
        "nombre_completo": nombre,
        "fecha_nacimiento": fecha_nac,
        "genero": genero,
        "celular_contacto": celular,
        "fecha_registro": fecha_registro
    }
    
    guardar_pacientes(pacientes)
    
    print("\n✅ Paciente agregado exitosamente!")
    print(f"   ID: {num_id}")
    print(f"   Nombre: {nombre}")
    print(f"   Fecha de registro: {fecha_registro}")


def editar_paciente(pacientes):
    """Menú 3: Editar información de un paciente"""
    print("\n" + "=" * 60)
    print("    EDITAR PACIENTE")
    print("=" * 60)
    
    busqueda = input("\nIngresa el número de identificación o nombre del paciente: ").strip()
    
    # Buscar paciente
    paciente_encontrado = None
    num_id_encontrado = None
    
    # Buscar por número de identificación
    if busqueda in pacientes:
        paciente_encontrado = pacientes[busqueda]
        num_id_encontrado = busqueda
    else:
        # Buscar por nombre
        for num_id, datos in pacientes.items():
            if busqueda.lower() in datos["nombre_completo"].lower():
                paciente_encontrado = datos
                num_id_encontrado = num_id
                break
    
    if not paciente_encontrado:
        print("❌ No se encontró ningún paciente con esa información.")
        return
    
    # Mostrar información actual
    print("\n📋 Información actual del paciente:")
    print(f"   ID: {num_id_encontrado}")
    print(f"   1. Nombre: {paciente_encontrado['nombre_completo']}")
    print(f"   2. Fecha de nacimiento: {paciente_encontrado['fecha_nacimiento']}")
    print(f"   3. Género: {paciente_encontrado['genero']}")
    print(f"   4. Celular: {paciente_encontrado['celular_contacto']}")
    print(f"   Fecha de registro: {paciente_encontrado['fecha_registro']}")
    
    # Menú de edición
    print("\n¿Qué deseas editar?")
    print("1. Nombre completo")
    print("2. Fecha de nacimiento")
    print("3. Género")
    print("4. Celular de contacto")
    print("5. Editar todo")
    print("0. Cancelar")
    
    opcion = input("\nSelecciona una opción: ").strip()
    
    if opcion == "1":
        nuevo_valor = input("Nuevo nombre completo: ").strip()
        if nuevo_valor:
            paciente_encontrado["nombre_completo"] = nuevo_valor
            print("✅ Nombre actualizado.")
    elif opcion == "2":
        nuevo_valor = input("Nueva fecha de nacimiento (DD/MM/AAAA): ").strip()
        if nuevo_valor:
            paciente_encontrado["fecha_nacimiento"] = nuevo_valor
            print("✅ Fecha de nacimiento actualizada.")
    elif opcion == "3":
        nuevo_valor = input("Nuevo género (M/F/Otro): ").strip().upper()
        if nuevo_valor in ["M", "F", "OTRO"]:
            paciente_encontrado["genero"] = nuevo_valor
            print("✅ Género actualizado.")
    elif opcion == "4":
        nuevo_valor = input("Nuevo celular de contacto: ").strip()
        if nuevo_valor:
            paciente_encontrado["celular_contacto"] = nuevo_valor
            print("✅ Celular actualizado.")
    elif opcion == "5":
        nombre = input("Nombre completo: ").strip()
        fecha_nac = input("Fecha de nacimiento (DD/MM/AAAA): ").strip()
        genero = input("Género (M/F/Otro): ").strip().upper()
        celular = input("Celular de contacto: ").strip()
        
        if nombre:
            paciente_encontrado["nombre_completo"] = nombre
        if fecha_nac:
            paciente_encontrado["fecha_nacimiento"] = fecha_nac
        if genero in ["M", "F", "OTRO"]:
            paciente_encontrado["genero"] = genero
        if celular:
            paciente_encontrado["celular_contacto"] = celular
        
        print("✅ Información actualizada.")
    elif opcion == "0":
        print("Operación cancelada.")
        return
    else:
        print("❌ Opción inválida.")
        return
    
    pacientes[num_id_encontrado] = paciente_encontrado
    guardar_pacientes(pacientes)


def buscar_paciente(pacientes, busqueda):
    """Busca un paciente por ID o nombre"""
    # Buscar por número de identificación
    if busqueda in pacientes:
        return busqueda, pacientes[busqueda]
    
    # Buscar por nombre
    for num_id, datos in pacientes.items():
        if busqueda.lower() in datos["nombre_completo"].lower():
            return num_id, datos
    
    return None, None


def consultar_paciente(pacientes, historial):
    """Menú 4: Consultar información de un paciente y gestionar historial"""
    print("\n" + "=" * 60)
    print("    CONSULTAR PACIENTE")
    print("=" * 60)
    
    busqueda = input("\nIngresa el número de identificación o nombre del paciente: ").strip()
    
    num_id, paciente = buscar_paciente(pacientes, busqueda)
    
    if not paciente:
        print("❌ No se encontró ningún paciente con esa información.")
        return
    
    # Mostrar información del paciente
    print("\n" + "=" * 60)
    print("📋 INFORMACIÓN DEL PACIENTE")
    print("=" * 60)
    print(f"ID: {num_id}")
    print(f"Nombre: {paciente['nombre_completo']}")
    print(f"Fecha de nacimiento: {paciente['fecha_nacimiento']}")
    print(f"Género: {paciente['genero']}")
    print(f"Celular: {paciente['celular_contacto']}")
    print(f"Fecha de registro: {paciente['fecha_registro']}")
    
    # Mostrar historial médico
    print("\n" + "=" * 60)
    print("📋 HISTORIAL MÉDICO")
    print("=" * 60)
    
    if num_id in historial:
        # Enfermedades
        if historial[num_id].get("enfermedades"):
            print("\n🦠 ENFERMEDADES:")
            for i, enf in enumerate(historial[num_id]["enfermedades"], 1):
                print(f"   {i}. {enf['nombre_enfermedad']}")
                print(f"      Síntomas: {enf['sintomas']}")
                print(f"      Fecha: {enf['fecha_registro']}")
        else:
            print("\n🦠 ENFERMEDADES: Ninguna registrada")
        
        # Tratamientos
        if historial[num_id].get("tratamientos"):
            print("\n💊 TRATAMIENTOS:")
            for i, trat in enumerate(historial[num_id]["tratamientos"], 1):
                print(f"   {i}. Medicamentos: {trat['medicamentos']}")
                print(f"      Dosis: {trat['dosis']}")
                print(f"      Fecha: {trat['fecha_registro']}")
        else:
            print("\n💊 TRATAMIENTOS: Ninguno registrado")
        
        # Alergias
        if historial[num_id].get("alergias"):
            print("\n⚠️  ALERGIAS:")
            for i, aler in enumerate(historial[num_id]["alergias"], 1):
                print(f"   {i}. Alérgeno: {aler['alergeno']}")
                print(f"      Síntomas: {aler['sintomas']}")
                print(f"      Fecha: {aler['fecha_registro']}")
        else:
            print("\n⚠️  ALERGIAS: Ninguna registrada")
    else:
        print("\nNo hay historial médico registrado para este paciente.")
    
    # Submenú para gestionar historial
    while True:
        print("\n" + "=" * 60)
        print("¿Qué deseas hacer?")
        print("5. Agregar una enfermedad")
        print("6. Agregar un tratamiento")
        print("7. Agregar una alergia")
        print("0. Volver al menú principal")
        
        opcion = input("\nSelecciona una opción: ").strip()
        
        if opcion == "5":
            agregar_enfermedad(num_id, historial)
        elif opcion == "6":
            agregar_tratamiento(num_id, historial)
        elif opcion == "7":
            agregar_alergia(num_id, historial)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida.")


# ==================== FUNCIONES DE HISTORIAL MÉDICO ====================

def agregar_enfermedad(num_id, historial):
    """Menú 5: Agregar una enfermedad usando el sistema de diagnóstico"""
    print("\n" + "=" * 60)
    print("    AGREGAR ENFERMEDAD")
    print("=" * 60)
    print("\nEl sistema diagnosticará la enfermedad basándose en los síntomas.")
    print()
    
    # Solicitar los tres síntomas (igual que en el sistema original)
    sintomas = []
    
    for i in range(1, 4):
        while True:
            sintoma = input(f"Ingresa el síntoma #{i}: ").strip()
            
            if sintoma == "":
                print("❌ Error: Debes ingresar un síntoma. No puede estar vacío.")
                continue
            
            if len(sintoma) < 2:
                print("❌ Error: El síntoma debe tener al menos 2 caracteres.")
                continue
            
            if len(sintoma) > 50:
                print("❌ Error: El síntoma es demasiado largo. Máximo 50 caracteres.")
                continue
            
            if sintoma.isdigit():
                print("❌ Error: Los síntomas deben ser texto, no números.")
                continue
            
            if not any(c.isalpha() for c in sintoma):
                print("❌ Error: El síntoma debe contener al menos una letra.")
                continue
            
            sintomas.append(sintoma.lower())
            break
    
    # Realizar el diagnóstico
    diagnostico = realizar_diagnostico(sintomas)
    
    print("\n" + "=" * 60)
    print(f"Diagnóstico: {diagnostico}")
    print("=" * 60)
    
    # Guardar en el historial
    if num_id not in historial:
        historial[num_id] = {"enfermedades": [], "tratamientos": [], "alergias": []}
    
    sintomas_str = ", ".join(sintomas)
    fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    historial[num_id]["enfermedades"].append({
        "sintomas": sintomas_str,
        "nombre_enfermedad": diagnostico,
        "fecha_registro": fecha_registro
    })
    
    guardar_historial_medico(historial)
    
    print("\n✅ Enfermedad agregada al historial del paciente.")


def agregar_tratamiento(num_id, historial):
    """Menú 6: Agregar un tratamiento"""
    print("\n" + "=" * 60)
    print("    AGREGAR TRATAMIENTO")
    print("=" * 60)
    
    medicamentos = input("\nMedicamentos (separados por comas): ").strip()
    if not medicamentos:
        print("❌ Debes ingresar al menos un medicamento.")
        return
    
    dosis = input("Dosis de cada medicamento: ").strip()
    if not dosis:
        print("❌ Debes ingresar la dosis.")
        return
    
    fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    if num_id not in historial:
        historial[num_id] = {"enfermedades": [], "tratamientos": [], "alergias": []}
    
    historial[num_id]["tratamientos"].append({
        "medicamentos": medicamentos,
        "dosis": dosis,
        "fecha_registro": fecha_registro
    })
    
    guardar_historial_medico(historial)
    
    print("\n✅ Tratamiento agregado al historial del paciente.")


def agregar_alergia(num_id, historial):
    """Menú 7: Agregar una alergia"""
    print("\n" + "=" * 60)
    print("    AGREGAR ALERGIA")
    print("=" * 60)
    
    alergeno = input("\nAlérgeno: ").strip()
    if not alergeno:
        print("❌ Debes ingresar el alérgeno.")
        return
    
    sintomas = input("Síntomas: ").strip()
    if not sintomas:
        print("❌ Debes ingresar los síntomas.")
        return
    
    fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    if num_id not in historial:
        historial[num_id] = {"enfermedades": [], "tratamientos": [], "alergias": []}
    
    historial[num_id]["alergias"].append({
        "alergeno": alergeno,
        "sintomas": sintomas,
        "fecha_registro": fecha_registro
    })
    
    guardar_historial_medico(historial)
    
    print("\n✅ Alergia agregada al historial del paciente.")


# ==================== FUNCIÓN PRINCIPAL DE DIAGNÓSTICO (ENTREGA 1) ====================

def diagnostico_sintomas():
    """Función original de diagnóstico de síntomas (Entrega 1)"""
    print("\n" + "=" * 60)
    print("    SISTEMA EXPERTO DE DIAGNÓSTICO MÉDICO")
    print("=" * 60)
    print()
    print("Este sistema te ayudará a identificar posibles enfermedades")
    print("basándose en los síntomas que estés experimentando.")
    print()
    print("IMPORTANTE: Este es solo un sistema educativo.")
    print("Siempre consulta a un médico profesional para un diagnóstico real.")
    print()
    
    # Solicitar los tres síntomas
    sintomas = []
    
    for i in range(1, 4):
        while True:
            sintoma = input(f"Ingresa tu síntoma #{i}: ").strip()
            
            # Validar que no esté vacío
            if sintoma == "":
                print("❌ Error: Debes ingresar un síntoma. No puede estar vacío.")
                continue
            
            # Validar que no sea muy corto (menos de 2 caracteres)
            if len(sintoma) < 2:
                print("❌ Error: El síntoma debe tener al menos 2 caracteres.")
                continue
            
            # Validar que no sea muy largo (más de 50 caracteres)
            if len(sintoma) > 50:
                print("❌ Error: El síntoma es demasiado largo. Máximo 50 caracteres.")
                continue
            
            # Verificar que no sea un número
            if sintoma.isdigit():
                print("❌ Error: Los síntomas deben ser texto, no números.")
                continue
            
            # Verificar que no sea solo símbolos
            if not any(c.isalpha() for c in sintoma):
                print("❌ Error: El síntoma debe contener al menos una letra.")
                continue
            
            # Verificar que no contenga caracteres especiales problemáticos
            caracteres_problematicos = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
            if any(caracter in sintoma for caracter in caracteres_problematicos):
                print("❌ Error: El síntoma no debe contener caracteres especiales como @, #, $, etc.")
                continue
            
            sintomas.append(sintoma.lower())
            break
    
    print()
    print("Analizando tus síntomas...")
    print()
    
    # Realizar el diagnóstico
    diagnostico = realizar_diagnostico(sintomas)
    
    # Mostrar resultado
    print("=" * 60)
    print("    RESULTADO DEL DIAGNÓSTICO")
    print("=" * 60)
    print()
    print(f"Síntomas ingresados:")
    for i, sintoma in enumerate(sintomas, 1):
        print(f"  {i}. {sintoma}")
    print()
    print(f"Diagnóstico: {diagnostico}")
    print()
    print("=" * 60)


def realizar_diagnostico(sintomas):
    """
    Realiza el diagnóstico basándose en los síntomas ingresados.
    Usa solo condicionales para determinar la enfermedad.
    """
    
    # Normalizar síntomas para comparación (eliminar espacios extra y convertir a minúsculas)
    sintoma1 = sintomas[0].strip().lower()  
    sintoma2 = sintomas[1].strip().lower()
    sintoma3 = sintomas[2].strip().lower()
    
    # Crear lista combinada de síntomas para búsqueda más flexible
    todos_sintomas = sintoma1 + " " + sintoma2 + " " + sintoma3
    
    # COVID-19: fiebre, tos, dificultad para respirar
    if (("fiebre" in todos_sintomas or "temperatura" in todos_sintomas or "calentura" in todos_sintomas) and
        ("tos" in todos_sintomas or "toser" in todos_sintomas) and
        ("dificultad" in todos_sintomas or "problema" in todos_sintomas) and
        ("respirar" in todos_sintomas or "respiracion" in todos_sintomas or "aliento" in todos_sintomas or "respiara" in todos_sintomas)):
        return "Podría ser COVID-19. Por favor, consulta a un médico."
    
    # Meningitis: dolor de cabeza, rigidez en el cuello, fiebre
    elif (("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("cabeza" in todos_sintomas or "craneo" in todos_sintomas) and
          ("rigidez" in todos_sintomas or "tension" in todos_sintomas or "tirantez" in todos_sintomas) and
          ("cuello" in todos_sintomas or "nuca" in todos_sintomas) and
          ("fiebre" in todos_sintomas or "temperatura" in todos_sintomas or "calentura" in todos_sintomas)):
        return "Podría ser meningitis. Por favor, busca atención médica inmediatamente."
    
    # Gastroenteritis: náuseas, vómitos, dolor abdominal
    elif (("nauseas" in todos_sintomas or "nausea" in todos_sintomas or "mareo" in todos_sintomas) and
          ("vomitos" in todos_sintomas or "vomito" in todos_sintomas or "vomitar" in todos_sintomas) and
          ("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("abdominal" in todos_sintomas or "estomago" in todos_sintomas or "panza" in todos_sintomas or "vientre" in todos_sintomas)):
        return "Podría ser una gastroenteritis. Descansa y mantente hidratado."
    
    # Resfriado común: dolor de garganta, tos, congestión nasal
    elif (("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("garganta" in todos_sintomas or "faringe" in todos_sintomas) and
          ("tos" in todos_sintomas or "toser" in todos_sintomas) and
          ("congestion" in todos_sintomas or "nariz" in todos_sintomas or "mocos" in todos_sintomas or "tapada" in todos_sintomas or "congestión" in todos_sintomas)):
        return "Podría ser un resfriado común. Descansa y bebe muchos líquidos."
    
    # Sarampión: fiebre, sarpullido, ojos rojos
    elif (("fiebre" in todos_sintomas or "temperatura" in todos_sintomas or "calentura" in todos_sintomas) and
          ("sarpullido" in todos_sintomas or "erupcion" in todos_sintomas or "ronchas" in todos_sintomas or "manchas" in todos_sintomas) and
          ("ojos" in todos_sintomas or "ocular" in todos_sintomas) and
          ("rojos" in todos_sintomas or "rojo" in todos_sintomas or "enrojecidos" in todos_sintomas)):
        return "Podría ser sarampión. Por favor, consulta a un médico."
    
    # Ataque al corazón: dolor de pecho, dificultad para respirar, sudoración excesiva
    elif (("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("pecho" in todos_sintomas or "torax" in todos_sintomas or "corazon" in todos_sintomas) and
          ("dificultad" in todos_sintomas or "problema" in todos_sintomas) and
          ("respirar" in todos_sintomas or "respiracion" in todos_sintomas or "aliento" in todos_sintomas) and
          ("sudoracion" in todos_sintomas or "sudor" in todos_sintomas or "transpiracion" in todos_sintomas)):
        return "Podría ser un ataque al corazón. Por favor, busca atención médica de inmediato."
    
    # Hepatitis: dolor abdominal, ictericia, fatiga
    elif (("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("abdominal" in todos_sintomas or "estomago" in todos_sintomas or "panza" in todos_sintomas or "vientre" in todos_sintomas) and
          ("ictericia" in todos_sintomas or "amarillo" in todos_sintomas or "amarillento" in todos_sintomas) and
          ("fatiga" in todos_sintomas or "cansancio" in todos_sintomas or "debilidad" in todos_sintomas)):
        return "Podría ser hepatitis. Por favor, consulta a un médico."
    
    # Reacción alérgica: picazón, erupción, hinchazón
    elif (("picazon" in todos_sintomas or "comezon" in todos_sintomas or "prurito" in todos_sintomas) and
          ("erupcion" in todos_sintomas or "ronchas" in todos_sintomas or "sarpullido" in todos_sintomas or "manchas" in todos_sintomas) and
          ("hinchazon" in todos_sintomas or "inflamacion" in todos_sintomas or "edema" in todos_sintomas)):
        return "Podría ser una reacción alérgica. Por favor, consulta a un médico."
    
    # Infección de oído: dolor de oído, drenaje del oído, pérdida de audición
    elif (("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("oido" in todos_sintomas or "oreja" in todos_sintomas) and
          ("drenaje" in todos_sintomas or "secrecion" in todos_sintomas or "liquido" in todos_sintomas) and
          ("perdida" in todos_sintomas or "disminucion" in todos_sintomas) and
          ("audicion" in todos_sintomas or "oír" in todos_sintomas or "escuchar" in todos_sintomas)):
        return "Podría ser una infección de oído. Por favor, consulta a un médico."
    
    # Gripe: fiebre, escalofríos, dolor muscular
    elif (("fiebre" in todos_sintomas or "temperatura" in todos_sintomas or "calentura" in todos_sintomas) and
          ("escalofrios" in todos_sintomas or "escalofríos" in todos_sintomas or "tiriton" in todos_sintomas or "frio" in todos_sintomas) and
          ("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("muscular" in todos_sintomas or "musculos" in todos_sintomas or "cuerpo" in todos_sintomas)):
        return "Podría ser una gripe. Descansa, mantente hidratado y consulta a un médico si los síntomas persisten."
    
    # Problema cardíaco: dolor en el pecho, mareos, palpitaciones
    elif (("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("pecho" in todos_sintomas or "torax" in todos_sintomas or "corazon" in todos_sintomas) and
          ("mareos" in todos_sintomas or "mareo" in todos_sintomas or "vertigo" in todos_sintomas) and
          ("palpitaciones" in todos_sintomas or "palpitacion" in todos_sintomas or "latidos" in todos_sintomas)):
        return "Podría ser un problema cardíaco. Por favor, busca atención médica inmediatamente."
    
    # Trastorno metabólico: pérdida de apetito, pérdida de peso, fatiga extrema
    elif (("perdida" in todos_sintomas or "disminucion" in todos_sintomas) and
          ("apetito" in todos_sintomas or "hambre" in todos_sintomas) and
          ("peso" in todos_sintomas or "kilos" in todos_sintomas) and
          ("fatiga" in todos_sintomas or "cansancio" in todos_sintomas or "debilidad" in todos_sintomas)):
        return "Podría ser un trastorno metabólico. Por favor, consulta a un médico."
    
    # Problema nervioso o muscular: dolor de espalda, dolor en las piernas, entumecimiento
    elif (("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("espalda" in todos_sintomas or "lumbar" in todos_sintomas or "columna" in todos_sintomas) and
          ("piernas" in todos_sintomas or "extremidades" in todos_sintomas) and
          ("entumecimiento" in todos_sintomas or "adormecimiento" in todos_sintomas or "hormigueo" in todos_sintomas)):
        return "Podría ser un problema nervioso o muscular. Por favor, consulta a un especialista."
    
    # Derrame cerebral: pérdida de memoria, confusión, dificultad para hablar
    elif (("perdida" in todos_sintomas or "disminucion" in todos_sintomas) and
          ("memoria" in todos_sintomas or "recuerdo" in todos_sintomas) and
          ("confusion" in todos_sintomas or "desorientacion" in todos_sintomas) and
          ("dificultad" in todos_sintomas or "problema" in todos_sintomas) and
          ("hablar" in todos_sintomas or "lenguaje" in todos_sintomas or "palabras" in todos_sintomas)):
        return "Podría ser un derrame cerebral. Por favor, busca atención médica de inmediato."
    
    # Hipotiroidismo: fatiga, depresión, aumento de peso
    elif (("fatiga" in todos_sintomas or "cansancio" in todos_sintomas or "debilidad" in todos_sintomas) and
          ("depresion" in todos_sintomas or "tristeza" in todos_sintomas or "melancolia" in todos_sintomas) and
          ("aumento" in todos_sintomas or "ganancia" in todos_sintomas) and
          ("peso" in todos_sintomas or "kilos" in todos_sintomas)):
        return "Podría ser hipotiroidismo. Por favor, consulta a un endocrinólogo."
    
    # Diabetes: sed excesiva, frecuencia urinaria, visión borrosa
    elif (("sed" in todos_sintomas or "sequedad" in todos_sintomas) and
          ("excesiva" in todos_sintomas or "mucho" in todos_sintomas or "demasiada" in todos_sintomas) and
          ("frecuencia" in todos_sintomas or "muchas" in todos_sintomas) and
          ("urinaria" in todos_sintomas or "orina" in todos_sintomas or "pipi" in todos_sintomas) and
          ("vision" in todos_sintomas or "vista" in todos_sintomas) and
          ("borrosa" in todos_sintomas or "difusa" in todos_sintomas or "opaca" in todos_sintomas)):
        return "Podría ser diabetes. Por favor, realiza una evaluación médica."
    
    # Tuberculosis: tos persistente, pérdida de peso, sudores nocturnos
    elif (("tos" in todos_sintomas or "toser" in todos_sintomas) and
          ("persistente" in todos_sintomas or "constante" in todos_sintomas or "continua" in todos_sintomas) and
          ("perdida" in todos_sintomas or "disminucion" in todos_sintomas) and
          ("peso" in todos_sintomas or "kilos" in todos_sintomas) and
          ("sudores" in todos_sintomas or "sudor" in todos_sintomas) and
          ("nocturnos" in todos_sintomas or "noche" in todos_sintomas or "nocturno" in todos_sintomas)):
        return "Podría ser tuberculosis. Por favor, consulta a un médico."
    
    # Artritis: dolor articular, rigidez, hinchazón
    elif (("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("articular" in todos_sintomas or "articulaciones" in todos_sintomas or "articulos" in todos_sintomas or "huesos" in todos_sintomas) and
          ("rigidez" in todos_sintomas or "tension" in todos_sintomas or "tirantez" in todos_sintomas) and
          ("hinchazon" in todos_sintomas or "inflamacion" in todos_sintomas or "edema" in todos_sintomas)):
        return "Podría ser artritis. Por favor, consulta a un médico."
    
    # Anemia: fatiga extrema, falta de aliento, dolor en el pecho
    elif (("fatiga" in todos_sintomas or "cansancio" in todos_sintomas or "debilidad" in todos_sintomas) and
          ("extrema" in todos_sintomas or "mucho" in todos_sintomas or "severo" in todos_sintomas) and
          ("falta" in todos_sintomas or "dificultad" in todos_sintomas or "problema" in todos_sintomas) and
          ("aliento" in todos_sintomas or "respiracion" in todos_sintomas or "respirar" in todos_sintomas) and
          ("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("pecho" in todos_sintomas or "torax" in todos_sintomas or "corazon" in todos_sintomas)):
        return "Podría ser anemia. Por favor, realiza un examen de sangre."
    
    # Infección ocular o glaucoma: visión borrosa, dolor ocular, enrojecimiento
    elif (("vision" in todos_sintomas or "vista" in todos_sintomas) and
          ("borrosa" in todos_sintomas or "difusa" in todos_sintomas or "opaca" in todos_sintomas) and
          ("dolor" in todos_sintomas or "dolores" in todos_sintomas) and
          ("ocular" in todos_sintomas or "ojos" in todos_sintomas) and
          ("enrojecimiento" in todos_sintomas or "rojo" in todos_sintomas or "rojos" in todos_sintomas or "irritacion" in todos_sintomas)):
        return "Podría ser una infección ocular o glaucoma. Por favor, consulta a un oftalmólogo."
    
    # Si no se encuentra ninguna coincidencia
    else:
        return "No puedo determinar la enfermedad. Por favor, consulta a un médico."


# ==================== MENÚ PRINCIPAL ====================

def main():
    """Función principal con menú integrado (Entregas 1 y 2)"""
    # Cargar datos
    pacientes = cargar_pacientes()
    historial = cargar_historial_medico()
    
    while True:
        print("\n" + "=" * 60)
        print("    SISTEMA DE GESTIÓN HOSPITALARIA")
        print("    Y DIAGNÓSTICO MÉDICO")
        print("=" * 60)
        print("\n📋 MENÚ PRINCIPAL")
        print("-" * 60)
        print("1. Realizar diagnóstico médico (Entrega 1)")
        print("2. Agregar nuevo paciente")
        print("3. Editar información de paciente")
        print("4. Consultar paciente y gestionar historial")
        print("0. Salir del sistema")
        print("-" * 60)
        
        opcion = input("\nSelecciona una opción: ").strip()
        
        if opcion == "1":
            diagnostico_sintomas()
        elif opcion == "2":
            agregar_paciente(pacientes)
        elif opcion == "3":
            if not pacientes:
                print("\n❌ No hay pacientes registrados en el sistema.")
                print("   Por favor, agrega un paciente primero.")
            else:
                editar_paciente(pacientes)
        elif opcion == "4":
            if not pacientes:
                print("\n❌ No hay pacientes registrados en el sistema.")
                print("   Por favor, agrega un paciente primero.")
            else:
                consultar_paciente(pacientes, historial)
        elif opcion == "0":
            print("\n" + "=" * 60)
            print("    Gracias por usar el sistema")
            print("    ¡Hasta pronto!")
            print("=" * 60)
            break
        else:
            print("\n❌ Opción inválida. Por favor, selecciona una opción del menú.")


if __name__ == "__main__":
    main()
