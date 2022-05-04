from numpy import string_
import pandas as pd 
import pymysql
pymysql.install_as_MySQLdb()
from tkinter import *
# from tkinter import font 
# from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
import os as sys
from os import path
from PIL import  Image,ImageTk
import sqlalchemy
from sqlalchemy import create_engine
from tkcalendar import DateEntry 
from datetime import date
import os
from os import path
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from datetime import datetime
from datetime import time
from openpyxl import load_workbook



class Generador_de_Reportes():
    def __init__(self,root):
        self.root = root
        self.root.title("REPORTES DEL SISTEMA")
        icono = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico"
        self.root.iconbitmap(path.abspath(icono))
        self.root.geometry("1300x770+0+0")
         #Imagen
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        self.root.config(bg="white")
        
        logo = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo.png"
        self.logo_icon=PhotoImage(file = path.abspath(logo))
        title=Label(self.root,text="REPORTES DEL SISTEMA",padx=10,image=self.logo_icon,compound=LEFT,font=("impact",40),anchor="w").place(x=0,y=0,relwidth=1)

        #====SECCION 1====
        lbl_select_folder = Label(self.root,text="REPORTES",font=("times new roman",25),bg="#ffff7a").place(x=50,y=120)
        # txt_folder_name=Entry(self.root,font=("times new roman",25),bg="lightgreen").place(x=200,y=100)
        hr = Label(self.root,bg="lightgray").place(x=50,y=175,height=2,width=1190)
        #Iconos de ventanas
        icono_residuos = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/pdf-word.png"
        self.residuos_icon=PhotoImage(file=path.abspath(icono_residuos))
        #fRAME 1
        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=200,width=595,height=540)
        title=Label(Frame1,text="REPORTES GENERALES",padx=20,compound=CENTER,font=("impact",40),bg="#ffff7a",anchor="w").place(x=0,y=0,relwidth=1)
        # title2=Label(Frame1,text="REPORTE GENERAL OEFA",padx=20,compound=CENTER,font=("impact",40),bg="#ffff7a",anchor="w").place(x=0,y=205,relwidth=1)
        #fRAME 2
        Frame2=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame2.place(x=600,y=200,width=595,height=540)
        title=Label(Frame2,text="REPORTES CON FILTRO",padx=20,compound=CENTER,font=("impact",40),bg="#ffff7a",anchor="w").place(x=0,y=0,relwidth=1)
        
    
        
        listado_residuos = Button(Frame1,text="Listado de residuos recibidos en planta",width=80,command=self.reporte_residuos).place(y = 70)
        listado_produccion = Button(Frame1,text="Listado de produccion de planta",width=80,command=self.reporte_produccion).place(x=1, y = 105)
        listado_producto_final = Button(Frame1,text="Listado de costales de planta",width=80,command=self.reporte_producto_final).place(x=1, y = 140)
        listado_ventas = Button(Frame1,text="Listado de boleta de ventas",width=80,command=self.reporte_ventas).place(x=1, y = 175)
        # btresiduos = Button(Frame1,text='REPORTE \nPDF',bg='lightgray',fg='red',font=('arial',20,'bold'),activebackground='#36d073',
        #               width=250,height=120,anchor=NE,cursor='clock',activeforeground='white',bd=8,relief=RIDGE,
        #               image=self.residuos_icon,compound= RIGHT).place(x=60,y=300)
        
        lbl_fecha = Label(Frame2,text="FECHA INICIO",bg="white",font=("times new roman",15,"bold"))
        lbl_fecha.place(x=18, y =90)
        self.fecha_var = StringVar()
        txt_fecha=DateEntry(Frame2,textvariable =self.fecha_var,date_pattern='d/mm/y',font=("times new roman",12,"bold"),state="readonly")
        txt_fecha.place(x=185, y =90)
        dt =date(2021,12,2)
        txt_fecha.set_date(dt)
        
        filtro_residuos = Button(Frame2,text="Listado de residuos filtrados recibidos en planta",width=80,command=self.reporte_filtrado_residuos).place(y = 200)
        filtro_produccion = Button(Frame2,text="Listado de produccion de planta",width=80,command = self.reporte_filtrado_pp).place(x=1, y = 225)
        listado_producto_final = Button(Frame2,text="Listado de costales de planta",width=80,command=self.reporte_filtrado_pf).place(x=1, y = 250)
        listado_ventas = Button(Frame2,text="Listado de boleta de ventas",width=80,command=self.reporte_ventas).place(x=1, y = 275)
        
        lbl_fecha_2 = Label(Frame2,text="FECHA FIN",bg="white",font=("times new roman",15,"bold"))
        lbl_fecha_2.place(x=18, y =145)
        self.fecha_2_var = StringVar()
        txt_fecha_2=DateEntry(Frame2,textvariable =self.fecha_2_var,date_pattern='d/mm/y',font=("times new roman",12,"bold"),state="readonly")
        txt_fecha_2.place(x=185, y =145)
        dt =date(2021,12,2)
        txt_fecha_2.set_date(dt)
        

    def reporte_residuos(self):
        my_con = create_engine("mysql+mysqldb://root:root@localhost:3306/municipalidad")
        sql= "SELECT * FROM materia_prima" 
        df=pd.read_sql(sql,my_con)
        #df[['LOTE']].astype(int)
        df[['PESO']].astype(float)
        text = df.to_excel("repore_residuos.xlsx")
        

    def reporte_produccion(self):
        my_con = create_engine("mysql+mysqldb://root:root@localhost:3306/municipalidad")
        sql= "SELECT * FROM producto_en_proceso" 
        df=pd.read_sql(sql,my_con)
       #df[['LOTE']].astype(int)
        df[['PESO']].astype(float)
        df[['CANT_MICROORGANISMO']].astype(float)
        df[['TEMPERATURA']].astype(int)
        df.to_excel("report_produccion.xlsx")
        
    def reporte_producto_final(self):
        my_con = create_engine("mysql+mysqldb://root:root@localhost:3306/municipalidad")
        sql= "SELECT * FROM producto_final" 
        df=pd.read_sql(sql,my_con)
        #df[['LOTE']].astype(int)
        df[['PESO']].astype(float)
        df.to_excel("report_producto_final.xlsx")
        
        
    def reporte_ventas(self):
        my_con = create_engine("mysql+mysqldb://root:root@localhost:3306/municipalidad")
        sql= "SELECT * FROM boleta_venta" 
        df=pd.read_sql(sql,my_con)
        df[['PRECIO']].astype(float)
        df[['CANTIDAD']].astype(int)
        df.to_excel("reporte_ventas.xlsx")
    
    
    def reporte_filtrado_residuos(self):
        my_con = create_engine("mysql+mysqldb://root:root@localhost:3306/municipalidad")
        sql= "SELECT * FROM materia_prima" 
        df=pd.read_sql(sql,my_con)
        fecha_1 = self.fecha_var.get()
        fecha_1 = datetime.strptime(fecha_1, '%d/%m/%Y')
        fecha_2 = self.fecha_2_var.get()
        fecha_2 = datetime.strptime(fecha_2, '%d/%m/%Y')
    
        df['FECHA'] = pd.to_datetime(df['FECHA'],format= '%d/%m/%Y')
        mask = (df['FECHA'] > fecha_1 ) & (df['FECHA'] <= fecha_2 )
        filtered_df=df.loc[mask]
        # filtered_df.strftime("'%m/%d/%Y")
        filtered_df.to_excel("reporte_filfftrado.xlsx")
        
    def reporte_filtrado_pp(self):
        my_con = create_engine("mysql+mysqldb://root:root@localhost:3306/municipalidad")
        sql= "SELECT * FROM producto_en_proceso" 
        df=pd.read_sql(sql,my_con)
        fecha_1 = self.fecha_var.get()
        fecha_1 = datetime.strptime(fecha_1, '%d/%m/%Y')
        fecha_2 = self.fecha_2_var.get()
        fecha_2 = datetime.strptime(fecha_2, '%d/%m/%Y')
        # df['HORA_ENTRADA'] = df['HORA_ENTRADA'].astype('timedelta64[s]')
        # df['HORA_ENTRADA'] = pd.to_datetime(df['HORA_ENTRADA'],format= '%HH:%M:%S' ).dt.time
        df['FECHA'] = pd.to_datetime(df['FECHA'],format= '%d/%m/%Y')
        mask = (df['FECHA'] > fecha_1 ) & (df['FECHA'] <= fecha_2 )
        filtered_df=df.loc[mask]
        filtered_df.to_excel("reporte_filtrado_producto_proceso.xlsx")
        
    def reporte_filtrado_pf(self):
        my_con = create_engine("mysql+mysqldb://root:root@localhost:3306/municipalidad")
        sql= "SELECT * FROM producto_final" 
        df=pd.read_sql(sql,my_con)
        fecha_1 = self.fecha_var.get()
        fecha_1 = datetime.strptime(fecha_1, '%d/%m/%Y')
        fecha_2 = self.fecha_2_var.get()
        fecha_2 = datetime.strptime(fecha_2, '%d/%m/%Y')
        # df['HORA_ENTRADA'] = df['HORA_ENTRADA'].astype('timedelta64[s]')
        # df['HORA_ENTRADA'] = pd.to_datetime(df['HORA_ENTRADA'],format= '%HH:%M:%S' ).dt.time
        df['FECHA'] = pd.to_datetime(df['FECHA'],format= '%d/%m/%Y')
        mask = (df['FECHA'] > fecha_1 ) & (df['FECHA'] <= fecha_2 )
        filtered_df=df.loc[mask]
        filtered_df.to_excel("reporte_filtrado_producto_final.xlsx")
    
    def reporte_filtrado_ventas(self):
        my_con = create_engine("mysql+mysqldb://root:root@localhost:3306/municipalidad")
        sql= "SELECT * FROM boleta_venta" 
        df=pd.read_sql(sql,my_con)
        fecha_1 = self.fecha_var.get()
        fecha_1 = datetime.strptime(fecha_1, '%d/%m/%Y')
        fecha_2 = self.fecha_2_var.get()
        fecha_2 = datetime.strptime(fecha_2, '%d/%m/%Y')
        # df['HORA_ENTRADA'] = df['HORA_ENTRADA'].astype('timedelta64[s]')
        # df['HORA_ENTRADA'] = pd.to_datetime(df['HORA_ENTRADA'],format= '%HH:%M:%S' ).dt.time
        df['FECHA'] = pd.to_datetime(df['FECHA'],format= '%d/%m/%Y')
        mask = (df['FECHA'] > fecha_1 ) & (df['FECHA'] <= fecha_2 )
        filtered_df=df.loc[mask]
        filtered_df.to_excel("reporte_filtrado_ventas.xlsx")
        
    def reporte_oefa(self):
        
        pass
        

if __name__ == "__main__":        
    root= Tk()
    obj = Generador_de_Reportes(root)
    root.mainloop()
