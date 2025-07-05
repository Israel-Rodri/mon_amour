import sqlite3

class InsModel():
    def __init__(self):
        self.conn = sqlite3.connect('nom.db')
        self.cursor = self.conn.cursor()

    #Funcion para retornar una lista con todos los datos de los insumos
    def show_ins(self):
        self.cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            self.cursor.execute(f'SELECT * FROM "insumos"')
            ins = self.cursor.fetchall()
            if ins:
                return ins
            else:
                return 'La tabla está vacía'
        except sqlite3.Error as e:
            return e
    
    #Funcion para agregar insumos
    def add_ins(self, nom, desc, med, can, pre):
        self.cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            self.cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{nom}"')
            conf = self.cursor.fetchone()
            if not conf:
                try:
                    self.cursor.execute(f'INSERT INTO "insumos" VALUES(NULL, "{nom}", "{desc}", "{med}", {can}, {pre})')
                    self.conn.commit()
                    return True
                except sqlite3.Error as e:
                    return e
            else:
                e = 'El insumo ya se encuentra registrado'
                return e
        except sqlite3.Error as e:
            return e
    
    #Funcion para borrar insumos
    def del_ins(self, values):
        self.cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            self.cursor.execute(f'SELECT "nom_ins" FROM "insumos" WHERE "id_ins"="{values[0]}"')
            conf = self.cursor.fetchone()
            if conf:
                try:
                    self.cursor.execute(f'DELETE FROM "insumos" WHERE "id_ins"="{values[0]}"')
                    self.conn.commit()
                    return True
                except sqlite3.Error as e:
                    return e
            else:
                return 'No existe un insumo asociado a esa id'
        except sqlite3.Error as e:
            return e
    
    def edit_ins(self, id, nom, desc, med, can, pre):
        self.cursor.execute('PRAGMA "foreign_keys"=ON')
        try:
            self.cursor.execute(f'SELECT "nom_ins" FROM "insumos" WHERE "id_ins"="{id}"')
            conf = self.cursor.fetchone()
            if conf:
                try:
                    self.cursor.execute(f'UPDATE "insumos" SET "nom_ins"="{nom}", "desc_ins"="{desc}", "med_ins"="{med}", "can_ins"={can}, "pre_ins"={pre} WHERE "id_ins"={id}')
                    self.conn.commit()
                    return True
                except sqlite3.Error as e:
                    return e
            else:
                return 'No existe el proveedor asociado a ese rif'
        except sqlite3.Error as e:
            return e