create database nombreBD;

use nombreBD;


create table tbl_clientes(

	rut varchar(20),
    nombres varchar(100),
    apellidos varchar(100),
    correo varchar(100),
    telefono varchar(100),
    direccion varchar(100),
    comuna varchar(100),
	primary key (rut)

);


create table tbl_autos(

	patente varchar(6),
    marca varchar(100),
    modelo varchar(100),
    year int,
    numero_chasis varchar(100),
    color varchar(100),
    rut_cliente varchar(20),
	primary key (patente),
    
    constraint fk_tblclientes_rut foreign key (rut_cliente) references tbl_clientes (rut)
    

);


create table tbl_mecanicos(

	rut varchar(20),
    nombres varchar(100),
    apellidos varchar(100),
    correo varchar(100),
    telefono varchar(100),
    direccion varchar(100),
    comuna varchar(100),
	primary key (rut)

);

create table tbl_reparaciones(

	cod_reparacion int primary key auto_increment,
    patente varchar(6),
    rut varchar(20),
    fecha date,
    costo int,
    observacion varchar(100),
    
    constraint fk_tblauto_patente foreign key (patente) references tbl_autos (patente),
    constraint fk_tblmecanicos_rut foreign key (rut) references tbl_mecanicos (rut)

);

create table tbl_detalleReparacion(
	
    cod_detalle int primary key auto_increment,
    cod_reparacion int,
    repuesto varchar(100),
    subtotal int,
    observacion varchar(100),
    
    constraint fk_tblreparaciones_cod_reparacion foreign key (cod_reparacion) references tbl_reparaciones (cod_reparacion)
	
);



