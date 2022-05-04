from tkinter import font
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
import mysql.connector
 


class Register():
    def __init__(self,root):
        self.root=root
        self.root.title("Registro")
        icono = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/logo_castillo_grande.ico"
        self.root.iconbitmap(path.abspath(icono))
        #self.root.iconbitmap("F:\\andres\\Ciclo 10\\Topicos\\Trabajo Grupal\\Trabajo Grupal-Software Municpal\\miproject\\Caja negra\\project\\logo_castillo_grande.ico")
        self.root.geometry("1300x770+0+0")
        #Imagen
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        #Imagen de lado izquierdo
        imagen_izquierda = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/economía-circular.png"
        self.izquierda=ImageTk.PhotoImage(file=path.abspath(imagen_izquierda))
        izquierda_lbl = Label(self.root,image=self.izquierda)
        izquierda_lbl.place(x=50,y=100,width=450,height=550)
        
        #=========== Main Frame ===========
        frame = Frame(self.root,bg="white")
        frame.place(x=500,y=100,width=740,height=550)
        
        registro_lbl=Label(frame,text="REGISTRO DE UN NUEVO USUARIO",font=("times new roman",20, "bold"), fg="black",bg="white")
        registro_lbl.place(x=20,y=20)
        
        #lABEL e ingreso de información
        #========== fila 1
        fname = Label(frame,text="Primer Nombre",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        self.var_fname = StringVar()
        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        sname = Label(frame,text="Segundo Nombre",font=("times new roman",15,"bold"),bg="white")
        sname.place(x=370,y=100)
        self.var_sname = StringVar()
        sname_entry = ttk.Entry(frame,textvariable=self.var_sname,font=("times new roman",15,"bold"))
        sname_entry.place(x=370,y=130,width=250)
        
        #========== fila 2
        contacto = Label(frame,text="Número de Contacto",font=("times new roman",15,"bold"),bg="white")
        contacto.place(x=50,y=170)
        self.var_contacto = StringVar()
        contacto_entry = ttk.Entry(frame,textvariable=self.var_contacto,font=("times new roman",15,"bold"))
        contacto_entry.place(x=50,y=200,width=250)
        
        correo = Label(frame,text="Correo Electrónico",font=("times new roman",15,"bold"),bg="white")
        correo.place(x=370,y=170)
        self.var_correo = StringVar()
        correo_entry = ttk.Entry(frame,textvariable=self.var_correo,font=("times new roman",15,"bold"))
        correo_entry.place(x=370,y=200,width=250)
        
        #========== fila 3
        Pregunta_seguridad = Label(frame,text="Seleccioné tipo de Pregunta",font=("times new roman",15,"bold"),bg="white")
        Pregunta_seguridad.place(x=50,y=240)
        self.var_Pregunta_seguridad = StringVar()
        self.combo_Pregunta_seguridad = ttk.Combobox(frame,textvariable=self.var_Pregunta_seguridad,font=("times new roman",15,"bold"),state="readonly")
        self.combo_Pregunta_seguridad['values'] = ("Selección","Lugar de nacimiento","Nombre de un familiar","Nombre de su mascota")
        self.combo_Pregunta_seguridad.place(x=50,y=270,width=250)
        self.combo_Pregunta_seguridad.current(0)
        
        Respuesta_Seguridad  = Label(frame,text="Pregunta de Seguridad",font=("times new roman",15,"bold"),bg="white",fg="black")
        Respuesta_Seguridad.place(x=370,y=240)
        self.var_Respuesta_Seguridad = StringVar()
        self.txt_Seguridad = ttk.Entry(frame,textvariable=self.var_Respuesta_Seguridad,font=("times new roman",15))
        self.txt_Seguridad.place(x=370,y=270,width=250)
        
        #========== fila 4
        Password = Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        Password.place(x=50,y=310)
        self.var_Password = StringVar()
        self.txt_Password = ttk.Entry(frame,textvariable=self.var_Password,font=("times new roman",15))
        self.txt_Password.place(x=50,y=340,width=250)
        
        confirm_Password = Label(frame,text="Confirmar Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_Password.place(x=370,y=310)
        self.var_confirm_Password = StringVar()
        self.txt_confirm_Password =ttk.Entry(frame,textvariable=self.var_confirm_Password,font=("times new roman",15))
        self.txt_confirm_Password.place(x=370,y=340,width=250)
        
        #Boton de verifficacion
        self.var_check = IntVar()
        checkboton = Checkbutton(frame,variable=self.var_check,text="Acepto los términos y condiciones",font=("times new roman",12,"bold"),bg="white",fg="black",onvalue=1,offvalue=0)
        checkboton.place(x=50,y=380)
        
        
        #Botones
        #registro
        imagen_registro = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/registro.png"
        self.imagen_registro=ImageTk.PhotoImage(file=path.abspath(imagen_registro))
        b1=Button(frame, image = self.imagen_registro,command=self.registrar_informacion,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white",activebackground="white")
        b1.place(x=10,y=410,width=350,height=80)
        
        #Ingresar
        imagen_ingresar = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/ingresar.png"
        self.imagen_ingresar=ImageTk.PhotoImage(file=path.abspath(imagen_ingresar))
        b1=Button(frame, image = self.imagen_ingresar,command = self.retornar_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white",activebackground="white")
        b1.place(x=360,y=400,width=300)
        
    # === Declaracion de funciones
    
    def registrar_informacion(self):
        if self.var_fname.get() == "" or self.var_correo.get() == "" or self.var_Pregunta_seguridad.get() == "":
            messagebox.showwarning("Atención","Debe llenar todos los datos requeridos")
        elif self.var_Password.get() != self.var_confirm_Password.get():
            messagebox.showerror("Error","Password y confirmación de password no coinciden")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Por favor acepte terminos y condiciones")
        else:
            conn  =mysql.connector.connect(host="localhost",user="root",password="root",database="municipalidad")
            my_cursor= conn.cursor()
            query = ("select * from usuario where CORREO=%s")
            value = (self.var_correo.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showwarning("Atención","Usuario ya existe , intenté con otro usuario")
            else:
                my_cursor.execute("insert into usuario values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_sname.get(),
                                                                                            self.var_contacto.get(),
                                                                                            self.var_correo.get(),
                                                                                            self.var_Pregunta_seguridad.get(),
                                                                                            self.var_Respuesta_Seguridad.get(),
                                                                                            self.var_Password.get()                                                                                                                                                                                                                                                                         
                                                                                     ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Excelente","Ha sido registrado correctamente")
                self.clear()
                
    
    def retornar_login(self):
        self.root.destroy()
    
    def clear(self):
        self.var_fname.set("")
        self.var_sname.set("")
        self.var_contacto.set("")
        self.var_correo.set("")
        self.var_Pregunta_seguridad.set("")
        self.var_Respuesta_Seguridad.set("")
        self.var_Password.set("")
        self.var_confirm_Password.set("")
    
if __name__ == '__main__':
    root=Tk()
    obj = Register(root)
    root.mainloop()
