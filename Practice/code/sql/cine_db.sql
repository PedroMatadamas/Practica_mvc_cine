#DROP DATABASE cine_db;
Create database if not exists cine_db;
use cine_db;

create table if not exists directores(
    id_director int not null auto_increment,
    d_nombre varchar(25) not null,
    d_apellidoPat varchar(25) not null,
    d_apellidoMat varchar(25),
    d_nacionalidad varchar(25) not null,
    d_fnacimiento DATE,
    d_educacion varchar(25),
    primary key (id_director)
)engine = InnoDB;

create table if not exists actores(
	id_actor int not null auto_increment,
    a_nombre varchar(25) not null,
    a_apellidoPat varchar(25) not null,
    a_apellidoMat varchar(25),
    a_nacionalidad varchar(25) not null,
    a_fnacimiento DATE,
    primary key(id_actor)
)engine = InnoDB;

create table if not exists peliculas(
		id_pelicula int not null auto_increment,
    	p_titulo varchar(25) not null,
    	p_idioma varchar(20) not null,
    	p_subtitulos varchar(40),
    	p_año varchar(5),
    	primary key(id_pelicula),
        dp_id_director int not null,
        descripcion varchar(100) not null,
        dp_duracion varchar (8) not null,
		constraint fkdp_id_director 
        foreign key(dp_id_director)
		references directores(id_director)
		ON DELETE CASCADE
        on update cascade
)engine = InnoDB;


create table if not exists actorpeliculas(
		ap_id_actor int not null,
		ap_id_pelicula int not null,
		primary key(ap_id_actor, ap_id_pelicula),
		constraint fkap_id_pelicula 
        foreign key(ap_id_pelicula)
		references peliculas(id_pelicula)
        ON DELETE CASCADE
        on update cascade,
		constraint fkap_id_actor 
        foreign key(ap_id_actor)
		references actores(id_actor)
        ON DELETE CASCADE
        on update cascade
)engine = InnoDB;

create table if not exists genero(
	id_genero int not null auto_increment,
    genero varchar(25) not null,
    primary key(id_genero)
)engine = InnoDB;

create table if not exists genpelicula(
		gp_id_genero int not null,
		gp_id_pelicula int not null,
		primary key(gp_id_genero,  gp_id_pelicula),
		constraint fkgp_id_genero 
        foreign key(gp_id_genero)
		references genero(id_genero)
        ON DELETE CASCADE
        on update cascade,
		constraint fkgp_id_pelicula 
        foreign key(gp_id_pelicula)
		references peliculas(id_pelicula)
        ON DELETE CASCADE
        on update cascade
)engine = InnoDB;


create table if not exists sala(
		id_sala int not null,
        filas int not null,
        columnas int not null,
        asientos_t int not null,	
        primary key(id_sala)
)engine = InnoDB;

create table if not exists Cartelera(
	c_id_sala int not null,
    c_id_pelicula int not null,
    c_hora TIME not null,
    o_date DATE NOT NULL,
    primary key(c_id_sala,c_hora,o_date),
	constraint fk_c_id_pelicula 
	foreign key(c_id_pelicula)
	references peliculas(id_pelicula)
	ON DELETE CASCADE
	on update cascade,
	constraint fk_c_id_sala 
	foreign key(c_id_sala)
	references sala(id_sala)
	ON DELETE CASCADE
	on update cascade
)engine = InnoDB;


create table if not exists administrador(
	id_administrador int not null auto_increment,
    a_nombre varchar(25) not null,
    a_apellidoPat varchar(25) not null,
    a_apellidoMat varchar(25),
    a_nacionalidad varchar(25) not null,
    a_fnacimiento DATE,
    correo varchar(25) not null,
    contrasena varchar(40) not null,
    primary key(id_administrador)
)engine = InnoDB;

create table if not exists cliente(
    a_nombre varchar(25) not null,
    a_apellidoPat varchar(25) not null,
    a_apellidoMat varchar(25),
    a_nacionalidad varchar(25) not null,
    a_fnacimiento DATE,
    correo varchar(40) not null,
    contrasena varchar(40) not null,
    primary key(correo)
)engine = InnoDB;

create table if not exists Boleto(
	id_boleto int not null auto_increment,
	id_asiento varchar(3) not null,
    peliula varchar(29),
	correo varchar(40),
	c_id_sala int not null,
    c_hora TIME not null,
	o_date DATE NOT NULL,
	constraint fk_b_id_sala 
	foreign key(c_id_sala)
	references sala(id_sala)
	ON DELETE CASCADE
	on update cascade,
	constraint fk_correo 
	foreign key(correo)
	references cliente(correo)
	ON DELETE SET null
	on update cascade,
	primary key(id_boleto),
	constraint fk_cartelera
	foreign key(c_id_sala,c_hora,o_date)
	references Cartelera(c_id_sala,c_hora,o_date)
	ON DELETE CASCADE
	on update cascade
)engine = InnoDB;
