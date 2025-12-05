"""
Sistema de Gestión Hospitalaria y Diagnóstico Médico
Tercera Entrega - Interfaz Gráfica Simplificada
Autor: Estudiante
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
from datetime import datetime
import re

# ==================== LÓGICA DE NEGOCIO (Sin Cambios) ====================

class SistemaGestor:
    def __init__(self):
        self.archivo_pacientes = "pacientes.txt"
        self.archivo_historial = "historial_medico.txt"
        self.pacientes = self.cargar_pacientes()
        self.historial = self.cargar_historial_medico()

    def cargar_pacientes(self):
        pacientes = {}
        if os.path.exists(self.archivo_pacientes):
            try:
                with open(self.archivo_pacientes, "r", encoding="utf-8") as archivo:
                    for linea in archivo:
                        datos = linea.strip().split("|")
                        if len(datos) >= 8:
                            doc = datos[0]
                            pacientes[doc] = {
                                "documento": doc,
                                "nombres": datos[1],
                                "apellidos": datos[2],
                                "fecha_nacimiento": datos[3],
                                "genero": datos[4],
                                "celular": datos[5],
                                "correo": datos[6],
                                "fecha_registro": datos[7]
                            }
            except Exception as e:
                print(f"Error cargando pacientes: {e}")
        return pacientes

    def guardar_pacientes(self):
        try:
            with open(self.archivo_pacientes, "w", encoding="utf-8") as archivo:
                for doc, p in self.pacientes.items():
                    linea = f"{p['documento']}|{p['nombres']}|{p['apellidos']}|{p['fecha_nacimiento']}|{p['genero']}|{p['celular']}|{p['correo']}|{p['fecha_registro']}\n"
                    archivo.write(linea)
            return True
        except Exception as e:
            print(f"Error guardando pacientes: {e}")
            return False

    def cargar_historial_medico(self):
        historial = {}
        if os.path.exists(self.archivo_historial):
            try:
                with open(self.archivo_historial, "r", encoding="utf-8") as archivo:
                    for linea in archivo:
                        datos = linea.strip().split("|")
                        if len(datos) >= 3:
                            num_id = datos[0]
                            tipo = datos[1]
                            if num_id not in historial:
                                historial[num_id] = {"enfermedades": [], "tratamientos": [], "alergias": []}
                            
                            if tipo == "enfermedad" and len(datos) >= 5:
                                historial[num_id]["enfermedades"].append({
                                    "sintomas": datos[2],
                                    "nombre_enfermedad": datos[3],
                                    "fecha_registro": datos[4]
                                })
                            elif tipo == "tratamiento" and len(datos) >= 5:
                                historial[num_id]["tratamientos"].append({
                                    "medicamentos": datos[2],
                                    "dosis": datos[3],
                                    "fecha_registro": datos[4]
                                })
                            elif tipo == "alergia" and len(datos) >= 5:
                                historial[num_id]["alergias"].append({
                                    "alergeno": datos[2],
                                    "sintomas": datos[3],
                                    "fecha_registro": datos[4]
                                })
            except Exception as e:
                print(f"Error cargando historial: {e}")
        return historial

    def guardar_historial(self):
        try:
            with open(self.archivo_historial, "w", encoding="utf-8") as archivo:
                for num_id, datos in self.historial.items():
                    for enf in datos.get("enfermedades", []):
                        archivo.write(f"{num_id}|enfermedad|{enf['sintomas']}|{enf['nombre_enfermedad']}|{enf['fecha_registro']}\n")
                    for trat in datos.get("tratamientos", []):
                        archivo.write(f"{num_id}|tratamiento|{trat['medicamentos']}|{trat['dosis']}|{trat['fecha_registro']}\n")
                    for alerg in datos.get("alergias", []):
                        archivo.write(f"{num_id}|alergia|{alerg['alergeno']}|{alerg['sintomas']}|{alerg['fecha_registro']}\n")
            return True
        except Exception as e:
            return False

    def validar_correo(self, correo):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, correo) is not None

    def validar_celular(self, celular):
        return celular.isdigit() and len(celular) == 10

    def validar_solo_letras(self, texto):
        return all(c.isalpha() or c.isspace() for c in texto)

    def calcular_edad(self, fecha_nacimiento_str):
        try:
            fecha_nac = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
            hoy = datetime.now()
            edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
            return edad
        except ValueError:
            return None

    def realizar_diagnostico(self, sintomas_lista):
        todos_sintomas = " ".join(sintomas_lista).lower()
        if (("fiebre" in todos_sintomas or "temperatura" in todos_sintomas) and
            ("tos" in todos_sintomas) and ("dificultad" in todos_sintomas or "respirar" in todos_sintomas)):
            return "Podría ser COVID-19. Consulta a un médico."
        elif "fiebre" in todos_sintomas and "dolor" in todos_sintomas:
            return "Síntomas generales de infección viral o bacteriana."
        else:
            return "No se pudo determinar un diagnóstico específico. Consulte a un médico."


# ==================== INTERFAZ GRÁFICA (Estructura Simplificada) ====================

class AplicacionHospital(tk.Tk):
    def __init__(self):
        super().__init__()
        self.gestor = SistemaGestor()
        self.title("Sistema de Gestión Hospitalaria")
        self.geometry("800x600")
        
        # Contenedor Principal
        self.contenedor = tk.Frame(self, bg="#f0f0f0")
        self.contenedor.pack(fill="both", expand=True)
        
        # Estilos
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        
        self.mostrar_menu_principal()

    def limpiar_contenedor(self):
        for widget in self.contenedor.winfo_children():
            widget.destroy()

    # --- VISTAS ---

    def mostrar_menu_principal(self):
        self.limpiar_contenedor()
        frame = tk.Frame(self.contenedor, bg="#f0f0f0")
        frame.pack(expand=True, fill="both")
        
        tk.Label(frame, text="Bienvenido al sistema de almacenamiento de\npacientes!", 
                 font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=40)
        
        # Logo simulado
        canvas = tk.Canvas(frame, width=150, height=150, bg="#f0f0f0", highlightthickness=0)
        canvas.create_oval(10, 10, 140, 140, outline="black", width=2)
        canvas.create_text(75, 75, text="LOGO", font=("Arial", 14, "bold"))
        canvas.pack(pady=10)
        
        btn_config = {"font": ("Arial", 12), "width": 25, "bg": "#2c3e50", "fg": "white"}
        tk.Button(frame, text="Agregar Paciente", command=self.vista_agregar_paciente, **btn_config).pack(pady=10)
        tk.Button(frame, text="Consultar Paciente", command=self.vista_consultar_paciente, **btn_config).pack(pady=10)
        tk.Button(frame, text="Listar Pacientes", command=self.vista_listar_pacientes, **btn_config).pack(pady=10)

    def vista_agregar_paciente(self):
        self.limpiar_contenedor()
        frame = tk.Frame(self.contenedor, bg="#f0f0f0")
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Agregar Paciente", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)
        
        # Formulario centrado
        form_frame = tk.Frame(frame, bg="#f0f0f0")
        form_frame.pack()
        
        entries = {}
        campos = [
            ("Nombres", "nombres"), ("Apellidos", "apellidos"),
            ("Documento", "documento"), ("Fecha Nacimiento (DD/MM/AAAA)", "fecha_nacimiento"),
            ("Celular (10 dígitos)", "celular"), ("Correo", "correo")
        ]
        
        for i, (label, key) in enumerate(campos):
            tk.Label(form_frame, text=label+":", width=30, anchor="e", bg="#f0f0f0").grid(row=i, column=0, pady=5)
            ent = tk.Entry(form_frame, width=30)
            ent.grid(row=i, column=1, pady=5)
            entries[key] = ent
            
        tk.Label(form_frame, text="Género:", width=30, anchor="e", bg="#f0f0f0").grid(row=6, column=0, pady=5)
        combo_genero = ttk.Combobox(form_frame, values=["Masculino", "Femenino", "No binario", "Otro"], state="readonly", width=27)
        combo_genero.grid(row=6, column=1, pady=5)
        combo_genero.current(0)
        
        def guardar():
            datos = {k: v.get().strip() for k, v in entries.items()}
            datos["genero"] = combo_genero.get()
            
            # Validaciones
            if not datos["documento"].isdigit():
                messagebox.showerror("Error", "El documento debe ser numérico.")
                return
            if datos["documento"] in self.gestor.pacientes:
                messagebox.showerror("Error", "Ya existe este documento.")
                return
            if not self.gestor.validar_solo_letras(datos["nombres"]) or not self.gestor.validar_solo_letras(datos["apellidos"]):
                messagebox.showerror("Error", "Nombres/Apellidos solo letras.")
                return
            edad = self.gestor.calcular_edad(datos["fecha_nacimiento"])
            if edad is None:
                messagebox.showerror("Error", "Fecha inválida (DD/MM/AAAA).")
                return
            if not self.gestor.validar_celular(datos["celular"]):
                messagebox.showerror("Error", "Celular debe ser 10 dígitos.")
                return
            if not self.gestor.validar_correo(datos["correo"]):
                messagebox.showerror("Error", "Correo inválido.")
                return
                
            datos["fecha_registro"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.gestor.pacientes[datos["documento"]] = datos
            if self.gestor.guardar_pacientes():
                messagebox.showinfo("Éxito", "Paciente guardado.")
                self.mostrar_menu_principal()
            else:
                messagebox.showerror("Error", "Error guardando archivo.")

        btn_frame = tk.Frame(frame, bg="#f0f0f0")
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Guardar", bg="#27ae60", fg="white", command=guardar).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Volver", command=self.mostrar_menu_principal).pack(side="left", padx=10)

    def vista_listar_pacientes(self):
        self.limpiar_contenedor()
        frame = tk.Frame(self.contenedor, bg="#f0f0f0")
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Lista de Pacientes", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
        
        cols = ("Documento", "Nombres", "Apellidos")
        tree = ttk.Treeview(frame, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        tree.pack(expand=True, fill="both")
        
        lista = list(self.gestor.pacientes.values())
        lista.sort(key=lambda x: (x.get("fecha_registro", ""), x["documento"]), reverse=True)
        
        for p in lista:
            tree.insert("", "end", values=(p["documento"], p["nombres"], p["apellidos"]))
            
        tk.Button(frame, text="Volver", command=self.mostrar_menu_principal).pack(pady=10)

    def vista_consultar_paciente(self):
        self.limpiar_contenedor()
        frame = tk.Frame(self.contenedor, bg="#f0f0f0")
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text="Consultar Paciente", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)
        
        tk.Label(frame, text="Documento:", bg="#f0f0f0").pack()
        entry_doc = tk.Entry(frame)
        entry_doc.pack(pady=5)
        
        def buscar():
            doc = entry_doc.get().strip()
            if doc in self.gestor.pacientes:
                self.vista_detalle_paciente(doc)
            else:
                messagebox.showerror("Error", "No encontrado.")
                
        tk.Button(frame, text="Consultar", bg="#2980b9", fg="white", command=buscar).pack(pady=10)
        tk.Button(frame, text="Volver", command=self.mostrar_menu_principal).pack()

    def vista_detalle_paciente(self, doc):
        self.limpiar_contenedor()
        p = self.gestor.pacientes[doc]
        
        frame = tk.Frame(self.contenedor, bg="#f0f0f0")
        frame.pack(expand=True, fill="both", padx=20, pady=10)
        
        # Info
        info = f"""
        Documento: {p['documento']}
        Nombre: {p['nombres']} {p['apellidos']}
        Edad: {self.gestor.calcular_edad(p['fecha_nacimiento'])} años
        Género: {p['genero']} | Celular: {p['celular']}
        Correo: {p['correo']}
        """
        lbl_info = tk.Label(frame, text=info, justify="left", bg="white", relief="solid", borderwidth=1)
        lbl_info.pack(fill="x", pady=10, ipady=10)
        
        # Botones Historial
        btn_frame = tk.Frame(frame, bg="#f0f0f0")
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Agregar Enfermedad", command=lambda: self.modal_agregar(doc, "enfermedad")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Agregar Tratamiento", command=lambda: self.modal_agregar(doc, "tratamiento")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Agregar Alergia", command=lambda: self.modal_agregar(doc, "alergia")).pack(side="left", padx=5)
        
        # Listas
        list_frame = tk.Frame(frame, bg="#f0f0f0")
        list_frame.pack(expand=True, fill="both")
        
        for i, (titulo, clave) in enumerate([("Enfermedades", "enfermedades"), 
                                             ("Tratamientos", "tratamientos"), 
                                             ("Alergias", "alergias")]):
            subf = tk.Frame(list_frame, bg="#f0f0f0")
            subf.grid(row=0, column=i, sticky="nsew", padx=5)
            list_frame.grid_columnconfigure(i, weight=1)
            tk.Label(subf, text=titulo, font=("Arial", 10, "bold"), bg="#f0f0f0").pack()
            lb = tk.Listbox(subf, height=8)
            lb.pack(fill="both", expand=True)
            
            if doc in self.gestor.historial:
                for item in self.gestor.historial[doc].get(clave, []):
                    texto = item.get('nombre_enfermedad') or item.get('medicamentos') or item.get('alergeno')
                    lb.insert("end", f"{item['fecha_registro']}: {texto}")

        tk.Button(frame, text="Volver al Menú", command=self.mostrar_menu_principal).pack(pady=10)

    def modal_agregar(self, doc, tipo):
        top = tk.Toplevel(self)
        top.title(f"Agregar {tipo}")
        top.geometry("400x300")
        
        entries = []
        if tipo == "enfermedad":
            tk.Label(top, text="Ingrese 3 síntomas:").pack(pady=5)
            for i in range(3):
                e = tk.Entry(top); e.pack(); entries.append(e)
        elif tipo == "tratamiento":
            tk.Label(top, text="Medicamentos:").pack(); e1=tk.Entry(top); e1.pack(); entries.append(e1)
            tk.Label(top, text="Dosis:").pack(); e2=tk.Entry(top); e2.pack(); entries.append(e2)
        elif tipo == "alergia":
            tk.Label(top, text="Alergeno:").pack(); e1=tk.Entry(top); e1.pack(); entries.append(e1)
            tk.Label(top, text="Síntomas:").pack(); e2=tk.Entry(top); e2.pack(); entries.append(e2)
            
        def guardar():
            vals = [e.get().strip() for e in entries]
            if any(not v for v in vals): return
            
            registro = {"fecha_registro": datetime.now().strftime("%Y-%m-%d")}
            if doc not in self.gestor.historial:
                self.gestor.historial[doc] = {"enfermedades": [], "tratamientos": [], "alergias": []}
                
            if tipo == "enfermedad":
                diag = self.gestor.realizar_diagnostico(vals)
                messagebox.showinfo("Diagnóstico", diag)
                registro.update({"sintomas": ", ".join(vals), "nombre_enfermedad": diag})
                self.gestor.historial[doc]["enfermedades"].append(registro)
            elif tipo == "tratamiento":
                registro.update({"medicamentos": vals[0], "dosis": vals[1]})
                self.gestor.historial[doc]["tratamientos"].append(registro)
            elif tipo == "alergia":
                registro.update({"alergeno": vals[0], "sintomas": vals[1]})
                self.gestor.historial[doc]["alergias"].append(registro)
                
            self.gestor.guardar_historial()
            top.destroy()
            self.vista_detalle_paciente(doc)
            
        tk.Button(top, text="Guardar", command=guardar).pack(pady=20)

if __name__ == "__main__":
    app = AplicacionHospital()
    app.mainloop()
