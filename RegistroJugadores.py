from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root=Tk()
root.geometry("630x301")
barra=Menu(root)
root.config(menu=barra, width=600, height=600, pady=10)

valor_nombre=StringVar()
valor_apellido=StringVar()
valor_usuario=StringVar()
valor_email=StringVar()
valor_categoria=StringVar()

#------------------Creando Conexion----------------
def conectar():
	try:
		conexion=sqlite3.connect("JUGADORESBBDD")
		cursor=conexion.cursor()
		cursor.execute("CREATE TABLE USUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(20), APELLIDO VARCHAR(30), USUARIO VARCHAR(20), EMAIL VARCHAR(30), CATEGORIA VARCHAR(20)) ")
		conexion.commit()
		messagebox.showinfo("Exito", "BD conectada")
	except sqlite3.OperationalError:
		messagebox.showwarning("Error", "La BD ya existe!")

def salir():
	mensaje=messagebox.askquestion("Salir", "¿Desea cerrar el programa?")
	if mensaje=="yes":
		root.destroy()
		
#----------------------INTERFAZ--------------------------------

label_nombre=Label(root, text="Nombre", pady=20, padx=20)
label_nombre.grid(row=2, column=1)
entry_nombre=Entry(root, textvariable=valor_nombre)
entry_nombre.grid(row=2, column=2)

label_apellido=Label(root, text="Apellido", pady=10, padx=10)
label_apellido.grid(row=2, column=3)
entry_apellido=Entry(root, textvariable=valor_apellido)
entry_apellido.grid(row=2, column=4)

label_usuario=Label(root, text="Crear Usuario", pady=10, padx=10)
label_usuario.grid(row=3, column=1)
entry_usuario=Entry(root, textvariable=valor_usuario)
entry_usuario.grid(row=3, column=2)

label_email=Label(root, text="E-Mail", pady=10, padx=10)
label_email.grid(row=3, column=3)
entry_email=Entry(root, textvariable=valor_email)
entry_email.grid(row=3, column=4)

label_categoria=Label(root, text="Categoria", pady=10, padx=10)
label_categoria.grid(row=4, column=1)
entry_categoria=Entry(root, textvariable=valor_categoria)
entry_categoria.grid(row=4, column=2)

#entry_categoria.config(show="*")#

#------------------LIMPIAR-------------------
def reseat():
	conexion=sqlite3.connect("JUGADORESBBDD")
	cursor=conexion.cursor()
	global entry_nombre
	global entry_apellido
	global entry_usuario
	global entry_email
	global entry_categoria
 
	valor_nombre.set(" ")
	valor_apellido.set(" ")
	valor_usuario.set(" ")
	valor_email.set(" ")
	valor_categoria.set(" ")

#----------------Mostrar Contraseña-------------
#def mostrar():#
	#entry_contraseña.config(show="")#
		
#def proteger():#
	#entry_contraseña.config(show="*")#

#--------------------Funciones CRUD---------------
def crear():
	conexion=sqlite3.connect("JUGADORESBBDD")
	cursor=conexion.cursor()
	global entry_nombre
	global entry_apellido
	global entry_usuario
	global entry_email
	global entry_categoria
	
	datos=[(entry_nombre.get(), entry_apellido.get(), entry_usuario.get(), entry_email(), entry_categoria())]
	try:
		cursor.executemany("INSERT INTO USUARIOS VALUES(NULL, ?,?,?)", datos)
		conexion.commit()
		messagebox.showinfo("Exito", " Usuario añadido con éxito")
	except:
		messagebox.showinfo("Error", "Ha ocurrido un error")

def buscando():
	conexion=sqlite3.connect("JUGADORESBBDD")
	cursor=conexion.cursor()
	try:
		cursor.execute("SELECT * FROM USUARIOS WHERE ID="+valor_nombre.get())
		usuario=cursor.fetchall()
		
		for dato in usuario:
			valor_nombre.set(dato[1])
			valor_apellido.set(dato[2])
			valor_usuario.set(dato[3])
			valor_email.set(dato[4])
			valor_categoria.set(dato[5])
	except:
		messagebox.showwarning(" Error", "El usuario no existe")

def reemplazar():
	conexion=sqlite3.connect("JUGADORESBBDD")
	cursor=conexion.cursor()
	datos=entry_nombre.get(), entry_apellido.get(), entry_usuario.get(), entry_email.get(), entry_categoria.get()
	cursor.execute("UPDATE USUARIOS SET NOMBRE=?, APELLIDO=?, USUARIO=?, EMAIL=?, CATEGORIA=?" +
	     "WHERE ID=" + valor_nombre.get(), (datos))
	messagebox.showinfo("Exito", "Se ha completado el reemplazo")
	conexion.commit()
	
def borrar():
	conexion=sqlite3.connect("JUGADORESBBDD")
	cursor=conexion.cursor()
	pregunta=messagebox.askquestion(" Borrar", "¿El usuario derá eliminado?")
	if pregunta=="yes":
		try:
			cursor.execute("DELETE FROM USUARIOS WHERE ID="+valor_nombre.get())
			valor_nombre.set(" ")
			valor_apellido.set(" ")
			valor_usuario.set(" ")
			valor_email.set(" ")
			valor_categoria.set(" ")
			messagebox.showinfo(" Exito", "¡Usuario eliminado con éxito!")
			conexion.commit()
		except:
			messagebox.showwarning(" Error", "El usuario no existe")

#------------------LICENCIA y VERSION-------------
def licencia():
	messagebox.showinfo("LICENCIA", "Licencia año 2022®")

def version():
	messagebox.showinfo("ACERCA DE", "Proyecto registro de Golfistas\ Version 0.1 \ WABV")	

#------------------MENU-------------------	
menu_archivo=Menu(barra, tearoff=0)
menu_archivo.add_command(label="Conectar BBDD", command=conectar)
menu_archivo.add_command(label="Cerrar", command=salir)

barra.add_cascade(label="Archivos", menu=menu_archivo)

menu_borrar=Menu(barra, tearoff=0)
menu_borrar.add_command(label="Reseat", command=reseat)

barra.add_cascade(label="Limpiar", menu=menu_borrar)

menu_opciones=Menu(barra, tearoff=0)
menu_opciones.add_command(label="Crear", command=crear)
menu_opciones.add_command(label="Buscar", command=buscando)
menu_opciones.add_command(label="Reemplazar", command=reemplazar)
menu_opciones.add_command(label="Borrar", command=borrar)

barra.add_cascade(label="Opciones", menu=menu_opciones)

menu_ayuda=Menu(barra, tearoff=0)
menu_ayuda.add_command(label="Licencia", command=licencia)
menu_ayuda.add_command(label="Acerca de...", command=version)

barra.add_cascade(label="Ayuda", menu=menu_ayuda)

#---------------------BOTONES---------------
frame=Frame(root)
frame.grid(row=5, column=1, columnspan=6)

boton_crear=Button(frame, text="Crear", width=10, command=crear)
boton_crear.grid(row=5, column=0, sticky="w",padx=10)

boton_buscar=Button(frame, text="Buscar", width=10, command=buscando)
boton_buscar.grid(row=5, column=1, pady=1)

boton_reemplazo=Button(frame, text="Reemplazar", command=reemplazar)
boton_reemplazo.grid(row=5, column=2, padx=10)

boton_borrar=Button(frame, text="Borrar", width=10, command=borrar)
boton_borrar.grid(row=5, column=3, pady=10)

#-------------Boton Mostrar Contraseña----------
#boton_mostrar=Button(frame, text="Mostrar contraseña", command=mostrar)#
#boton_mostrar.grid(row=6, column=0, padx=10, columnspan=2)#

#boton_proteger=Button(frame, text="Proteger contraseña", command=proteger)#
#boton_proteger.grid(row=6, column=1, pady=10, padx=100, columnspan=7)#

#------------------Tabla---------------
def mostrar_tabla():
	conexion=sqlite3.connect("JUGADORESBBDD")
	cursor=conexion.cursor()
	
	tabla=Tk()
	tabla.title("Base de Datos")
	tabla.config(width=500, height=500)
	
	fila_ID=Label(tabla, text="NOMBRE", relief="solid", padx=20)
	fila_ID.grid(row=0, column=0)
	
	fila_nombre=Label(tabla, text="APELLIDO", relief="solid")
	fila_nombre.grid(row=0, column=1)
	
	fila_apellido=Label(tabla, text="USUARIO", relief="solid")
	fila_apellido.grid(row=0, column=2)
	
	fila_contraseña=Label(tabla, text="EMAIL", relief="solid")
	fila_contraseña.grid(row=0, column=3)
 
	fila_contraseña=Label(tabla, text="CATEGORIA", relief="solid")
	fila_contraseña.grid(row=0, column=4)
	
	#------------Posicionando datos-----------------
	cursor.execute("SELECT * FROM USUARIOS")
	usuarios=cursor.fetchall()

	
	contador=1
	
	for usuario in usuarios:
		row_nombre=Label(tabla)
		row_nombre.grid(row=1, column=0)
		
		row_apellido=Label(tabla)
		row_apellido.grid(row=1, column=1)
		
		row_usuario=Label(tabla)
		row_usuario.grid(row=1, column=2)
		
		row_email=Label(tabla)
		row_email.grid(row=1, column=3)
  
		row_categoria=Label(tabla)
		row_categoria.grid(row=1, column=4)
	
		contador+=1
		row_nombre.grid(row=contador)
		row_nombre.config(text=usuario[0])
			
		row_apellido.grid(row=contador)
		row_apellido.config(text=usuario[1])
			
		row_usuario.grid(row=contador)
		row_usuario.config(text=usuario[2])
		
		row_email.grid(row=contador)
		row_email.config(text=usuario[3])
  
		row_categoria.grid(row=contador)
		row_categoria.config(text=usuario[4])

	
	tabla.mainloop()

#---------------Boton base de datos----------
Button(root, text="Mostrar Tabla", command=mostrar_tabla, width=13).grid(row=7, column=1, sticky="e")

#---------------Encabezado----------
root.title("Resgistro de Jugador")
bienvenido = Label(text="Bienvenido al Registro de Jugadores")
bienvenido.grid(row=0, column=2,)
bienvenido.config(font=('Arial', 14))
root.mainloop()