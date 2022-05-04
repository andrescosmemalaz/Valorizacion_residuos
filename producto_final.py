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


class Costalescompost():
    def __init__(self,root):
        self.root=root
        self.root.title("Sistema Administracion Producto Final")
        icono = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico"
        self.root.iconbitmap(path.abspath(icono))
        self.root.geometry("1300x770+0+0")
        #Imagen
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        title = Label(self.root,text="Sistema Administración Producto Final",bd=12,relief=GROOVE,font=("times new roman",40,"bold"),bg="#008f4c",fg="black")
        title.pack(side=TOP,fill=X)

        #Todas las variables
        self.ID_var = StringVar()
        self.AREA_var = StringVar()
        self.FECHA_var = StringVar()
        self.HORA_ENTRADA_var = StringVar()
        # self.ZONA_var = StringVar()
        self.LOTE_var = StringVar()
        self.PESO_Var = StringVar()
        self.ENCARGADO_var = StringVar()
        self.SOPORTE_Var = StringVar()
        self.buscar_por_var = StringVar()
        self.texto_buscar_var = StringVar()

        #Frame de administracion
        Managment_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="orange")
        Managment_Frame.place(x=20, y=100,width=450,height=645)


        m_title = Label(Managment_Frame,text="Ingresar Registro Producto Final", bg="orange",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_id = Label(Managment_Frame,text="ID",bg="orange",fg="black",font=("times new roman",15,"bold"))
        lbl_id.grid(row=1,column=0, pady=10,padx=20,sticky="w")
        txt_id  =Entry(Managment_Frame,textvariable =self.ID_var,font=("times new roman",15,"bold"))
        txt_id.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_area = Label(Managment_Frame,text="AREA",bg="orange",fg="black",font=("times new roman",15,"bold"))
        lbl_area.grid(row=2,column=0, pady=10,padx=20,sticky="w")
        
        combo_area = ttk.Combobox(Managment_Frame,textvariable =self.AREA_var,font=("times new roman",13,"bold"),state="readonly")
        combo_area['values'] = ('Almacen_PF')
        combo_area.grid(row=2,column=1,pady=10,padx=21,ipady=2)

        lbl_fecha = Label(Managment_Frame,text="FECHA",bg="orange",fg="black",font=("times new roman",15,"bold"))
        lbl_fecha.grid(row=3,column=0, pady=10,padx=20,sticky="w")
        
        txt_fecha=DateEntry(Managment_Frame,textvariable =self.FECHA_var,date_pattern='dd/mm/y',font=("times new roman",15,"bold"),state="readonly")
        txt_fecha.grid(row=3, column=1,padx=10,ipadx=30)
        dt =date(2021,12,2)
        txt_fecha.set_date(dt)
       

        lbl_hora_entrada = Label(Managment_Frame,text="HORA ENTRADA",bg="orange",fg="black",font=("times new roman",15,"bold"))
        lbl_hora_entrada.grid(row=4,column=0, pady=10,padx=20,sticky="w")
        txt_hora_entrada  =Entry(Managment_Frame,textvariable =self.HORA_ENTRADA_var,font=("times new roman",15,"bold"))
        txt_hora_entrada.grid(row=4,column=1,pady=10,padx=20,sticky="w")

    

        lbl_lote = Label(Managment_Frame,text="LOTE",bg="orange",fg="black",font=("times new roman",15,"bold"))
        lbl_lote.grid(row=5,column=0, pady=10,padx=20,sticky="w")
        txt_lote  = Entry(Managment_Frame,textvariable =self.LOTE_var,font=("times new roman",15,"bold"))
        txt_lote.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_peso = Label(Managment_Frame,text="PESO",bg="orange",fg="black",font=("times new roman",15,"bold"))
        lbl_peso.grid(row=6,column=0, pady=10,padx=20,sticky="w")
        txt_peso  = Entry(Managment_Frame,textvariable =self.PESO_Var,font=("times new roman",15,"bold"))
        txt_peso.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_encargado = Label(Managment_Frame,text="ENCARGADO",bg="orange",fg="black",font=("times new roman",15,"bold"))
        lbl_encargado.grid(row=7,column=0, pady=10,padx=20,sticky="w")
        txt_encargado  = Entry(Managment_Frame,textvariable =self.ENCARGADO_var,font=("times new roman",15,"bold"))
        txt_encargado.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        lbl_soporte = Label(Managment_Frame,text="SOPORTE",bg="orange",fg="black",font=("times new roman",15,"bold"))
        lbl_soporte.grid(row=8,column=0, pady=10,padx=20,sticky="w")
        txt_soporte  = Entry(Managment_Frame,textvariable =self.SOPORTE_Var,font=("times new roman",15,"bold"))
        txt_soporte.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        #Botom Frame
        btn_frame = Frame(Managment_Frame,bd=3,relief=RIDGE,bg="black")
        btn_frame.place(x=15,y=510,width=420)

        agregar_botom = Button(btn_frame,text="Agregar",width=10,command=self.agregar_COSTAL).grid(row=0,column=0,padx=10,pady=10)
        actualizar_botom = Button(btn_frame,text="Actualizar",width=10,command=self.actualizar_COSTAL).grid(row=0,column=1,padx=10,pady=10)
        eliminar_botom = Button(btn_frame,text="Eliminar",width=10,command=self.eliminar_COSTAL).grid(row=0,column=2,padx=10,pady=10)
        limpiar_botom = Button(btn_frame,text="Limpiar",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        # Base de Datos Frame 
        BD_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#36d073")
        BD_Frame.place(x=500,y=100,width=770,height=645)

        lbl_buscar = Label(BD_Frame, text="Buscar por",bg="#36d073",fg="white",font=("times new roman",15,"bold"))
        lbl_buscar.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        #Combobox   
        combo_buscar = ttk.Combobox(BD_Frame,textvariable =self.buscar_por_var,font=("times new roman",13,"bold"),state="readonly")
        combo_buscar['values'] = ("FECHA","LOTE")
        combo_buscar.grid(row=0,column=1,pady=15,padx=20,sticky="w")
        texto_buscar = Entry(BD_Frame,textvariable =self.texto_buscar_var,font=("times new roman",10,"bold"),width=20,bd=5,relief=GROOVE)
        texto_buscar.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        #Botones
        buscarboton= Button(BD_Frame,text="Buscar",width=10,pady=5,command=self.buscar_COSTAL).grid(row=0,column=3,padx=10,pady=10)
        mostrarboton = Button(BD_Frame,text="Listar",width=8,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #===========Tabla de registros ======= 
        Table_Frame = Frame(BD_Frame,bd=4,relief=RIDGE,bg="yellow")
        Table_Frame.place(x=10,y=70,width=740,height=550)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Productofinal_table = ttk.Treeview(Table_Frame,column=("ID","AREA","FECHA","HORA_ENTRADA","LOTE","PESO","ENCARGADO","SOPORTE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Productofinal_table.xview)
        scroll_y.config(command=self.Productofinal_table.yview)
        

        self.Productofinal_table.heading("ID",text ="ID")
        # self.Materiaprima_table.heading("CODIGO",text ="CODIGO")
        self.Productofinal_table.heading("AREA",text ="AREA")
        self.Productofinal_table.heading("FECHA",text ="FECHA")
        self.Productofinal_table.heading("HORA_ENTRADA",text ="HORA_ENTRADA")
        # self.Productofinal_table.heading("ZONA",text ="ZONA")
        self.Productofinal_table.heading("LOTE",text ="LOTE")
        self.Productofinal_table.heading("PESO",text ="PESO")
        self.Productofinal_table.heading("ENCARGADO",text ="ENCARGADO")
        self.Productofinal_table.heading("SOPORTE",text ="SOPORTE")

        self.Productofinal_table['show'] = 'headings'
        self.Productofinal_table.column("ID",width=100)
        # self.Materiaprima_table.column("CODIGO",width=100)
        self.Productofinal_table.column("AREA",width=100)
        self.Productofinal_table.column("FECHA",width=100)
        self.Productofinal_table.column("HORA_ENTRADA",width=100)
        # self.Productofinal_table.column("ZONA",width=100)
        self.Productofinal_table.column("LOTE",width=100)
        self.Productofinal_table.column("PESO",width=100)
        self.Productofinal_table.column("ENCARGADO",width=100)
        self.Productofinal_table.column("SOPORTE",width=100)

        self.Productofinal_table.pack(fill=BOTH,expand=1)
        self.Productofinal_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.clear()

    def agregar_COSTAL(self):
        try:
                if self.ID_var.get() == "" or self.PESO_Var.get() == "":
                    messagebox.showerror("Error","Todos los campos deben ser llenados")
                else:
                    con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
                    cur=con.cursor()
                    cur.execute("insert into producto_final values (%s,%s,%s,%s,%s,%s,%s,%s)",(self.ID_var.get(),
                                                                                                self.AREA_var.get(),
                                                                                                self.FECHA_var.get(),
                                                                                                self.HORA_ENTRADA_var.get(),
                                                                                                self.LOTE_var.get(),
                                                                                                self.PESO_Var.get(),
                                                                                                self.ENCARGADO_var.get(),
                                                                                                self.SOPORTE_Var.get()))  
                    con.commit()
                    self.fetch_data()
                    self.clear()
                    con.close()
                    messagebox.showinfo("Correcto","Se ha realizado el registro con éxito")
        except pymysql.err.IntegrityError:
            messagebox.showerror("Error","El ID  ya existe , ingresé otro por favor")
            self.clear()
    
    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from producto_final")
        rows = cur.fetchall()
        if len(rows) !=0:
            self.Productofinal_table.delete(*self.Productofinal_table.get_children())
            for row in rows:
                self.Productofinal_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def get_cursor(self,ev):
        cursor_row = self.Productofinal_table.focus()
        contents = self.Productofinal_table.item(cursor_row)
        row = contents['values']
        self.ID_var.set(row[0])
        self.AREA_var.set(row[1])
        self.FECHA_var.set(row[2])
        self.HORA_ENTRADA_var.set(row[3])
        self.LOTE_var.set(row[4])
        self.PESO_Var.set(row[5])
        self.ENCARGADO_var.set(row[6])
        self.SOPORTE_Var.set(row[7])
    
    def actualizar_COSTAL(self):
        try:
                con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
                cur=con.cursor()
                cur.execute("update producto_final set AREA=%s,FECHA=%s,HORA_ENTRADA=%s,LOTE=%s,PESO=%s,ENCARGADO=%s,SOPORTE=%s where ID=%s",(

                                                                                                self.AREA_var.get(),
                                                                                                self.FECHA_var.get(),
                                                                                                self.HORA_ENTRADA_var.get(),
                                                                                                self.LOTE_var.get(),
                                                                                                self.PESO_Var.get(),
                                                                                                self.ENCARGADO_var.get(),
                                                                                                self.SOPORTE_Var.get(),
                                                                                                self.ID_var.get()))  
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Correcto","Se ha actualizado el registro con éxito")
        except IndexError:
            messagebox.showerror("Error","El ID  no  existe , ingresé el correcto otro por favor")
            self.clear()   

    
    def clear(self):
        self.ID_var.set("")
        self.AREA_var.set("")
        self.FECHA_var.set("")
        self.HORA_ENTRADA_var.set("")
        self.LOTE_var.set("")
        self.PESO_Var.set("")
        self.ENCARGADO_var.set("")
        self.SOPORTE_Var.set("")
    
    def eliminar_COSTAL(self):
        con =pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("delete from producto_final where ID=%s",self.ID_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def buscar_COSTAL(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from producto_final where " + str(self.buscar_por_var.get()) + " Like '%" + str(self.texto_buscar_var.get())+"%'")
        rows =  cur.fetchall()
        if len(rows) != 0:
            self.Productofinal_table.delete(*self.Productofinal_table.get_children())
            for row in rows:
                self.Productofinal_table.insert('',END,values=row)
            con.commit()
        con.close()
        self.texto_buscar_var.set("")

if __name__ == '__main__':
    root = Tk()
    obj = Costalescompost(root)
    root.mainloop()
















