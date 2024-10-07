import inspect
import re
import customtkinter as CTk
import tkinter 
from tkinter import ttk
from CTkMessagebox import CTkMessagebox as CTkM
import tkinter.messagebox

class Aplicacion(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Restaurant choro")
        self.geometry("1500x600")
        
        self.tabview = CTk.CTkTabview(self, 10,10)
        self.tabview.pack()

        self.crearpestañas()

    def crearpestañas(self):
        self.tabing = self.tabview.add("Ingreso de Ingredientes")
        self.tabped = self.tabview.add("Pedido")

        self.configpestañaing()
        self.configpestañaped()

    def configpestañaing(self):
        self.ing_frame = CTk.CTkFrame(self.tabing)
        self.ing_frame.grid(row=0, column=0)

        lbl_nombre = CTk.CTkLabel(self.ing_frame, text= "Ingrese el nombre del ingrediente.")
        lbl_nombre.pack(pady=10)
        self.entry_nombre = CTk.CTkEntry(self.ing_frame)
        self.entry_nombre.pack(pady=10)

        lbl_cantidad = CTk.CTkLabel(self.ing_frame, text= "Ingrese la cantidad.")
        lbl_cantidad.pack(pady=10)
        self.entry_cantidad = CTk.CTkEntry(self.ing_frame)
        self.entry_cantidad.pack(pady=10)

        self.bttn_ingresar = CTk.CTkButton(self.ing_frame, text="Ingresar Ingrediente", hover_color="purple")
        self.bttn_ingresar.pack(pady=10)

        self.tabla_frame = CTk.CTkFrame(self.tabing)
        self.tabla_frame.grid(row=0, column=1, padx=20)

        self.bttn_eliminar = CTk.CTkButton(self.tabla_frame, text="Eliminar Ingrediente.", hover_color="red")
        self.bttn_eliminar.grid(row=0, column=1, pady=10)

        self.bttn_menu = CTk.CTkButton(self.tabla_frame, text="Generar Menu.", hover_color="green")
        self.bttn_menu.grid(row=2, column=1, pady=10)

        # atributos = inspect.getfullargspec(Ingredientes.__init__).args 
        # atributos.remove('self')  # Remover 'self'

        # self.tablalista = ttk.Treeview(self.tabla_frame, columns=atributos, show="headings")

        # for atributo in atributos:
        #     self.tablalista.heading(atributo, text=atributo.capitalize())

        # self.tablalista.grid(row=1, column=1)
    
    def configpestañaped(self):
        self.img_frame = CTk.CTkFrame(self.tabped)
        self.img_frame.grid(row=0, column=0)

        self.total_frame = CTk.CTkFrame(self.tabped)
        self.total_frame.grid(row=1, column=0, sticky="e")

    
        self.lbl_total = CTk.CTkLabel(self.total_frame, text=f"El Total del pedido es: $0")
        self.lbl_total.grid(row=0, column=0, padx=20, sticky="e")

        bttn_delete = CTk.CTkButton(self.total_frame, text="Eliminar Menu.")
        bttn_delete.grid(row=0, column=1, padx=20, sticky="e")

        self.menus_frame = CTk.CTkFrame(self.tabped)
        self.menus_frame.grid(row=2, column=0) 

        self.tablamenus = ttk.Treeview(self.menus_frame, columns=("nombre", "cantidad", "total"), show="headings")
        self.tablamenus.heading("nombre", text="Nombre del Menu")
        self.tablamenus.heading("cantidad", text="Cantidad")
        self.tablamenus.heading("total", text="Precio Total")

        self.tablamenus.grid(row=0, column=0) 

        self.bttn_pdf = CTk.CTkButton(self.menus_frame, text="Generar boleta.")
        self.bttn_pdf.grid(row=1, pady=25)

    def validar_nombre(self, nombre, cantidad):
            if not re.match(r"^[a-zA-Z\s]+$", nombre):
                CTkM(title="Error", message="El nombre solo puede contener letras", icon="cancel")
                return False 

            if not cantidad.isdigit() or int(cantidad) <= 0:
                CTkM(title="Error", message="La cantidad debe ser un número positivo", icon="cancel")
                return False
            
            return True
    
CTk.set_appearance_mode("Dark")
app = Aplicacion()
app.mainloop()