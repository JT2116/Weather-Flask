use ciudades;

create or replace table Ciudades(
    ID int not null auto_increment primary key,
    Nombre varchar(80) not null
);

insert into Ciudades (ID,Nombre) values (1, 'London');
insert into Ciudades (ID,Nombre) values (2, 'Seattle');
insert into Ciudades (ID,Nombre) values (3, 'Las Vegas');
insert into Ciudades (ID,Nombre) values (4, 'Shanghai');
insert into Ciudades (ID,Nombre) values (5, 'Santiago de los Caballeros');
insert into Ciudades (ID,Nombre) values (6, 'New York City');
insert into Ciudades (ID,Nombre) values (7, 'Ciudad de México');
insert into Ciudades (ID,Nombre) values (8, 'Tokyo');
insert into Ciudades (ID,Nombre) values (9, 'Madrid');
insert into Ciudades (ID,Nombre) values (10, 'Buenos Aires');
insert into Ciudades (ID,Nombre) values (11, 'Paris');
insert into Ciudades (ID,Nombre) values (12, 'Santo Domingo');

