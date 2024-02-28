create database if not exists assignment;
use assignment;
 -- Creating Tables
 
create table if not exists Members (
  MemberID varchar(10) NOT NULL,
  MemberFName varchar(20) NOT NULL,
  MemberLName varchar(20) NOT NULL,
  MemberLoc varchar(40)default NULL,
  PRIMARY KEY  (MemberID));
  
  create table if not exists Vehicles (
  VehicleReg varchar(20) NOT NULL,
  VehicleMake varchar(20) NOT NULL,
  VehicleModel varchar(10) NOT NULL,
  MemberID varchar(10)default NULL,
  PRIMARY KEY  (VehicleReg)); 
  
  create table if not exists Engineers (
  EngineerID int NOT NULL,
  EngineerFName varchar(20) NOT NULL,
  EngineerLName varchar(20) NOT NULL,
  PRIMARY KEY  (EngineerID));
  
  create table if not exists Breakdowns (
  BreakdownID varchar(10) NOT NULL,
  VehicleReg varchar(20) NOT NULL,
  EngineerID int NOT NULL,
  BreakdownDate date NOT NULL,
  BreakdownTime time DEFAULT NULL,
  BreakdownLoc varchar(40) NOT NULL,
  PRIMARY KEY  (BreakdownID));
  
  -- Alter key to add foreign keys
  
ALTER TABLE Vehicles ADD  FOREIGN KEY (MemberID) REFERENCES Members (MemberID);

ALTER TABLE Breakdowns ADD  FOREIGN KEY (VehicleReg) REFERENCES Vehicles (VehicleReg);
ALTER TABLE Breakdowns ADD  FOREIGN KEY (EngineerID) REFERENCES Engineers (EngineerID);

-- Adding Data

INSERT INTO Members (MemberID,  MemberFName, MemberLName, MemberLoc) VALUES 
(123456789, 'John', 'Smith','731 Fondren, Houston, TX'),
(333445555, 'Franklin', 'Wong', '638 Voss, Houston, TX'),
(453453453,'Joyce', 'English', '5631 Rice, Houston, TX'),
(666884444, 'Ramesh',  'Narayan', '975 Fire Oak, Humble, TX'),
(888665555, 'James', 'Borg', '3321 Castle, Spring, TX');

INSERT INTO Vehicles (VehicleReg,  VehicleMake, VehicleModel, MemberID) VALUES 
('2G4WB52K321479906', 'Mercedes-Benz', 'R-Class', 123456789),
('2C3CDZATXFH249283', 'Suzuki', 'SJ', 123456789),
('5TFBY5F16BX583344','Mercedes-Benz', 'C-Class', 333445555),
('1FAHP2DW5AG988139', 'Honda',  'Civic', 453453453),
('SAJWA4GB3FL343223', 'Mazda', 'MX-6', 666884444),
('WP0AA2A80CS303614', 'Chevrolet', '1500', 666884444),
('2C3CDXEJ8DH063087', 'Hyundai', 'XG350', 888665555),
('5FRYD3H62GB792342', 'Chrysler', 'LHS', 333445555);

INSERT INTO Engineers (EngineerID,  EngineerFName, EngineerLName) VALUES 
(88291011, 'Bob', 'Blank'),
(38821291, 'Mark', 'Write'),
(92372921,'Daemon', 'Trow');


INSERT INTO Breakdowns (BreakdownID, VehicleReg, EngineerID, BreakdownDate, BreakdownTime, BreakdownLoc) VALUES 
('110201A','2G4WB52K321479906', 88291011, '2001-02-11', '11:00:00', 'Houston, TX'),
('110201B','2C3CDZATXFH249283', 88291011, '2001-02-11', '18:00:00', 'Houston, TX'),
('270201A','5TFBY5F16BX583344',38821291, '2001-02-27', '13:00:00', 'Houston, TX'),
('280201A','1FAHP2DW5AG988139', 38821291,  '2001-02-28', '10:00:00', 'Houston, TX'),
('150301A','SAJWA4GB3FL343223', 92372921, '2001-03-15', '14:20:00', 'Spring, TX'),
('010401A','WP0AA2A80CS303614', 92372921, '2001-04-01', '13:00:00', 'Spring, TX'),
('140401A','2C3CDXEJ8DH063087', 92372921, '2001-04-14', '15:00:00', 'Spring, TX'),
('030501A','5FRYD3H62GB792342', 88291011, '2001-05-03', '09:00:00', 'Houston, TX'), 
('070501A','2C3CDZATXFH249283', 88291011, '2001-05-07', '18:00:00', 'Houston, TX'),
('010601A','2G4WB52K321479906', 88291011, '2001-06-01', '10:00:00', 'Houston, TX'),
('180601A','SAJWA4GB3FL343223', 92372921, '2001-06-18', '14:00:00', 'Spring, TX'),
('280701A','1FAHP2DW5AG988139', 38821291,  '2001-07-28', '15:00:00', 'Houston, TX');

-- Preview 
select * from Members;
select * from Engineers;
select * from Vehicles;
select * from Breakdowns;

-- ----------------- Task 3 ------------------- --

-- Name of Members living in a location: 
select * from Members where Members.MemberLoc like '%Houston%';

-- All Cars Registered with a company ie Nissan Cars
select * from Vehicles where Vehicles.VehicleMake = 'Mercedes-Benz';

-- The number of engineers that work for the company
select count(Engineers.EngineerFName) as 'Number of Engineers' from Engineers ;

-- The number of members registered
select count(Members.MemberFName) as 'Number of Members' from Members;

-- All breakdown after particular date
select * from Breakdowns where Breakdowns.BreakdownDate > '01-04-11' order by BreakdownDate;

-- All breakdown after particular date
select * from Breakdowns where Breakdowns.BreakdownDate between '01-02-11' and '01-05-01'  order by BreakdownDate;

-- The number of times a particular vehicle has broken down 
select Breakdowns.VehicleReg, Vehicles.VehicleMake, Vehicles.VehicleModel, count(Breakdowns.VehicleReg) as '# of breakdowns' 
from Breakdowns LEFT JOIN Vehicles ON Breakdowns.VehicleReg=Vehicles.VehicleReg group by Breakdowns.VehicleReg;  -- Total Breakdowns

select Breakdowns.VehicleReg, Vehicles.VehicleMake, Vehicles.VehicleModel, count(Breakdowns.VehicleReg) as '# of breakdowns' 
from Breakdowns LEFT JOIN Vehicles ON Breakdowns.VehicleReg=Vehicles.VehicleReg where Breakdowns.VehicleReg='1FAHP2DW5AG988139' group by Breakdowns.VehicleReg;  -- Specific Breakdown

-- The number of vehicles broken down more than once 
select VehicleReg, count(VehicleReg) as '# of breakdowns' from Breakdowns group by VehicleReg having count(VehicleReg) > 1; 


-- ----------------- Task 3 ------------------- --









