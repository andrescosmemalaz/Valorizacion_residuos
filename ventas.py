import pymysql
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry 
from datetime import date
import os 
from os import path
from PIL import  Image,ImageTk


class Boleta_ventas():
    def __init__(self,root):
        self.root=root
        self.root.title("Sistema Administracion de Ventas")
        icono = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico"
        self.root.iconbitmap(path.abspath(icono))
        #self.root.iconbitmap("F:\\andres\\Ciclo 10\\Topicos\\Trabajo Grupal\\Trabajo Grupal-Software Municpal\\miproject\\Caja negra\\project\\logo_castillo_grande.ico")
        self.root.geometry("1300x770+0+0")
        #Imagen
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        title = Label(self.root,text="Sistema Administración de Ventas",bd=12,relief=GROOVE,font=("times new roman",40,"bold"),bg="#008f4c",fg="black")
        title.pack(side=TOP,fill=X)

        #Todas las variables
        self.n_boleta_var = IntVar()
        self.lote_var = StringVar()
        self.FECHA_var = StringVar()
        self.estado_var = StringVar()
        self.CANTIDAD_var = DoubleVar()
        self.PRECIO_var = DoubleVar()
        self.TOTAL_var = DoubleVar()
        self.nombre_cliente_var = StringVar()
        self.ruc_cliente = IntVar()
        self.buscar_por_var = StringVar()
        self.texto_buscar_var = StringVar()

        #Frame de administracion
        Managment_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="orange")
        Managment_Frame.place(x=20, y=100,width=450,height=605)


        m_title = Label(Managment_Frame,text="Registrar Ventas", bg="orange",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_n_boleta = Label(Managment_Frame,text="NUM_BOLETA",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_n_boleta.grid(row=1,column=0, pady=10,padx=20,sticky="w")
        txt_n_boleta  =Entry(Managment_Frame,textvariable =self.n_boleta_var,font=("times new roman",12,"bold"))
        txt_n_boleta.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lbl_lote = Label(Managment_Frame,text="LOTE",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_lote.grid(row=2,column=0, pady=10,padx=20,sticky="w")
        txt_lote  =Entry(Managment_Frame,textvariable =self.lote_var,font=("times new roman",12,"bold"))
        txt_lote.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_fecha_ingreso = Label(Managment_Frame,text="FECHA INGRESO",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_fecha_ingreso.grid(row=3,column=0, pady=10,padx=20,sticky="w")
        # txt_fecha  =Entry(Managment_Frame,textvariable =self.FECHA_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        # txt_fecha.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        txt_fecha_ingreso=DateEntry(Managment_Frame,textvariable =self.FECHA_var,date_pattern='dd/mm/y',font=("times new roman",12,"bold"),state="readonly")
        txt_fecha_ingreso.grid(row=3, column=1,padx=10,ipadx=25)
        dt =date(2021,12,2)
        txt_fecha_ingreso.set_date(dt)
        
        lbl_ESTADO = Label(Managment_Frame,text="ESTADO",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_ESTADO.grid(row=4,column=0, pady=10,padx=20,sticky="w")
        # txt_PRODUCTO  =Entry(Managment_Frame,textvariable =self.PRODUCTO_var,font=("times new roman",12,"bold"))
        # txt_PRODUCTO.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        #Combobox
        combo_ESTADO = ttk.Combobox(Managment_Frame,textvariable =self.estado_var,font=("times new roman",10,"bold"),state="readonly")
        combo_ESTADO['values'] = ('PAGADO',['POR PAGAR'])
        combo_ESTADO.grid(row=4,column=1,pady=14,padx=10,ipady=2,ipadx=2)
        
        lbl_CANTIDAD = Label(Managment_Frame,text="CANTIDAD",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_CANTIDAD.grid(row=5,column=0, pady=10,padx=20,sticky="w")
        txt_CANTIDAD=Entry(Managment_Frame,textvariable =self.CANTIDAD_var,font=("times new roman",12,"bold"))
        txt_CANTIDAD.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        
        lbl_PRECIO = Label(Managment_Frame,text="PRECIO",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_PRECIO.grid(row=6,column=0, pady=10,padx=20,sticky="w")
        txt_PRECIO  =Entry(Managment_Frame,textvariable =self.PRECIO_var,font=("times new roman",12,"bold"))
        txt_PRECIO.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        lbl_TOTAL = Label(Managment_Frame,text="TOTAL",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_TOTAL.grid(row=7,column=0, pady=10,padx=20,sticky="w")
        txt_TOTAL  =Entry(Managment_Frame,textvariable =self.TOTAL_var,font=("times new roman",12,"bold"))
        txt_TOTAL.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        lbl_NOMBRE_CLIENTE = Label(Managment_Frame,text="NOMBRE CLIENTE",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_NOMBRE_CLIENTE.grid(row=8,column=0, pady=10,padx=20,sticky="w")
        txt_NOMBRE_CLIENTE  =Entry(Managment_Frame,textvariable =self.nombre_cliente_var,font=("times new roman",12,"bold"))
        txt_NOMBRE_CLIENTE.grid(row=8,column=1,pady=10,padx=20,sticky="w")
        
        lbl_RUC = Label(Managment_Frame,text="RUC",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_RUC.grid(row=9,column=0, pady=10,padx=20,sticky="w")
        txt_RUC  =Entry(Managment_Frame,textvariable =self.ruc_cliente,font=("times new roman",12,"bold"))
        txt_RUC.grid(row=9,column=1,pady=10,padx=20,sticky="w")
    
    
        #Botom Frame
        btn_frame = Frame(Managment_Frame,bd=3,relief=RIDGE,bg="black")
        btn_frame.place(x=15,y=500,width=420)

        agregar_botom = Button(btn_frame,text="Agregar",width=10,command=self.agregar_VENTA).grid(row=0,column=0,padx=10,pady=10)
        actualizar_botom = Button(btn_frame,text="Actualizar",width=10,command=self.actualizar_VENTA).grid(row=0,column=1,padx=10,pady=10)
        eliminar_botom = Button(btn_frame,text="Eliminar",width=10,command=self.eliminar_VENTA).grid(row=0,column=2,padx=10,pady=10)
        limpiar_botom = Button(btn_frame,text="Limpiar",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        # Base de Datos Frame 
        BD_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#36d073")
        BD_Frame.place(x=500,y=100,width=770,height=645)

        lbl_buscar = Label(BD_Frame, text="Buscar por",bg="#36d073",fg="white",font=("times new roman",15,"bold"))
        lbl_buscar.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        #Combobox
        combo_buscar = ttk.Combobox(BD_Frame,textvariable =self.buscar_por_var,font=("times new roman",13,"bold"),state="readonly")
        combo_buscar['values'] = ("NUM_BOLETA","LOTE","NOMBRE_CLIENTE")
        combo_buscar.grid(row=0,column=1,pady=15,padx=20,sticky="w")
        texto_buscar = Entry(BD_Frame,textvariable =self.texto_buscar_var,font=("times new roman",10,"bold"),width=20,bd=5,relief=GROOVE)
        texto_buscar.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        #Botones
        buscarboton= Button(BD_Frame,text="Buscar",width=10,pady=5,command=self.buscar_VENTA).grid(row=0,column=3,padx=10,pady=10)
        mostrarboton = Button(BD_Frame,text="Listar",width=8,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #===========Tabla de registros ======= 
        Table_Frame = Frame(BD_Frame,bd=4,relief=RIDGE,bg="yellow")
        Table_Frame.place(x=10,y=70,width=740,height=550)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Ventas_table = ttk.Treeview(Table_Frame,column=("NUM_BOLETA","LOTE","FECHA","ESTADO","CANTIDAD","PRECIO","TOTAL","NOMBRE_CLIENTE","RUC_CLIENTE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Ventas_table.xview)
        scroll_y.config(command=self.Ventas_table.yview)
        

        self.Ventas_table.heading("NUM_BOLETA",text ="NUM_BOLETA")
        # self.Materiaprima_table.heading("CODIGO",text ="CODIGO")
        self.Ventas_table.heading("LOTE",text ="LOTE")
        self.Ventas_table.heading("FECHA",text ="FECHA")
        self.Ventas_table.heading("ESTADO",text ="ESTADO")
        self.Ventas_table.heading("CANTIDAD",text ="CANTIDAD")
        self.Ventas_table.heading("PRECIO",text ="PRECIO")
        self.Ventas_table.heading("TOTAL",text ="TOTAL")
        self.Ventas_table.heading("NOMBRE_CLIENTE",text ="NOMBRE_CLIENTE")
        self.Ventas_table.heading("RUC_CLIENTE",text ="RUC_CLIENTE")
        

        self.Ventas_table['show'] = 'headings'
        self.Ventas_table.column("NUM_BOLETA",width=100)
        self.Ventas_table.column("LOTE",width=100)
        self.Ventas_table.column("FECHA",width=100)
        self.Ventas_table.column("ESTADO",width=100)
        self.Ventas_table.column("CANTIDAD",width=100)
        self.Ventas_table.column("PRECIO",width=100)
        self.Ventas_table.column("TOTAL",width=100)
        self.Ventas_table.column("NOMBRE_CLIENTE",width=100)
        self.Ventas_table.column("RUC_CLIENTE",width=100)
        
        
        

        self.Ventas_table.pack(fill=BOTH,expand=1)
        self.Ventas_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.clear()

    def agregar_VENTA(self):
        if self.n_boleta_var.get() == "":
            messagebox.showerror("Error","Todos los campos deben ser llenados")
        else:
            con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
            cur=con.cursor()
            cur.execute("insert into boleta_venta values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.n_boleta_var.get(),
                                                                                        self.lote_var.get(),
                                                                                        self.FECHA_var.get(),
                                                                                        self.estado_var.get(),
                                                                                        self.CANTIDAD_var.get(),
                                                                                        self.PRECIO_var.get(),                                             
                                                                                        self.TOTAL_var.get(),
                                                                                        self.nombre_cliente_var.get(),
                                                                                        self.ruc_cliente.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Correcto","Se ha realizado el registro con éxito")
    
    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from boleta_venta")
        rows = cur.fetchall()
        if len(rows) !=0:
            self.Ventas_table.delete(*self.Ventas_table.get_children())
            for row in rows:
                self.Ventas_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def get_cursor(self,ev):
        cursor_row = self.Ventas_table.focus()
        contents = self.Ventas_table.item(cursor_row)
        row = contents['values']
        self.n_boleta_var.set(row[0])
        self.lote_var.set(row[1])
        self.FECHA_var.set(row[2])
        self.estado_var.set(row[3])
        self.CANTIDAD_var.set(row[4])
        self.PRECIO_var.set(row[5])
        self.TOTAL_var.set(row[6])
        self.nombre_cliente_var.set(row[7])
        self.ruc_cliente.set(row[8])
                                                              
    
    def actualizar_VENTA(self):

        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur=con.cursor()
        cur.execute("update boleta_venta set LOTE=%s,FECHA=%s,ESTADO=%s,CANTIDAD=%s,PRECIO=%s,TOTAL=%s,NOMBRE_CLIENTE=%s,RUC_CLIENTE=%s where NUM_BOLETA=%s",(
                                                                                    self.lote_var.get(),
                                                                                    self.FECHA_var.get(),
                                                                                    self.estado_var.get(),
                                                                                    self.CANTIDAD_var.get(),
                                                                                    self.PRECIO_var.get(),                                             
                                                                                    self.TOTAL_var.get(),
                                                                                    self.nombre_cliente_var.get(),
                                                                                    self.ruc_cliente.get(),
                                                                                    self.n_boleta_var.get()))  
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Correcto","Se ha actualizado el registro con éxito")
    
    def clear(self):
        self.n_boleta_var.set("")
        self.lote_var.set(""),
        self.FECHA_var.set(""),
        self.estado_var.set(""),
        self.CANTIDAD_var.set(""),
        self.PRECIO_var.set(""),                                             
        self.TOTAL_var.set(""),
        self.nombre_cliente_var.set(""),
        self.ruc_cliente.set("")
        
    
        
    
    def eliminar_VENTA(self):
        con =pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("delete from boleta_venta where NUM_BOLETA=%s",self.n_boleta_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def buscar_VENTA(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from boleta_venta where " + str(self.buscar_por_var.get()) + " Like '%" + str(self.texto_buscar_var.get())+"%'")
        rows =  cur.fetchall()
        if len(rows) != 0:
            self.Ventas_table.delete(*self.Ventas_table.get_children())
            for row in rows:
                self.Ventas_table.insert('',END,values=row)
            con.commit()
        con.close()
        self.texto_buscar_var.set("")
    

if __name__ == "__main__":
    root = Tk()
    obj = Boleta_ventas(root)
    root.mainloop()
