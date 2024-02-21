-- use test1;
-- create table if not exists Student (
-- id int auto_increment primary key,
-- stdName varchar(20) not null,
-- stdClass varchar(10),
-- stdMark int check(stdMark>=0 and stdMark <= 100),
-- stdGender enum('male','female'),
-- stdCountry varchar(20) default 'England'
-- );

-- insert into Student ( stdName, stdClass, stdMark, stdGender)
-- values('John Deo', 'Four', 75, 'female'), ('Max Ruin', 'Three', 85, 'male'),
--  ('Arnold', 'Three', 55, 'male'), ('Krish Star', 'Four', 60, 'female'),
--  ('John Mike', 'Four', 60, 'female'), ('Alex John', 'Four', 55, 'male'),
--  ('My John Rob', 'Five', 78, 'male'), ('Asruid', 'Five', 85, 'male'),
--  ('Tes Qry', 'Six', 78, 'male'), ('Big John', 'Four', 55, 'female');

-- select * from Student;

create database if not exists world;
use world;

create table if not exists Region (
regionId int auto_increment primary key,
regionName varchar(24),
continentId varchar(24)
);

create table if not exists Country (
countryId int primary key auto_increment,
countryName varchar(24) not null,
regionId int,
foreign key (regionId) references Region(regionId)
);

insert into Region(regionName) value ('North America'), ('Europe'), ('Asia'), ('Oceania'), ('South America'), ('Africa');
insert into Country(countryName, regionId) value ('London', 2), ('France', 2), ('Stockholm', 2), ('Portland', 1), ('Atlanta', 1), ('Miami', 5);

select * from Country;



