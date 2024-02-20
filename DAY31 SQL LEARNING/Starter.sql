use test1;
create table if not exists Student (
id int auto_increment primary key,
stdName varchar(20) not null,
stdClass varchar(10),
stdMark int check(stdMark>=0 and stdMark <= 100),
stdGender enum('male','female')
);

insert into Student ( stdName, stdClass, stdMark, stdGender)
values('John Deo', 'Four', 75, 'female'), ('Max Ruin', 'Three', 85, 'male'),
 ('Arnold', 'Three', 55, 'male'), ('Krish Star', 'Four', 60, 'female'),
 ('John Mike', 'Four', 60, 'female'), ('Alex John', 'Four', 55, 'male'),
 ('My John Rob', 'Five', 78, 'male'), ('Asruid', 'Five', 85, 'male'),
 ('Tes Qry', 'Six', 78, 'male'), ('Big John', 'Four', 55, 'female');

select * from Student;




