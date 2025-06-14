import sqlite3
import os
import hashlib

#Comandos para obtener el directorio actual y por ende la ubicacion de la BD
currentDir = os.getcwd()
dbPath = os.path.join(currentDir, r'nom.db')

#Clase padre para los modelos
class Model():
    #Funcion para realizar conexion a la BD
    def connect(self):
        connection = sqlite3.connect(dbPath)
        return connection

# -------- Agregar --------#

    #Funcion para agregar proveedores
    def insertProv(self, rif, nom, tel, email):
        conn = self.connect()
        cursor = conn.cursor()
        #Habilitacion de los constraints de las llaves foraneas, cosas de sqlite
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT "nom_prov" FROM "proveedor" WHERE "rif_prov"="{rif}"')
            conf = cursor.fetchone()
            if conf == None:
                try:
                    cursor.execute(f'INSERT INTO "proveedor" VALUES("{rif}", "{nom}", "{tel}", "{email}")')
                    result = True
                    conn.commit()
                    conn.close()
                    return result
                except sqlite3.Error as e:
                    return e
            else:
                e = 'El proveedor ya se encuentra registrado'
                return e
        except sqlite3.Error as e:
            return e

    #Funcion para agregar insumos
    def insertIns(self, nom, desc, med, can, rif, pre):
        conn = self.connect()
        cursor = conn.cursor()
        #Habilitacion de los constraints de las llaves foraneas, cosas de sqlite
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{nom}"')
            conf = cursor.fetchone()
            if conf == None:
                try:
                    cursor.execute(f'SELECT "rif_prov" FROM "proveedor" WHERE "nom_prov"="{rif}"')
                    rifT = cursor.fetchone()
                    rif = int(rifT[0])
                    cursor.execute(f'INSERT INTO "insumos" VALUES(NULL, "{nom}", "{desc}", "{med}", {can}, {rif}, {pre})')
                    result = True
                    conn.commit()
                    conn.close()
                    return result
                except sqlite3.Error as e:
                    return e
            else:
                e = 'El insumo ya se encuentra registrado'
                return e
        except sqlite3.Error as e:
            return e

    #Funcion para asociar insumos a receta
    def insertInsRec(self, rec, ins, can):
        conn = self.connect()
        cursor = conn.cursor()
        #Habilitacion de los constraints de las llaves foraneas, cosas de sqlite
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            #Obtener id del insumo
            cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{ins}"')
            insT = cursor.fetchone()
            ins = int(insT[0])
            #Obtener id de receta
            cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{rec}"')
            recT = cursor.fetchone()
            rec = int(recT[0])
            #Confirma que el insumo no se encuentre asociado a la receta
            cursor.execute(f'SELECT "can_ut_ins" FROM "ins_rec" WHERE "id_rec"={rec} AND "id_ins"={ins}')
            conf = cursor.fetchone()
            if conf == None:
                try:
                    #Asocia el insumo a la receta
                    cursor.execute(f'INSERT INTO "ins_rec" VALUES({rec}, {ins}, {can})')
                    conn.commit()
                    try:
                        #Lista de los insumos asociados a la receta
                        cursor.execute(f'SELECT "id_ins" FROM "ins_rec" WHERE "id_rec"={rec}')
                        idInsList = cursor.fetchall()
                        #Lista de los precios de los insumos asociados a la receta
                        preList = []
                        #Lista de la cantidad a utilizar de los insumos asociados a la receta
                        canList = []
                        for i in range(len(idInsList)):
                            #Consulta para obtener los precios de los insumos
                            cursor.execute(f'SELECT "pre_ins" FROM "insumos" WHERE "id_ins"={idInsList[i][0]}')
                            pre = cursor.fetchone()
                            preList.append(pre[0])
                            #Consulta para obtener las cantidades a utilizar de los insumos
                            cursor.execute(f'SELECT "can_ut_ins" FROM "ins_rec" WHERE "id_ins"={idInsList[i][0]} AND "id_rec"={rec}')
                            can = cursor.fetchone()
                            canList.append(can[0])
                        #Sumatoria de los precios totales de los insumos
                        preTot = 0
                        for i in range(len(preList)):
                            pre = canList[i] * preList[i]
                            preTot += pre
                        #Actualizacion del precio base de la receta
                        cursor.execute(f'UPDATE "recetas" SET "pre_rec"={preTot} WHERE "id_rec"={rec}')
                        conn.commit()
                        result = True
                        return result
                    except sqlite3.Error as e:
                        return e
                except sqlite3.Error as e:
                    return e
            else:
                e = 'El insumo ya se encuentra asociado a la receta'
                return e
        except sqlite3.Error as e:
            return e

    #Funcion para crear receta, solo nombre y descripcion
    def insertRecNom(self, nom, desc):
        conn = self.connect()
        cursor = conn.cursor()
        #Habilitacion de los constraints de las llaves foraneas, cosas de sqlite
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{nom}"')
            conf = cursor.fetchone()
            if conf == None:
                try:
                    cursor.execute(f'INSERT INTO "recetas" VALUES(NULL, "{nom}", "{desc}", 0, 0)')
                    result = True
                    conn.commit()
                    conn.close()
                    return result
                except sqlite3.Error as e:
                    return e
            else:
                e = 'La receta ya se encuentra registrada'
                return e
        except sqlite3.Error as e:
            return e

# -------- Mostrar -------- #

    #Funcion para mostrar proveedores
    def showProv(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT * FROM "proveedor"')
            prov = cursor.fetchall()
            if prov != None:
                return prov
            else:
                e = 'La tabla esta vacia'
                return e
        except sqlite3.Error as e:
            return e

    #Funcion para mostrar insumos
    def showIns(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT * FROM "insumos"')
            ins = cursor.fetchall()
            if ins != None:
                return ins
            else:
                e = 'La tabla esta vacia'
                return e
        except sqlite3.Error as e:
            return e

#Funcion para mostrar recetas
    def showRec(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT * FROM "recetas"')
            rec = cursor.fetchall()
            if rec != None:
                return rec
            else:
                e = 'La tabla esta vacia'
                return e
        except sqlite3.Error as e:
            return e

#Funcion para mostrar la tabla transicional
    def showInsRec(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute('SELECT * FROM "ins_rec"')
            insrec = cursor.fetchall()
            if insrec != None:
                return insrec
            else:
                e = 'La tabla esta vacia'
                return e
        except sqlite3.Error as e:
            return e


# -------- Devolver en lista -------- #

    #Funcion para devolver todos los nombres de proveedores
    def nomProvList(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT "nom_prov" FROM "proveedor"')
            nom = cursor.fetchall()
            if nom != None:
                return nom
            else:
                e = 'La tabla está vacía'
                return e
        except sqlite3.Error as e:
            return e

    #Funcion para devolver todos los nombres de insumos
    def nomInsList(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT "nom_ins" FROM "insumos"')
            nom = cursor.fetchall()
            if nom != None:
                return nom
            else:
                e = 'La tabla está vacía'
                return e
        except sqlite3.Error as e:
            return e

    #Funcion para devolver todos los nombres de recetas
    def nomRecList(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT "nom_rec" FROM "recetas"')
            nom = cursor.fetchall()
            if nom != None:
                return nom
            else:
                e = 'La tabla está vacía'
                return e
        except sqlite3.Error as e:
            return e

# -------- Actualizar -------- #

    #Actualizar cantidad de la receta
    def updCanRec(self, rec, can):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            #Obtener id de receta
            cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{rec}"')
            recT = cursor.fetchone()
            rec = int(recT[0])
            #Obtener ids de insumos asociados a la receta
            cursor.execute(f'SELECT "id_ins" FROM "ins_rec" WHERE "id_rec"={rec}')
            insList = cursor.fetchall()
            canUtList = [] #Lista de las cantidades necesarias del insumo
            canInsList = [] #Lista de la cantidad existente del insumo
            for i in range(len(insList)):
                #Sentencia para obtener las cantidades a utilizar de los insumos
                cursor.execute(f'SELECT "can_ut_ins" FROM "ins_rec" WHERE "id_ins"={insList[i][0]} AND "id_rec"={rec}')
                canUt = cursor.fetchone()
                canUtList.append(canUt[0])
                #Sentencia para obtener las cantidades en existencia de los insumos a utilizar
                cursor.execute(f'SELECT "can_ins" FROM "insumos" WHERE "id_ins"={insList[i][0]}')
                canIns = cursor.fetchone()
                canInsList.append(canIns[0])
            canList = [] #Lista de las cantidades de insumo necesarias en base a la cantidad a agregar de receta
            for i in range(len(canUtList)):
                #Multiplicación de la cantidad de insumo necesaria por la cantidad de veces a agregar la receta
                canX = canUtList[i] * can
                canList.append(canX)
            #Borrar despues
            print(canList)
            updt = False #Boolean para verificar si hay suficiente insumo para la creación de la receta
            c = 0
            for i in range(len(canList)):
                #Confirmación para saber si la cantidad de insumo existente es suficiente
                if canList[i] <= canInsList[i]:
                    updt = True
                else:
                    updt = False
                    break
                c += 1
            if updt == True:
                newCanInsList = [] #Lista de las nuevas cantidades de insumo existentes
                for i in range(len(canInsList)):
                    #Cantidad existente de insumo menos cantidad a utilizar
                    newCanIns = canInsList[i] - canList[i]
                    newCanInsList.append(newCanIns)
                for i in range(len(newCanInsList)):
                    try:
                        #Actualizar la cantidad del insumo
                        cursor.execute(f'UPDATE "insumos" SET "can_ins"={newCanInsList[i]} WHERE "id_ins"={insList[i][0]}')
                        conn.commit()
                        #Obtener la cantidad actual de la receta
                        cursor.execute(f'SELECT "can_rec" FROM "recetas" WHERE "id_rec"={rec}')
                        canRec = cursor.fetchone()
                        #Actualizar la cantidad de la receta
                        cursor.execute(f'UPDATE "recetas" SET "can_rec"={canRec[0] + can} WHERE "id_rec"={rec}')
                        conn.commit()
                        result = True
                        conn.close()
                        return result
                    except sqlite3.Error as e:
                        return e
            else:
                try:
                    cursor.execute(f'SELECT "nom_ins" FROM "insumos" WHERE "id_ins"={insList[c][0]}')
                    insE = cursor.fetchone()
                    conn.close()
                except sqlite3.Error as e:
                    return e
                e = f'No hay suficiente insumo {insE[0]}'
                return e
        except sqlite3.Error as e:
            return e

    #Actualizar insumos
    def updIns(self, ins, nom, desc, med, can, pre):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            #Obtener id de insumos
            cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{ins}"')
            idInsT = cursor.fetchone()
            idIns = int(idInsT[0])
            if idIns != None:
                #Confirmacion para cuando solo se escribe el nombre
                if nom != '' and desc == '' and med == '' and can == '' and pre == '':
                    try:
                        #Actualizar nombre del insumo
                        cursor.execute(f'UPDATE "insumos" SET "nom_ins"="{nom}" WHERE "id_ins"={idIns}')
                        conn.commit()
                        result = True
                        return result
                    except sqlite3.Error as e:
                        return e
                #Confirmacion para cuando solo se escribe la descripcion
                elif nom == '' and desc != '' and med == '' and can == '' and pre == '':
                    try:
                        #Actualizar descripcion del insumo
                        cursor.execute(f'UPDATE "insumos" SET "desc_ins"="{desc}" WHERE "id_ins"={idIns}')
                        conn.commit()
                        result = True
                        return result
                    except sqlite3.Error as e:
                        return e
                #Confirmacion para cuando solo se escribe la cantidad
                elif nom == '' and desc == '' and med == '' and can != '' and pre == '':
                    try:
                        #Actualizar descripcion del insumo
                        canNum = float(can)
                        cursor.execute(f'UPDATE "insumos" SET "can_ins"="{canNum}" WHERE "id_ins"={idIns}')
                        conn.commit()
                        result = True
                        return result
                    except sqlite3.Error as e:
                        return e
        except sqlite3.Error as e:
            return e

# -------- Inicio de sesión -------- #
    #Login
    def login(self, user, passw):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT "id_user" FROM "usuarios" WHERE "email_user"="{user}"')
            userId = cursor.fetchone()
            print(f'Id: {userId[0]}')
            if userId != None:
                hashedPassw = hashlib.sha256(passw.encode('utf-8')).hexdigest()
                cursor.execute(f'SELECT "passw_user" FROM "usuarios" WHERE "id_user"={int(userId[0])}')
                passwdBd = cursor.fetchone()
                print(f'PasswBd: {passwdBd[0]}')
                cursor.execute(f'SELECT "email_user" FROM "usuarios" WHERE "id_user"={int(userId[0])}')
                userBd = cursor.fetchone()
                print(f'UserBd: {userBd[0]}')
                if userBd[0] == user and passwdBd[0] == hashedPassw:
                    result = True
                    print(f'Result: {result}')
                    return result
                else:
                    e = 'Usuario o clave inválido'
                    print(f'Error: {e}')
                    return e
            else:
                e = 'Usuario no registrado en el sistema'
                print(f'Error: {e}')
                return e
        except sqlite3.Error as e:
            return e