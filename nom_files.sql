BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "clientes" (
	"ci_cli"	INTEGER NOT NULL,
	"nom_cli"	TEXT(20) NOT NULL,
	"ape_cli"	TEXT(20) NOT NULL,
	"tel_cli"	TEXT(12),
	PRIMARY KEY("ci_cli")
);
CREATE TABLE IF NOT EXISTS "ins_rec" (
	"id_rec"	INTEGER NOT NULL,
	"id_ins"	INTEGER,
	"can_ut_ins"	FLOAT(8),
	CONSTRAINT "id_ins_cons" FOREIGN KEY("id_ins") REFERENCES "insumos"("id_ins") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT "id_rec_cons" FOREIGN KEY("id_rec") REFERENCES "recetas"("id_rec") ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS "insumos" (
	"id_ins"	INTEGER NOT NULL,
	"nom_ins"	TEXT(25) NOT NULL,
	"desc_ins"	TEXT(50) NOT NULL,
	"med_ins"	TEXT(10),
	"can_ins"	FLOAT(8) NOT NULL,
	"rif_prov"	INTEGER NOT NULL,
	"pre_ins"	FLAOT(8) NOT NULL,
	PRIMARY KEY("id_ins" AUTOINCREMENT),
	FOREIGN KEY("rif_prov") REFERENCES "proveedor"("rif_prov") ON DELETE SET NULL ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS "proveedor" (
	"rif_prov"	INTEGER NOT NULL,
	"nom_prov"	TEXT(30) NOT NULL,
	"tel_prov"	TEXT(11) NOT NULL,
	"email_prov"	TEXT(25),
	PRIMARY KEY("rif_prov")
);
CREATE TABLE IF NOT EXISTS "recetas" (
	"id_rec"	INTEGER NOT NULL,
	"nom_rec"	TEXT(20) NOT NULL,
	"desc_rec"	TEXT(50) NOT NULL,
	"can_rec"	INTEGER(8),
	"pre_rec"	FLOAT(8),
	PRIMARY KEY("id_rec" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "usuarios" (
	"id_user"	INTEGER NOT NULL,
	"email_user"	TEXT(20) NOT NULL,
	"passw_user"	TEXT(45) NOT NULL,
	PRIMARY KEY("id_user" AUTOINCREMENT)
);
INSERT INTO "clientes" VALUES (4448349,'Pepe','Rodriguez','0276-7881122');
INSERT INTO "clientes" VALUES (12334657,'Juan','Perez','0416-2231156');
INSERT INTO "clientes" VALUES (12345678,'Prueba','Gomez','0416-1234567');
INSERT INTO "ins_rec" VALUES (300,1,120.0);
INSERT INTO "ins_rec" VALUES (300,2,350.0);
INSERT INTO "ins_rec" VALUES (300,3,3.0);
INSERT INTO "ins_rec" VALUES (301,2,120.0);
INSERT INTO "ins_rec" VALUES (301,1,45.0);
INSERT INTO "ins_rec" VALUES (302,1,35.0);
INSERT INTO "ins_rec" VALUES (302,2,120.0);
INSERT INTO "ins_rec" VALUES (302,3,2.0);
INSERT INTO "ins_rec" VALUES (302,4,50.0);
INSERT INTO "ins_rec" VALUES (303,1,50.0);
INSERT INTO "ins_rec" VALUES (303,3,3.0);
INSERT INTO "ins_rec" VALUES (303,4,55.2);
INSERT INTO "ins_rec" VALUES (304,1,50.0);
INSERT INTO "ins_rec" VALUES (304,4,25.0);
INSERT INTO "ins_rec" VALUES (304,2,120.3);
INSERT INTO "ins_rec" VALUES (305,5,25.0);
INSERT INTO "ins_rec" VALUES (305,7,5.0);
INSERT INTO "insumos" VALUES (1,'Azucar','Azucar glass, especial para reposteria','Grs',500.0,282563178,0.03);
INSERT INTO "insumos" VALUES (2,'Harina','Harina de trigo sin leudante marca la lucha','Gr',2340.0,115040882,0.01);
INSERT INTO "insumos" VALUES (3,'Huevos','Huevos organicos','Unidades',3270.0,282563178,0.4);
INSERT INTO "insumos" VALUES (4,'Mantequilla','Mantequilla Nelly','Gr',3180.0,115040882,0.1);
INSERT INTO "insumos" VALUES (5,'Leche','Leche pasteurizada deslactosada','Ml',0.0,282563178,0.7);
INSERT INTO "insumos" VALUES (7,'Canela','Canela orgánica en polvo','Gr',125.0,28230229,0.03);
INSERT INTO "proveedor" VALUES (28230229,'Sol F.P.','0212-7569553','wisinyyandelqhotmail.com');
INSERT INTO "proveedor" VALUES (44483490,'Comercializadora La Buena Fe','0276-7883321','comeclabuenafe@yahoo.com');
INSERT INTO "proveedor" VALUES (115040882,'Distribuciones La Sayona','0276-7880201','distlasayona@outlook.com');
INSERT INTO "proveedor" VALUES (273445621,'Distribuciones e importaciones Su Merced','0416-1145325','distimportsm@gmail.com');
INSERT INTO "proveedor" VALUES (282563178,'Comercializadora La Ñapa','0414-7406044','comlanapa@gmail.com');
INSERT INTO "proveedor" VALUES (282563321,'Frutas y Verduras Sin Ideas','0412-2213421','fryverdsi@yahoo.com');
INSERT INTO "recetas" VALUES (300,'Torta','Torta de chocolate',3,30.0);
INSERT INTO "recetas" VALUES (301,'Macarron','Macarron chavista',4,2.55);
INSERT INTO "recetas" VALUES (302,'Hojaldre','Hojaldre de bocadillo con otras vainas',2,16.5);
INSERT INTO "recetas" VALUES (303,'Quesillo','Quesillo artesanal para vender por porciones',0,8.22);
INSERT INTO "recetas" VALUES (304,'Pan Dulce','Pan dulce sin gluten',1,5.203);
INSERT INTO "recetas" VALUES (305,'Bocadillo','Bocadillo de prueba ',1,17.65);
INSERT INTO "usuarios" VALUES (1,'pepe','trueno');
INSERT INTO "usuarios" VALUES (1501,'israel5302@gmail.com','974a2be4c0f6db85c78778e367e905f6f4c1b3524505872ade3ddae1d9ef43b8');
COMMIT;
