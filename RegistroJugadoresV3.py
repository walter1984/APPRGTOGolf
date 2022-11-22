from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.geometry("630x301")
barra = Menu(root)
root.config(menu=barra, width=600, height=600, pady=10)

valor_nombre = StringVar()
valor_apellido = StringVar()
valor_usuario = StringVar()
valor_email = StringVar()
valor_categoria = StringVar()

# ---------------Encabezado----------
root.title("Resgistro de Jugador")
bienvenido = Label(text="Bienvenido al Registro de Jugadores")
bienvenido.grid(row=0, column=2, )
bienvenido.config(font=('Arial', 14))

# ----------------------INTERFAZ--------------------------------
label_nombre = Label(root, text="Nombre", pady=20, padx=20)
label_nombre.grid(row=2, column=1)
entry_nombre = Entry(root, textvariable=valor_nombre)
entry_nombre.grid(row=2, column=2)

label_apellido = Label(root, text="Apellido", pady=10, padx=10)
label_apellido.grid(row=2, column=3)
entry_apellido = Entry(root, textvariable=valor_apellido)
entry_apellido.grid(row=2, column=4)

label_usuario = Label(root, text="Crear Usuario", pady=10, padx=10)
label_usuario.grid(row=3, column=1)
entry_usuario = Entry(root, textvariable=valor_usuario)
entry_usuario.grid(row=3, column=2)

label_email = Label(root, text="E-Mail", pady=10, padx=10)
label_email.grid(row=3, column=3)
entry_email = Entry(root, textvariable=valor_email)
entry_email.grid(row=3, column=4)

label_categoria = Label(root, text="Categoria", pady=10, padx=10)
label_categoria.grid(row=4, column=1)
entry_categoria = Entry(root, textvariable=valor_categoria)
entry_categoria.grid(row=4, column=2)

# --------------------Funciones CRUD---------------
def crear():
    conexion = sqlite3.connect("JUGADORESBBDD.db")
    cursor = conexion.cursor()
    global entry_nombre
    global entry_apellido
    global entry_usuario
    global entry_email
    global entry_categoria

    datos = [(entry_nombre.get(), entry_apellido.get(), entry_usuario.get(), entry_email.get(), entry_categoria.get())]
    try:
        insertQuery = ("INSERT INTO JUGADORES (ID, NOMBRE, APELLIDO, USUARIO, EMAIL, CATEGORIA) VALUES(NULL,?,?,?,?,?)")
        conexion.executemany(insertQuery,datos)
        conexion.commit()
        messagebox.showinfo("Exito", "Jugador registrado con éxito")
    except sqlite3.OperationalError:
        messagebox.showinfo("Error", "Ha ocurrido en el registro del Jugador" )

# ------------------LIMPIAR-------------------
def reseat():
    conexion = sqlite3.connect("JUGADORESBBDD.db")
    cursor = conexion.cursor()
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

# ------------------Creando Conexion----------------
def conectar():
    try:
        conexion = sqlite3.connect("JUGADORESBBDD.db")
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE JUGADORES(ID INTEGER PRIMARY KEY AUTOINCREMENT, ID NUMERIC, NOMBRE VARCHAR(30), APELLIDO VARCHAR(30), USUARIO VARCHAR(20), EMAIL VARCHAR(30), CATEGORIA VARCHAR(20));")
        conexion.commit()
        messagebox.showinfo("Exito", "Base de Datos conectada")
    except sqlite3.OperationalError:
        messagebox.showwarning("Error", "La Base de Datos ya existe!")

def salir():
    mensaje = messagebox.askquestion("Salir", "¿Desea cerrar el registro?")
    if mensaje == "yes":
        root.destroy()

# ------------------Tabla---------------
def mostrar_tabla():
    conexion = sqlite3.connect("JUGADORESBBDD.db")
    cursor = conexion.cursor()

    tabla = Tk()
    tabla.title("JUGADORES")
    tabla.config(width=500, height=500)
    
    fila_id = Label(tabla, text="ID", relief="solid", padx=20)
    fila_id.grid(row=0, column=0)
 
    fila_nombre = Label(tabla, text="NOMBRE", relief="solid")
    fila_nombre.grid(row=0, column=1)

    fila_apellido = Label(tabla, text="APELLIDO", relief="solid")
    fila_apellido.grid(row=0, column=2)

    fila_usuario = Label(tabla, text="USUARIO", relief="solid")
    fila_usuario.grid(row=0, column=3)

    fila_email = Label(tabla, text="EMAIL", relief="solid")
    fila_email.grid(row=0, column=4)
        
    fila_categoria = Label(tabla, text="CATEGORIA", relief="solid", padx=20)
    fila_categoria.grid(row=0, column=5)

    # ------------Posicionando datos-----------------
    cursor.execute("SELECT * FROM JUGADORES WHERE ID")
    JUGADORESBBDD = cursor.fetchall()

    contador = 1

    for Jugador in JUGADORESBBDD:
        row_id = Label(tabla)
        row_id.grid(row=0, column=0)
        
        row_nombre = Label(tabla)
        row_nombre.grid(row=0, column=1)

        row_apellido = Label(tabla)
        row_apellido.grid(row=0, column=2)

        row_usuario = Label(tabla)
        row_usuario.grid(row=0, column=3)

        row_email = Label(tabla)
        row_email.grid(row=0, column=4)

        row_categoria = Label(tabla)
        row_categoria.grid(row=0, column=5)

        contador += 1
        
        row_id.grid(row=contador)
        row_id.config(text=Jugador[0])
        
        row_nombre.grid(row=contador)
        row_nombre.config(text=Jugador[1])

        row_apellido.grid(row=contador)
        row_apellido.config(text=Jugador[2])

        row_usuario.grid(row=contador)
        row_usuario.config(text=Jugador[3])

        row_email.grid(row=contador)
        row_email.config(text=Jugador[4])

        row_categoria.grid(row=contador)
        row_categoria.config(text=Jugador[5])

    tabla.mainloop()

# ------------------MENU-------------------
menu_archivo = Menu(barra, tearoff=0)
menu_archivo.add_command(label="Conectar JUGADORESBBDD", command=conectar)
menu_archivo.add_command(label="Cerrar", command=salir)

barra.add_cascade(label="Archivos", menu=menu_archivo)

menu_borrar = Menu(barra, tearoff=0)
menu_borrar.add_command(label="Reseat", command=reseat)

barra.add_cascade(label="Limpiar", menu=menu_borrar)

menu_opciones = Menu(barra, tearoff=0)
menu_opciones.add_command(label="Crear", command=crear)

barra.add_cascade(label="Opciones", menu=menu_opciones)

# ------------------LICENCIA y VERSION-------------
def licencia():
    messagebox.showinfo("LICENCIA", "Licencia año 2022®")

def version():
    messagebox.showinfo("ACERCA DE", "Proyecto registro de Golfistas\ Version 0.1 \ WABV")

menu_ayuda = Menu(barra, tearoff=0)
menu_ayuda.add_command(label="Licencia", command=licencia)
menu_ayuda.add_command(label="Acerca de...", command=version)
barra.add_cascade(label="Ayuda", menu=menu_ayuda)

# ---------------------BOTONES---------------
frame = Frame(root)
frame.grid(row=5, column=1, columnspan=6)

boton_crear = Button(frame, text="Crear", width=10, command=crear)
boton_crear.grid(row=5, column=0, sticky="w", padx=10)

# ---------------Boton base de datos----------
Button(root, text="Mostrar Registro", command=mostrar_tabla, width=13).grid(row=7, column=1, sticky="e")

root.mainloop()