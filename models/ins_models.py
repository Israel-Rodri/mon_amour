import sqlite3
import os

#Comandos para obtener el directorio actual y por ende la ubicacion de la BD
currentDir = os.getcwd()
dbPath = os.path.join(currentDir, r'nom.db')

class InsModels:
    #Funcion para realizar conexion a la BD
    def connect(self):
        connection = sqlite3.connect(dbPath)
        return connection
    
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
                    cursor.execute(f'INSERT INTO "insumos" VALUES(NULL, "{nom}", "{desc}", "{med}", {can}, "{rif}", {pre})')
                    result = True
                    conn.commit()
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
                return 'El insumoa ya se encuetra registrado'
        except sqlite3.Error as e:
            cursor.close()
            conn.close()
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
                cursor.close()
                conn.close()
                return ins
            else:
                cursor.close()
                conn.close()
                return 'La tabla está vacía'
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
            if idIns:
                camposUpd = []
                valoresUpd = []
            if nom:
                camposUpd.append('"nom_ins"=?')
                valoresUpd.append(nom)
            if desc:
                camposUpd.append('"desc_ins"=?')
                valoresUpd.append(desc)
            if med:
                camposUpd.append('"med_ins"=?')
                valoresUpd.append(med)
            if can:
                camposUpd.append('"can_ins"=?')
                valoresUpd.append(can)
            if pre:
                camposUpd.append('"pre_ins"=?')
                valoresUpd.append(pre)
            if camposUpd:
                query = f'UPDATE "insumos" SET {", ".join(camposUpd)} WHERE "id_ins"={idIns}'
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
        except sqlite3.Error as e:
            cursor.close()
            conn.close()
            return e