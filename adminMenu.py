from tkinter import *
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font 
from tkinter import messagebox
from os import path
# from PIL import  Image,ImageTk
from materia_prima import Materiaprima
from produccion import Productoenproceso
from producto_final import Costalescompost
from personal import Personal
from ventas import Boleta_ventas
from reportes_sistema import Generador_de_Reportes
from inventario import Inventario
from compras import Compras
from proveedores import Proveedor
from dash import Dashboard

class App_Menu():
    def __init__(self,root):
        self.root = root
        self.root.title("Menu Central")
        icono = path.abspath("F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico")
        self.root.iconbitmap(icono)
        self.root.geometry("1300x770+0+0")
        #Imagen
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        self.root.config(bg="white")
        logo_empresa = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo.png"
        self.logo_icon=PhotoImage(file =path.abspath(logo_empresa))
        title=Label(self.root,text="PLANTA DE VALORIZACIÓN DE RESIDUOS ORGANICOS",padx=10,image=self.logo_icon,compound=LEFT,font=("impact",40),anchor="w").place(x=0,y=0,relwidth=1)
        
        #====SECCION 1====
        lbl_select_folder = Label(self.root,text="Sistema de Gestión de Recursos",font=("times new roman",25),bg="white").place(x=50,y=120)
        # txt_folder_name=Entry(self.root,font=("times new roman",25),bg="lightgreen").place(x=200,y=100)
        hr = Label(self.root,bg="lightgray").place(x=50,y=175,height=2,width=1190)
        
        #Iconos de ventanas
        icono_residuos = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/materia_prima.png"
        self.residuos_icon=PhotoImage(file=path.abspath(icono_residuos))
        icono_produccion = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/produccion.png"
        self.produccion_icon = PhotoImage(file=path.abspath(icono_produccion))
        icono_compost = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/compost.png"
        self.compost_icon = PhotoImage(file=path.abspath(icono_compost))
        incono_personal ="F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/personal.png"
        self.personal_icon = PhotoImage(file=path.abspath(incono_personal))
        incono_insumos ="F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/insumo.png"
        self.insumos_icon = PhotoImage(file=path.abspath(incono_insumos))
        incono_compras ="F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/compras.png"
        self.compras_icon = PhotoImage(file=path.abspath(incono_compras))
        incono_proveedor ="F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/proveedor.png"
        self.proveedor_icon = PhotoImage(file=path.abspath(incono_proveedor))
        icono_ventas = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/ventas.png"
        self.ventas_icon = PhotoImage(file=path.abspath(icono_ventas))
        icono_reporte = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/reportes.png"
        self.reporte_icon = PhotoImage(file=path.abspath(icono_reporte))
        icono_dash = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/dashboard.png"
        self.dashboard_icon = PhotoImage(file=path.abspath(icono_dash))
        icono_salida = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/salida.png"
        self.salida_icon = PhotoImage(file=path.abspath(icono_salida))
        
        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=200,width=1190,height=500)
        
        btresiduos = Button(Frame1,text='MATERIA \nPRIMA',bg='lightgray',fg='green',font=('arial',20,'bold'),activebackground='#36d073',
                      width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=self.residuos,
                      image=self.residuos_icon,compound= RIGHT).grid(row=0,column=1,padx=10,pady=15)
        btproduccion = Button(Frame1,text='PRODUCTO \n EN PROCESO',bg='lightgray',fg='green',font=('arial',15,'bold'),activebackground='#36d073',
                      width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=self.produccion,
                      image=self.produccion_icon,compound=RIGHT).grid(row=0,column=2,padx=10,pady=5)
        btpcompost = Button(Frame1,text='COMPOST',bg='lightgray',fg='green',font=('arial',20,'bold'),activebackground='#36d073',
                      width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=self.compost,
                      image=self.compost_icon,compound=RIGHT).grid(row=0,column=3,padx=10,pady=5)
        btpventas = Button(Frame1,text='VENTAS \nCOMPOST',bg='lightgray',fg='green',font=('arial',20,'bold'),activebackground='#36d073',
                      width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=self.ventas,
                      image=self.ventas_icon,compound=RIGHT).grid(row=0,column=4,padx=10,pady=5)

        btppersonal = Button(Frame1,text='PERSONAL',bg='lightgray',fg='green',font=('arial',20,'bold'),activebackground='#36d073',
                      width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=self.personal,
                      image=self.personal_icon,compound=RIGHT).grid(row=1,column=1,padx=10,pady=5)
        
        btp_inventario =Button(Frame1,text='ALMACEN',bg='lightgray',fg='green',font=('arial',20,'bold'),activebackground='#36d073',
                      width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=self.inventario,
                      image=self.insumos_icon,compound=RIGHT).grid(row=1,column=2,padx=10,pady=5)
        btp_compras=Button(Frame1,text='COMPRAS',bg='lightgray',fg='green',font=('arial',20,'bold'),activebackground='#36d073',
                      width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=self.compras,
                      image=self.compras_icon,compound=RIGHT).grid(row=1,column=3,padx=10,pady=5)
        btp_proveedor =Button(Frame1,text='PROVEEDOR',bg='lightgray',fg='green',font=('arial',15,'bold'),activebackground='#36d073',
                      width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=self.proveedores,
                      image=self.proveedor_icon,compound=RIGHT).grid(row=1,column=4,padx=10,pady=5)
        
        btp_reporte =Button(Frame1,text='GENERAR \nREPORTES',bg='lightgray',fg='green',font=('arial',20,'bold'),activebackground='#36d073',
                      width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=self.reporte,
                      image=self.reporte_icon,compound=RIGHT).grid(row=2,column=1,padx=10,pady=5)
        btp_dash =Button(Frame1,text='GRAFICAS',bg='lightgray',fg='green',font=('arial',17,'bold'),activebackground='#36d073',
                      width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=self.dashboard,
                      image=self.dashboard_icon,compound=RIGHT).grid(row=2,column=2,padx=10,pady=5)
        btp_salir =Button(Frame1,text='CERRAR \n PROGRAMA',bg='lightgray',fg='green',font=('arial',15,'bold'),activebackground='#36d073',
                      width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,command=self.salir,
                      image=self.salida_icon,compound=RIGHT).grid(row=2,column=3,padx=10,pady=5)
        
        
    def residuos(self):
        self.new_window = Toplevel(self.root)
        self.app = Materiaprima(self.new_window)
        
    def produccion(self):
        self.new_window = Toplevel(self.root)
        self.app = Productoenproceso(self.new_window)
    
    def compost(self):
        self.new_window = Toplevel(self.root)
        self.app = Costalescompost(self.new_window)
        
    def personal(self):
        self.new_window = Toplevel(self.root)
        self.app = Personal(self.new_window)
        
    def ventas(self):
        self.new_window = Toplevel(self.root)
        self.app = Boleta_ventas(self.new_window)
    
    def inventario(self):
        self.new_window = Toplevel(self.root)
        self.app = Inventario(self.new_window)
    
    def compras(self):
        self.new_window = Toplevel(self.root)
        self.app = Compras(self.new_window)
    def proveedores(self):
        self.new_window = Toplevel(self.root)
        self.app = Proveedor(self.new_window)
        
    def reporte(self):
        self.new_window = Toplevel(self.root)
        self.app = Generador_de_Reportes(self.new_window)
        
    def dashboard(self):
        self.new_window = Toplevel(self.root)
        self.app = Dashboard(self.new_window)
        
    def salir(self):
        self.root.quit() 
       

if __name__ == "__main__":
    root= Tk()
    obj = App_Menu(root)
    root.mainloop()

    
     