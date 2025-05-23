import sqlite3
import os

currentDir = os.getcwd()
dbPath = os.path.join(currentDir, r'nom.db')

class Model():
    def connect(self):
        connection = sqlite3.connect(dbPath)
        return connection

    def insert(self, rif, nom, tel, email):
        conn = self.connect()
        cursor = conn.cursor()
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

    def show(self):
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