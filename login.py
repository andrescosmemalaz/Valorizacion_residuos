from tkinter import *
from tkinter import font
from PIL import  Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
import os 
from os import path
from register import *
import mysql.connector
from adminMenu import * 

def main():
    root = Tk()
    app = Login_ventana(root)
    root.mainloop()
    
class Login_ventana:
    def __init__(self,root):
        self.root = root
        self.root.title("Login pantalla")
        #Icono
        icono = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project//IMAGENES/logo_castillo_grande.ico"
        self.root.iconbitmap(path.abspath(icono))
        #Tamaño de pantall
        self.root.geometry("1300x770+0+0")
        
        #Imagen Central Panorama
        imagen_central = "F:/andres/Ciclo 10/Topicos/Trabajo Grupal/Trabajo Grupal-Software Municpal/miproject/Caja negra/project/IMAGENES/central imagen.png"
        self.imagen_central=ImageTk.PhotoImage(file=path.abspath(imagen_central))
        bg=Label(self.root,image=self.imagen_central).place(x=0,y=0,relwidth=1,relheight=1)
        
        #Frame Registro blanco
        Frame1= Frame(self.root, bg="white")
        Frame1.place(x=400,y=120,width=500,height=520)
        
        #Titulo dentro de frame
        title = Label(Frame1,text="Formulario de Ingreso",font=("times new roman",25,"bold"),bg="white",fg="black").place(x=70,y=30)
        # title.place(x=70,y=30)
        # Etiqueta correo
        correo = Label(Frame1, text="Correo",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=220,y=100)
        #Entrada de correo
        self.var_correo = StringVar()
        self.txt_correo = Entry(Frame1,textvariable=self.var_correo, font=("times new roman",15),bg="lightgray") 
        self.txt_correo.place(x=135,y=150,width=250)
        
        # Etiqueta password
        password = Label(Frame1, text="Password",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=220,y=200)
         #Entrada de password
        self.var_password = StringVar()
        self.txt_password = Entry(Frame1, textvariable = self.var_password, font=("times new roman",15),bg="lightgray",show="*") 
        self.txt_password.place(x=135,y=250,width=250)
        
        #Boton de logearse
        ingresarboton= Button(Frame1,command =self.login ,text="Ingresar",width=35,pady=20)
        ingresarboton.place(x=210,y=300,width=100,height=35)
        #Boton registrar nuevo usuario
        registarboton= Button(Frame1,text="Registrar nuevo usuario",command=self.registro_ventana,font=("times new roman",15,"bold"),borderwidth=0,fg="black",bg="white",activebackground="white")
        registarboton.place(x=50,y=350)
        #Boton para restablecer contraseña
        recordarboton= Button(Frame1,text="Recordar Password",command = self.ventana_recordar_password,font=("times new roman",15,"bold"),borderwidth=0,fg="black",bg="white",activebackground="white")
        recordarboton.place(x=50,y=400)
        

    # Metodo para logearse
    def login(self):
        #Validacion de ingreso vacio
        if self.var_correo.get() == "" or self.txt_password.get()=="":
            messagebox.showwarning("Cuidado","Debe ingresar un usuario o un password")
        # Permisos de administrador
        elif self.var_correo.get()=="admin" and self.txt_password.get() == "admin":
            messagebox.showinfo("Correcto","Bienvenido al Sistema de Administración de la Planta de Valorización de residuos")
            self.clear()
            self.Menu()
        else:
            #Validacion de usuari
            #Conexion a BD
            conn  =mysql.connector.connect(host="localhost",user="root",password="root",database="municipalidad")
            # La clase Cursor es una instancia mediante la cual puede invocar métodos que ejecutan declaraciones SQL, obtener datos de los conjuntos de resultados de las consultas.
            my_cursor= conn.cursor()
            # Utilice el método de ejecución para ejecutar sentencias SQL
            my_cursor.execute("select * from usuario where CORREO=%s and PASSWORD=%s",(
                                                                                    self.var_correo.get(),
                                                                                    self.var_password.get()
                                                                                ))
            print(my_cursor)
            #Utilice el método fetchone () para obtener una pieza de datos especie de tupla
            row = my_cursor.fetchone()
            print(row)
            if row == None:
                messagebox.showerror("Error","Usuario o Password invalido")
                self.clear()
            else:
                self.clear()
                self.Menu()
                
            conn.commit()
            conn.close()
    
    # Metodo para llamar pantalla de registro de nuevos usuarios al sistema
    def registro_ventana(self):
        self.new_window = Toplevel(self.root)
        self.app  = Register(self.new_window)
    
    
    def restablecer_password(self):
        if self.combo_Pregunta_seguridad.get() == "Selección":
            messagebox.showerror("Error","Selección no es una opción valida, intente otra")
        elif self.txt_Respuesta_seguridad.get() == "":
            messagebox.showwarning("Cuidado","Debe ingresar la respuesta de Seguridad")
        elif self.txt_Nuevo_Password.get() == "":
            messagebox.showwarning("Cuidado","Debe ingresar un nuevo password")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="root",database="municipalidad")
            my_cursor= conn.cursor()
            query =("select * from usuario where CORREO=%s and P_SEGURIDAD=%s and R_SEGURIDAD=%s")
            value =(self.var_correo.get(),self.combo_Pregunta_seguridad.get(),self.txt_Respuesta_seguridad.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            print(row)
            if row == None:
                messagebox.showerror("Error","Su respuesta de Seguridad es incorrecta, ingresé la correcta")
            else:
                query = ("update usuario set PASSWORD=%s where CORREO=%s")
                value = (self.txt_Nuevo_Password.get(),self.var_correo.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","El password ha sido actualizado correctamente")
                self.root2.destroy()
            

    
    def ventana_recordar_password(self):
        if self.var_correo.get() == "":
            messagebox.showerror("Error","Ingresé por favor un correo para poder restablecer contraseña")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="root",database="municipalidad")
            my_cursor= conn.cursor()
            query=("select * from usuario where CORREO=%s")
            value= (self.var_correo.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            #print(row)
            
            if row == None:
                messagebox.showerror("Error","Ingresé un correo valido, por favor")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Restablecer Password")
                self.root2.geometry("340x450+610+170")
                
                l = Label(self.root2,text="Restablecer Password",font=("times new roman",15,"bold"),fg="black",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                Pregunta_seguridad = Label(self.root2,text="Pregunta de Seguridad",font=("times new roman",15,"bold"),bg="white",fg="black")
                Pregunta_seguridad.place(x=50,y=80)
                # self.Pregunta_seguridad = StringVar()
                self.combo_Pregunta_seguridad = ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_Pregunta_seguridad['values'] = ("Selección","Lugar de nacimiento","Nombre de un familiar","Nombre de su mascota")
                self.combo_Pregunta_seguridad.place(x=50,y=110,width =250)
                self.combo_Pregunta_seguridad.current(0)
                
                Respuesta_seguridad = Label(self.root2,text="Respuesta de Seguridad",font=("times new roman",15,"bold"),bg="white",fg="black")
                Respuesta_seguridad.place(x=50,y=150)
                # self.Respuesta_seguridad = StringVar()
                self.txt_Respuesta_seguridad = ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_Respuesta_seguridad.place(x=50,y = 180,width =250)
                
                Nuevo_Password = Label(self.root2,text="Nuevo Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                Nuevo_Password.place(x=50,y=220)
                self.txt_Nuevo_Password = StringVar()
                self.txt_Nuevo_Password = ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_Nuevo_Password.place(x=50,y = 250,width =250)
                
                btn = Button(self.root2,text="Restablecer",command=self.restablecer_password,font=("times new roman",15,"bold"),fg="white",bg="black")
                btn.place(x=100,y=290)
                self.clear()
                
    def Menu(self):
        self.new_window = Toplevel(self.root)
        self.app = App_Menu(self.new_window)
        

    def clear(self):
        self.var_correo.set("")
        self.var_password.set("")

if __name__ == "__main__":   
    main()



        