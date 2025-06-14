import sqlite3
import os

currentDir = os.getcwd()
dbPath = os.path.join(currentDir, r'nom.db')

class ProvModels:
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