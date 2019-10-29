#create database Products_DD;
use Products_DD;
#Name: Charles Pink
#Date: 10/22/2019
#Class: Data Fundamentals

#I need to create tables in this order so later I can put in f_keys correctly
#In this order Supplier, Product, Clothing Category, Clothing Size, Colour, Product Category,
#Product Size, Product Colour

drop table if exists PRODUCTSIZE;
drop table if exists PRODUCTCATEGORY;
drop table if exists PRODUCTCOLOUR;
drop table if exists CLOTHINGCATEGORY;
drop table if exists CLOTHINGSIZE;
drop table if exists COLOUR;
drop table if exists PRODUCT;
drop table if exists SUPPLIER;


create table SUPPLIER
(
    SupplierID integer auto_increment,
    SupplierName varchar (100) NOT NULL,
    Address varchar (255) NOT NULL,
    ContactName varchar (100),
    ContactPhone varchar (20),
    ContactEmail varchar (50),
    IsActive BIT NOT NULL DEFAULT 1,
    PRIMARY KEY (SupplierID)



);

create table PRODUCT
(
    ProductID integer auto_increment,
    ProductCode integer NOT NULL UNIQUE ,
    ProductName char (8) NOT NULL,
    Description varchar (50),
    RetailPrice varchar (100) NOT NULL CHECK ( RetailPrice < 0 ),
    SalePrice float CHECK ( SalePrice < 0 ),
    ProductRating int (2) NOT NULL CHECK ( ProductRating >= 1 AND ProductRating <= 5 ),
    NumberInStock varchar (100) NOT NULL DEFAULT 0,
    IsActive BIT NOT NULL DEFAULT 1,
    IsDiscontinued BIT NOT NULL DEFAULT 0,
    SupplierID Integer,
    PRIMARY KEY (ProductID)
);
create table CLOTHINGCATEGORY
(
    CategoryID integer auto_increment,
    CategoryName varchar (50),
    IsActive BIT NOT NULL DEFAULT 1,
    PRIMARY KEY (CategoryID)
);

create table CLOTHINGSIZE
(
    SizeID integer AUTO_INCREMENT,
    SizeName varchar (50) NOT NULL,
    SizeAbbreviation varchar (3) NOT NULL CHECK ( SizeAbbreviation = 'XS' OR SizeAbbreviation = 'S' OR SizeAbbreviation = 'M' OR SizeAbbreviation = 'L' OR SizeAbbreviation = 'XL' OR SizeAbbreviation = 'XXL' ),
    IsActive BIT NOT NULL DEFAULT 1,
    PRIMARY KEY (SizeID)
);

create table COLOUR
(
    ColourID integer auto_increment,
    ColourName varchar(50) NOT NULL ,
    ColourCode char(3) NOT NULL UNIQUE ,
    IsActive BIT NOT NULL DEFAULT 1,
    PRIMARY KEY (ColourID)
);

create table PRODUCTCATEGORY
(
    ProductID integer,
    CategoryID integer,
    PRIMARY KEY (ProductID, CategoryID)

);

create table PRODUCTSIZE
(
    ProductID integer,
    SizeID integer,
    PRIMARY KEY (ProductID, SizeID)

);

create table PRODUCTCOLOUR
(
    ProductID integer,
    ColourID integer,
    PRIMARY KEY (ProductID, ColourID)

);

