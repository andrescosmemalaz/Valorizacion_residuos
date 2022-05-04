import os
from os import path
import tkinter as tk
from tkinter.constants import RIDGE
import tkinter.ttk as ttk
from PIL import  Image,ImageTk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sqlalchemy import create_engine
class Dashboard():
    def __init__(self,root):
        self.root=root
        self.root.title("Dashboard")
        icono = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico"
        self.root.iconbitmap(path.abspath(icono))
        self.root.geometry("970x570+0+0")
        self.panel = ttk.Notebook(root)
        self.panel.pack(fill='both',expand='yes')
        
        tab1 = ttk.Frame(self.panel)
        self.panel.add(tab1,text='Materia Prima')
        
        tab2 = ttk.Frame(self.panel)
        self.panel.add(tab2,text='Produccion')
        etiqueta = ttk.Label(self.root)
        
        # tab3 = ttk.Frame(self.panel)
        # self.panel.add(tab3,text='Producto Final')
        # etiqueta = ttk.Label(self.root)
        
        # tab4 = ttk.Frame(self.panel)
        # self.panel.add(tab4,text='Venta')
        # etiqueta = ttk.Label(self.root)
        
        etiqueta1 = tk.Label(tab1,text="Gráficas de Materia Prima por KG",font=("times new roman",20,"bold")).place(x=300,y=20)
        # etiqueta1 = tk.Label(tab1,text="Numero 2").place(x=20,y=40)

        etiqueta2 = tk.Label(tab2,text="Gráficas de Productos en Proceso",font=("times new roman",20,"bold")).place(x=300,y=20)
        # etiqueta2 = tk.Label(tab2,text="Numero 5").place(x=20,y=40)
        
        # etiqueta3 = tk.Label(tab3,text="Gráfica de Productos Finales",font=("times new roman",20,"bold")).place(x=300,y=20)
        # # etiqueta3 = tk.Label(tab3,text="Numero 7").place(x=20,y=40)
        
        boton_e_1 = tk.Button(tab1,text="Generar Grafica",command=self.reporte_1)
        boton_e_1.place(x=10,y=20,width=200)
        boton_e_2 = tk.Button(tab2,text="Generar Grafica",command=self.reporte_2)
        boton_e_2.place(x=10,y=20,width=200)
        # boton_e_3 = tk.Button(tab3,text="Generar Grafica",command=self.reporte_3)
        # boton_e_3.place(x=10,y=20,width=200)
    
        self.frame1 = tk.Frame(tab1,bd=2,relief=RIDGE,bg="white")
        self.frame1.place(x=100,y=60,width=720,height=400)
        self.frame2 = tk.Frame(tab2,bd=2,relief=RIDGE,bg="white")
        self.frame2.place(x=10,y=60,width=900,height=400)
        # self.frame3 = tk.Frame(tab3,bd=2,relief=RIDGE,bg="white")
        # self.frame3.place(x=100,y=60,width=720,height=400)
        
    def reporte_1(self):
        my_con = create_engine("mysql+mysqldb://root:root@localhost:3306/municipalidad")
        sql= "SELECT * FROM materia_prima" 
        df=pd.read_sql(sql,my_con)
        print(df)
        df['FECHA'] = pd.to_datetime(df['FECHA'])
        df['PESO'] = pd.to_numeric(df['PESO'])
        self.frame1 = tk.Frame(self.frame1,bd=7,relief=RIDGE,bg="#D4E1E7")
        self.frame1.pack()
        fecha = df['FECHA']
        lista_de_lotes = ['MP-001','MP-002', 'MP-003','MP-004','MP-005','MP-006']
        zona = ['Zona 1','Zona 2','Zona 3','Zona 4','Zona 5']
        fechas = ['2020-01-12','2020-02-12','2020-05-12','2020-07-12','2020-09-12','2020-10-12']
        # print(df.groupby('ZONA')['PESO'].sum())
        z = list()
        total_residuos = list()
        z = df.groupby('ZONA')['PESO'].sum()
        for x in z:
            total_residuos.append(x)
        w = list()
        fecha_residuos = list()
        w = df.groupby('FECHA')['PESO'].sum()
        for x in w:
            fecha_residuos.append(x)
        
        lote = list()
        total_por_lote = list()
        z = df.groupby('LOTE')['PESO'].sum()
        for x in z:
            total_por_lote.append(x)

        fig1, axs1 = plt.subplots(2,1 , dpi=70 ,figsize=(10, 6), 
        sharey=True, facecolor='#00f9f844')
        fig1.suptitle('Graficas Materia Prima por KG')
        
        axs1[0].bar(lista_de_lotes,total_por_lote)
        axs1[1].bar(zona, total_residuos, color = 'blue')
        # axs1[2].plot(fecha, temperatura_avg, color = 'm')
        canvas1 = FigureCanvasTkAgg(fig1, master =  self.frame1)  # Crea el area de dibujo en Tkinter
        canvas1.draw()
        canvas1.get_tk_widget().grid(column=0, row=0)
        
    def reporte_2(self):
        my_con = create_engine("mysql+mysqldb://root:root@localhost:3306/municipalidad")
        sql= "SELECT * FROM producto_en_proceso" 
        df=pd.read_sql(sql,my_con)
        print(df)
        df['FECHA'] = pd.to_datetime(df['FECHA'])
        df['PESO'] = pd.to_numeric(df['PESO'])
        df['CANT_MICROORGANISMO'] = pd.to_numeric(df['CANT_MICROORGANISMO'])
        df['TEMPERATURA'] = pd.to_numeric(df['TEMPERATURA'])
        lista_de_lotes = ['MP-001','MP-002', 'MP-003','MP-004','MP-005','MP-006']
        self.frame2 = tk.Frame(self.frame2,bd=7,relief=RIDGE,bg="#D4E1E7")
        self.frame2.pack()
        fecha = df['FECHA']
        peso = df['PESO']
        camas = ['Cama 1','Cama 2','Cama 3','Cama 4','Cama 5']
        # microorganismo = df['CANT_MICROORGANISMO']
        z = list()
        total_microorganismo = list()
        z = df.groupby('NRO_CAMA')['CANT_MICROORGANISMO'].sum()
        for x in z:
            total_microorganismo.append(x)
        # temperatura = df['TEMPERATURA']
        z = list()
        temperatura_mean = list()
        z = df.groupby('NRO_CAMA')['TEMPERATURA'].mean()
        for x in z:
            temperatura_mean.append(x)
        
        lote = list()
        total_por_lote = list()
        z = df.groupby('LOTE')['PESO'].sum()
        for x in z:
            total_por_lote.append(x)
    
        fig1, axs1 = plt.subplots(1,3 , dpi=50 ,figsize=(18, 8), 
        sharey=True, facecolor='grey')
        fig1.suptitle('Graficas Produccion')
        
        axs1[0].bar(lista_de_lotes,total_por_lote, color = 'y')
        axs1[1].bar(camas, total_microorganismo, color = 'g')
        axs1[2].bar(camas, temperatura_mean, color = 'm')
        canvas1 = FigureCanvasTkAgg(fig1, master =  self.frame2)  # Crea el area de dibujo en Tkinter
        canvas1.draw()
        canvas1.get_tk_widget().grid(column=0, row=0)   
    
    # def reporte_3(self):
    #     my_con = create_engine("mysql+mysqldb://root:root@localhost:3306/municipalidad")
    #     sql= "SELECT * FROM producto_final" 
    #     df=pd.read_sql(sql,my_con)
    #     print(df)
    #     df['FECHA'] = pd.to_datetime(df['FECHA'])
    #     df['PESO'] = pd.to_numeric(df['PESO'])
    #     lista_de_lotes = ['MP-001','MP-002', 'MP-003','MP-004','MP-005','MP-006']
    #     lote = list()
    #     total_por_lote = list()
    #     z = df.groupby('LOTE')['PESO'].sum()
    #     for x in z:
    #         total_por_lote.append(x)
    #     self.frame3 = tk.Frame(self.frame3,bd=7,relief=RIDGE,bg="#D4E1E7")
    #     self.frame3.pack()
    #     fecha = df['FECHA']
    #     peso = df['PESO']
    #     # fig1, axs1 = plt.subplots(2,1 ,dpi=50 ,figsize=(10, 6), 
    #     # sharey=True, facecolor='#00f9f844')
    #     # fig1.suptitle('Graficas Produccion')
        
    #     # axs1[0].plot(fecha,peso, color = 'y')
    #     # axs1[1].bar(lista_de_lotes,total_por_lote,color = 'y')
    #     # # axs1[1].plot(fecha, microorganismo, color = 'g')
    #     # # axs1[2].plot(fecha, temperatura, color = 'm')
    #     fig1 = plt.bar(lista_de_lotes,total_por_lote,color = 'y')
    #     canvas1 = FigureCanvasTkAgg(fig1, master =  self.frame3)  # Crea el area de dibujo en Tkinter
    #     canvas1.draw()
    #     canvas1.get_tk_widget().grid(column=0, row=0)


if __name__ == "__main__":        
    root= tk.Tk()
    obj = Dashboard(root)
    root.mainloop()