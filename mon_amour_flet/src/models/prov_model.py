import sqlite3

class ProvModel():
    def __init__(self):
        self.conn = sqlite3.connect('nom.db')
        self.cursor = self.conn.cursor()

    #Funcion para retornar una lista con todos los datos de los proveedores
    def show_prov(self):
        self.cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            self.cursor.execute(f'SELECT * FROM "proveedor"')
            prov = self.cursor.fetchall()
            if prov:
                return prov
            else:
                return 'La tabla está vacía'
        except sqlite3.Error as e:
            return e
    
    #Funcion para agregar proveedores
    def add_prov(self, rif, nom, tel, email):
        self.cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            self.cursor.execute(f'SELECT "nom_prov" FROM "proveedor" WHERE "rif_prov"="{rif}"')
            conf = self.cursor.fetchone()
            if not conf:
                try:
                    self.cursor.execute(f'INSERT INTO "proveedor" VALUES("{rif}", "{nom}", "{tel}", "{email}")')
                    self.conn.commit()
                    return True
                except sqlite3.Error as e:
                    return e
            else:
                e = 'El proveedor ya se encuentra registrado'
                return e
        except sqlite3.Error as e:
            return e
    
    #Funcion para borrar proveedores
    def del_prov(self, values):
        self.cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            self.cursor.execute(f'SELECT "nom_prov" FROM "proveedor" WHERE "rif_prov"="{values[0]}"')
            conf = self.cursor.fetchone()
            if conf:
                try:
                    self.cursor.execute(f'DELETE FROM "proveedor" WHERE "rif_prov"="{values[0]}"')
                    self.conn.commit()
                    return True
                except sqlite3.Error as e:
                    return e
            else:
                return 'No existe un proveedor asociado a ese numero de rif'
        except sqlite3.Error as e:
            return e
        
    def edit_prov(self, rif, nom, tel, email):
        self.cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            self.cursor.execute(f'SELECT "nom_prov" FROM "proveedor" WHERE "rif_prov"="{rif}"')
            conf = self.cursor.fetchone()
            if conf:
                try:
                    self.cursor.execute(f'UPDATE "proveedor" SET "nom_prov"="{nom}", "tel_prov"="{tel}", "email_prov"="{email}" WHERE "rif_prov"="{rif}"')
                    self.conn.commit()
                    return True
                except sqlite3.Error as e:
                    return e
            else:
                return 'No existe el proveedor asociado a ese rif'
        except sqlite3.Error as e:
            return e