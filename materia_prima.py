import pymysql
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkcalendar import DateEntry 
from datetime import date
import os 
from os import path
from PIL import  Image,ImageTk
 


class Materiaprima():
    def __init__(self,root):
        self.root=root
        self.root.title("Sistema Administracion Materia Prima")
        icono = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico"
        self.root.iconbitmap(path.abspath(icono))
        self.root.geometry("1300x770+0+0")
        #Imagen
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        
        title = Label(self.root,text="Sistema Administración Materia Prima",bd=12,relief=GROOVE,font=("times new roman",40,"bold"),fg="black")
        title.pack(side=TOP,fill=X)

        #Frame de administracion
        Managment_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#D4E1E7")
        Managment_Frame.place(x=20, y=100,width=450,height=645)


        m_title = Label(Managment_Frame,text="Ingresar Materia prima", bg="#D4E1E7",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_id = Label(Managment_Frame,text="ID",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_id.grid(row=1,column=0, pady=10,padx=20,sticky="w")
        self.ID_var = StringVar()
        txt_id  =Entry(Managment_Frame,textvariable =self.ID_var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_id.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_area = Label(Managment_Frame,text="AREA",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_area.grid(row=2,column=0, pady=10,padx=20,sticky="w")
        # txt_area  =Entry(Managment_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        # txt_area.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        #Combobox
        self.AREA_var = StringVar()
        combo_area = ttk.Combobox(Managment_Frame,textvariable =self.AREA_var,font=("times new roman",13,"bold"),state="readonly")
        combo_area['values'] = ('Recepción_MP')
        combo_area.grid(row=2,column=1,pady=10,padx=21,ipady=2)
        

        lbl_fecha = Label(Managment_Frame,text="FECHA",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_fecha.grid(row=3,column=0, pady=10,padx=20,sticky="w")
        # txt_fecha  =Entry(Managment_Frame,textvariable =self.FECHA_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        # txt_fecha.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        self.FECHA_var = StringVar()
        txt_fecha=DateEntry(Managment_Frame,textvariable =self.FECHA_var,date_pattern='d/mm/y',font=("times new roman",15,"bold"),state="readonly")
        txt_fecha.grid(row=3, column=1,padx=10,ipadx=30)
        dt =date(2021,12,2)
        txt_fecha.set_date(dt)
        # my_w.mainloop()
        
        self.HORA_ENTRADA_var = StringVar()
        lbl_hora_entrada = Label(Managment_Frame,text="HORA ENTRADA",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_hora_entrada.grid(row=4,column=0, pady=10,padx=20,sticky="w")
        txt_hora_entrada  =Entry(Managment_Frame,textvariable =self.HORA_ENTRADA_var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_hora_entrada.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        

        self.ZONA_var = StringVar()
        lbl_zona = Label(Managment_Frame,text="ZONA",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_zona.grid(row=5,column=0, pady=10,padx=20,sticky="w")
        # txt_zona  = Entry(Managment_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        # txt_zona.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        combo_zona = ttk.Combobox(Managment_Frame,textvariable =self.ZONA_var,font=("times new roman",13,"bold"),state="readonly")
        combo_zona['values'] = ('Zona 1','Zona 2','Zona 3','Zona 4','Zona 5')
        combo_zona.grid(row=5,column=1,pady=15,padx=21,ipady=2,sticky="w")
        

        lbl_lote = Label(Managment_Frame,text="LOTE",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_lote.grid(row=6,column=0, pady=10,padx=20,sticky="w")
        self.LOTE_var = StringVar()
        txt_lote  = Entry(Managment_Frame,textvariable =self.LOTE_var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_lote.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_peso = Label(Managment_Frame,text="PESO",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_peso.grid(row=7,column=0, pady=10,padx=20,sticky="w")
        self.PESO_Var = DoubleVar()
        txt_peso  = Entry(Managment_Frame,textvariable =self.PESO_Var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_peso.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        lbl_encargado = Label(Managment_Frame,text="ENCARGADO",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_encargado.grid(row=8,column=0, pady=10,padx=20,sticky="w")
        self.ENCARGADO_var = StringVar()
        txt_encargado  = Entry(Managment_Frame,textvariable =self.ENCARGADO_var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_encargado.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        lbl_soporte = Label(Managment_Frame,text="SOPORTE",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_soporte.grid(row=9,column=0, pady=10,padx=20,sticky="w")
        self.SOPORTE_Var = StringVar()
        txt_soporte  = Entry(Managment_Frame,textvariable =self.SOPORTE_Var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_soporte.grid(row=9,column=1,pady=10,padx=20,sticky="w")

        #Botom Frame
        btn_frame = Frame(Managment_Frame,bd=3,relief=RIDGE)
        btn_frame.place(x=15,y=575,width=420)

        agregar_botom = Button(btn_frame,text="Agregar",width=10,bg="#ffff7a",command=self.agregar_MP).grid(row=0,column=0,padx=10,pady=10)
        actualizar_botom = Button(btn_frame,text="Actualizar",width=10,bg="#ffff7a",command=self.actualizarMP).grid(row=0,column=1,padx=10,pady=10)
        eliminar_botom = Button(btn_frame,text="Eliminar",width=10,bg="#ffff7a",command=self.eliminarMP).grid(row=0,column=2,padx=10,pady=10)
        limpiar_botom = Button(btn_frame,text="Limpiar",width=10,bg="#ffff7a",command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        # Base de Datos Frame 
        BD_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#D4E1E7")
        BD_Frame.place(x=500,y=100,width=770,height=645)

        lbl_buscar = Label(BD_Frame, text="Buscar por",bg="#D4E1E7",fg="white",font=("times new roman",15,"bold"))
        lbl_buscar.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        self.buscar_por_var = StringVar()
        #Combobox
        combo_buscar = ttk.Combobox(BD_Frame,textvariable =self.buscar_por_var,font=("times new roman",13,"bold"),state="readonly")
        combo_buscar['values'] = ("FECHA","ZONA")
        self.texto_buscar_var = StringVar()
        combo_buscar.grid(row=0,column=1,pady=15,padx=20,sticky="w")
        texto_buscar = Entry(BD_Frame,textvariable =self.texto_buscar_var,bg="#ffff7a",font=("times new roman",10,"bold"),width=20,bd=5,relief=GROOVE)
        texto_buscar.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        #Botones
        buscarboton= Button(BD_Frame,text="Buscar",bg = "#ffff7a",width=10,pady=5,command=self.buscarMP).grid(row=0,column=3,padx=10,pady=10)
        mostrarboton = Button(BD_Frame,text="Listar",bg = "#ffff7a",width=8,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #===========Tabla de registros ======= 
        Table_Frame = Frame(BD_Frame,bd=4,relief=RIDGE)
        Table_Frame.place(x=10,y=70,width=740,height=550)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Materiaprima_table = ttk.Treeview(Table_Frame,column=("ID","AREA","FECHA","HORA_ENTRADA","ZONA","LOTE","PESO","ENCARGADO","SOPORTE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Materiaprima_table.xview)
        scroll_y.config(command=self.Materiaprima_table.yview)
        

        self.Materiaprima_table.heading("ID",text ="ID")
        self.Materiaprima_table.heading("AREA",text ="AREA")
        self.Materiaprima_table.heading("FECHA",text ="FECHA")
        self.Materiaprima_table.heading("HORA_ENTRADA",text ="HORA_ENTRADA")
        self.Materiaprima_table.heading("ZONA",text ="ZONA")
        self.Materiaprima_table.heading("LOTE",text ="LOTE")
        self.Materiaprima_table.heading("PESO",text ="PESO")
        self.Materiaprima_table.heading("ENCARGADO",text ="ENCARGADO")
        self.Materiaprima_table.heading("SOPORTE",text ="SOPORTE")

        self.Materiaprima_table['show'] = 'headings'
        self.Materiaprima_table.column("ID",width=100)
        # self.Materiaprima_table.column("CODIGO",width=100)
        self.Materiaprima_table.column("AREA",width=100)
        self.Materiaprima_table.column("FECHA",width=100)
        self.Materiaprima_table.column("HORA_ENTRADA",width=100)
        self.Materiaprima_table.column("ZONA",width=100)
        self.Materiaprima_table.column("LOTE",width=100)
        self.Materiaprima_table.column("PESO",width=100)
        self.Materiaprima_table.column("ENCARGADO",width=100)
        self.Materiaprima_table.column("SOPORTE",width=100)

        self.Materiaprima_table.pack(fill=BOTH,expand=1)
        self.Materiaprima_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.clear()

    def agregar_MP(self):
        try:
                if self.ID_var.get() == "" or self.PESO_Var.get() == "":
                    messagebox.showerror("Error","Todos los campos deben ser llenados")
                else:
                    con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
                    cur=con.cursor()
                    cur.execute("insert into materia_prima values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ID_var.get(),
                                                                                                self.AREA_var.get(),
                                                                                                self.FECHA_var.get(),
                                                                                                self.HORA_ENTRADA_var.get(),
                                                                                                self.ZONA_var.get(),
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
        cur.execute("select * from materia_prima")
        rows = cur.fetchall()
        if len(rows) !=0:
            self.Materiaprima_table.delete(*self.Materiaprima_table.get_children())
            for row in rows:
                self.Materiaprima_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def get_cursor(self,ev):
        cursor_row = self.Materiaprima_table.focus()
        contents = self.Materiaprima_table.item(cursor_row)
        row = contents['values']
        self.ID_var.set(row[0])
        self.AREA_var.set(row[1])
        self.FECHA_var.set(row[2])
        self.HORA_ENTRADA_var.set(row[3])
        self.ZONA_var.set(row[4])
        self.LOTE_var.set(row[5])
        self.PESO_Var.set(row[6])
        self.ENCARGADO_var.set(row[7])
        self.SOPORTE_Var.set(row[8])
    
    def actualizarMP(self):

        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur=con.cursor()
        cur.execute("update materia_prima set AREA=%s,FECHA=%s,HORA_ENTRADA=%s,ZONA=%s,LOTE=%s,PESO=%s,ENCARGADO=%s,SOPORTE=%s where ID=%s",(

                                                                                    self.AREA_var.get(),
                                                                                    self.FECHA_var.get(),
                                                                                    self.HORA_ENTRADA_var.get(),
                                                                                    self.ZONA_var.get(),
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
    
    def clear(self):
        self.ID_var.set("")
        self.AREA_var.set("")
        self.FECHA_var.set("")
        self.HORA_ENTRADA_var.set("")
        self.ZONA_var.set("")
        self.LOTE_var.set("")
        self.PESO_Var.set("")
        self.ENCARGADO_var.set("")
        self.SOPORTE_Var.set("")
    
    def eliminarMP(self):
        con =pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("delete from materia_prima where ID=%s",self.ID_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def buscarMP(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from materia_prima where " + str(self.buscar_por_var.get()) + " Like '%" + str(self.texto_buscar_var.get())+"%'")
        rows =  cur.fetchall()
        if len(rows) != 0:
            self.Materiaprima_table.delete(*self.Materiaprima_table.get_children())
            for row in rows:
                self.Materiaprima_table.insert('',END,values=row)
            con.commit()
        con.close()
        self.texto_buscar_var.set("")


if __name__ == "__main__":
        root = Tk()
        obj = Materiaprima(root)
        root.mainloop()

