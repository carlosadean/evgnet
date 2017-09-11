PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
COMMIT;
sqlite> .dump cadastro_evangelista
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "cadastro_evangelista" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nome" varchar(200) NOT NULL, "data_nascimento" date NOT NULL, "data_entrada_evg" date NOT NULL, "foto_perfil" varchar(100) NOT NULL, "funcao_id" integer NOT NULL REFERENCES "cadastro_funcao" ("id"), "igreja_id" integer NOT NULL REFERENCES "cadastro_igreja" ("id"), "projeto_id" integer NOT NULL REFERENCES "cadastro_projeto" ("id"), "inativo" bool NOT NULL);
INSERT INTO "cadastro_evangelista" VALUES(1,'Carlos Alberto de Souza','1960-09-06','2010-09-06','',1,1,1,0);
INSERT INTO "cadastro_evangelista" VALUES(2,'Carlos Eduardo Peixoto','1979-09-06','2015-09-06','',1,1,3,0);
INSERT INTO "cadastro_evangelista" VALUES(3,'Carol de Sousa','1990-09-06','2014-09-06','',1,3,1,0);
INSERT INTO "cadastro_evangelista" VALUES(4,'Sara Rodrigues de Souza','1988-03-15','2015-08-01','',5,3,5,0);
INSERT INTO "cadastro_evangelista" VALUES(5,'Aguida da Silva','1990-01-01','2013-04-01','',3,1,5,0);
INSERT INTO "cadastro_evangelista" VALUES(6,'Danniel Librelon','1980-07-03','2017-04-17','',4,3,5,0);
CREATE INDEX "cadastro_evangelista_funcao_id_07b5c58e" ON "cadastro_evangelista" ("funcao_id");
CREATE INDEX "cadastro_evangelista_igreja_id_f36135b3" ON "cadastro_evangelista" ("igreja_id");
CREATE INDEX "cadastro_evangelista_projeto_id_d54c03bb" ON "cadastro_evangelista" ("projeto_id");
COMMIT;
sqlite> .dump cadastro_evangelista > cadastro_evangelista.sql
Error: unknown command or invalid arguments:  "dump". Enter ".help" for help
sqlite> .dump cadastro_evangelista
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "cadastro_evangelista" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nome" varchar(200) NOT NULL, "data_nascimento" date NOT NULL, "data_entrada_evg" date NOT NULL, "foto_perfil" varchar(100) NOT NULL, "funcao_id" integer NOT NULL REFERENCES "cadastro_funcao" ("id"), "igreja_id" integer NOT NULL REFERENCES "cadastro_igreja" ("id"), "projeto_id" integer NOT NULL REFERENCES "cadastro_projeto" ("id"), "inativo" bool NOT NULL);
INSERT INTO "cadastro_evangelista" VALUES(1,'Carlos Alberto de Souza','1960-09-06','2010-09-06','',1,1,1,0);
INSERT INTO "cadastro_evangelista" VALUES(2,'Carlos Eduardo Peixoto','1979-09-06','2015-09-06','',1,1,3,0);
INSERT INTO "cadastro_evangelista" VALUES(3,'Carol de Sousa','1990-09-06','2014-09-06','',1,3,1,0);
INSERT INTO "cadastro_evangelista" VALUES(4,'Sara Rodrigues de Souza','1988-03-15','2015-08-01','',5,3,5,0);
INSERT INTO "cadastro_evangelista" VALUES(5,'Aguida da Silva','1990-01-01','2013-04-01','',3,1,5,0);
INSERT INTO "cadastro_evangelista" VALUES(6,'Danniel Librelon','1980-07-03','2017-04-17','',4,3,5,0);
CREATE INDEX "cadastro_evangelista_funcao_id_07b5c58e" ON "cadastro_evangelista" ("funcao_id");
CREATE INDEX "cadastro_evangelista_igreja_id_f36135b3" ON "cadastro_evangelista" ("igreja_id");
CREATE INDEX "cadastro_evangelista_projeto_id_d54c03bb" ON "cadastro_evangelista" ("projeto_id");
COMMIT;

