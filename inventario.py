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

class Inventario():
    def __init__(self,root):
        self.root=root
        self.root.title("Sistema Administracion de Almacen")
        icono = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico"
        self.root.iconbitmap(path.abspath(icono))
        #self.root.iconbitmap("F:\\andres\\Ciclo 10\\Topicos\\Trabajo Grupal\\Trabajo Grupal-Software Municpal\\miproject\\Caja negra\\project\\logo_castillo_grande.ico")
        self.root.geometry("1300x770+0+0")
        
         #Imagen
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        
        title = Label(self.root,text="Sistema Administración de Almacen",bd=12,relief=GROOVE,font=("times new roman",40,"bold"))
        title.pack(side=TOP,fill=X)

        #Todas las variables
        self.ID_INV_var = StringVar()
        self.ID_COMPRA_var = StringVar()
        self.AREA_var = StringVar()
        self.TIPO_RECURSO_var = StringVar()
        self.NOMBRE_RECURSO_var = StringVar()
        self.UNIDAD_var = StringVar()
        self.CANTIDAD_var = IntVar()
        self.DESCRIPCION_var = StringVar()
        self.buscar_por_var = StringVar()
        self.texto_buscar_var = StringVar()

        #Frame de administracion
        Managment_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#D4E1E7")
        Managment_Frame.place(x=20, y=100,width=450,height=605)


        m_title = Label(Managment_Frame,text="Registrar Inventario", bg="#D4E1E7",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_id_inv = Label(Managment_Frame,text="ID",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_id_inv.grid(row=1,column=0, pady=10,padx=20,sticky="w")
        txt_id_inv  =Entry(Managment_Frame,textvariable =self.ID_INV_var,font=("times new roman",12,"bold"))
        txt_id_inv.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lbl_id_compra = Label(Managment_Frame,text="ID_COMPRA",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_id_compra.grid(row=2,column=0, pady=10,padx=20,sticky="w")
        txt_id_compra  =Entry(Managment_Frame,textvariable =self.ID_COMPRA_var,font=("times new roman",12,"bold"))
        txt_id_compra.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_AREA = Label(Managment_Frame,text="ESTADO",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_AREA.grid(row=3,column=0, pady=10,padx=20,sticky="w")
        #Combobox
        combo_AREA = ttk.Combobox(Managment_Frame,textvariable =self.AREA_var,font=("times new roman",10,"bold"),state="readonly")
        combo_AREA['values'] = ('Recepción_MP','PRODUCCION','Almacen_PF')
        combo_AREA.grid(row=3,column=1,pady=14,padx=10,ipady=2,ipadx=2)
        
        lbl_T_RECURSO = Label(Managment_Frame,text="TIPO DE RECURSO",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_T_RECURSO.grid(row=4,column=0, pady=10,padx=20,sticky="w")
        #Combobox
        combo_T_RECURSO = ttk.Combobox(Managment_Frame,textvariable =self.TIPO_RECURSO_var,font=("times new roman",10,"bold"),state="readonly")
        combo_T_RECURSO['values'] = ('INSUMO','MATERIAL','MAQUINA','OTROS')
        combo_T_RECURSO.grid(row=4,column=1,pady=14,padx=10,ipady=2,ipadx=2)
        
        lbl_NOMBRE_RECURSO = Label(Managment_Frame,text="NOMBRE DE RECURSO",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_NOMBRE_RECURSO.grid(row=5,column=0, pady=10,padx=20,sticky="w")
        txt_NOMBRE_RECURSO=Entry(Managment_Frame,textvariable =self.NOMBRE_RECURSO_var,font=("times new roman",12,"bold"))
        txt_NOMBRE_RECURSO.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        
        lbl_UNIDAD = Label(Managment_Frame,text="CANTIDAD",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_UNIDAD.grid(row=6,column=0, pady=10,padx=20,sticky="w")
        combo_UNIDAD = ttk.Combobox(Managment_Frame,textvariable =self.UNIDAD_var,font=("times new roman",10,"bold"),state="readonly")
        combo_UNIDAD['values'] = (['NO APLICA'],'GRAMOS','KG','METROS','LITROS')
        combo_UNIDAD.grid(row=6,column=1,pady=14,padx=10,ipady=2,ipadx=2)
        
        lbl_CANTIDAD = Label(Managment_Frame,text="CANTIDAD",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_CANTIDAD.grid(row=7,column=0, pady=10,padx=20,sticky="w")
        txt_CANTIDAD  =Entry(Managment_Frame,textvariable =self.CANTIDAD_var,font=("times new roman",12,"bold"))
        txt_CANTIDAD.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        lbl_DESCRIPCION = Label(Managment_Frame,text="DESCRIPCION",bg="#D4E1E7",fg="black",font=("times new roman",12,"bold"))
        lbl_DESCRIPCION.grid(row=8,column=0, pady=10,padx=20,sticky="w")
        txt_DESCRIPCION  =Entry(Managment_Frame,textvariable =self.DESCRIPCION_var,font=("times new roman",12,"bold"))
        txt_DESCRIPCION.grid(row=8,column=1,pady=10,padx=20,sticky="w")
        
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
        combo_buscar['values'] = ("TIPO_RECURSO","AREA","ID_INV")
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

        self.Inventario_table = ttk.Treeview(Table_Frame,column=("ID_INV","ID_COMPRA","AREA","TIPO_RECURSO","NOMBRE_RECURSO","UNIDAD","CANTIDAD","DESCRIPCION"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Inventario_table.xview)
        scroll_y.config(command=self.Inventario_table.yview)
        

        self.Inventario_table.heading("ID_INV",text ="ID_INV")
        # self.Materiaprima_table.heading("CODIGO",text ="CODIGO")
        self.Inventario_table.heading("ID_COMPRA",text ="ID_COMPRA")
        self.Inventario_table.heading("AREA",text ="AREA")
        self.Inventario_table.heading("TIPO_RECURSO",text ="TIPO_RECURSO")
        self.Inventario_table.heading("NOMBRE_RECURSO",text ="NOMBRE_RECURSO")
        self.Inventario_table.heading("UNIDAD",text ="UNIDAD")
        self.Inventario_table.heading("CANTIDAD",text ="CANTIDAD")
        self.Inventario_table.heading("DESCRIPCION",text ="DESCRIPCION")
        

        self.Inventario_table['show'] = 'headings'
        self.Inventario_table.column("ID_INV",width=100)
        self.Inventario_table.column("ID_COMPRA",width=100)
        self.Inventario_table.column("AREA",width=100)
        self.Inventario_table.column("TIPO_RECURSO",width=100)
        self.Inventario_table.column("NOMBRE_RECURSO",width=100)
        self.Inventario_table.column("UNIDAD",width=100)
        self.Inventario_table.column("CANTIDAD",width=100)
        self.Inventario_table.column("DESCRIPCION",width=100)
        
        
        

        self.Inventario_table.pack(fill=BOTH,expand=1)
        self.Inventario_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.clear()
    
    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from inventario")
        rows = cur.fetchall()
        if len(rows) !=0:
            self.Inventario_table.delete(*self.Inventario_table.get_children())
            for row in rows:
                self.Inventario_table.insert('',END,values=row)
            con.commit()
        con.close()

    def get_cursor(self,ev):
        cursor_row = self.Inventario_table.focus()
        contents = self.Inventario_table.item(cursor_row)
        row = contents['values']
        self.ID_INV_var.set(row[0])
        self.ID_COMPRA_var.set(row[1])
        self.AREA_var.set(row[2])
        self.TIPO_RECURSO_var.set(row[3])
        self.NOMBRE_RECURSO_var.set(row[4])
        self.UNIDAD_var.set(row[5])
        self.CANTIDAD_var.set(row[6])
        self.DESCRIPCION_var.set(row[7])


    def agregar_VENTA(self):
        try:
                if self.ID_INV_var.get() == "":
                    messagebox.showerror("Error","Todos los campos deben ser llenados")
                else:
                    con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
                    cur=con.cursor()
                    cur.execute("insert into inventario values (%s,%s,%s,%s,%s,%s,%s,%s)",(self.ID_INV_var.get(),
                                                                                                self.ID_COMPRA_var.get(),
                                                                                                self.AREA_var.get(),
                                                                                                self.TIPO_RECURSO_var.get(),
                                                                                                self.NOMBRE_RECURSO_var.get(),
                                                                                                self.UNIDAD_var.get(),                                             
                                                                                                self.CANTIDAD_var.get(),
                                                                                                self.DESCRIPCION_var.get()
                                                                                                ))
                    con.commit()
                    self.fetch_data()
                    self.clear()
                    con.close()
                    messagebox.showinfo("Correcto","Se ha realizado el registro con éxito")
        except pymysql.err.IntegrityError:
            messagebox.showerror("Error","El ID  ya existe , ingresé otro por favor")
            self.clear()
                                     
    def actualizar_VENTA(self):

        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur=con.cursor() 
        cur.execute("update inventario set ID_COMPRA=%s,AREA=%s,TIPO_RECURSO=%s,NOMBRE_RECURSO=%s,UNIDAD=%s,CANTIDAD=%s,DESCRIPCION=%s where ID_INV=%s",(
                                                                                        self.ID_COMPRA_var.get(),   
                                                                                        self.AREA_var.get(),
                                                                                        self.TIPO_RECURSO_var.get(),
                                                                                        self.NOMBRE_RECURSO_var.get(),
                                                                                        self.UNIDAD_var.get(),                                             
                                                                                        self.CANTIDAD_var.get(),
                                                                                        self.DESCRIPCION_var.get(),
                                                                                        self.ID_INV_var.get()))  
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Correcto","Se ha actualizado el registro con éxito")
    
    def clear(self):
        self.ID_INV_var.set("")
        self.ID_COMPRA_var.set("")
        self.AREA_var.set(""),
        self.TIPO_RECURSO_var.set(""),
        self.NOMBRE_RECURSO_var.set(""),
        self.UNIDAD_var.set(""),
        self.CANTIDAD_var.set(""),
        self.DESCRIPCION_var.set("")                                                                                                                     
    
    def eliminar_VENTA(self):
        con =pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("delete from inventario where ID_INV=%s",self.ID_INV_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def buscar_VENTA(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from inventario where " + str(self.buscar_por_var.get()) + " Like '%" + str(self.texto_buscar_var.get())+"%'")
        rows =  cur.fetchall()
        if len(rows) != 0:
            self.Inventario_table.delete(*self.Inventario_table.get_children())
            for row in rows:
                self.Inventario_table.insert('',END,values=row)
            con.commit()
        con.close()
        self.texto_buscar_var.set("")
    

if __name__ == "__main__":
    root = Tk()
    obj = Inventario(root)
    root.mainloop()
