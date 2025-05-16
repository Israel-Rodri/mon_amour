import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime
from tkinter import messagebox
import os

currentDir = os.getcwd()
dbPath = os.path.join(currentDir, r'mon_amour\nom.db')
conn = sqlite3.connect(dbPath)
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

        self.botmenu = tk.Frame(self.mainwindow)
        self.botmenu.pack(side='bottom', fill='both', expand=True)

        self.mainmenu = tk.Frame(self.botmenu, bg='#788692')
        self.mainmenu.pack(side='top', fill='both', expand=True)

        self.bottomhalf = tk.Frame(self.botmenu, bg='lightgreen')
        self.bottomhalf.pack(side='top', fill='both', expand=True)

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
        self.addinsmenu()
        self.updateinsmenu()
        self.showins()
        self.mainwindow.mainloop()

    def showins(self):
        self.showtitle = tk.Label(self.bottomhalf, text='Mostrar Insumos', font=('Times New Roman', 24), bg='lightgreen')
        self.showtitle.pack()

        cursor.execute(f'SELECT * FROM "insumos"')
        ins = cursor.fetchall()
        r = 7
        variables = []
        for i in range(len(ins)):
            variables.append(i)
            variables[i] = tk.Label(self.bottomhalf, text=ins[i], font=('Times New Roman', 18), bg='lightgreen')
            variables[i].pack()
            r += 1

    def addinsmenu(self):
        self.addtitle = tk.Label(self.mainmenu, text='Agregar Insumo', font=('Times New Roman', 24), bg='#788692')
        self.addtitle.grid(row=0, column=2, pady=20)

        self.addInsNomLabel = tk.Label(self.mainmenu, text='Nombre Insumo:', font=('Times New Roman', 18), bg='#788692')
        self.addInsNomLabel.grid(row=1, column=2, padx=10)
        self.addInsNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addInsNomEntry.grid(row=1, column=3)

        self.addInsDescLabel = tk.Label(self.mainmenu, text='Descripcion Insumo:', font=('Times New Roman', 18), bg='#788692')
        self.addInsDescLabel.grid(row=2, column=2, padx=10)
        self.addInsDescEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addInsDescEntry.grid(row=2, column=3)

        self.addInsMedLabel = tk.Label(self.mainmenu, text='Medida Insumo:', font=('Times New Roman', 18), bg='#788692')
        self.addInsMedLabel.grid(row=3, column=2, padx=10)
        self.addInsMedEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addInsMedEntry.grid(row=3, column=3)

        self.addInsCanLabel = tk.Label(self.mainmenu, text='Cantidad Insumo:', font=('Times New Roman', 18), bg='#788692')
        self.addInsCanLabel.grid(row=4, column=2, padx=10)
        self.addInsCanEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addInsCanEntry.grid(row=4, column=3)

        self.addinsComboLabel = tk.Label(self.mainmenu, text='Proveedor del insumo:', font=('Times New Roman', 18), bg='#788692')
        self.addinsComboLabel.grid(row=5, column=2, padx=10)
        self.addinsCombo = ttk.Combobox(self.mainmenu, font=('Times New Roman', 16))
        self.addinsListVal = []
        self.addinslistvalues()
        self.addinsCombo['values'] = self.addinsListVal
        self.addinsCombo.current(0)
        self.addinsCombo.grid(row=5, column=3)

        self.addInsPreLabel = tk.Label(self.mainmenu, text='Precio Insumo:', font=('Times New Roman', 18), bg='#788692')
        self.addInsPreLabel.grid(row=6, column=2, padx=10)
        self.addInsPreEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addInsPreEntry.grid(row=6, column=3)

        self.addInsButton = tk.Button(self.mainmenu, text='Agregar Insumos', font=('Times New Roman', 18), command=self.addins)
        self.addInsButton.grid(row=7, column=2, padx=15)

    def updateinsmenu(self):
        self.updatetitle = tk.Label(self.mainmenu, text='Actualizar Insumo', font=('Times New Roman', 24), bg='#788692')
        self.updatetitle.grid(row=0, column=0, pady=20)

        self.insComboLabel = tk.Label(self.mainmenu, text='Nombre del insumo:', font=('Times New Roman', 18), bg='#788692')
        self.insComboLabel.grid(row=1, column=0, pady=10)
        self.insCombo = ttk.Combobox(self.mainmenu, font=('Times New Roman', 16))
        self.insListVal = []
        self.inslistvalues()
        self.insCombo['values'] = self.insListVal
        self.insCombo.current(0)
        self.insCombo.grid(row=1, column=1)

        self.insDescLabel = tk.Label(self.mainmenu, text='Descripcion Insumo:', font=('Times New Roman', 18), bg='#788692')
        self.insDescLabel.grid(row=2, column=0, padx=10)
        self.insDescEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insDescEntry.grid(row=2, column=1)

        self.insMedLabel = tk.Label(self.mainmenu, text='Medida Insumo:', font=('Times New Roman', 18), bg='#788692')
        self.insMedLabel.grid(row=3, column=0, padx=10)
        self.insMedEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insMedEntry.grid(row=3, column=1)

        self.insPreLabel = tk.Label(self.mainmenu, text='Precio Insumo:', font=('Times New Roman', 18), bg='#788692')
        self.insPreLabel.grid(row=4, column=0, padx=10)
        self.insPreEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insPreEntry.grid(row=4, column=1)

        self.updateInsButton = tk.Button(self.mainmenu, text='Actualizar Insumos', font=('Times New Roman', 18), command=self.updateins)
        self.updateInsButton.grid(row=5, column=0)

    def inslistvalues(self):
        cursor.execute(f'SELECT "nom_ins" FROM "insumos"')
        ins = cursor.fetchall()
        for i in range(len(ins)):
            self.insListVal.append(ins[i][0])

    def addinslistvalues(self):
        cursor.execute(f'SELECT "nom_prov" FROM "proveedor"')
        ins = cursor.fetchall()
        for i in range(len(ins)):
            self.addinsListVal.append(ins[i][0])

    def addins(self):
        nom = self.addInsNomEntry.get()
        if nom == '':
            errormessage('Nombre no puede estar vacio')
            self.reload(Insumos)
        desc = self.addInsDescEntry.get()
        if desc == '':
            errormessage('Descripcion no puede estar vacio')
            self.reload(Insumos)
        med = self.addInsMedEntry.get()
        if med == '':
            errormessage('Medida no puede estar vacio')
            self.reload(Insumos)
        can = self.addInsCanEntry.get()
        if can == '':
            errormessage('Cantidad no puede estar vacio')
            self.reload(Insumos)
        else:
            canNum = float(can)
        prov = self.addinsCombo.get()
        pre = self.addInsPreEntry.get()
        if pre == '':
            errormessage('Precio no puede estar vacio')
            self.reload(Insumos)
        else:
            preNum = float(pre)
        cursor.execute(f'SELECT "id_ins" FROM "insumos" WHERE "nom_ins"="{nom}"')
        conf = cursor.fetchone()
        if conf == None:
            try:
                cursor.execute(f'SELECT "rif_prov" FROM "proveedor" WHERE "nom_prov"="{prov}"')
                rif = cursor.fetchone()
                cursor.execute(f'INSERT INTO "insumos" VALUES(NULL, "{nom}", "{desc}", "{med}", {canNum}, {int(rif[0])}, {preNum})')
                conn.commit()
                succsefulmessage(f'El insumo {nom} ha sido agregado de forma exitosa')
                self.reload(Insumos)
            except sqlite3.Error as e:
                errormessage(e)
                print(f'Error: {e}')
                self.addInsNomEntry.delete(0, tk.END)
                self.addInsDescEntry.delete(0, tk.END)
                self.addInsMedEntry.delete(0, tk.END)
                self.addInsCanEntry.delete(0, tk.END)
                self.addInsPreEntry.delete(0, tk.END)
        else:
            errormessage(f'Ya existe un insumo con el nombre {nom}')
            self.addInsNomEntry.delete(0, tk.END)
            self.addInsDescEntry.delete(0, tk.END)
            self.addInsMedEntry.delete(0, tk.END)
            self.addInsCanEntry.delete(0, tk.END)
            self.addInsPreEntry.delete(0, tk.END)

    def updateins(self):
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
        self.addprovmenu()
        self.updateprovmenu()
        self.showprov()
        self.mainwindow.mainloop()

    def showprov(self):
        self.showtitle = tk.Label(self.bottomhalf, text='Mostrar Proveedores', font=('Times New Roman', 24), bg='lightgreen')
        self.showtitle.pack()

        cursor.execute(f'SELECT * FROM "proveedor"')
        prov = cursor.fetchall()
        r = 1
        variables = []
        for i in range(len(prov)):
            variables.append(i)
            variables[i] = tk.Label(self.bottomhalf, text=prov[i], font=('Times New Roman', 18), bg='lightgreen')
            variables[i].pack()
            r += 1

    def updateprovmenu(self):
        self.updatetitle = tk.Label(self.mainmenu, text='Actualizar Proveedores', font=('Times New Roman', 24), bg='#788692')
        self.updatetitle.grid(row=0, column=0, pady=20)

        self.provComboLabel = tk.Label(self.mainmenu, text='Seleccione Proveedor:', font=('Times New Roman', 18), bg='#788692')
        self.provComboLabel.grid(row=1, column=0, padx=10)
        self.provCombo = ttk.Combobox(self.mainmenu, font=('Times New Roman', 16))
        self.provListval = []
        self.provlistvalues()
        self.provCombo['values'] = self.provListval
        self.provCombo.current(0)
        self.provCombo.grid(row=1, column=1)

        self.provNomLabel = tk.Label(self.mainmenu, text='Nuevo nombre Proveedor:', font=('Times New Roman', 18), bg='#788692')
        self.provNomLabel.grid(row=2, column=0, padx=10)
        self.provNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.provNomEntry.grid(row=2, column=1)

        self.provTelLabel = tk.Label(self.mainmenu, text='Nuevo telefono Proveedor:', font=('Times New Roman', 18), bg='#788692')
        self.provTelLabel.grid(row=3, column=0, padx=10)
        self.provTelEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.provTelEntry.grid(row=3, column=1)

        self.provEmailLabel = tk.Label(self.mainmenu, text='Nuevo email Proveedor:', font=('Times New Roman', 18), bg='#788692')
        self.provEmailLabel.grid(row=4, column=0, padx=10)
        self.provEmailEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.provEmailEntry.grid(row=4, column=1)

        self.updateProvButton = tk.Button(self.mainmenu, text='Actualizar Proveedor', font=('Times New Roman', 18), command=self.updateprov)
        self.updateProvButton.grid(row=5, column=0)

    def addprovmenu(self):
        self.addtitle = tk.Label(self.mainmenu, text='Agregar Proveedor:', font=('Times New Roman', 24), bg='#788692')
        self.addtitle.grid(row=0, column=2, pady=20)

        self.addProvRifLabel = tk.Label(self.mainmenu, text='RIF Proveedor:', font=('Times New Roman', 18), bg='#788692')
        self.addProvRifLabel.grid(row=1, column=2, padx=10)
        self.addProvRifEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addProvRifEntry.grid(row=1, column=3)

        self.addProvNomLabel = tk.Label(self.mainmenu, text='Nombre Proveedor:', font=('Times New Roman', 18), bg='#788692')
        self.addProvNomLabel.grid(row=2, column=2, padx=10)
        self.addProvNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addProvNomEntry.grid(row=2, column=3)

        self.addProvTelLabel = tk.Label(self.mainmenu, text='Telefono Proveedor:', font=('Times New Roman', 18), bg='#788692')
        self.addProvTelLabel.grid(row=3, column=2, padx=10)
        self.addProvTelEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addProvTelEntry.grid(row=3, column=3)

        self.addProvEmailLabel = tk.Label(self.mainmenu, text='Email Proveedor:', font=('Times New Roman', 18), bg='#788692')
        self.addProvEmailLabel.grid(row=4, column=2, padx=10)
        self.addProvEmailEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addProvEmailEntry.grid(row=4, column=3)

        self.addProvButton = tk.Button(self.mainmenu, text='Agregar Proveedor', font=('Times New Roman', 18), command=self.addprov)
        self.addProvButton.grid(row=5, column=2)

    def provlistvalues(self):
        cursor.execute('SELECT "nom_prov" FROM "proveedor"')
        prov = cursor.fetchall()
        for i in range(len(prov)):
            self.provListval.append(prov[i][0])

    def addprov(self):
        rif = self.addProvRifEntry.get()
        if rif == '':
            errormessage('El RIF del proveedor no puede estar vacio')
            self.reload(Proveedores)
        nom = self.addProvNomEntry.get()
        if nom == '':
            errormessage('El nombre del proveedor no puede estar vacio')
            self.reload(Proveedores)
        tel = self.addProvTelEntry.get()
        if tel == '':
            errormessage('El apellido del proveedor no puede estar vacio')
            self.reload(Proveedores)
        email = self.addProvEmailEntry.get()
        if email == '':
            errormessage('El telefono del proveedor no puede estar vacio')
            self.reload(Proveedores)
        cursor.execute(f'SELECT "nom_prov" FROM "proveedor" WHERE "rif_prov"="{int(rif)}"')
        conf = cursor.fetchone()
        if conf == None:
            try:
                cursor.execute(f'INSERT INTO "proveedor" VALUES ({int(rif)}, "{nom}", "{tel}", "{email}")')
                conn.commit()
                succsefulmessage(f'El proveedor {nom} con el rif {rif} ha sido agregado de forma exitosa')
                self.reload(Proveedores)
            except sqlite3.Error as e:
                errormessage(e)
                print(f'Error: {e}')
                self.addProvRifEntry.delete(0, tk.END)
                self.addProvNomEntry.delete(0, tk.END)
                self.addProvTelEntry.delete(0, tk.END)
                self.addProvEmailEntry.delete(0, tk.END)
        else:
            errormessage(f'El proveedor con el rif {rif} ya se encuentra registrado')
            self.addProvRifEntry.delete(0, tk.END)
            self.addProvNomEntry.delete(0, tk.END)
            self.addProvTelEntry.delete(0, tk.END)
            self.addProvEmailEntry.delete(0, tk.END)

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
        self.addcanrectitle = tk.Label(self.mainmenu, text='Agregar cantidad de receta', font=('Times New Roman', 24), bg='#788692')
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
        self.addrectitle = tk.Label(self.mainmenu, text='Agregar receta', font=('Times New Roman', 24), bg='#788692')
        self.addrectitle.grid(row=0, column=1, pady=20)

        self.addrecnomLabel = tk.Label(self.mainmenu, text='Nombre receta:', font=('Times New Roman', 18), bg='#788692')
        self.addrecnomLabel.grid(row=1, column=1, padx=5)    
        self.addrecnom = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addrecnom.grid(row=1, column=2)

        self.addrecdescLabel = tk.Label(self.mainmenu, text='Descripcion receta', font=('Times New Roman', 18), bg='#788692')
        self.addrecdescLabel.grid(row=2, column=1)
        self.addrecdesc = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addrecdesc.grid(row=2, column=2)

        self.addrecButton = tk.Button(self.mainmenu, text='Agregar receta', font=('Times New Roman', 18), command=self.addrec)
        self.addrecButton.grid(row=3, column=1, pady=10)

    def addinsrecmenu(self):
        self.addinsrectitle = tk.Label(self.mainmenu, text='Asociar insumos a receta', font=('Times New Roman', 24), bg='#788692')
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

        self.caninsLabel = tk.Label(self.mainmenu, text='Cantidad a utilizar del insumo:', font=('Times New Roman', 18), bg='#788692')
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
        self.showtitle = tk.Label(self.bottomhalf, text='Mostrar Recetas', font=('Times New Roman', 24), bg='lightgreen')
        self.showtitle.pack()

        cursor.execute(f'SELECT * FROM "recetas"')
        prov = cursor.fetchall()
        r = 7
        variables = []
        for i in range(len(prov)):
            variables.append(i)
            variables[i] = tk.Label(self.bottomhalf, text=prov[i], font=('Times New Roman', 18), bg='lightgreen')
            variables[i].pack()
            r += 1

class Clientes(Main):
    def __init__(self):
        super().__init__()
        self.addclimenu()
        self.updateclimenu()
        self.showcli()
        self.mainwindow.mainloop()

    def showcli(self):
        self.showtitle = tk.Label(self.bottomhalf, text='Mostrar Clientes', font=('Times New Roman', 24), bg='lightgreen')
        self.showtitle.pack()

        cursor.execute(f'SELECT * FROM "clientes"')
        cli = cursor.fetchall()
        r = 7
        variables = []
        for i in range(len(cli)):
            variables.append(i)
            variables[i] = tk.Label(self.bottomhalf, text=cli[i], font=('Times New Roman', 18), bg='lightgreen')
            variables[i].pack()
            r += 1

    def addclimenu(self):
        self.addtitle = tk.Label(self.mainmenu, text='Crear Clientes', font=('Times New Roman', 24), bg='#788692')
        self.addtitle.grid(row=0, column=2, pady=20)

        self.addcliCiLabel = tk.Label(self.mainmenu, text='Cedula cliente:', font=('Times New Roman', 18), bg='#788692')
        self.addcliCiLabel.grid(row=1, column=2, padx=10)
        self.addcliCiEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addcliCiEntry.grid(row=1, column=3)

        self.addcliNomLabel = tk.Label(self.mainmenu, text='Nombre cliente:', font=('Times New Roman', 18), bg='#788692')
        self.addcliNomLabel.grid(row=2, column=2, padx=10)
        self.addcliNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addcliNomEntry.grid(row=2, column=3)

        self.addcliApeLabel = tk.Label(self.mainmenu, text='Apellido cliente:', font=('Times New Roman', 18), bg='#788692')
        self.addcliApeLabel.grid(row=3, column=2, padx=10)
        self.addcliApeEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addcliApeEntry.grid(row=3, column=3)

        self.addcliTelLabel = tk.Label(self.mainmenu, text='Telefono cliente:', font=('Times New Roman', 18), bg='#788692')
        self.addcliTelLabel.grid(row=4, column=2, padx=10)
        self.addcliTelEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.addcliTelEntry.grid(row=4, column=3)

        self.addCliButton = tk.Button(self.mainmenu, text='Crear Cliente', font=('Times New Roman', 18), command=self.addcli)
        self.addCliButton.grid(row=5, column=2, padx=10)

    def updateclimenu(self):
        self.updatetitle = tk.Label(self.mainmenu, text='Actualizar Clientes', font=('Times New Roman', 24), bg='#788692')
        self.updatetitle.grid(row=0, column=0, pady=20)

        self.clicomboLabel = tk.Label(self.mainmenu, text='Seleccione cliente:', font=('Times New Roman', 18), bg='#788692')
        self.clicomboLabel.grid(row=1, column=0, padx=10)
        self.addcliCombo = ttk.Combobox(self.mainmenu, font=('Times New Roman', 16))
        self.addcliListval = []
        self.clilistvalues()
        self.addcliCombo['values'] = self.addcliListval
        self.addcliCombo.current(0)
        self.addcliCombo.grid(row=1, column=1)

        self.cliNomLabel = tk.Label(self.mainmenu, text='Nuevo nombre cliente:', font=('Times New Roman', 18), bg='#788692')
        self.cliNomLabel.grid(row=2, column=0, padx=10)
        self.cliNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.cliNomEntry.grid(row=2, column=1)

        self.cliApeLabel = tk.Label(self.mainmenu, text='Nuevo apellido cliente:', font=('Times New Roman', 18), bg='#788692')
        self.cliApeLabel.grid(row=3, column=0, padx=10)
        self.cliApeEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.cliApeEntry.grid(row=3, column=1)

        self.cliTelLabel = tk.Label(self.mainmenu, text='Nuevo telefono cliente:', font=('Times New Roman', 18), bg='#788692')
        self.cliTelLabel.grid(row=4, column=0, padx=10)
        self.cliTelEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.cliTelEntry.grid(row=4, column=1)

        self.updateCliButton = tk.Button(self.mainmenu, text='Actualizar Cliente', font=('Times New Roman', 18), command=self.updatecli)
        self.updateCliButton.grid(row=5, column=0)

    def clilistvalues(self):
        cursor.execute(f'SELECT "nom_cli" FROM "clientes"')
        clinom = cursor.fetchall()
        cursor.execute(f'SELECT "ape_cli" FROM "clientes"')
        cliape = cursor.fetchall()
        for i in range(len(clinom)):
            self.addcliListval.append(f'{clinom[i][0]} {cliape[i][0]}')

    def addcli(self):
        ci = self.addcliCiEntry.get()
        if ci == '':
            errormessage('Cedula no puede estar vacio')
            self.reload(Clientes)
        nom = self.addcliNomEntry.get()
        if nom == '':
            errormessage('Nombre no puede estar vacio')
            self.reload(Clientes)
        ape = self.addcliApeEntry.get()
        if ape == '':
            errormessage('Apellido no puede estar vacio')
            self.reload(Clientes)
        tel = self.addcliTelEntry.get()
        if tel == '':
            errormessage('Telefono no puede estar vacio')
            self.reload(Clientes)
        cursor.execute(f'SELECT "nom_cli" FROM "clientes" WHERE "ci_cli"="{int(ci)}"')
        conf = cursor.fetchone()
        if conf == None:
            try:
                cursor.execute(f'INSERT INTO "clientes" VALUES({int(ci)}, "{nom}", "{ape}", "{tel}")')
                conn.commit()
                succsefulmessage(f'Cliente {nom} {ape} ha sido creado de forma exitosa')
                self.reload(Clientes)
            except sqlite3.Error as e:
                errormessage({e})
                print(f'Error: {e}')
        else:
            errormessage(f'Ya existe un cliente registrado con la cedula {ci}\nConfirmacion: {conf}')
            self.addcliCiEntry.delete(0, tk.END)
            self.addcliNomEntry.delete(0, tk.END)
            self.addcliApeEntry.delete(0, tk.END)
            self.addcliTelEntry.delete(0, tk.END)

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
        self.showtitle = tk.Label(self.bottomhalf, text='Mostrar Insumos utilizados en recetas', font=('Times New Roman', 24), bg='lightgreen')
        self.showtitle.pack()

        cursor.execute(f'SELECT * FROM "ins_rec"')
        ins_rec = cursor.fetchall()
        r = 6
        variables = []
        for i in range(len(ins_rec)):
            variables.append(i)
            variables[i] = tk.Label(self.bottomhalf, text=ins_rec[i], font=('Times New Roman', 18), bg='lightgreen')
            variables[i].pack()
            r += 1

    def updateinsrecmenu(self):
        self.updatetitle = tk.Label(self.mainmenu, text='Actualizar Insumos a utilizar', font=('Times New Roman', 24), bg='#788692')
        self.updatetitle.grid(row=0, column=0, pady=20)

        self.recNomLabel = tk.Label(self.mainmenu, text='Nombre de la receta:', font=('Times New Roman', 18), bg='#788692')
        self.recNomLabel.grid(row=1, column=0, padx=10)
        self.recNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.recNomEntry.grid(row=1, column=1)

        self.insNomLabel = tk.Label(self.mainmenu, text='Nombre del insumo:', font=('Times New Roman', 18), bg='#788692')
        self.insNomLabel.grid(row=2, column=0, padx=10)
        self.insNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insNomEntry.grid(row=2, column=1)

        self.insCanLabel = tk.Label(self.mainmenu, text='Cantidad a utilizar del insumo:', font=('Times New Roman', 18), bg='#788692')
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
            variables[i] = tk.Label(self.mainmenu, text=ord[i], font=('Times New Roman', 18), bg='#788692')
            variables[i].grid(row=r)
            r += 1

class Newven(Main):
    def __init__(self):
        super().__init__()
        self.newvenmenu()
        self.mainwindow.mainloop()

    def newvenmenu(self):
        self.ciLabel = tk.Label(self.mainmenu, text='CI', font=('Times New Roman', 18), bg='#788692')
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
        self.recNomLabel = tk.Label(self.mainmenu, text='Nombre Receta:', font=('Times New Roman', 18), bg='#788692')
        self.recNomLabel.grid(row=0, column=0, padx=10)
        self.recNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.recNomEntry.grid(row=0, column=1)

        self.recDescLabel = tk.Label(self.mainmenu, text='Descripcion Receta:', font=('Times New Roman', 18), bg='#788692')
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
        self.recNomLabel = tk.Label(self.mainmenu, text='Nombre Receta:', font=('Times New Roman', 18), bg='#788692')
        self.recNomLabel.grid(row=3, column=0, padx=10)
        self.recNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.recNomEntry.grid(row=3, column=1)

        self.insNomLabel = tk.Label(self.mainmenu, text='Nombre Insumo:', font=('Times New Roman', 18), bg='#788692')
        self.insNomLabel.grid(row=4, column=0, padx=10)
        self.insNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.insNomEntry.grid(row=4, column=1)

        self.canUtInsNomLabel = tk.Label(self.mainmenu, text='Cantidad a utilizar insumo:', font=('Times New Roman', 18), bg='#788692')
        self.canUtInsNomLabel.grid(row=5, column=0, padx=10)
        self.canUtInsNomEntry = tk.Entry(self.mainmenu, font=('Times New Roman', 16))
        self.canUtInsNomEntry.grid(row=5, column=1)

        self.canRecLabel = tk.Label(self.mainmenu, text='Cantidad agregar Receta:', font=('Times New Roman', 18), bg='#788692')
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

"""root = tk.Tk()
root.withdraw()
messagebox.showwarning('aaaaaaaaaaaa', 'Terminar de poner los agregar')"""
if __name__ == '__main__':
    x = Recetas()
    x

"""now = datetime.now()
form = now.strftime('%d/%m/%Y')"""