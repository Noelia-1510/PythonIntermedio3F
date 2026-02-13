import tkinter as tk
from tkinter import ttk, messagebox
import modelo.consultas_dao as consulta

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=800, height=450)
        self.root = root
        self.pack()
        self.id_peli = None
        
        self.color_bg      = "#121212"
        self.color_card    = "#1E1E1E"
        self.color_text    = "#FFFFFF"
        self.color_accent  = "#BB86FC"
        self.color_entry   = "#2C2C2C"
        
        self.config(bg=self.color_bg)

        self.nombre = tk.StringVar()
        self.duracion = tk.StringVar()
        self.director = tk.StringVar()
        self.anio_lanzamiento = tk.StringVar()

        self.generos_map = {}
        self.generos_nombres = []
        
        self.configurar_estilos()
        self.cargar_generos_combobox()
        self.label_form()
        self.input_form()
        self.botones_principales()
        self.crear_tabla_estructura()
        self.actualizar_tabla()

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox", 
                        fieldbackground=self.color_entry, background=self.color_entry, 
                        foreground="white", darkcolor=self.color_entry,
                        lightcolor=self.color_entry, arrowcolor=self.color_accent)
        
        style.configure("Treeview", background=self.color_card, foreground="white", 
                        fieldbackground=self.color_card, rowheight=28)
        style.configure("Treeview.Heading", background="#333333", foreground=self.color_accent, 
                        font=('Segoe UI', 10, 'bold'))
        style.map("Treeview", background=[('selected', '#3700B3')])

    def label_form(self):
        labels_info = [
            ("Nombre Película:", 0), ("Duración:", 1), ("Género:", 2),
            ("Director:", 3), ("Año:", 4)
        ]
        for text, row_num in labels_info:
            label = tk.Label(self, text=text)
            label.config(font=('Segoe UI', 10, 'bold'), bg=self.color_bg, fg=self.color_text)
            label.grid(row=row_num, column=0, padx=20, pady=8, sticky='e')

    def cargar_generos_combobox(self):
        try:
            generos_db = consulta.listar_generos()
            self.generos_map = {nombre: id for id, nombre in generos_db}
            self.generos_nombres = ['Seleccione Uno'] + [nombre for id, nombre in generos_db]
        except:
            self.generos_nombres = ['Seleccione Uno']

    def input_form(self):
        estilo_entry = {
            'width': 40, 
            'state': 'disabled', 
            'bg': self.color_entry, 
            'fg': 'white', 
            'insertbackground': 'white',
            'font': ('Segoe UI', 10),
            'borderwidth': 0,
            'highlightthickness': 1,
            'highlightbackground': "#444444"
        }
        
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre, **estilo_entry)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=8, sticky='w', columnspan=2)

        self.entry_duracion = tk.Entry(self, textvariable=self.duracion, **estilo_entry)
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=8, sticky='w', columnspan=2)

        self.entry_genero = ttk.Combobox(self, state="readonly", values=self.generos_nombres, width=44, style="TCombobox")
        self.entry_genero.current(0)
        self.entry_genero.config(state='disabled')
        self.entry_genero.grid(row=2, column=1, padx=10, pady=8, sticky='w', columnspan=2)

        self.entry_director = tk.Entry(self, textvariable=self.director, **estilo_entry)
        self.entry_director.grid(row=3, column=1, padx=10, pady=8, sticky='w', columnspan=2)

        self.entry_anio_lanzamiento = tk.Entry(self, textvariable=self.anio_lanzamiento, **estilo_entry)
        self.entry_anio_lanzamiento.grid(row=4, column=1, padx=10, pady=8, sticky='w', columnspan=2)

    def botones_principales(self):
        btn_estilo = {'font': ('Segoe UI', 9, 'bold'), 'cursor': 'hand2', 'width': 18, 'borderwidth': 0}
        
        self.btn_alta = tk.Button(self, text='NUEVO', command=self.habilitar_campos, 
                                  bg="#03DAC6", fg="black", activebackground="#018786", **btn_estilo)
        self.btn_alta.grid(row=5, column=0, padx=20, pady=20, sticky='w')

        self.btn_modi = tk.Button(self, text='GUARDAR', command=self.guardar_campos, 
                                  bg=self.color_accent, fg="black", activebackground="#9965f4", state='disabled', **btn_estilo)
        self.btn_modi.grid(row=5, column=1, padx=10, pady=20, sticky='n')

        self.btn_cance = tk.Button(self, text='CANCELAR', command=self.bloquear_campos, 
                                   bg="#CF6679", fg="black", activebackground="#b00020", state='disabled', **btn_estilo)
        self.btn_cance.grid(row=5, column=2, padx=10, pady=20, sticky='e')

    def crear_tabla_estructura(self):
        self.tabla = ttk.Treeview(self, columns=('N', 'D', 'G', 'Dir', 'A'), height=8)
        self.tabla.grid(row=6, column=0, columnspan=3, sticky='nsew', padx=20, pady=10)

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=3, sticky='nse', pady=10)
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID'); self.tabla.heading('#1', text='Película')
        self.tabla.heading('#2', text='Duración'); self.tabla.heading('#3', text='Género')
        self.tabla.heading('#4', text='Director'); self.tabla.heading('#5', text='Año')

        self.tabla.column('#0', width=50, anchor='center')
        self.tabla.column('#1', width=250)
        self.tabla.column('#2', width=80, anchor='center')
        self.tabla.column('#3', width=120)
        self.tabla.column('#4', width=150)
        self.tabla.column('#5', width=70, anchor='center')

        self.btn_editar = tk.Button(self, text='EDITAR SELECCIÓN', command=self.editar_registro,
                                    bg="#333333", fg="white", width=25, font=('Segoe UI', 9), borderwidth=0, activebackground="#444444", activeforeground="white")
        self.btn_editar.grid(row=7, column=0, padx=20, pady=10, sticky='w')

        self.btn_delete = tk.Button(self, text='ELIMINAR SELECCIÓN', command=self.eliminar_regristro,
                                    bg="#333333", fg="white", width=25, font=('Segoe UI', 9), borderwidth=0, activebackground="#A90A0A", activeforeground="white")
        self.btn_delete.grid(row=7, column=2, padx=10, pady=10, sticky='e')


    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        try:
            self.lista_p = consulta.listar_peli()
            for p in reversed(self.lista_p):
                self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3], p[4], p[5]))
        except: pass

    def editar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']
            values = self.tabla.item(self.tabla.selection())['values']
            self.habilitar_campos()
            self.nombre.set(values[0]); self.duracion.set(values[1])
            self.entry_genero.set(values[2]); self.director.set(values[3])
            self.anio_lanzamiento.set(values[4])
        except: messagebox.showwarning("QA Check", "Selecciona una fila primero")

    def eliminar_regristro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']
            if messagebox.askyesno("Confirmar", "¿Eliminar definitivamente?"):
                consulta.borrar_peli(int(self.id_peli))
                self.actualizar_tabla()
            self.id_peli = None
        except: messagebox.showwarning("QA Check", "Selecciona una fila primero")

    def guardar_campos(self):
        try:
            genero_id = self.generos_map.get(self.entry_genero.get())
            if not genero_id: 
                messagebox.showwarning("QA Check", "Selecciona un género válido")
                return
            pelicula = consulta.Peliculas(
                self.nombre.get(), self.duracion.get(), genero_id,
                consulta.obtener_o_crear_director(self.director.get()),
                int(self.anio_lanzamiento.get())
            )
            if self.id_peli is None: consulta.guardar_peli(pelicula)
            else: consulta.editar_peli(pelicula, int(self.id_peli))
            self.actualizar_tabla(); self.bloquear_campos()
        except ValueError: messagebox.showerror("Error", "El año debe ser un número")

    def habilitar_campos(self):
        estado = 'normal'
        self.entry_nombre.config(state=estado); self.entry_duracion.config(state=estado)
        self.entry_genero.config(state=estado); self.entry_director.config(state=estado)
        self.entry_anio_lanzamiento.config(state=estado)
        self.btn_modi.config(state=estado); self.btn_cance.config(state=estado)
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.id_peli = None
        self.nombre.set(''); self.duracion.set(''); self.director.set(''); self.anio_lanzamiento.set('')
        self.entry_genero.current(0)
        estado = 'disabled'
        self.entry_nombre.config(state=estado); self.entry_duracion.config(state=estado)
        self.entry_genero.config(state=estado); self.entry_director.config(state=estado)
        self.entry_anio_lanzamiento.config(state=estado)
        self.btn_modi.config(state=estado); self.btn_cance.config(state=estado)
        self.btn_alta.config(state='normal')