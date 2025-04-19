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

def succesfulUpdateMessage(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo('', f'¡{message} actualizado de forma exitosa!')
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
        cursor.execute(f'SELECT "nom_prov" FROM "proveedor" WHERE "rif_prov"={rif};')
        confirmacion = cursor.fetchone()
        if confirmacion == None:
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
        errorMessage(e)
        print(f'Error: {e}')

#Agregar datos a la tabla insumos
def addIns(nom, desc, med, can, rif, pre):
    try:
        #Confirmar si los datos ingresados no se encuentran almacenados
        cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{nom}";')
        confirmacion = cursor.fetchone()
        if confirmacion == None:
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
        errorMessage(e)
        print(f'Error: {e}')

#Agregar cliente
def addCli(ci, nom, ape, tel):
    try:
        cursor.execute(f'SELECT "nom_cli" FROM "clientes" WHERE "ci_cli"={ci};')
        confirmacion = cursor.fetchone()
        if confirmacion == None:
            cursor.execute(f'INSERT INTO "clientes" VALUES({ci}, "{nom}", "{ape}", "{tel}");')
            conn.commit()
            succesfulAddMessage('Cliente')
        else:
            errorMessage(f'El cliente {nom} con el numero de cedula {ci} ya se encuentra registrado')
    except sqlite3.Error as e:
        errorMessage(e)
        print(f'Error: {e}')

#Mostrar clientes
def showCli():
    try:
        cursor.execute('SELECT * FROM "clientes";')
        cli = cursor.fetchall()
        return cli
    except sqlite3.Error as e:
        errorMessage(e)
        print(f'Error: {e}')

#Crear recetas, falta modificar para que descuente insumos
def addRec(nom, desc):
    try:
        cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{nom}";')
        confirmacion = cursor.fetchone()
        if confirmacion == None:
            cursor.execute(f'INSERT INTO "recetas" VALUES(NULL, "{nom}", "{desc}", 0);')
            conn.commit()
            succesfulAddMessage('Receta')
        else:
            errorMessage(f'La receta {nom} ya se encuntra registrada en el sistema')
    except sqlite3.Error as e:
        errorMessage(e)
        print(f'Error: {e}')

#Agregar inumos y recetas a la tabla ins_rec
def addInsRec(rec, ins, can):
    try:
        cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{rec}";')
        receta = cursor.fetchone()
        recetaNum = int(receta[0])
        if receta != None:
            cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{ins}";')
            insumo = cursor.fetchone()
            insumoNum = int(insumo[0])
            if insumo != None:
                cursor.execute(f'INSERT INTO "ins_rec" VALUES({recetaNum}, {insumoNum}, {can})')
                conn.commit()
                succesfulAddMessage('Insumo a utilizar')
            else:
                errorMessage(f'El insumo {ins} no se encuentra registrado en el sistema')
        else:
            errorMessage(f'La receta {rec} no se encuentra registrada en el sistema')
    except sqlite3.Error as e:
        errorMessage(e)
        print(f'Error: {e}')

#Aumentar la cantidad disponible de una receta descontando los insumos
def updateCanRec(rec, canAddRec):
    try:
        cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{rec}";')
        idRec =  cursor.fetchone()
        idRecNum = int(idRec[0])
        cursor.execute(f'SELECT "pre_rec" FROM "recetas" WHERE "id_rec"={idRecNum}')
        preActRec = cursor.fetchone()
        cursor.execute(f'SELECT "can_rec" FROM "recetas" WHERE "id_rec"={idRecNum}')
        canActRec = cursor.fetchone()
        if idRec != None:
            if preActRec[0] == None:
                cursor.execute(f'SELECT "id_ins" FROM "ins_rec" WHERE "id_rec"={idRecNum};')
                idIns = cursor.fetchall()
                preList = []
                canList = []
                canInsList = []
                for i in range(len(idIns)):
                    cursor.execute(f'SELECT "pre_ins" FROM "insumos" WHERE "id_ins"={idIns[i][0]}')
                    pre = cursor.fetchone()
                    preList.append(pre[0])
                    cursor.execute(f'SELECT "can_ut_ins_rec" FROM "ins_rec" WHERE "id_ins"={idIns[i][0]}')
                    can = cursor.fetchone()
                    canList.append(can[0])
                    cursor.execute(f'SELECT "can_ins" FROM "insumos" WHERE "id_ins"={idIns[i][0]}')
                    canIns = cursor.fetchone()
                    canInsList.append(canIns[0])
                preVenList = []
                for i in range(len(idIns)):
                    if canList[i] * canAddRec <= canInsList[i]:
                        newCan = canInsList[i] - canList[i] * canAddRec
                        preVen = canList[i] * preList[i]
                        cursor.execute(f'UPDATE "insumos" SET "can_ins"={newCan} WHERE "id_ins"={idIns[i][0]}')
                        conn.commit()
                        preVenList.append(preVen)
                    else:
                        errorMessage('No hay suficiente insumo en existencia para la creacion de esta receta')
                cursor.execute(f'UPDATE "recetas" SET "can_rec"={canActRec[0] + canAddRec}, "pre_rec"={sum(preVenList)} WHERE "id_rec"={idRecNum}')
                conn.commit()
                succesfulUpdateMessage('Cantidad de receta')
            else:
                cursor.execute(f'SELECT "id_ins" FROM "ins_rec" WHERE "id_rec"={idRecNum};')
                idIns = cursor.fetchall()
                canList = []
                canInsList = []
                for i in range(len(idIns)):
                    cursor.execute(f'SELECT "can_ut_ins_rec" FROM "ins_rec" WHERE "id_ins"={idIns[i][0]}')
                    can = cursor.fetchone()
                    canList.append(can[0])
                    cursor.execute(f'SELECT "can_ins" FROM "insumos" WHERE "id_ins"={idIns[i][0]}')
                    canIns = cursor.fetchone()
                    canInsList.append(canIns[0])
                for i in range(len(idIns)):
                    if canList[i] * canAddRec <= canInsList[i]:
                        newCan = canInsList[i] - canList[i] * canAddRec
                        cursor.execute(f'UPDATE "insumos" SET "can_ins"={newCan} WHERE "id_ins"={idIns[i][0]}')
                        conn.commit()
                    else:
                        errorMessage('No hay suficiente insumo en existencia para la creacion de esta receta')
                cursor.execute(f'UPDATE "recetas" SET "can_rec"={canActRec[0] + canAddRec} WHERE "id_rec"={idRecNum}')
                succesfulUpdateMessage('Cantidad de receta')
        else:
            errorMessage(f'La receta {rec} no se encuentra registrada en el sistema')
    except sqlite3.Error as e:
        errorMessage(e)
        print(f'Error: {e}')

#Actualizar la cantidad de insumos
def updateCanIns(ins, canAddIns):
    try:
        cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{ins}"')
        idIns = cursor.fetchone()
        idInsNum = int(idIns[0])
        if idIns != None:
            cursor.execute(f'SELECT "can_ins" FROM "insumos" WHERE "id_ins"={idInsNum}')
            can = cursor.fetchone()
            cursor.execute(f'UPDATE "insumos" SET "can_ins"={can[0] + canAddIns} WHERE "id_ins"={idInsNum}')
            conn.commit()
            succesfulUpdateMessage('Insumo')
        else:
            errorMessage(f'El insumo {ins} no se encuentra registrado en el sistema')
    except sqlite3.Error as e:
        errorMessage(e)
        print(f'Error: {e}')

#Mostrar todas las recetas
def showRec():
    try:
        cursor.execute('SELECT * FROM "recetas";')
        rec = cursor.fetchall()
        return rec
    except sqlite3.Error as e:
        errorMessage(e)
        print(f'Error: {e}')