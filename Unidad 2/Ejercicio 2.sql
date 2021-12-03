CREATE DATABASE Ejercicio2;

USE Ejercicio2;

#Television, Audio, Computacion, Refrigeracion, Tarjetas de Video, Teclados, Mouse
CREATE TABLE tblCategorias (
	CategoriaId VARCHAR(100) PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion VARCHAR(200)
);

#Teclado Logitech G500, Uno de los mejores teclados gamer, 129990, 10, 00123(Teclados)
#Samsung TV802323 LED, La mejor tv del mercado, 599990, 5, 00234 (Televisores)
CREATE TABLE tblProductos (
	ProductoId VARCHAR(100) PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion VARCHAR(200),
    Precio Int,
    Stock Int,
    CategoriaId VARCHAR(100),
    CONSTRAINT fk_categoriaProducto FOREIGN KEY (CategoriaId) REFERENCES
    tblCategorias (CategoriaId)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);