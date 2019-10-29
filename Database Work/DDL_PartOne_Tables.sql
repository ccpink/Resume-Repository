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

create table SUPPLIER(
    SupplierID integer,
    SupplierName varchar(100),
    Address varchar(255),
    ContactName varchar(100),
    ContactPhone varchar(20),
    ContactEmail varchar(50),
    IsActive BIT
);

create table PRODUCT(
    ProductID integer,
    ProductCode Integer,
    ProductName Char(8),
    Description VARCHAR(50),
    RetailPrice Varchar(100),
    SalePrice float,
    ProductRating int(2),
    NumberInStock varchar(100),
    IsActive BIT,
    IsDiscontinued BIT,
    SupplierID Integer
);
create table CLOTHINGCATEGORY(
    CategoryID integer,
    CategoryName varchar(50),
    IsActive BIT
);

create table CLOTHINGSIZE(
    SizeID integer,
    SizeName varchar(50),
    SizeAbbreviation varchar(3),
    IsActive BIT
);

create table COLOUR(
    ColourID integer,
    ColourName varchar(50),
    ColourCode char(3),
    IsActive BIT
);

create table PRODUCTCATEGORY(
    ProductID integer,
    CategoryID integer
);

create table PRODUCTSIZE(
    ProductID integer,
    SizeID integer
);

create table PRODUCTCOLOUR(
    ProductID integer,
    ColourID integer
);

