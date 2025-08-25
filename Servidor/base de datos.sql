--INSERT INTO ESP32(Nombre,Valor)  VALUES ('luxometro','135')--
--sqlite datos3.sqilite <datos.sql-- 
--cat  {nombre archivo} ,ves lo que tiene el archivo --

CREATE TABLE "ESP32" (
	"id"	INTEGER NOT NULL,
	"Nombre"	TEXT NOT NULL,
	"Valor"	TEXT NOT NULL,
	"Hora"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id" AUTOINCREMENT)
);