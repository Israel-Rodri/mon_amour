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

    def upProv(self, nomAct, nom, tel, email):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT "rif_prov" FROM "proveedor" WHERE "nom_prov"="{nomAct}"')
            rifProvT = cursor.fetchone()
            rifProv = rifProvT[0]
            if rifProv:
                camposUpd = []
                valoresUpd = []
                if nom:
                    camposUpd.append('"nom_prov"=?')
                    valoresUpd.append(nom)
                if tel:
                    camposUpd.append('"tel_prov"=?')
                    valoresUpd.append(tel)
                if email:
                    camposUpd.append('"email_prov"=?')
                    valoresUpd.append(email)
                if camposUpd:
                    query = f'UPDATE "proveedor" SET {", ".join(camposUpd)} WHERE "rif_prov"="{rifProv}"'
                try:
                    cursor.execute(query, valoresUpd)
                    conn.commit()
                    result = True
                    cursor.close()
                    conn.close()
                    return result
                except sqlite3.Error as e:
                    cursor.close()
                    conn.close()
                    return e
            else:
                cursor.close()
                conn.close()
                return 'El proveedor seleccionado no se encuentra registrado en el sistema'
        except sqlite3.Error as e:
            cursor.close()
            conn.close()
            return e

    def delProv(self, prov):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            cursor.execute(f'SELECT "rif_prov" FROM "proveedor" WHERE "nom_prov"="{prov}"')
            rifProvT = cursor.fetchone()
            if rifProvT:
                rifProv = rifProvT[0]
                cursor.execute(f'DELETE FROM "proveedor" WHERE "rif_prov"="{rifProv}"')
                conn.commit()
                cursor.close()
                conn.close()
                return True
            else:
                cursor.close()
                conn.close()
                return 'El proveedor seleccionado no se encuentra registrado en el sistema'
        except sqlite3.Error as e:
            cursor.close()
            conn.close()
            return e