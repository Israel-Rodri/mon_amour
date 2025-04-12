import sqlite3
import sys
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('nom.db') #Si existe un error en la conexion con la base intenten colocar la direccion completa del directorio, es decir C:/Lo que sea/Lo que sea/Y asi
cursor = conn.cursor()

#Muestra un mensaje emergente si el agragar algo sale bien
def succesfulAddMessage(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo('', f'¡{message} agregado de forma exitosa!')
    root.destroy()

#Muestra un mensaje emergente en caso de error
def errorMessage(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror('Ocurrió un error', message)

#Agregar datos a la tabla proveedor
def addProv(rif, nom, tel, email):
    try:
        #Confirmar si los datos ingresados no se encuentran almacenados
        confimacion = cursor.execute(f'SELECT "nom_prov" FROM "proveedor" WHERE "rif_prov"={rif}')
        if not confimacion:
            cursor.execute(f'INSERT INTO "proveedor" VALUES({rif}, "{nom}", "{tel}", "{email}");')
            conn.commit()
            succesfulAddMessage('Proveedor')
        else:
            errorMessage(f'El proveedor {nom} con el rif {rif} ya se encuentra registrado en la base de datos')
    except sqlite3.Error as e:
        errorMessage(e)
        print(f'Error: {e}')

#Mostrar todos los proveedores
def showProv():
    try:
        cursor.execute('SELECT * FROM "proveedor";')
        prov = cursor.fetchall()
        return prov
    except sqlite3.Error as e:
        errorMessage('Proveedor')
        print(f'Error: {e}')

#Agregar datos a la tabla insumos
def addIns(nom, desc, med, can, rif, pre):
    try:
        #Confirmar si los datos ingresados no se encuentran almacenados
        confirmacion = cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{nom}"')
        if not confirmacion:
            if med == '': #En caso de que medida este vacio, agrega "Unidad" como medida de forma automatica
                med = 'Unidades'
            cursor.execute(f'INSERT INTO "insumos" VALUES(NULL, "{nom}", "{desc}", "{med}", {can}, {rif}, {pre});')
            conn.commit()
            succesfulAddMessage('Insumo')
        else:
            errorMessage(f'El insumo {nom} ya se encuentra registrado en la base de datos')
    except sqlite3.Error as e:
        errorMessage(e)
        print(f'Error: {e}')

#Mostrar todos los insumos
def showIns():
    try:
        cursor.execute('SELECT * FROM "insumos";')
        ins = cursor.fetchall()
        return ins
    except sqlite3.Error as e:
        errorMessage('Insumo')
        print(f'Error: {e}')