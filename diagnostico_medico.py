"""
Sistema Experto de Diagnóstico Médico
Proyecto de Fundamentos de Programación
Autor: Estudiante
"""

def main():
    print("=" * 60)
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
          ("congestion" in todos_sintomas or "nariz" in todos_sintomas or "mocos" in todos_sintomas or "tapada" in todos_sintomas)):
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


if __name__ == "__main__":
    main()
