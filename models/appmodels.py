import sqlite3
import os

#Comandos para obtener el directorio actual y por ende la ubicacion de la BD
currentDir = os.getcwd()
dbPath = os.path.join(currentDir, r'nom.db')

#Clase padre para los modelos
class Model():
    #Funcion para realizar conexion a la BD
    def connect(self):
        connection = sqlite3.connect(dbPath)
        return connection

    #Funcion para agregar proveedores
    def insertProv(self, rif, nom, tel, email):
        conn = self.connect()
        cursor = conn.cursor()
        #Habilitacion de los constraints de las llaves foraneas, cosas de sqlite
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT "nom_prov" FROM "proveedor" WHERE "rif_prov"={rif}')
            conf = cursor.fetchone()
            if conf == None:
                try:
                    cursor.execute(f'INSERT INTO "proveedor" VALUES({rif}, "{nom}", "{tel}", "{email}")')
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

#Funcion para mostrar la tabla trnasicional
    def showInsRec(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT * FROM "ins_rec"')
            insrec = cursor.fetchall()
            if insrec != None:
                return insrec
            else:
                e = 'La tabla esta vacia'
                return e
        except sqlite3.Error as e:
            return e

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