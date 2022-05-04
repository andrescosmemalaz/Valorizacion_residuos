import pymysql
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import  Image,ImageTk
from tkcalendar import DateEntry 
from datetime import date
from os import path
 


class Personal():
    def __init__(self,root):
        self.root=root
        self.root.title("Sistema Administracion Personal")
        icono = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico"
        self.root.iconbitmap(path.abspath(icono))
        #self.root.iconbitmap("F:\\andres\\Ciclo 10\\Topicos\\Trabajo Grupal\\Trabajo Grupal-Software Municpal\\miproject\\Caja negra\\project\\logo_castillo_grande.ico")
        self.root.geometry("1300x770+0+0")
        #Imagen
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        
        title = Label(self.root,text="Sistema Administración de Personal",bd=12,relief=GROOVE,font=("times new roman",40,"bold"),bg="#008f4c",fg="black")
        title.pack(side=TOP,fill=X)

        #Todas las variables
        self.ID_var = StringVar()
        self.NOMBRE_var = StringVar()
        self.APELLIDO_var = StringVar()
        self.FECHA_NACIMIENTO_var = StringVar()
        self.FECHA_INGRESO_var = StringVar()
        self.PUESTO_var = StringVar()
        self.EDAD_Var = IntVar()
        self.ANOS_EXPERIENCIA_var = IntVar()
        self.CORREO_Var = StringVar()
        self.TELEFONO_var = IntVar()
        self.SALARIO_MENSUAL_Var = IntVar()
        self.buscar_por_var = StringVar()
        self.texto_buscar_var = StringVar()

        #Frame de administracion
        Managment_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="orange")
        Managment_Frame.place(x=20, y=100,width=450,height=645)


        m_title = Label(Managment_Frame,text="Registrar Personal", bg="orange",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_id = Label(Managment_Frame,text="ID",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_id.grid(row=1,column=0, pady=10,padx=20,sticky="w")
        txt_id  =Entry(Managment_Frame,textvariable =self.ID_var,font=("times new roman",12,"bold"))
        txt_id.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lbl_NOMBRE = Label(Managment_Frame,text="NOMBRE",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_NOMBRE.grid(row=2,column=0, pady=10,padx=20,sticky="w")
        txt_NOMBRE  =Entry(Managment_Frame,textvariable =self.NOMBRE_var,font=("times new roman",12,"bold"))
        txt_NOMBRE.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_APELLIDO = Label(Managment_Frame,text="APELLIDO",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_APELLIDO.grid(row=3,column=0, pady=10,padx=20,sticky="w")
        txt_APELLIDO  =Entry(Managment_Frame,textvariable =self.APELLIDO_var,font=("times new roman",12,"bold"))
        txt_APELLIDO.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_fecha_nacimiento = Label(Managment_Frame,text="FECHA NACIMIENTO",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_fecha_nacimiento.grid(row=4,column=0, pady=10,padx=20,sticky="w")
        # txt_fecha  =Entry(Managment_Frame,textvariable =self.FECHA_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        # txt_fecha.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        txt_fecha_nacimiento=DateEntry(Managment_Frame,textvariable =self.FECHA_NACIMIENTO_var,date_pattern='dd/mm/y',font=("times new roman",12,"bold"),state="readonly")
        txt_fecha_nacimiento.grid(row=4, column=1,padx=10,ipadx=25)
        dt =date(2021,12,2)
        txt_fecha_nacimiento.set_date(dt)
        
        lbl_fecha_ingreso = Label(Managment_Frame,text="FECHA INGRESO",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_fecha_ingreso.grid(row=5,column=0, pady=10,padx=20,sticky="w")
        # txt_fecha  =Entry(Managment_Frame,textvariable =self.FECHA_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        # txt_fecha.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        txt_fecha_ingreso=DateEntry(Managment_Frame,textvariable =self.FECHA_INGRESO_var,date_pattern='dd/mm/y',font=("times new roman",12,"bold"),state="readonly")
        txt_fecha_ingreso.grid(row=5, column=1,padx=10,ipadx=25)
        dt =date(2021,12,2)
        txt_fecha_ingreso.set_date(dt)
        
        
        lbl_puesto = Label(Managment_Frame,text="PUESTO",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_puesto.grid(row=6,column=0, pady=10,padx=20,sticky="w")
        txt_puesto =Entry(Managment_Frame,textvariable =self.PUESTO_var,font=("times new roman",12,"bold"))
        txt_puesto.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        # #Combobox
        combo_puesto = ttk.Combobox(Managment_Frame,textvariable =self.PUESTO_var,font=("times new roman",10,"bold"),state="readonly")
        combo_puesto['values'] = ('Ingeniero','Operario','Chofer','Técnico','Otro')
        combo_puesto.grid(row=6,column=1,pady=10,padx=10)
        
        # lbl_area = Label(Managment_Frame,text="AREA",bg="blue",fg="white",font=("times new roman",15,"bold"))
        # lbl_area.grid(row=2,column=0, pady=10,padx=20,sticky="w")
        # # txt_area  =Entry(Managment_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        # # txt_area.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        
        
        lbl_edad = Label(Managment_Frame,text="EDAD",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_edad.grid(row=7,column=0, pady=10,padx=20,sticky="w")
        txt_edad =Entry(Managment_Frame,textvariable =self.EDAD_Var,font=("times new roman",12,"bold"))
        txt_edad.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        lbl_anos_experiencia = Label(Managment_Frame,text="AÑOS EXPERIENCIA",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_anos_experiencia.grid(row=8,column=0, pady=10,padx=20,sticky="w")
        txt_anos_experiencia =Entry(Managment_Frame,textvariable =self.ANOS_EXPERIENCIA_var,font=("times new roman",12,"bold"))
        txt_anos_experiencia.grid(row=8,column=1,pady=10,padx=20,sticky="w")
        
        lbl_correo = Label(Managment_Frame,text="CORREO",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_correo.grid(row=9,column=0, pady=10,padx=20,sticky="w")
        txt_correo =Entry(Managment_Frame,textvariable =self.CORREO_Var,font=("times new roman",12,"bold"))
        txt_correo.grid(row=9,column=1,pady=10,padx=20,sticky="w")
        
        lbl_telefono = Label(Managment_Frame,text="TELEFONO",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_telefono.grid(row=10,column=0, pady=10,padx=20,sticky="w")
        txt_telefono =Entry(Managment_Frame,textvariable =self.TELEFONO_var,font=("times new roman",12,"bold"))
        txt_telefono.grid(row=10,column=1,pady=10,padx=20,sticky="w")
        
        lbl_salario = Label(Managment_Frame,text="SALARIO",bg="orange",fg="black",font=("times new roman",12,"bold"))
        lbl_salario.grid(row=11,column=0, pady=10,padx=20,sticky="w")
        txt_salario=Entry(Managment_Frame,textvariable =self.SALARIO_MENSUAL_Var,font=("times new roman",12,"bold"))
        txt_salario.grid(row=11,column=1,pady=10,padx=20,sticky="w")
        

        #Botom Frame
        btn_frame = Frame(Managment_Frame,bd=3,relief=RIDGE,bg="black")
        btn_frame.place(x=15,y=575,width=420)

        agregar_botom = Button(btn_frame,text="Agregar",width=10,command=self.agregar_EMPLEADO).grid(row=0,column=0,padx=10,pady=10)
        actualizar_botom = Button(btn_frame,text="Actualizar",width=10,command=self.actualizarEMPLEADO).grid(row=0,column=1,padx=10,pady=10)
        eliminar_botom = Button(btn_frame,text="Eliminar",width=10,command=self.eliminarEMPLEADO).grid(row=0,column=2,padx=10,pady=10)
        limpiar_botom = Button(btn_frame,text="Limpiar",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        # Base de Datos Frame 
        BD_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#36d073")
        BD_Frame.place(x=500,y=100,width=770,height=645)

        lbl_buscar = Label(BD_Frame, text="Buscar por",bg="#36d073",fg="white",font=("times new roman",15,"bold"))
        lbl_buscar.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        #Combobox
        combo_buscar = ttk.Combobox(BD_Frame,textvariable =self.buscar_por_var,font=("times new roman",13,"bold"),state="readonly")
        combo_buscar['values'] = ("FECHA_NACIMIENTO","FECHA_INGRESO","PUESTO")
        combo_buscar.grid(row=0,column=1,pady=15,padx=20,sticky="w")
        texto_buscar = Entry(BD_Frame,textvariable =self.texto_buscar_var,font=("times new roman",10,"bold"),width=20,bd=5,relief=GROOVE)
        texto_buscar.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        #Botones
        buscarboton= Button(BD_Frame,text="Buscar",width=10,pady=5,command=self.buscarEMPLEADO).grid(row=0,column=3,padx=10,pady=10)
        mostrarboton = Button(BD_Frame,text="Listar",width=8,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #===========Tabla de registros ======= 
        Table_Frame = Frame(BD_Frame,bd=4,relief=RIDGE,bg="yellow")
        Table_Frame.place(x=10,y=70,width=740,height=550)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Empleado_table = ttk.Treeview(Table_Frame,column=("ID","NOMBRE","APELLIDO","FECHA_NACIMIENTO","FECHA_INGRESO","PUESTO","EDAD","AÑOS_EXPERIENCIA","CORREO","TELEFONO","SALARIO_MENSUAL"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Empleado_table.xview)
        scroll_y.config(command=self.Empleado_table.yview)
        

        self.Empleado_table.heading("ID",text ="ID")
        # self.Materiaprima_table.heading("CODIGO",text ="CODIGO")
        self.Empleado_table.heading("NOMBRE",text ="NOMBRE")
        self.Empleado_table.heading("APELLIDO",text ="APELLIDO")
        self.Empleado_table.heading("FECHA_NACIMIENTO",text ="FECHA_NACIMIENTO")
        self.Empleado_table.heading("FECHA_INGRESO",text ="FECHA_INGRESO")
        self.Empleado_table.heading("PUESTO",text ="PUESTO")
        self.Empleado_table.heading("EDAD",text ="EDAD")
        self.Empleado_table.heading("AÑOS_EXPERIENCIA",text ="AÑOS_EXPERIENCIA")
        self.Empleado_table.heading("CORREO",text ="CORREO")
        self.Empleado_table.heading("TELEFONO",text ="TELEFONO")
        self.Empleado_table.heading("SALARIO_MENSUAL",text ="SALARIO_MENSUAL")

        self.Empleado_table['show'] = 'headings'
        self.Empleado_table.column("ID",width=100)
        self.Empleado_table.column("NOMBRE",width=100)
        self.Empleado_table.column("FECHA_NACIMIENTO",width=100)
        self.Empleado_table.column("FECHA_INGRESO",width=100)
        self.Empleado_table.column("PUESTO",width=100)
        self.Empleado_table.column("EDAD",width=100)
        self.Empleado_table.column("AÑOS_EXPERIENCIA",width=100)
        self.Empleado_table.column("CORREO",width=100)
        self.Empleado_table.column("TELEFONO",width=100)
        self.Empleado_table.column("SALARIO_MENSUAL",width=100)

        self.Empleado_table.pack(fill=BOTH,expand=1)
        self.Empleado_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.clear()

    def agregar_EMPLEADO(self):
        if self.ID_var.get() == "":
            messagebox.showerror("Error","Todos los campos deben ser llenados")
        else:
            con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
            cur=con.cursor()
            cur.execute("insert into personal values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ID_var.get(),
                                                                                        self.NOMBRE_var.get(),
                                                                                        self.APELLIDO_var.get(),
                                                                                        self.FECHA_NACIMIENTO_var.get(),
                                                                                        self.FECHA_INGRESO_var.get(),
                                                                                        self.PUESTO_var.get(),
                                                                                        self.EDAD_Var.get(),
                                                                                        self.ANOS_EXPERIENCIA_var.get(),
                                                                                        self.CORREO_Var.get(),
                                                                                        self.TELEFONO_var.get(),
                                                                                        self.SALARIO_MENSUAL_Var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Correcto","Se ha realizado el registro con éxito")
    
    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from personal")
        rows = cur.fetchall()
        if len(rows) !=0:
            self.Empleado_table.delete(*self.Empleado_table.get_children())
            for row in rows:
                self.Empleado_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def get_cursor(self,ev):
        cursor_row = self.Empleado_table.focus()
        contents = self.Empleado_table.item(cursor_row)
        row = contents['values']
        self.ID_var.set(row[0])
        self.NOMBRE_var.set(row[1])
        self.APELLIDO_var.set(row[2])
        self.FECHA_NACIMIENTO_var.set(row[3])
        self.FECHA_INGRESO_var.set(row[4])
        self.PUESTO_var.set(row[5])
        self.EDAD_Var.set(row[6])
        self.ANOS_EXPERIENCIA_var.set(row[7])
        self.CORREO_Var.set(row[8])
        self.TELEFONO_var.set(row[9])
        self.SALARIO_MENSUAL_Var.set(row[10])
    
    def actualizarEMPLEADO(self):

        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur=con.cursor()
        cur.execute("update personal set NOMBRE=%s,APELLIDO=%s,FECHA_NACIMIENTO=%s,FECHA_INGRESO=%s,PUESTO=%s,EDAD=%s,AÑOS_EXPERIENCIA=%s,CORREO=%s,TELEFONO=%s,SALARIO_MENSUAL=%s where ID=%s",(

                                                                                    self.NOMBRE_var.get(),
                                                                                    self.APELLIDO_var.get(),
                                                                                    self.FECHA_NACIMIENTO_var.get(),
                                                                                    self.FECHA_INGRESO_var.get(),
                                                                                    self.PUESTO_var.get(),
                                                                                    self.EDAD_Var.get(),
                                                                                    self.ANOS_EXPERIENCIA_var.get(),
                                                                                    self.CORREO_Var.get(),
                                                                                    self.TELEFONO_var.get(),
                                                                                    self.SALARIO_MENSUAL_Var.get(),
                                                                                    self.ID_var.get()))  
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Correcto","Se ha actualizado el registro con éxito")
    
    def clear(self):
        self.ID_var.set("")
        self.NOMBRE_var.set(""),
        self.APELLIDO_var.set(""),
        self.FECHA_NACIMIENTO_var.set(""),
        self.FECHA_INGRESO_var.set(""),
        self.PUESTO_var.set(""),
        self.EDAD_Var.set(""),
        self.ANOS_EXPERIENCIA_var.set(""),
        self.CORREO_Var.set(""),
        self.TELEFONO_var.set("")
        self.SALARIO_MENSUAL_Var.set("")
        
    
        
    def eliminarEMPLEADO(self):
        con =pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("delete from personal where ID=%s",self.ID_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def buscarEMPLEADO(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="municipalidad")
        cur = con.cursor()
        cur.execute("select * from personal where " + str(self.buscar_por_var.get()) + " Like '%" + str(self.texto_buscar_var.get())+"%'")
        rows =  cur.fetchall()
        if len(rows) != 0:
            self.Empleado_table.delete(*self.Empleado_table.get_children())
            for row in rows:
                self.Empleado_table.insert('',END,values=row)
            con.commit()
        con.close()
        self.texto_buscar_var.set("")
    


if __name__ == "__main__":
    root = Tk()
    obj = Personal(root)
    root.mainloop()
