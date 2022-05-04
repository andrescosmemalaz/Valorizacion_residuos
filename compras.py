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

class Compras():
    def __init__(self,root):
        self.root=root
        self.root.title("Sistema Administracion de Compras")
        icono = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico"
        self.root.iconbitmap(path.abspath(icono))
        #self.root.iconbitmap("F:\\andres\\Ciclo 10\\Topicos\\Trabajo Grupal\\Trabajo Grupal-Software Municpal\\miproject\\Caja negra\\project\\logo_castillo_grande.ico")
        self.root.geometry("1300x770+0+0")
        #Imagen
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        
        title = Label(self.root,text="Sistema Administración de Compras",bd=12,relief=GROOVE,font=("times new roman",40,"bold"))
        title.pack(side=TOP,fill=X)

        #Todas las variables
        self.ID_COMPRA_var = StringVar()
        self.ID_PROVEEDOR_var = StringVar()
        self.FECHA_var = StringVar()
        self.PRODUCTO_var = StringVar()
        self.PRECIO_var = DoubleVar()
        self.CANTIDAD_var = DoubleVar()
        self.TOTAL_var = DoubleVar()
        self.buscar_por_var = StringVar()
        self.texto_buscar_var = StringVar()

        #Frame de administracion
        Managment_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#D4E1E7")
        Managment_Frame.place(x=20, y=100,width=450,height=605)


        m_title = Label(Managment_Frame,text="Registrar Compra", bg="#D4E1E7",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_id_compra = Label(Managment_Frame,text="ID COMPRA",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_id_compra.grid(row=1,column=0, pady=10,padx=20,sticky="w")
        txt_id_compra  =Entry(Managment_Frame,textvariable =self.ID_COMPRA_var,font=("times new roman",12,"bold"))
        txt_id_compra.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lbl_id_proveedor = Label(Managment_Frame,text="ID PROVEEDOR",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_id_proveedor.grid(row=2,column=0, pady=10,padx=20,sticky="w")
        txt_id_proveedor  =Entry(Managment_Frame,textvariable =self.ID_PROVEEDOR_var,font=("times new roman",12,"bold"))
        txt_id_proveedor.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        
        lbl_fecha = Label(Managment_Frame,text="FECHA",bg="#D4E1E7",fg="black",font=("times new roman",11,"bold"))
        lbl_fecha.grid(row=3,column=0, pady=10,padx=20,sticky="w")
        txt_fecha=DateEntry(Managment_Frame,textvariable =self.FECHA_var,date_pattern='dd/mm/y',font=("times new roman",10,"bold"),state="readonly")
        txt_fecha.grid(row=3, column=1,padx=10,ipadx=30)
        dt =date(2021,12,2)
        txt_fecha.set_date(dt)
        
        lbl_NOMBRE_PRODUCTO= Label(Managment_Frame,text="PRODUCTO",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_NOMBRE_PRODUCTO.grid(row=4,column=0, pady=10,padx=20,sticky="w")
        txt_NOMBRE_PRODUCTO=Entry(Managment_Frame,textvariable =self.PRODUCTO_var,font=("times new roman",12,"bold"))
        txt_NOMBRE_PRODUCTO.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        lbl_PRECIO = Label(Managment_Frame,text="PRECIO",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_PRECIO.grid(row=5,column=0, pady=10,padx=20,sticky="w")
        txt_PRECIO=Entry(Managment_Frame,textvariable =self.PRECIO_var,font=("times new roman",12,"bold"))
        txt_PRECIO.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        
        lbl_CANTIDAD = Label(Managment_Frame,text="CANTIDAD",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_CANTIDAD.grid(row=6,column=0, pady=10,padx=20,sticky="w")
        txt_CANTIDAD  =Entry(Managment_Frame,textvariable =self.CANTIDAD_var,font=("times new roman",12,"bold"))
        txt_CANTIDAD.grid(row=6,column=1,pady=10,padx=20,sticky="w")
    
        lbl_TOTAL = Label(Managment_Frame,text="TOTAL",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_TOTAL.grid(row=7,column=0, pady=10,padx=20,sticky="w")
        txt_TOTAL  =Entry(Managment_Frame,textvariable =self.TOTAL_var,font=("times new roman",12,"bold"))
        txt_TOTAL.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        
        #Botom Frame
        btn_frame = Frame(Managment_Frame,bd=3,relief=RIDGE,bg="black")
        btn_frame.place(x=15,y=500,width=420)

        agregar_botom = Button(btn_frame,text="Agregar",width=10,command=self.agregar_compra).grid(row=0,column=0,padx=10,pady=10)
        actualizar_botom = Button(btn_frame,text="Actualizar",width=10,command=self.actualizar_compra).grid(row=0,column=1,padx=10,pady=10)
        eliminar_botom = Button(btn_frame,text="Eliminar",width=10,command=self.eliminar_compra).grid(row=0,column=2,padx=10,pady=10)
        limpiar_botom = Button(btn_frame,text="Limpiar",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        # Base de Datos Frame 
        BD_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#36d073")
        BD_Frame.place(x=500,y=100,width=770,height=645)

        lbl_buscar = Label(BD_Frame, text="Buscar por",bg="#36d073",fg="white",font=("times new roman",15,"bold"))
        lbl_buscar.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        #Combobox
        combo_buscar = ttk.Combobox(BD_Frame,textvariable =self.buscar_por_var,font=("times new roman",13,"bold"),state="readonly")
        combo_buscar['values'] = ("ID_PROVEDOR","ID_COMPRA")
        combo_buscar.grid(row=0,column=1,pady=15,padx=20,sticky="w")
        texto_buscar = Entry(BD_Frame,textvariable =self.texto_buscar_var,font=("times new roman",10,"bold"),width=20,bd=5,relief=GROOVE)
        texto_buscar.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        #Botones
        buscarboton= Button(BD_Frame,text="Buscar",width=10,pady=5,command=self.buscar_compra).grid(row=0,column=3,padx=10,pady=10)
        mostrarboton = Button(BD_Frame,text="Listar",width=8,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #===========Tabla de registros ======= 
        Table_Frame = Frame(BD_Frame,bd=4,relief=RIDGE,bg="yellow")
        Table_Frame.place(x=10,y=70,width=740,height=550)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Compras_table = ttk.Treeview(Table_Frame,column=("ID_COMPRA","ID_PROVEEDOR","FECHA","PRODUCTO","PRECIO","CANTIDAD","TOTAL"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Compras_table.xview)
        scroll_y.config(command=self.Compras_table.yview)
        

        self.Compras_table.heading("ID_COMPRA",text ="ID_COMPRA")
        # self.Materiaprima_table.heading("CODIGO",text ="CODIGO")
        self.Compras_table.heading("ID_PROVEEDOR",text ="ID_PROVEEDOR")
        self.Compras_table.heading("FECHA",text ="FECHA")
        self.Compras_table.heading("PRODUCTO",text ="PRODUCTO")
        self.Compras_table.heading("PRECIO",text ="PRECIO")
        self.Compras_table.heading("CANTIDAD",text ="CANTIDAD")
        self.Compras_table.heading("TOTAL",text ="TOTAL")
        

        self.Compras_table['show'] = 'headings'
        self.Compras_table.column("ID_COMPRA",width=100)
        self.Compras_table.column("ID_PROVEEDOR",width=100)
        self.Compras_table.column("FECHA",width=100)
        self.Compras_table.column("PRODUCTO",width=100)
        self.Compras_table.column("PRECIO",width=100)
        self.Compras_table.column("CANTIDAD",width=100)
        self.Compras_table.column("TOTAL",width=100)
        self.Compras_table.pack(fill=BOTH,expand=1)
        self.Compras_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.clear()

    def agregar_compra(self):
        if self.ID_COMPRA_var.get() == "":
            messagebox.showerror("Error","Todos los campos deben ser llenados")
        else:
            con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
            cur=con.cursor()
            cur.execute("insert into compras values (%s,%s,%s,%s,%s,%s,%s)",(self.ID_COMPRA_var.get(),
                                                                                        self.ID_PROVEEDOR_var.get(),
                                                                                        self.FECHA_var.get(),
                                                                                        self.PRODUCTO_var.get(),
                                                                                        self.PRECIO_var.get(),
                                                                                        self.CANTIDAD_var.get(),                                             
                                                                                        self.TOTAL_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Correcto","Se ha realizado el registro con éxito")
    
    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from compras")
        rows = cur.fetchall()
        if len(rows) !=0:
            self.Compras_table.delete(*self.Compras_table.get_children())
            for row in rows:
                self.Compras_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def get_cursor(self,ev):
        cursor_row = self.Compras_table.focus()
        contents = self.Compras_table.item(cursor_row)
        row = contents['values']
        self.ID_COMPRA_var.set(row[0])
        self.ID_PROVEEDOR_var.set(row[1])
        self.FECHA_var.set(row[2])
        self.PRODUCTO_var.set(row[3])
        self.PRECIO_var.set(row[4])
        self.CANTIDAD_var.set(row[5])
        self.TOTAL_var.set(row[6])
        
                                                              
    
    def actualizar_compra(self):

        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur=con.cursor() 
        cur.execute("update compras set ID_PROVEEDOR=%s,FECHA=%s,PRODUCTO=%s,PRECIO=%s,CANTIDAD=%s,TOTAL=%s where ID_COMPRA=%s",(
                                                                                        self.ID_COMPRA_var.get(),   
                                                                                        self.ID_PROVEEDOR_var.get(),
                                                                                        self.FECHA_var.get(),
                                                                                        self.PRODUCTO_var.get(),
                                                                                        self.PRECIO_var.get(),                                             
                                                                                        self.CANTIDAD_var.get(),
                                                                                        self.TOTAL_var.get()))  
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Correcto","Se ha actualizado el registro con éxito")
    
    def clear(self):
        self.ID_COMPRA_var.set("")
        self.ID_PROVEEDOR_var.set("")
        self.FECHA_var.set("")
        self.PRODUCTO_var.set("")
        self.PRECIO_var.set("")
        self.CANTIDAD_var.set("")
        self.TOTAL_var.set("")                                                                                                                     
    
    def eliminar_compra(self):
        con =pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("delete from compras where ID_COMPRA=%s",self.ID_COMPRA_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def buscar_compra(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from compras where " + str(self.buscar_por_var.get()) + " Like '%" + str(self.texto_buscar_var.get())+"%'")
        rows =  cur.fetchall()
        if len(rows) != 0:
            self.Compras_table.delete(*self.Compras_table.get_children())
            for row in rows:
                self.Compras_table.insert('',END,values=row)
            con.commit()
        con.close()
        self.texto_buscar_var.set("")
    

if __name__ == "__main__":
    root = Tk()
    obj = Compras(root)
    root.mainloop()
