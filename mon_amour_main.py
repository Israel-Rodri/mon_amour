import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime
from tkinter import messagebox

conn = sqlite3.connect('C:/Users/ASUS/Documents/Prog/Mon amour/nom.db')
cursor = conn.cursor()

class Main:
    def __init__(self):
        self.mainwindow = tk.Tk()
        self.mainwindow.title('Prueba')
        self.mainwindow.geometry('1500x750')

        self.topmenu = tk.Frame(self.mainwindow, height=150, bg='#212c79')
        self.topmenu.pack(side='top', fill='x')

        self.insbtn = tk.Button(self.topmenu, text='Insumos', font=('Times New Roman', 18), command=self.insbutton)
        self.insbtn.grid(row=0, column=0, padx=15)
        self.provbtn = tk.Button(self.topmenu, text='Proveedores', font=('Times New Roman', 18), command=self.provbutton)
        self.provbtn.grid(row=0, column=1, padx=15)
        self.clibtn = tk.Button(self.topmenu, text='Clientes', font=('Times New Roman', 18), command=self.clibutton)
        self.clibtn.grid(row=0, column=2, padx=15)
        self.insrecbtn = tk.Button(self.topmenu, text='Insumos Recetas', font=('Times New Roman', 18), command=self.insrecbutton)
        self.insrecbtn.grid(row=0, column=3, padx=15)
        self.insrecbtn = tk.Button(self.topmenu, text='Recetas', font=('Times New Roman', 18), command=self.recbutton)
        self.insrecbtn.grid(row=0, column=4, padx=15)

        self.mainmenu = tk.Frame(self.mainwindow, bg='#d8f9ff')
        self.mainmenu.pack(side='right', fill='both', expand=True)

    def insbutton(self):
        self.mainwindow.destroy()
        x = Insumos()
        x

    def provbutton(self):
        self.mainwindow.destroy()
        x = Proveedores()
        x

    def recbutton(self):
        self.mainwindow.destroy()
        x = Recetas()
        x

    def clibutton(self):
        self.mainwindow.destroy()
        x = Clientes()
        x

    def insrecbutton(self):
        self.mainwindow.destroy()
        x = Insrec()
        x

    def showordbutton(self):
        self.mainwindow.destroy()
        x = Showord()
        x

    def newvenbutton(self):
        self.mainwindow.destroy()
        x = Newven()
        x

    def newrecbutton(self):
        self.mainwindow.destroy()
        x = Newrec()
        x

    def reload(self, clase):
        self.mainwindow.destroy()
        x = clase()
        x

class Insumos(Main):
    def __init__(self):
        super().__init__()
        self.updateinsmenu()
        self.addinsmenu()
        self.showins()
        self.mainwindow.mainloop()

    def showins(self):
        self.showtitle = tk.Label(self.mainmenu, text='Mostrar Insumos', font=('Times New Roman', 24), bg='#d8f9ff')
        self.showtitle.grid(row=7, column=0, pady=20)

        cursor.execute(f'SELECT * FROM "insumos"')
        ins = cursor.fetchall()
        r = 8
        variables = []
        for i in range(len(ins)):
            variables.append(i)
            variables[i] = tk.Label(self.mainmenu, text=ins[i], font=('Times New Roman', 18), bg='#d8f9ff')
            variables[i].grid(row=r, column=3)
            r += 1

    def addinsmenu(self): #Menu para agregar insumos
        self.addtitle = tk.Label(self.mainmenu, text='Agregar Insumo', font=('Times New Roman', 24), bg='#d8f9ff')
        self.addtitle.grid(row=0, column=2, pady=20)

        self.insnomLabel = tk.Label(self.mainmenu, text='Nombre Insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.insnomLabel.grid(row=1, column=2, padx=5)
        self.insnomentry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insnomentry.grid(row=1, column=3)

        self.insdesclabel = tk.Label(self.mainmenu, text='Descripcion Insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.insdesclabel.grid(row=2, column=2)
        self.insdescentry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insdescentry.grid(row=2, column=3)

        self.insmedlabel = tk.Label(self.mainmenu, text='Medida Insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.insmedlabel.grid(row=3, column=2)
        self.insmedentry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insmedentry.grid(row=3, column=3)

        self.inscanlabel = tk.Label(self.mainmenu, text='Cantidad Insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.inscanlabel.grid(row=4, column=2)
        self.inscanentry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.inscanentry.grid(row=4, column=3)

        self.insprelabel = tk.Label(self.mainmenu, text='Precio Insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.insprelabel.grid(row=5, column=2)
        self.inspreentry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))   
        self.inspreentry.grid(row=5, column=3)

        self.provCombo = ttk.Combobox(self.mainmenu, font=('Times New Roman', 16))
        self.provListVal = []
        self.provlistvalues()
        self.provCombo['values'] = self.provListVal
        self.provCombo.current(0)
        self.provCombo.grid(row=6, column=2)

        self.addinsbutton = tk.Button(self.mainmenu, text='Agregar Insumo', font=('Times New Roman', 18), command=self.addins)
        self.addinsbutton.grid(row=7, column=2, pady=10)

    def updateinsmenu(self): #menu para actualizar insumos
        self.updatetitle = tk.Label(self.mainmenu, text='Actualizar Insumo', font=('Times New Roman', 24), bg='#d8f9ff')
        self.updatetitle.grid(row=0, column=0, pady=20)

        self.insCombo = ttk.Combobox(self.mainmenu, font=('Times New Roman', 16))
        self.insListVal = []
        self.inslistvalues()
        self.insCombo['values'] = self.insListVal
        self.insCombo.current(0)
        self.insCombo.grid(row=1, column=0)

        self.insDescLabel = tk.Label(self.mainmenu, text='Descripcion Insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.insDescLabel.grid(row=2, column=0, padx=10)
        self.insDescEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insDescEntry.grid(row=2, column=1)

        self.insMedLabel = tk.Label(self.mainmenu, text='Medida Insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.insMedLabel.grid(row=3, column=0, padx=10)
        self.insMedEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insMedEntry.grid(row=3, column=1)

        self.insPreLabel = tk.Label(self.mainmenu, text='Precio Insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.insPreLabel.grid(row=4, column=0, padx=10)
        self.insPreEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insPreEntry.grid(row=4, column=1)

        self.updateInsButton = tk.Button(self.mainmenu, text='Actualizar Insumos', font=('Times New Roman', 18), command=self.updateins)
        self.updateInsButton.grid(row=5, column=0)

    def inslistvalues(self): #Funcion para obtener los nombres de insumos para un combobox
        cursor.execute(f'SELECT "nom_ins" FROM "insumos"')
        ins = cursor.fetchall()
        for i in range(len(ins)):
            self.insListVal.append(ins[i][0])

    def provlistvalues(self): #Funcion para obtener los nombres de proveedores para un combobox
        cursor.execute(f'SELECT "nom_prov" FROM "proveedor"')
        prov = cursor.fetchall()
        for i in range(len(prov)):
            self.provListVal.append(prov[i][0])

    def addins(self): #Metodo para agregar insumos
        insnom = self.insnomentry.get()
        if insnom == '':
            errormessage('Nombre del insumo no puede estar vacio')
            self.reload(Insumos)
        insdesc = self.insdescentry.get()
        if insdesc == '':
            errormessage('Descripcion del insumo no puede estar vacio')
            self.reload(Insumos)
        insmed = self.insmedentry.get()
        if insmed == '':
            errormessage('Unidad de medida del insumo no puede estar vacio')
            self.reload(Insumos)
        inscan = self.inscanentry.get()
        if inscan == '':
            errormessage('Cantidad del insumo no puede estar vacio')
            self.reload(Insumos)
        inscannum = float(inscan)
        inspre = self.inspreentry.get()
        if inspre == '':
            errormessage('Precio del insumo no puede estar vacio')
            self.reload(Insumos)
        insprenum = float(inspre)
        prov = self.provCombo.get()
        cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{insnom}"')
        conf = cursor.fetchone()
        if conf == None:
            try:
                cursor.execute(f'SELECT "rif_prov" FROM "proveedor" WHERE "nom_prov"="{prov}"')
                rifprov = cursor.fetchone()
                try:
                    cursor.execute(f'INSERT INTO "insumos" VALUES(NULL, "{insnom}", "{insdesc}", "{insmed}", {inscannum}, {rifprov[0]}, {insprenum})')
                    conn.commit()
                    succsefulmessage(f'Insumo {insnom} agregado de forma exitosa')
                    self.reload(Insumos)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            except sqlite3.Error as e:
                errormessage(e)
                print(f'Error: {e}')
        else:
            errormessage(f'El insumo {insnom} ya se encuentra registrado en el sistema')
            self.insnomentry.delete(0, tk.END)
            self.insdescentry.delete(0, tk.END)
            self.insmedentry.delete(0, tk.END)
            self.inscanentry.delete(0, tk.END)
            self.inspreentry.delete(0, tk.END)            

    def updateins(self): #Metodo para actualizar insumos
        insnom = self.insCombo.get()
        insdesc = self.insDescEntry.get()
        insmed = self.insMedEntry.get()
        inspre = self.insPreEntry.get()
        cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{insnom}"')
        idinsT = cursor.fetchone()
        if idinsT != None:
            idins = idinsT[0]
            if insdesc != '' and insmed == '' and inspre == '':
                try:
                    cursor.execute(f'UPDATE "insumos" SET "desc_ins"="{insdesc}" WHERE "id_ins"={idins}')
                    conn.commit()
                    succsefulmessage(f'Descripcion del insumo {insnom} actualizada exitosamente')
                    self.reload(Insumos)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif insdesc == '' and insmed != '' and inspre == '':
                try:
                    cursor.execute(f'UPDATE "insumos" SET "med_ins"="{insmed}" WHERE "id_ins"={idins}')
                    conn.commit()
                    succsefulmessage(f'Unidad de medida del insumos {insnom} actualizada de forma exitosa')
                    self.reload(Insumos)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif insdesc == '' and insmed == '' and inspre != '':
                try:
                    insprenum = float(inspre)
                    cursor.execute(f'UPDATE "insumos" SET "pre_ins"={insprenum} WHERE "id_ins"={idins}')
                    conn.commit()
                    succsefulmessage(f'Precio del insumo {insnom} actualizado exitosamente')
                    self.reload(Insumos)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif insdesc != '' and insmed != '' and inspre == '':
                try:
                    cursor.execute(f'UPDATE "insumos" SET "desc_ins"="{insdesc}" WHERE "id_ins"={idins}')
                    conn.commit()
                    cursor.execute(f'UPDATE "insumos" SET "med_ins"="{insmed}" WHERE "id_ins"={idins}')
                    conn.commit()
                    succsefulmessage(f'Descripcion y medida del insumo {insnom} acutalizadas de forma exitosa')
                    self.reload(Insumos)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif insdesc != '' and insmed == '' and inspre != '':
                try:
                    cursor.execute(f'UPDATE "insumos" SET "desc_ins"="{insdesc}" WHERE "id_ins"={idins}')
                    conn.commit()
                    insprenum = float(inspre)
                    cursor.execute(f'UPDATE "insumos" SET "pre_ins"={insprenum} WHERE "id_ins"={idins}')
                    conn.commit()
                    succsefulmessage(f'Descripcion y precio del insumo {insnom} actualizados de forma exitosa')
                    self.reload(Insumos)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif insdesc == '' and insmed != '' and inspre != '':
                try:
                    cursor.execute(f'UPDATE "insumos" SET "med_ins"="{insmed}" WHERE "id_ins"={idins}')
                    conn.commit()
                    insprenum = float(inspre)
                    cursor.execute(f'UPDATE "insumos" SET "pre_ins"={insprenum} WHERE "id_ins"={idins}')
                    conn.commit()
                    succsefulmessage(f'Medida y precio del insumo {insnom} acutalizados de forma exitosa')
                    self.reload(Insumos)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif insdesc != '' and insmed != '' and inspre != '':
                try:
                    cursor.execute(f'UPDATE "insumos" SET "desc_ins"="{insdesc}" WHERE "id_ins"={idins}')
                    conn.commit()
                    cursor.execute(f'UPDATE "insumos" SET "med_ins"="{insmed}" WHERE "id_ins"={idins}')
                    conn.commit()
                    insprenum = float(inspre)
                    cursor.execute(f'UPDATE "insumos" SET "pre_ins"={insprenum} WHERE "id_ins"={idins}')
                    conn.commit()
                    succsefulmessage(f'Descripcion, medida y precio del insumo {insnom} actualizados de forma exitosa')
                    self.reload(Insumos)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            else:
                errormessage('Deber rellenar al menos uno de los campos')
            self.insNomEntry.delete(0, tk.END)
            self.insDescEntry.delete(0, tk.END)
            self.insMedEntry.delete(0, tk.END)
            self.insPreEntry.delete(0, tk.END)
        else:
            errormessage(f'La receta con el nombre {insnom} no se encuentra registrada en el sistema')
            self.insNomEntry.delete(0, tk.END)
            self.insDescEntry.delete(0, tk.END)
            self.insMedEntry.delete(0, tk.END)
            self.insPreEntry.delete(0, tk.END)

class Proveedores(Main):
    def __init__(self):
        super().__init__()
        self.updateprovmenu()
        self.addprovmenu()
        self.showprov()
        self.mainwindow.mainloop()

    def showprov(self): #Menu para mostrar proveedores
        self.showtitle = tk.Label(self.mainmenu, text='Mostrar Proveedores', font=('Times New Roman', 24), bg='#d8f9ff')
        self.showtitle.grid(row=6, column=0, pady=20)

        cursor.execute(f'SELECT * FROM "proveedor"')
        prov = cursor.fetchall()
        r = 7
        variables = []
        for i in range(len(prov)):
            variables.append(i)
            variables[i] = tk.Label(self.mainmenu, text=prov[i], font=('Times New Roman', 18), bg='#d8f9ff')
            variables[i].grid(row=r)
            r += 1

    def addprovmenu(self): #Menu para agregar proveedores
        self.addtitle = tk.Label(self.mainmenu, text='Agregar Proveedor', font=('Times New Roman', 24), bg='#d8f9ff')   
        self.addtitle.grid(row=0, column=2, pady=20)

        self.provrifLabel = tk.Label(self.mainmenu, text='Rif Proveedor:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.provrifLabel.grid(row=1, column=2, padx=5)
        self.provrifentry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.provrifentry.grid(row=1, column=3)

        self.provnomLabel = tk.Label(self.mainmenu, text='Nombre Proveedor:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.provnomLabel.grid(row=2, column=2)
        self.provnomentry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.provnomentry.grid(row=2, column=3)

        self.provtelLabel = tk.Label(self.mainmenu, text='Telefono Proveedor:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.provtelLabel.grid(row=3, column=2)
        self.provtelentry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.provtelentry.grid(row=3, column=3)

        self.provemailLabel = tk.Label(self.mainmenu, text='Email Proveedor:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.provemailLabel.grid(row=4, column=2)
        self.provemailentry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.provemailentry.grid(row=4, column=3)

        self.addprovbutton = tk.Button(self.mainmenu, text='Agregar Proveedor', font=('Times New Roman', 18), command=self.addprov)
        self.addprovbutton.grid(row=5, column=2, pady=10)

    def updateprovmenu(self): #Menu para actualizar proveedores
        self.updatetitle = tk.Label(self.mainmenu, text='Actualizar Proveedores', font=('Times New Roman', 24), bg='#d8f9ff')
        self.updatetitle.grid(row=0, column=0, pady=20)

        self.provCombo = ttk.Combobox(self.mainmenu, font=('Times New Roman', 16))
        self.provListval = []
        self.provlistvalues()
        self.provCombo['values'] = self.provListval
        self.provCombo.current(0)
        self.provCombo.grid(row=1, column=0)

        self.provNomLabel = tk.Label(self.mainmenu, text='Nombre Proveedor:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.provNomLabel.grid(row=2, column=0, padx=10)
        self.provNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.provNomEntry.grid(row=2, column=1)

        self.provTelLabel = tk.Label(self.mainmenu, text='Telefono Proveedor:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.provTelLabel.grid(row=3, column=0, padx=10)
        self.provTelEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.provTelEntry.grid(row=3, column=1)

        self.provEmailLabel = tk.Label(self.mainmenu, text='Email Proveedor:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.provEmailLabel.grid(row=4, column=0, padx=10)
        self.provEmailEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.provEmailEntry.grid(row=4, column=1)

        self.updateProvButton = tk.Button(self.mainmenu, text='Actualizar Proveedor', font=('Times New Roman', 18), command=self.updateprov)
        self.updateProvButton.grid(row=5, column=0)

    def addprov(self): #Metodo para agregar proveedores
        provrif = self.provrifentry.get()
        if provrif == '':
            errormessage('Rif del proveedor no puede estar vacio')
            self.reload(Proveedores)
        provnom = self.provnomentry.get()
        if provnom == '':
            errormessage('Nombre del proveedor no puede estar vacio')
            self.reload(Proveedores)
        provtel = self.provtelentry.get()
        if provtel == '':
            errormessage('Telefono del proveedor no puede estar vacio')
            self.reload(Proveedores)
        provemail = self.provemailentry.get()
        if provemail == '':
            errormessage('Email del proveedor no puede estar vacio')
            self.reload(Proveedores)
        cursor.execute(f'SELECT "nom_prov" FROM "proveedor" WHERE "rif_prov"="{provrif}"')
        conf = cursor.fetchone()
        if conf == None:
            try:
                cursor.execute(f'INSERT INTO "proveedor" VALUES("{provrif}", "{provnom}", "{provtel}", "{provemail}")')
                conn.commit()
                succsefulmessage(f'Proveedor {provnom} agregado de forma exitosa')
                self.reload(Proveedores)
            except sqlite3.Error as e:
                errormessage(e)
                print(f'Error: {e}')
        else:
            errormessage(f'El rif {provrif} ya se encuentra registrado en el sistema')
            self.provrifentry.delete(0, tk.END)
            self.provnomentry.delete(0, tk.END)
            self.provtelentry.delete(0, tk.END)
            self.provemailentry.delete(0, tk.END)

    def provlistvalues(self): #Funcion para obtener los nombres de proveedores para un combobox
        cursor.execute('SELECT "nom_prov" FROM "proveedor"')
        prov = cursor.fetchall()
        for i in range(len(prov)):
            self.provListval.append(prov[i][0])

    def updateprov(self):
        prov = self.provList.get()
        nom = self.provNomEntry.get()
        tel = self.provTelEntry.get()
        email = self.provEmailEntry.get()
        cursor.execute(f'SELECT "rif_prov" FROM "proveedor" WHERE "nom_prov"="{prov}"')
        conf = cursor.fetchone()
        if conf != None:
            if nom != '' and tel == '' and email == '':
                try:
                    cursor.execute(f'UPDATE "proveedor" SET "nom_prov"="{nom}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    succsefulmessage(f'Nombre del proveedor con el rif {conf[0]} actualizado de forma exitosa')
                    self.reload(Proveedores)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom == '' and tel != '' and email == '':
                try:
                    cursor.execute(f'UPDATE "proveedor" SET "tel_prov"="{tel}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    succsefulmessage(f'Telefono del proveedor {prov} actualizado de forma exitosa')
                    self.reload(Proveedores)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom == '' and tel == '' and email != '':
                try:
                    cursor.execute(f'UPDATE "proveedor" SET "email_prov"="{email}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    succsefulmessage(f'Email del proveedor {prov} actualizado de forma exitosa')
                    self.reload(Proveedores)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom != '' and tel != '' and email == '':
                try:
                    cursor.execute(f'UPDATE "proveedor" set "nom_prov"="{nom}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    cursor.execute(f'UPDATE "proveedor" SET "tel_prov"="{tel}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    succsefulmessage(f'Nombre y telefono del proveedor {prov} actualizados de forma exitosa')
                    self.reload(Proveedores)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom != '' and tel == '' and email != '':
                try:
                    cursor.execute(f'UPDATE "proveedor" set "nom_prov"="{nom}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    cursor.execute(f'UPDATE "proveedor" SET "email_prov"="{email}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    succsefulmessage(f'Nombre y email del proveedor {prov} actualizados de forma exitosa')
                    self.reload(Proveedores)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom == '' and tel != '' and email != '':
                try:
                    cursor.execute(f'UPDATE "proveedor" SET "tel_prov"="{tel}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    cursor.execute(f'UPDATE "proveedor" SET "email_prov"="{email}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    succsefulmessage(f'Telefono y email del proveedor {prov} actualizados de forma exitosa')
                    self.reload(Proveedores)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom != '' and tel != '' and email != '':
                try:
                    cursor.execute(f'UPDATE "proveedor" set "nom_prov"="{nom}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    cursor.execute(f'UPDATE "proveedor" SET "tel_prov"="{tel}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    cursor.execute(f'UPDATE "proveedor" SET "email_prov"="{email}" WHERE "rif_prov"={conf[0]}')
                    conn.commit()
                    succsefulmessage(f'Nombre, telefono y email del proveedor {prov} actualizados de forma exitosa')
                    self.reload(Proveedores)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            else:
                errormessage('Debe rellenar al menos uno de los campos')
            self.provRifEntry.delete(0, tk.END)
            self.provNomEntry.delete(0, tk.END)
            self.provTelEntry.delete(0, tk.END)
            self.provEmailEntry.delete(0, tk.END)
        else:
            errormessage(f'El rif {conf[0]} no se encuentra asociado a ningun proveedor')
            self.provRifEntry.delete(0, tk.END)
            self.provNomEntry.delete(0, tk.END)
            self.provTelEntry.delete(0, tk.END)
            self.provEmailEntry.delete(0, tk.END)

class Recetas(Main):
    def __init__(self):
        super().__init__()
        self.addcanrecmenu()
        self.addrecmenu()
        self.addinsrecmenu()
        self.showrec()
        self.mainwindow.mainloop()

    def addcanrecmenu(self): #Menu para aumentar la cantidad de receta
        self.addcanrectitle = tk.Label(self.mainmenu, text='Agregar cantidad de receta', font=('Times New Roman', 24), bg='#d8f9ff')
        self.addcanrectitle.grid(row=0, column=0, pady=20)

        self.addcanrecCombo = ttk.Combobox(self.mainmenu, font=('Times New Roman', 16))
        self.addcanrecListval = []
        self.reclistvalues()
        self.addcanrecCombo['values'] = self.addcanrecListval
        self.addcanrecCombo.current(0)
        self.addcanrecCombo.grid(row=1, column=0)

        self.addcan = tk.Spinbox(self.mainmenu, from_=0, to=100, increment=1, font=('Times New Roman', 16))
        self.addcan.grid(row=2, column=0)

        self.addRecButton = tk.Button(self.mainmenu, text='Agregar cantidad de receta', font=('Times New Roman', 18), command=self.addcanrec)
        self.addRecButton.grid(row=3, column=0, pady=10)

    def addrecmenu(self): #Menu para crear nueva receta (solo nombre y descripcion)
        self.addrectitle = tk.Label(self.mainmenu, text='Agregar receta', font=('Times New Roman', 24), bg='#d8f9ff')
        self.addrectitle.grid(row=0, column=1, pady=20)

        self.addrecnomLabel = tk.Label(self.mainmenu, text='Nombre receta:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.addrecnomLabel.grid(row=1, column=1, padx=5)    
        self.addrecnom = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addrecnom.grid(row=1, column=2)

        self.addrecdescLabel = tk.Label(self.mainmenu, text='Descripcion receta', font=('Times New Roman', 18), bg='#d8f9ff')
        self.addrecdescLabel.grid(row=2, column=1)
        self.addrecdesc = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addrecdesc.grid(row=2, column=2)

        self.addrecButton = tk.Button(self.mainmenu, text='Agregar receta', font=('Times New Roman', 18), command=self.addrec)
        self.addrecButton.grid(row=3, column=1, pady=10)

    def addinsrecmenu(self):
        self.addinsrectitle = tk.Label(self.mainmenu, text='Asociar insumos a receta', font=('Times New Roman', 24), bg='#d8f9ff')
        self.addinsrectitle.grid(row=0, column=3, pady=20)

        self.addrecCombo = ttk.Combobox(self.mainmenu, font=('Times New Roman', 16))
        self.addcanrecListval = []
        self.reclistvalues()
        self.addrecCombo['values'] = self.addcanrecListval
        self.addrecCombo.current(0)
        self.addrecCombo.grid(row=1, column=3)

        self.addinsCombo = ttk.Combobox(self.mainmenu, font=('Times New Roman', 16))
        self.addinsListval = []
        self.inslistvalues()
        self.addinsCombo['values'] = self.addinsListval
        self.addinsCombo.current(0)
        self.addinsCombo.grid(row=2, column=3)

        self.caninsLabel = tk.Label(self.mainmenu, text='Cantidad a utilizar del insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.caninsLabel.grid(row=3, column=3, padx=10)
        self.caninsEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.caninsEntry.grid(row=3, column=4)

        self.addinsrecButton = tk.Button(self.mainmenu, text='Asociar insumo', font=('Times New Roman', 18), command=self.addinsrec)
        self.addinsrecButton.grid(row=4, column=3, pady=10)

    def reclistvalues(self): #Funcion para obtener los nombres de receta para un combobox
        cursor.execute(f'SELECT "nom_rec" FROM "recetas"')
        rec = cursor.fetchall()
        for i in range(len(rec)):
            self.addcanrecListval.append(rec[i][0])

    def inslistvalues(self): #Funcion para obtner los nombres de los insumos para un combobox
        cursor.execute(f'SELECT "nom_ins" FROM "insumos"')
        ins = cursor.fetchall()
        for i in range(len(ins)):
            self.addinsListval.append(ins[i][0])

    def addinsrec(self): #Metodo para asociar insumos a recetas
        recnom = self.addrecCombo.get()
        insnom = self.addinsCombo.get()
        canins = self.caninsEntry.get()
        if canins == '':
            errormessage('La cantidad a utilizar del insumo no puede estar vacia')
            self.reload(Recetas)
        caninsnum = float(canins)
        cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{recnom}"')
        recid = cursor.fetchone()
        cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{insnom}"')
        insid = cursor.fetchone()
        cursor.execute(f'SELECT "can_ut_ins" FROM "ins_rec" WHERE "id_rec"={recid[0]} AND "id_ins"={insid[0]}')
        conf = cursor.fetchone()
        if conf == None:
            try:
                cursor.execute(f'INSERT INTO "ins_rec" VALUES({recid[0]}, {insid[0]}, {caninsnum})')
                conn.commit()
                succsefulmessage(f'Insumo {insnom} asociado exitosamente a la receta {recnom}')
                self.addpricerec()
                self.reload(Recetas)
            except sqlite3.Error as e:
                errormessage(e)
                print(f'Error: {e}')
                self.reload(Recetas)
        else:
            errormessage(f'El insumo {insnom} ya se encuentra asociado a la receta {recnom}')
            self.caninsEntry.delete(0, tk.END)

    def addrec(self): #Metodo para agregar receta (solo nombre y descripcion)
        rec = self.addrecnom.get()
        if rec == '':
            errormessage('Nombre de la receta no puede estar vacio')
            self.reload(Recetas)
        desc = self.addrecdesc.get()
        if desc == '':
            errormessage('Descripcion de la receta no puede estar vacio')
            self.reload(Recetas)
        cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{rec}"')
        conf = cursor.fetchone()
        if conf == None:
            try:
                cursor.execute(f'INSERT INTO "recetas" VALUES(NULL, "{rec}", "{desc}", 0, 0)')
                conn.commit()
                succsefulmessage(f'Receta {rec} agregada de forma exitosa')
                self.reload(Recetas)
            except sqlite3.Error as e:
                errormessage(e)
                print(f'Error: {e}')
                self.reload(Recetas)
        else:
            errormessage(f'La receta {rec} ya se encuentra registrada en el sistema')
            self.addrecnom.delete(0, tk.END)
            self.addrecdesc.delete(0, tk.END)

    def addcanrec(self): #Metodo para aumentar la cantidad de receta
        rec = self.addcanrecCombo.get() #Nombre de la receta a agregar
        reccan = self.addcan.get()
        reccannum = int(reccan) #Cantidad a agregar de la receta
        if reccannum == 0:
            errormessage('La cantidad a agregar no puede ser igual a 0')
            self.reload(Recetas)
        cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{rec}"')
        idrec = cursor.fetchone()
        cursor.execute(f'SELECT "id_ins" FROM "ins_rec" WHERE "id_rec"={idrec[0]}')
        idinslistSF = cursor.fetchall()
        idinslist = [] #Lista de id de insumos a utilizar en la receta
        for i in idinslistSF:
            idinslist.append(i[0])
        cursor.execute(f'SELECT "can_ut_ins" FROM "ins_rec" WHERE "id_rec"={idrec[0]}')
        canutlistSF = cursor.fetchall()
        canutlist = [] 
        for i in canutlistSF:
            canutlist.append(i[0])
        canlist = [] #Cantidad de insumo a utilizar
        for i in canutlist:
            canlist.append(i * reccannum)
        canactins = [] #Cantidades existentes del insumo
        for i in range(len(canlist)):
            cursor.execute(f'SELECT "can_ins" FROM "insumos" WHERE "id_ins"={idinslist[i]}')
            can = cursor.fetchone()
            canactins.append(can[0])
        conf = False
        for i in range(len(canlist)):
            if canactins[i] >= canlist[i]:
                conf = True
            else:
                conf = False
                cursor.execute(f'SELECT "nom_ins" FROM "insumos" WHERE "id_ins"={idinslist[i]}')
                insnom = cursor.fetchone()
                errormessage(f'No es posible agregar receta, no hay suficiente {insnom[0]}')
                break
        if conf == True:
            for i in range(len(canlist)):
                try:
                    newcanins = canactins[i] - canlist[i]
                    succsefulmessage(f'Insumo id {idinslist[i]}\ncantidad anterior: {canactins[i]}\nnueva cantidad {newcanins}') #Linea para confirmar que sirve
                    cursor.execute(f'UPDATE "insumos" SET "can_ins"={newcanins} WHERE "id_ins"={idinslist[i]}')
                    conn.commit()
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
                    self.reload(Recetas)
            try:
                cursor.execute(f'SELECT "can_rec" FROM "recetas" WHERE "nom_rec"="{rec}"')
                canactrec = cursor.fetchone()
                newcanrec = canactrec[0] + reccannum
                succsefulmessage(f'Cantidad anterior receta: {canactrec[0]}\nCantidad nueva receta: {newcanrec}') #Linea para confirmar que sirve
                cursor.execute(f'UPDATE "recetas" SET "can_rec"={newcanrec} WHERE "nom_rec"="{rec}"')
            except sqlite3.Error as e:
                errormessage(e)
                print(f'Error: {e}')
                self.reload(Recetas)
            succsefulmessage(f'Cantidad de la receta {rec} actualizada de forma exitosa')
        else:
            self.reload(Recetas)

    def addpricerec(self):
        recnom = self.addrecCombo.get()
        cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{recnom}"')
        recid = cursor.fetchone()
        cursor.execute(f'SELECT "id_ins" FROM "ins_rec" WHERE "id_rec"={recid[0]}')
        insidlistSF = cursor.fetchall()
        insidlist = []
        for i in insidlistSF:
            insidlist.append(i[0])
        pricelist = []
        canlist = []
        for i in insidlist:
            try:
                cursor.execute(f'SELECT "pre_ins" FROM "insumos" WHERE "id_ins"={i}')
                price = cursor.fetchone()
                pricelist.append(price[0])
                cursor.execute(f'SELECT "can_ut_ins" FROM "ins_rec" WHERE "id_ins"={i} AND "id_rec"={recid[0]}')
                can = cursor.fetchone()
                canlist.append(can[0])
            except sqlite3.Error as e:
                errormessage(e)
                print(f'Error: {e}')
        pricetot = []
        for i in range(len(insidlist)):
            pricetot.append(pricelist[i] * canlist[i])
        pricefinal = sum(pricetot)
        try:
            cursor.execute(f'UPDATE "recetas" SET "pre_rec"={pricefinal} WHERE "id_rec"={recid[0]}')
            conn.commit()
            succsefulmessage(f'Precio de la receta {recnom} actualizado de forma exitosa')
        except sqlite3.Error as e:
            errormessage(e)
            print(f'Error: {e}')

    def showrec(self):
        self.showtitle = tk.Label(self.mainmenu, text='Mostrar Recetas', font=('Times New Roman', 24), bg='#d8f9ff')
        self.showtitle.grid(row=5, column=0, pady=20)

        cursor.execute(f'SELECT * FROM "recetas"')
        prov = cursor.fetchall()
        r = 7
        variables = []
        for i in range(len(prov)):
            variables.append(i)
            variables[i] = tk.Label(self.mainmenu, text=prov[i], font=('Times New Roman', 18), bg='#d8f9ff')
            variables[i].grid(row=r)
            r += 1

class Clientes(Main):
    def __init__(self):
        super().__init__()
        self.updateclimenu()
        self.showcli()
        self.mainwindow.mainloop()

    def showcli(self):
        self.showtitle = tk.Label(self.mainmenu, text='Mostrar Clientes', font=('Times New Roman', 24), bg='#d8f9ff')
        self.showtitle.grid(row=6, column=0, pady=20)

        cursor.execute(f'SELECT * FROM "clientes"')
        cli = cursor.fetchall()
        r = 7
        variables = []
        for i in range(len(cli)):
            variables.append(i)
            variables[i] = tk.Label(self.mainmenu, text=cli[i], font=('Times New Roman', 18), bg='#d8f9ff')
            variables[i].grid(row=r)
            r += 1

    def updateclimenu(self):
        self.updatetitle = tk.Label(self.mainmenu, text='Actualizar Clientes', font=('Times New Roman', 24), bg='#d8f9ff')
        self.updatetitle.grid(row=0, column=0, pady=20)

        self.cliCiLabel = tk.Label(self.mainmenu, text='Cedula cliente:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.cliCiLabel.grid(row=1, column=0, padx=10)
        self.cliCiEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.cliCiEntry.grid(row=1, column=1)

        self.cliNomLabel = tk.Label(self.mainmenu, text='Nombre cliente:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.cliNomLabel.grid(row=2, column=0, padx=10)
        self.cliNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.cliNomEntry.grid(row=2, column=1)

        self.cliApeLabel = tk.Label(self.mainmenu, text='Apellido cliente:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.cliApeLabel.grid(row=3, column=0, padx=10)
        self.cliApeEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.cliApeEntry.grid(row=3, column=1)

        self.cliTelLabel = tk.Label(self.mainmenu, text='Telefono cliente:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.cliTelLabel.grid(row=4, column=0, padx=10)
        self.cliTelEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.cliTelEntry.grid(row=4, column=1)

        self.updateCliButton = tk.Button(self.mainmenu, text='Actualizar Cliente', font=('Times New Roman', 18), command=self.updatecli)
        self.updateCliButton.grid(row=5, column=0)

    def updatecli(self):
        ci = self.cliCiEntry.get()
        if ci == '':
            errormessage('Cedula no puede estar vacio')
            self.reload(Clientes)
        cinum = int(ci)
        nom = self.cliNomEntry.get()
        ape = self.cliApeEntry.get()
        tel = self.cliTelEntry.get()
        cursor.execute(f'SELECT "nom_cli" FROM "clientes" WHERE "ci_cli"={cinum}')
        conf = cursor.fetchone()
        if conf != None:
            if nom != '' and ape == '' and tel == '':
                try:
                    cursor.execute(f'UPDATE "clientes" SET "nom_cli"="{nom}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    succsefulmessage(f'Nombre del cliente con la cedula {cinum} actualizada de forma exitosa')
                    self.reload(Clientes)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom == '' and ape != '' and tel == '':
                try:
                    cursor.execute(f'UPDATE "clientes" SET "ape_cli"="{ape}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    succsefulmessage(f'Apellido del cliente {conf[0]} actualizado de forma exitosa')
                    self.reload(Clientes)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom == '' and ape == '' and tel != '':
                try:
                    cursor.execute(f'UPDATE "clientes" SET "tel_cli"="{tel}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    succsefulmessage(f'Telefono del cliente {conf[0]} actualizado de forma exitosa')
                    self.reload(Clientes)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom != '' and ape != '' and tel == '':
                try:
                    cursor.execute(f'UPDATE "clientes" SET "nom_cli"="{nom}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    cursor.execute(f'UPDATE "clientes" SET "ape_cli"="{ape}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    succsefulmessage(f'Nombre y apellido del cliente con la cedula {cinum} actualizados de forma exitosa')
                    self.reload(Clientes)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom != '' and ape == '' and tel != '':
                try:
                    cursor.execute(f'UPDATE "clientes" SET "nom_cli"="{nom}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    cursor.execute(f'UPDATE "clientes" SET "tel_cli"="{tel}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    succsefulmessage(f'Nonbre y telefono del cliente con la cedula {cinum} actualizados de forma exitosa')
                    self.reload(Clientes)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom == '' and ape != '' and tel != '':
                try:
                    cursor.execute(f'UPDATE "clientes" SET "ape_cli"="{ape}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    cursor.execute(f'UPDATE "clientes" SET "tel_cli"="{tel}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    succsefulmessage(f'Apellido y telefono del cliente {conf[0]} actualizados de forma exitosa')
                    self.reload(Clientes)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            elif nom != '' and ape != '' and tel != '':
                try:
                    cursor.execute(f'UPDATE "clientes" SET "nom_cli"="{nom}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    cursor.execute(f'UPDATE "clientes" SET "ape_cli"="{ape}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    cursor.execute(f'UPDATE "clientes" SET "tel_cli"="{tel}" WHERE "ci_cli"={cinum}')
                    conn.commit()
                    succsefulmessage(f'Nombre, apellido y telefono del cliente con la cedula {cinum} actualizados de forma exitosa')
                    self.reload(Clientes)
                except sqlite3.Error as e:
                    errormessage(e)
                    print(f'Error: {e}')
            else:
                errormessage('Debe rellenar al menos uno de los campos')
            self.cliCiEntry.delete(0, tk.END)
            self.cliNomEntry.delete(0, tk.END)
            self.cliApeEntry.delete(0, tk.END)
            self.cliTelEntry.delete(0, tk.END)
        else:
            errormessage(f'No existe ningun cliente asociado a la cedula {cinum}')
            self.cliCiEntry.delete(0, tk.END)
            self.cliNomEntry.delete(0, tk.END)
            self.cliApeEntry.delete(0, tk.END)
            self.cliTelEntry.delete(0, tk.END)

class Insrec(Main):
    def __init__(self):
        super().__init__()
        self.updateinsrecmenu()
        self.showinsrec()
        self.mainwindow.mainloop()

    def showinsrec(self):
        self.showtitle = tk.Label(self.mainmenu, text='Mostrar Insumos utilizados en recetas', font=('Times New Roman', 24), bg='#d8f9ff')
        self.showtitle.grid(row=5, column=0, pady=20)

        cursor.execute(f'SELECT * FROM "ins_rec"')
        ins_rec = cursor.fetchall()
        r = 6
        variables = []
        for i in range(len(ins_rec)):
            variables.append(i)
            variables[i] = tk.Label(self.mainmenu, text=ins_rec[i], font=('Times New Roman', 18), bg='#d8f9ff')
            variables[i].grid(row=r)
            r += 1

    def updateinsrecmenu(self):
        self.updatetitle = tk.Label(self.mainmenu, text='Actualizar Insumos a utilizar', font=('Times New Roman', 24), bg='#d8f9ff')
        self.updatetitle.grid(row=0, column=0, pady=20)

        self.recNomLabel = tk.Label(self.mainmenu, text='Nombre de la receta:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.recNomLabel.grid(row=1, column=0, padx=10)
        self.recNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.recNomEntry.grid(row=1, column=1)

        self.insNomLabel = tk.Label(self.mainmenu, text='Nombre del insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.insNomLabel.grid(row=2, column=0, padx=10)
        self.insNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insNomEntry.grid(row=2, column=1)

        self.insCanLabel = tk.Label(self.mainmenu, text='Cantidad a utilizar del insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.insCanLabel.grid(row=3, column=0, padx=10)
        self.insCanEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insCanEntry.grid(row=3, column=1)

        self.updateInsButton = tk.Button(self.mainmenu, text='Actualizar Insumo a utilizar', font=('Times New Roman', 18), command=self.updateinsrec)
        self.updateInsButton.grid(row=4, column=0)

    def updateinsrec(self):
        recnom = self.recNomEntry.get()
        if recnom == '':
            errormessage('Nombre de receta no puede estar vacio')
            self.reload(Insrec)
        insnom = self.insNomEntry.get()
        if insnom == '':
            errormessage('Nombre del insumo no puede estar vacio')
            self.reload(Insrec)
        inscan = self.insCanEntry.get()
        if inscan == '':
            errormessage('Cantidad a utilizar del insumo no puede estar vacio')
            self.reload(Insrec)
        inscannum = float(inscan)
        cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{recnom}"')
        recid = cursor.fetchone()
        cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{insnom}"')
        insid = cursor.fetchone()
        cursor.execute(f'SELECT "can_ut_ins" FROM "ins_rec" WHERE "id_rec"={recid[0]} AND "id_ins"={insid[0]}')
        conf = cursor.fetchone()
        if conf != None:
            try:
                cursor.execute(f'UPDATE "ins_rec" SET "can_ut_ins"={inscannum} WHERE "id_rec"={recid[0]} AND "id_ins"={insid[0]}')
                conn.commit()
                succsefulmessage(f'Cantidad a utilizar de {insnom} en la receta {recnom} actualizado de forma exitosa')
                self.reload(Insrec)
            except sqlite3.Error as e:
                errormessage(e)
                print(f'Error_ {e}')
            self.recNomEntry.delete(0, tk.END)
            self.insNomEntry.delete(0, tk.END)
            self.insCanEntry.delete(0, tk.END)
        else:
            errormessage(f'El insumo {insnom} no se encuentra asociado a la receta {recnom}')
            self.recNomEntry.delete(0, tk.END)
            self.insNomEntry.delete(0, tk.END)
            self.insCanEntry.delete(0, tk.END)

class Showord(Main):
    def __init__(self):
        super().__init__()
        self.showord()
        self.mainwindow.mainloop()

    def showord(self):
        cursor.execute(f'SELECT * FROM "ordenes"')
        ord = cursor.fetchall()
        r = 0
        variables = []
        for i in range(len(ord)):
            variables.append(i)
            variables[i] = tk.Label(self.mainmenu, text=ord[i], font=('Times New Roman', 18), bg='#d8f9ff')
            variables[i].grid(row=r)
            r += 1

class Newven(Main):
    def __init__(self):
        super().__init__()
        self.newvenmenu()
        self.mainwindow.mainloop()

    def newvenmenu(self):
        self.ciLabel = tk.Label(self.mainmenu, text='CI', font=('Times New Roman', 18), bg='#d8f9ff')
        self.ciLabel.grid(row=0, column=0)
        self.ciEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.ciEntry.grid(row=1, column=0)
        self.venAdd = tk.Button(self.mainmenu, text='Agregar venta', font=('Times New Roman', 18), command=self.newven)
        self.venAdd.grid(row=2, column=0)

    def newven(self):
        ci = self.ciEntry.get()
        if ci == '':
            errormessage('CI no puede estar vacío')
        ciNum = int(ci)
        fulldate = datetime.now()
        date = fulldate.strftime('%d/%m/%Y')
        cursor.execute(f'INSERT INTO "ventas" VALUES(NULL, {ciNum}, "{date}")')
        conn.commit()
        succsefulmessage('Venta agregada de forma exitosa')
        self.ciEntry.delete(0, tk.END)

class Newrec(Main):
    def __init__(self):
        super().__init__()
        self.newrecmenu()
        self.newcanrecmenu()
        self.mainwindow.mainloop()

    def newrecmenu(self):
        self.recNomLabel = tk.Label(self.mainmenu, text='Nombre Receta:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.recNomLabel.grid(row=0, column=0, padx=10)
        self.recNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.recNomEntry.grid(row=0, column=1)

        self.recDescLabel = tk.Label(self.mainmenu, text='Descripcion Receta:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.recDescLabel.grid(row=1, column=0, padx=10)
        self.recDescEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.recDescEntry.grid(row=1, column=1)

        self.newrecButton = tk.Button(self.mainmenu, text='Agregar receta', font=('Times New Roman', 18), command=self.newrec)
        self.newrecButton.grid(row=2, column=0)

    def newrec(self):
        nom = self.recNomEntry.get()
        if nom == '':
            errormessage('Nombre no puede estar vacío')
        desc = self.recDescEntry.get()
        if desc == '':
            errormessage('Descripcion no puede estar vacío')
        try:
            cursor.execute(f'INSERT INTO "recetas" VALUES(NULL, "{nom.capitalize()}", "{desc}", 0, 0)')
            conn.commit()
            succsefulmessage('Receta creada de forma exitosa')
        except sqlite3.Error as e:
            errormessage(e)
            print(f'Error: {e}')
        self.recNomEntry.delete(0, tk.END)
        self.recDescEntry.delete(0, tk.END)

    def newcanrecmenu(self):
        self.recNomLabel = tk.Label(self.mainmenu, text='Nombre Receta:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.recNomLabel.grid(row=3, column=0, padx=10)
        self.recNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.recNomEntry.grid(row=3, column=1)

        self.insNomLabel = tk.Label(self.mainmenu, text='Nombre Insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.insNomLabel.grid(row=4, column=0, padx=10)
        self.insNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insNomEntry.grid(row=4, column=1)

        self.canUtInsNomLabel = tk.Label(self.mainmenu, text='Cantidad a utilizar insumo:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.canUtInsNomLabel.grid(row=5, column=0, padx=10)
        self.canUtInsNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.canUtInsNomEntry.grid(row=5, column=1)

        self.canRecLabel = tk.Label(self.mainmenu, text='Cantidad agregar Receta:', font=('Times New Roman', 18), bg='#d8f9ff')
        self.canRecLabel.grid(row=6, column=0, padx=10)
        self.canRecEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.canRecEntry.grid(row=6, column=1)

        self.newrecButton = tk.Button(self.mainmenu, text='Agregar receta', font=('Times New Roman', 18), command=self.newrec2)
        self.newrecButton.grid(row=7, column=0)

    def newrec2(self):
        recnom = self.recNomEntry.get()
        if recnom == '':
            errormessage('Nombre receta no puede estar vacío')
        insnom = self.insNomEntry.get()
        canins = self.canUtInsNomEntry.get()
        if canins != '':
            caninsnum = float(canins)
        canrec = self.canRecEntry.get()
        if canrec != '':
            canrecnum = int(canrec)
        if insnom == '' and canins == '' and canrec != '':
            iscan = False
            cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{recnom}"')
            idrecT = cursor.fetchone()
            idrec = idrecT[0]
            cursor.execute(f'SELECT "id_ins" FROM "ins_rec" WHERE "id_rec"={idrec}')
            idinslistT = cursor.fetchall()
            idinslist = []
            for i in range(len(idinslistT)):
                idinslist.append(idinslistT[i][0])
            caninsactlist = []
            for i in range(len(idinslist)):
                cursor.execute(f'SELECT "can_ins" FROM "insumos" WHERE "id_ins"={idinslist[0]}')
                caninsact = cursor.fetchone()
                caninsactlist.append(caninsact[0])
            canutninlist = []
            for i in range(len(idinslist)):
                cursor.execute(f'SELECT "can_ut_ins" FROM "ins_rec" WHERE "id_rec"={idrec} AND "id_ins"={idinslist[i]}')
                canutins = cursor.fetchone()
                canutninlist.append(canutins[0] * canrecnum)
            preinslist = []
            for i in range(len(idinslist)):
                cursor.execute(f'SELECT "pre_ins" FROM "insumos" WHERE "id_ins"={idinslist[i]}')
                preins = cursor.fetchone()
                preinslist.append(preins[0])
            newprelist = []
            for i in range(len(idinslist)):
                newpren = canutninlist[i] * preinslist[i]
                newprelist.append(newpren)
            for i in range(len(canutninlist)):
                if caninsactlist[i] >= canutninlist[i]:
                    iscan = True
                else:
                    iscan = False
                    errormessage('No se, algo')
            if iscan == True:
                for i in range(len(canutninlist)):
                    newcan = caninsactlist[i] - canutninlist[i]
                    cursor.execute(f'UPDATE "insumos" SET "can_ins"={newcan} WHERE "id_ins"={idinslist[i]}')
                    conn.commit()
                cursor.execute(f'SELECT "can_rec" FROM "recetas" WHERE "id_rec"={idrec}')
                canrecT = cursor.fetchone()
                canactrec = canrecT[0]
                newcanrec = canactrec + canrecnum
                cursor.execute(f'UPDATE "recetas" SET "can_rec"={newcanrec} WHERE "id_rec"={idrec}')
                conn.commit()
                cursor.execute(f'SELECT "pre_rec" FROM "recetas" WHERE "id_rec"={idrec}')
                ispre = cursor.fetchone()
                if ispre[0] == 0:
                    newpre = sum(newprelist)
                    cursor.execute(f'UPDATE "recetas" SET "pre_rec"={newpre} WHERE "id_rec"={idrec}')
                    conn.commit()
                else:
                    pass
                succsefulmessage(f'Receta {recnom} actualizada de forma exitosa')
                self.recNomEntry.delete(0, tk.END)
                self.canRecEntry.delete(0, tk.END)
            else:
                errormessage('No hay suficientes insumos para actualizar la receta\nAdivine usted cual es el que falta')
                self.recNomEntry.delete(0, tk.END)
                self.canRecEntry.delete(0, tk.END)
        elif insnom != '' and canins != '' and canrec == '':
            cursor.execute(f'SELECT "id_rec" FROM "recetas" WHERE "nom_rec"="{recnom}"')
            idrecT = cursor.fetchone()
            idrec = idrecT[0]
            cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{insnom}"')
            idinsT = cursor.fetchone()
            idins = idinsT[0]
            cursor.execute(f'SELECT "id_ins" FROM "ins_rec" WHERE "id_rec"={idrec}')
            conf = cursor.fetchall()
            confList = []
            for i in range(len(conf)):
                confList.append(conf[i][0])
            if idins not in confList:
                cursor.execute(f'INSERT INTO "ins_rec" VALUES({idrec}, {idins}, {caninsnum})')
                conn.commit()
                succsefulmessage(f'Insumo {insnom} agregado de forma exitosa a la receta {recnom}')
                self.recNomEntry.delete(0, tk.END)
                self.insNomEntry.delete(0, tk.END)
                self.canUtInsNomEntry.delete(0, tk.END)
            else:
                errormessage(f'El insumo {insnom} ya se encuentra asociado a la receta {recnom}')
        else:
            errormessage(f'Nom: {recnom}\nIns: {insnom}\nCanins: {canins}\nCanrec: {canrec}')

def errormessage(error):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror('Error', error)

def succsefulmessage(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo('Info', message)

root = tk.Tk()
root.withdraw()
messagebox.showwarning('aaaaaaaaaaaa', 'Ahora si que si, vamos a hacer ventas')
if __name__ == '__main__':
    x = Recetas()
    x

"""now = datetime.now()
form = now.strftime('%d/%m/%Y')"""