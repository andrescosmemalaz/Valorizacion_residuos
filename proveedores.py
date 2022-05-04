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

class Proveedor():
    def __init__(self,root):
        self.root=root
        self.root.title("Sistema Administracion de Compras")
        icono = path.abspath('F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico')
        self.root.iconbitmap(bitmap = icono)
        
        self.root.geometry("1300x770+0+0")
        #Imagen
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        
        title = Label(self.root,text="Sistema Administración de Proveedores",bd=12,relief=GROOVE,font=("times new roman",40,"bold"))
        title.pack(side=TOP,fill=X)
        
        #Frame de administracion
        Managment_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#D4E1E7")
        Managment_Frame.place(x=20, y=100,width=450,height=605)

        m_title = Label(Managment_Frame,text="Registrar Proveedor", bg="#D4E1E7",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lblID_PROVEEDOR = Label(Managment_Frame,text="ID PROVEEDOR",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lblID_PROVEEDOR.grid(row=1,column=0, pady=10,padx=20,sticky="w")
        self.ID_PROVEEDOR_var = StringVar()
        txtID_PROVEEDOR  =Entry(Managment_Frame,textvariable =self.ID_PROVEEDOR_var,font=("times new roman",12,"bold"))
        txtID_PROVEEDOR.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lbl_NOMBRE = Label(Managment_Frame,text="NOMBRE",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_NOMBRE.grid(row=2,column=0, pady=10,padx=20,sticky="w")
        self.NOMBRE_var = StringVar()
        txt_NOMBRE  =Entry(Managment_Frame,textvariable =self.NOMBRE_var,font=("times new roman",12,"bold"))
        txt_NOMBRE.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_APELLIDO = Label(Managment_Frame,text="APELLIDO",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_APELLIDO.grid(row=3,column=0, pady=10,padx=20,sticky="w")
        self.APELLIDO_var = StringVar()
        txt_APELLIDO  =Entry(Managment_Frame,textvariable =self.APELLIDO_var,font=("times new roman",12,"bold"))
        txt_APELLIDO.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_EMPRESA = Label(Managment_Frame,text="EMPRESA",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_EMPRESA.grid(row=4,column=0, pady=10,padx=20,sticky="w")
        self.EMPRESA_var = StringVar()
        txt_EMPRESA  =Entry(Managment_Frame,textvariable =self.EMPRESA_var,font=("times new roman",12,"bold"))
        txt_EMPRESA.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        lbl_RUC = Label(Managment_Frame,text="RUC",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_RUC.grid(row=5,column=0, pady=10,padx=20,sticky="w")
        self.RUC_var = StringVar()
        txt_RUC=Entry(Managment_Frame,textvariable =self.RUC_var,font=("times new roman",12,"bold"))
        txt_RUC.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        
        lbl_TELEFONO = Label(Managment_Frame,text="TELEFONO",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_TELEFONO.grid(row=6,column=0, pady=10,padx=20,sticky="w")
        self.TELEFONO_var = IntVar()
        txt_TELEFONO=Entry(Managment_Frame,textvariable =self.TELEFONO_var,font=("times new roman",12,"bold"))
        txt_TELEFONO.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        lbl_CORREO= Label(Managment_Frame,text="CORREO",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_CORREO.grid(row=7,column=0, pady=10,padx=20,sticky="w")
        self.CORREO_var = StringVar()
        txt_CORREO=Entry(Managment_Frame,textvariable =self.CORREO_var,font=("times new roman",12,"bold"))
        txt_CORREO.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        lbl_DESCRIPCION= Label(Managment_Frame,text="DESCRIPCION",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_DESCRIPCION.grid(row=8,column=0, pady=10,padx=20,sticky="w")
        self.DESCRIPCION_var = StringVar()
        txt_DESCRIPCION=Entry(Managment_Frame,textvariable =self.DESCRIPCION_var,font=("times new roman",12,"bold"))
        txt_DESCRIPCION.grid(row=8,column=1,pady=10,padx=20,sticky="w")
        
        #Botom Frame
        btn_frame = Frame(Managment_Frame,bd=3,relief=RIDGE,bg="black")
        btn_frame.place(x=10,y=450,width=420)

        agregar_botom = Button(btn_frame,text="Agregar",width=10,command=self.agregar_proveedor).grid(row=0,column=0,padx=10,pady=10)
        actualizar_botom = Button(btn_frame,text="Actualizar",width=10,command=self.actualizar_proveedor).grid(row=0,column=1,padx=10,pady=10)
        eliminar_botom = Button(btn_frame,text="Eliminar",width=10,command=self.eliminar_proveedor).grid(row=0,column=2,padx=10,pady=10)
        limpiar_botom = Button(btn_frame,text="Limpiar",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        # Base de Datos Frame 
        BD_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#36d073")
        BD_Frame.place(x=500,y=100,width=770,height=645)

        lbl_buscar = Label(BD_Frame, text="Buscar por",bg="#36d073",fg="white",font=("times new roman",15,"bold"))
        lbl_buscar.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        #Combobox
        self.buscar_por_var = StringVar()
        combo_buscar = ttk.Combobox(BD_Frame,textvariable =self.buscar_por_var,font=("times new roman",13,"bold"),state="readonly")
        combo_buscar['values'] = ("ID_PROVEDOR","ID_COMPRA")
        combo_buscar.grid(row=0,column=1,pady=15,padx=20,sticky="w")
        self.texto_buscar_var = StringVar()
        texto_buscar = Entry(BD_Frame,textvariable =self.texto_buscar_var,font=("times new roman",10,"bold"),width=20,bd=5,relief=GROOVE)
        texto_buscar.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        #Botones
        buscarboton= Button(BD_Frame,text="Buscar",width=10,pady=5,command=self.buscar_proveedor).grid(row=0,column=3,padx=10,pady=10)
        mostrarboton = Button(BD_Frame,text="Listar",width=8,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #===========Tabla de registros ======= 
        Table_Frame = Frame(BD_Frame,bd=4,relief=RIDGE,bg="yellow")
        Table_Frame.place(x=10,y=70,width=740,height=550)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Proveedor_table = ttk.Treeview(Table_Frame,column=("ID_PROVEEDOR","NOMBRE","APELLIDO","EMPRESA","RUC","TELEFONO","CORREO","DESCRIPCION"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Proveedor_table.xview)
        scroll_y.config(command=self.Proveedor_table.yview)
        

        self.Proveedor_table.heading("ID_PROVEEDOR",text ="ID_PROVEEDOR")
        # self.Materiaprima_table.heading("CODIGO",text ="CODIGO")
        self.Proveedor_table.heading("NOMBRE",text ="NOMBRE")
        self.Proveedor_table.heading("APELLIDO",text ="APELLIDO")
        self.Proveedor_table.heading("EMPRESA",text ="EMPRESA")
        self.Proveedor_table.heading("RUC",text ="RUC")
        self.Proveedor_table.heading("TELEFONO",text ="TELEFONO")
        self.Proveedor_table.heading("CORREO",text ="CORREO")
        self.Proveedor_table.heading("DESCRIPCION",text ="DESCRIPCION")

        self.Proveedor_table['show'] = 'headings'
        self.Proveedor_table.column("ID_PROVEEDOR",width=100)
        self.Proveedor_table.column("NOMBRE",width=100)
        self.Proveedor_table.column("APELLIDO",width=100)
        self.Proveedor_table.column("EMPRESA",width=100)
        self.Proveedor_table.column("RUC",width=100)
        self.Proveedor_table.column("TELEFONO",width=100)
        self.Proveedor_table.column("CORREO",width=100)
        self.Proveedor_table.column("DESCRIPCION",width=100)
        self.Proveedor_table.pack(fill=BOTH,expand=1)
        self.Proveedor_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.clear()

    def agregar_proveedor(self):
        if self.ID_PROVEEDOR_var.get() == "":
            messagebox.showerror("Error","Todos los campos deben ser llenados")
        else:
            con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
            cur=con.cursor()
            cur.execute("insert into proveedores values (%s,%s,%s,%s,%s,%s,%s,%s)",(self.ID_PROVEEDOR_var.get(),
                                                                                        self.NOMBRE_var.get(),
                                                                                        self.APELLIDO_var.get(),
                                                                                        self.EMPRESA_var.get(),
                                                                                        self.RUC_var.get(),
                                                                                        self.TELEFONO_var.get(),                                             
                                                                                        self.CORREO_var.get(),
                                                                                        self.DESCRIPCION_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Correcto","Se ha realizado el registro con éxito")
    
    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from proveedores")
        rows = cur.fetchall()
        if len(rows) !=0:
            self.Proveedor_table.delete(*self.Proveedor_table.get_children())
            for row in rows:
                self.Proveedor_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def get_cursor(self,ev):
        cursor_row = self.Proveedor_table.focus()
        contents = self.Proveedor_table.item(cursor_row)
        row = contents['values']
        self.ID_PROVEEDOR_var.set(row[0])
        self.NOMBRE_var.set(row[1])
        self.APELLIDO_var.set(row[2])
        self.EMPRESA_var.set(row[3])
        self.RUC_var.set(row[4])
        self.TELEFONO_var.set(row[5])
        self.CORREO_var.set(row[6])
        self.DESCRIPCION_var.set(row[7])
        
                                                              
    
    def actualizar_proveedor(self):

        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur=con.cursor() 
        cur.execute("update proveedores set NOMBRE=%s,APELLIDO=%s,EMPRESA=%s,RUC=%s,TELEFONO=%s,CORREO=%s,DESCRIPCION=%s where ID_PROVEEDOR=%s",(
                                                                                        self.NOMBRE_var(),   
                                                                                        self.APELLIDO_var.get(),
                                                                                        self.EMPRESA_var.get(),
                                                                                        self.RUC_var.get(),
                                                                                        self.TELEFONO_var.get(),                                             
                                                                                        self.CORREO_var.get(),
                                                                                        self.DESCRIPCION_var.get(),
                                                                                        self.ID_PROVEEDOR_var.get()))  
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Correcto","Se ha actualizado el registro con éxito")
    
    def clear(self):
        self.ID_PROVEEDOR_var.set("")
        self.NOMBRE_var.set("")
        self.APELLIDO_var.set(""),
        self.EMPRESA_var.set(""),
        self.RUC_var.set(""),
        self.TELEFONO_var.set(""),
        self.CORREO_var.set(""),
        self.DESCRIPCION_var.set("")                                                                                                                  
    
    def eliminar_proveedor(self):
        con =pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("delete from proveedores where ID_PROVEEDOR=%s",self.ID_PROVEEDOR_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def buscar_proveedor(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from proveedores where " + str(self.buscar_por_var.get()) + " Like '%" + str(self.texto_buscar_var.get())+"%'")
        rows =  cur.fetchall()
        if len(rows) != 0:
            self.Proveedor_table.delete(*self.Proveedor_table.get_children())
            for row in rows:
                self.Proveedor_table.insert('',END,values=row)
            con.commit()
        con.close()
        self.texto_buscar_var.set("")
    

if __name__ == "__main__":
    root = Tk()
    obj = Proveedor(root)
    root.mainloop()
