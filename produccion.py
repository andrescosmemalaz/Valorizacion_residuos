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


class Productoenproceso():
    def __init__(self,root):
        self.root=root
        self.root.title("Sistema Administracion Produccion Compost")
        icono = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico"
        self.root.iconbitmap(path.abspath(icono))
        self.root.geometry("1300x770+0+0")
    
        #Imagen
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        title = Label(self.root,text="Sistema Administración Producción Compost",bd=12,relief=GROOVE,font=("times new roman",40,"bold"),fg="black")
        title.pack(side=TOP,fill=X)

        #Todas las variables
        self.ID_var = StringVar()
        self.AREA_var = StringVar()
        self.FECHA_var = StringVar()
        self.HORA_ENTRADA_var = StringVar()
        self.NRO_CAMA_var = StringVar()
        self.LOTE_var = StringVar()
        self.PESO_Var = DoubleVar()
        self.CANT_MICROORGANISMO_var = DoubleVar()
        self.TEMPERATURA_var = IntVar()
        self.ENCARGADO_var = StringVar()
        # self.SOPORTE_Var = StringVar()
        self.buscar_por_var = StringVar()
        self.texto_buscar_var = StringVar()

        #Frame de administracion
        Managment_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#D4E1E7")
        Managment_Frame.place(x=20, y=100,width=450,height=645)


        m_title = Label(Managment_Frame,text="Ingresar Registro Producción",bg="#D4E1E7",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_id = Label(Managment_Frame,text="ID",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_id.grid(row=1,column=0, pady=10,padx=20,sticky="w")
        txt_id  =Entry(Managment_Frame,textvariable =self.ID_var,bg = "#ffff7a",font=("times new roman",15,"bold"))
        txt_id.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_area = Label(Managment_Frame,text="AREA",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_area.grid(row=2,column=0, pady=10,padx=20,sticky="w")
        # txt_area  =Entry(Managment_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        # txt_area.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        #Combobox
        combo_area = ttk.Combobox(Managment_Frame,textvariable =self.AREA_var,font=("times new roman",13,"bold"),state="readonly")
        combo_area['values'] = ('Producción')
        combo_area.grid(row=2,column=1,pady=10,padx=21,ipady=2)


        lbl_fecha = Label(Managment_Frame,text="FECHA",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_fecha.grid(row=3,column=0, pady=10,padx=20,sticky="w")
        # txt_fecha  =Entry(Managment_Frame,textvariable =self.FECHA_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        # txt_fecha.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        txt_fecha=DateEntry(Managment_Frame,textvariable =self.FECHA_var,date_pattern='dd/mm/y',font=("times new roman",15,"bold"),state="readonly")
        txt_fecha.grid(row=3, column=1,padx=10,ipadx=30)
        dt =date(2021,12,2)
        txt_fecha.set_date(dt)
        # my_w.mainloop()

        lbl_hora_entrada = Label(Managment_Frame,text="HORA ENTRADA",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_hora_entrada.grid(row=4,column=0, pady=10,padx=20,sticky="w")
        txt_hora_entrada  =Entry(Managment_Frame,textvariable =self.HORA_ENTRADA_var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_hora_entrada.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        combostyle = ttk.Style()
        lbl_nro_cama = Label(Managment_Frame,text="NRO_CAMA",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_nro_cama.grid(row=5,column=0, pady=10,padx=20,sticky="w")
        # txt_zona  = Entry(Managment_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        # txt_zona.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        combo_nro_cama = ttk.Combobox(Managment_Frame,textvariable =self.NRO_CAMA_var,font=("times new roman",13,"bold"),state="readonly")
        combo_nro_cama['values'] = ('Cama 1','Cama 2','Cama 3','Cama 4','Cama 5','Cama 6','Cama 7','Cama 8','Cama 9')
        combo_nro_cama.grid(row=5,column=1,pady=15,padx=21,ipady=2,sticky="w")

        lbl_lote = Label(Managment_Frame,text="LOTE",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_lote.grid(row=6,column=0, pady=10,padx=20,sticky="w")
        txt_lote  = Entry(Managment_Frame,textvariable =self.LOTE_var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_lote.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_peso = Label(Managment_Frame,text="PESO",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_peso.grid(row=7,column=0, pady=10,padx=20,sticky="w")
        txt_peso  = Entry(Managment_Frame,textvariable =self.PESO_Var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_peso.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        lbl_cant_microorganismo = Label(Managment_Frame,text="CANT. MICROORGANISMO",bg="#D4E1E7",fg="black",font=("times new roman",10,"bold"))
        lbl_cant_microorganismo.grid(row=8,column=0, pady=10,padx=20,sticky="w")
        txt_cant_microorganismo  = Entry(Managment_Frame,textvariable =self.CANT_MICROORGANISMO_var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_cant_microorganismo.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        lbl_temperatura = Label(Managment_Frame,text="TEMPERATURA",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_temperatura.grid(row=9,column=0, pady=10,padx=20,sticky="w")
        txt_temperatura  = Entry(Managment_Frame,textvariable =self.TEMPERATURA_var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_temperatura.grid(row=9,column=1,pady=10,padx=20,sticky="w")

        lbl_encargado = Label(Managment_Frame,text="ENCARGADO",bg="#D4E1E7",fg="black",font=("times new roman",15,"bold"))
        lbl_encargado.grid(row=10,column=0, pady=10,padx=20,sticky="w")
        txt_encargado  = Entry(Managment_Frame,textvariable =self.ENCARGADO_var,bg="#ffff7a",font=("times new roman",15,"bold"))
        txt_encargado.grid(row=10,column=1,pady=10,padx=20,sticky="w")


        #Botom Frame
        btn_frame = Frame(Managment_Frame,bd=3,relief=RIDGE,bg="white")
        btn_frame.place(x=15,y=575,width=420)

        agregar_botom = Button(btn_frame,text="Agregar",bg = "#ffff7a",width=10,command=self.agregar_CT).grid(row=0,column=0,padx=10,pady=10)
        actualizar_botom = Button(btn_frame,text="Actualizar",bg = "#ffff7a",width=10,command=self.actualizarCT).grid(row=0,column=1,padx=10,pady=10)
        eliminar_botom = Button(btn_frame,text="Eliminar",bg = "#ffff7a",width=10,command=self.eliminarCT).grid(row=0,column=2,padx=10,pady=10)
        limpiar_botom = Button(btn_frame,text="Limpiar",bg = "#ffff7a",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        # Base de Datos Frame 
        BD_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#D4E1E7")
        BD_Frame.place(x=500,y=100,width=770,height=645)

        lbl_buscar = Label(BD_Frame, text="Buscar por",fg="black",bg="#D4E1E7",font=("times new roman",15,"bold"))
        lbl_buscar.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        #Combobox
        combo_buscar = ttk.Combobox(BD_Frame,textvariable =self.buscar_por_var,font=("times new roman",13,"bold"),state="readonly")
        combo_buscar['values'] = ("FECHA","NRO_CAMA")
        combo_buscar.grid(row=0,column=1,pady=15,padx=20,sticky="w")
        texto_buscar = Entry(BD_Frame,textvariable =self.texto_buscar_var,font=("times new roman",10,"bold"),width=20,bd=5,relief=GROOVE)
        texto_buscar.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        #Botones
        buscarboton= Button(BD_Frame,text="Buscar",bg = "#ffff7a",width=10,pady=5,command=self.buscarCT).grid(row=0,column=3,padx=10,pady=10)
        mostrarboton = Button(BD_Frame,text="Listar",bg = "#ffff7a",width=8,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #===========Tabla de registros ======= 
        Table_Frame = Frame(BD_Frame,bd=4,relief=RIDGE)
        Table_Frame.place(x=10,y=70,width=740,height=550)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Produccion_table = ttk.Treeview(Table_Frame,column=("ID","AREA","FECHA","HORA_ENTRADA","NRO_CAMA","LOTE","PESO","CANT_MICROORGANISMO","TEMPERATURA","ENCARGADO"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Produccion_table.xview)
        scroll_y.config(command=self.Produccion_table.yview)
        

        self.Produccion_table.heading("ID",text ="ID")
        # self.Materiaprima_table.heading("CODIGO",text ="CODIGO")
        self.Produccion_table.heading("AREA",text ="AREA")
        self.Produccion_table.heading("FECHA",text ="FECHA")
        self.Produccion_table.heading("HORA_ENTRADA",text ="HORA_ENTRADA")
        self.Produccion_table.heading("NRO_CAMA",text ="NRO_CAMA")
        self.Produccion_table.heading("LOTE",text ="LOTE")
        self.Produccion_table.heading("PESO",text ="PESO")
        self.Produccion_table.heading("CANT_MICROORGANISMO",text ="CANT_MICROORGANISMO")
        self.Produccion_table.heading("TEMPERATURA",text ="TEMPERATURA")
        self.Produccion_table.heading("ENCARGADO",text ="ENCARGADO")

        self.Produccion_table['show'] = 'headings'
        self.Produccion_table.column("ID",width=100)
        # self.Materiaprima_table.column("CODIGO",width=100)
        self.Produccion_table.column("AREA",width=100)
        self.Produccion_table.column("FECHA",width=100)
        self.Produccion_table.column("HORA_ENTRADA",width=100)
        self.Produccion_table.column("NRO_CAMA",width=100)
        self.Produccion_table.column("LOTE",width=100)
        self.Produccion_table.column("PESO",width=100)
        self.Produccion_table.column("CANT_MICROORGANISMO",width=100)
        self.Produccion_table.column("TEMPERATURA",width=100)
        self.Produccion_table.column("ENCARGADO",width=100)

        self.Produccion_table.pack(fill=BOTH,expand=1)
        self.Produccion_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.clear()

    def agregar_CT(self):
        try:
                if self.ID_var.get() == "" or self.PESO_Var.get() == "":
                    messagebox.showerror("Error","Todos los campos deben ser llenados")
                else:
                    con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
                    cur=con.cursor()
                    cur.execute("insert into producto_en_proceso values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ID_var.get(),
                                                                                                self.AREA_var.get(),
                                                                                                self.FECHA_var.get(),
                                                                                                self.HORA_ENTRADA_var.get(),
                                                                                                self.NRO_CAMA_var.get(),                                                              
                                                                                                self.LOTE_var.get(),
                                                                                                self.PESO_Var.get(),
                                                                                                self.CANT_MICROORGANISMO_var.get(),
                                                                                                self.TEMPERATURA_var.get(),
                                                                                                self.ENCARGADO_var.get()))  
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
        cur.execute("select * from producto_en_proceso")
        rows = cur.fetchall()
        if len(rows) !=0:
            self.Produccion_table.delete(*self.Produccion_table.get_children())
            for row in rows:
                self.Produccion_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def get_cursor(self,ev):
        cursor_row = self.Produccion_table.focus()
        contents = self.Produccion_table.item(cursor_row)
        row = contents['values']
        self.ID_var.set(row[0])
        self.AREA_var.set(row[1])
        self.FECHA_var.set(row[2])
        self.HORA_ENTRADA_var.set(row[3])
        self.NRO_CAMA_var.set(row[4])
        self.LOTE_var.set(row[5])
        self.PESO_Var.set(row[6])
        self.CANT_MICROORGANISMO_var.set(row[7])
        self.TEMPERATURA_var.set(row[8])
        self.ENCARGADO_var.set(row[9])

    
    def actualizarCT(self):

        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur=con.cursor()
        cur.execute("update producto_en_proceso set AREA=%s,FECHA=%s,HORA_ENTRADA=%s,NRO_CAMA=%s,LOTE=%s,PESO=%s,CANT_MICROORGANISMO=%s,TEMPERATURA=%s,ENCARGADO=%s where ID=%s",(
                                                            
                                                                                    self.AREA_var.get(),
                                                                                    self.FECHA_var.get(),
                                                                                    self.HORA_ENTRADA_var.get(),
                                                                                    self.NRO_CAMA_var.get(),                                                              
                                                                                    self.LOTE_var.get(),
                                                                                    self.PESO_Var.get(),
                                                                                    self.CANT_MICROORGANISMO_var.get(),
                                                                                    self.TEMPERATURA_var.get(),
                                                                                    self.ENCARGADO_var.get(),
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
        self.NRO_CAMA_var.set("")
        self.LOTE_var.set("")
        self.PESO_Var.set("")
        self.CANT_MICROORGANISMO_var.set("")
        self.TEMPERATURA_var.set("")
        self.ENCARGADO_var.set("")

    
    def eliminarCT(self):
        con =pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("delete from producto_en_proceso where ID=%s",self.ID_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def buscarCT(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from producto_en_proceso where " + str(self.buscar_por_var.get()) + " Like '%" + str(self.texto_buscar_var.get())+"%'")
        rows =  cur.fetchall()
        if len(rows) != 0:
            self.Produccion_table.delete(*self.Produccion_table.get_children())
            for row in rows:
                self.Produccion_table.insert('',END,values=row)
            con.commit()
        con.close()
        self.texto_buscar_var.set("")
        

if __name__ == "__main__":
    root = Tk()
    obj = Productoenproceso(root)
    root.mainloop()




















