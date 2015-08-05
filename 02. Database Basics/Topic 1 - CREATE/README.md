Topic 1: CREATE Statement
=======

CREATE DATABASE 
-------

For this course it is important to understand the basics of database design and SQL syntax to familiarize yourself with the data used for the examples. This course uses a Mysql database to store data, but there are many different options, as the textbook explains, for storing and accessing data. We use Mysql because its free and easy to use. 

We begin by creating a database. A CREATE DATABASE statement can be both complicated and simple. For our purposes we are going to create a very simple database to help you get started. If you need additional information on how to make edits to the database or assign permissions, please refer to https://dev.mysql.com/doc/refman/5.5/en/create-database.html

The syntax for CREATE DATABASE is as following:

CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
	[create_specification]...

create_specification:
		[DEFAULT] CHARACTER SET [=] charset_name
	|	[DEFAULT] COLLATE [=] collation_name

EXERCISE
------

CREATE DATABASE nsf_grant

CREATE TABLE
------

Now that you have a database created, you can CREATE TABLE to add tables to that database. The syntax for CREATE TABLE can vary depending on where the data is located. You can create a table from existing databases or tables which pulls the data from one table and creates and inserts the data into another. For this exercise, we are going to create an empty table and then insert data from a CSV file.

CREATE TABLE comes with many different options. For an in-depth description, please refer to http://dev.mysql.com/doc/refman/5.1/en/create-table.html

The syntax for CREATE TABLE is as following:

CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
	(create_definition,...)
	[table_options]
	[partition_options]

EXERCISE
------

delimiter $$

CREATE TABLE `nsf_award` (
  `AwardPKId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `AwardId` varchar(10) NOT NULL,
  `AwardTitle` varchar(200) DEFAULT NULL,
  `AwardEffectiveDate` date DEFAULT NULL,
  `AwardExpirationDate` date DEFAULT NULL,
  `AwardAmount` decimal(13,2) DEFAULT NULL,
  `AwardInstrument` varchar(50) DEFAULT NULL,
  `AwardInstrumentCode` varchar(50) DEFAULT NULL,
  `OrganizationCode` int(11) DEFAULT NULL,
  `Directorate` varchar(100) DEFAULT NULL,
  `DirectorateAbbreviation` varchar(50) DEFAULT NULL,
  `DirectorateCode` varchar(50) DEFAULT NULL,
  `Division` varchar(100) DEFAULT NULL,
  `DivisionAbbreviation` varchar(50) DEFAULT NULL,
  `DivisionCode` varchar(50) DEFAULT NULL,
  `ProgramOfficer` varchar(50) DEFAULT NULL,
  `AbstractNarration` text,
  `MinAmdLetterDate` date DEFAULT NULL,
  `MaxAmdLetterDate` date DEFAULT NULL,
  `ARRAAmount` decimal(13,2) DEFAULT NULL,
  `IsHistoricalAward` varchar(10) DEFAULT NULL,
  `UM_ProgramOfficer_Prefix` varchar(50) DEFAULT NULL,
  `UM_ProgramOfficer_GivenName` varchar(50) DEFAULT NULL,
  `UM_ProgramOfficer_OtherName` varchar(50) DEFAULT NULL,
  `UM_ProgramOfficer_FamilyName` varchar(50) DEFAULT NULL,
  `UM_ProgramOfficer_Suffix` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`AwardPKId`),
  KEY `AwardId` (`AwardId`)
) ENGINE=InnoDB AUTO_INCREMENT=486645 DEFAULT CHARSET=utf8$$

delimiter $$

CREATE TABLE `nsf_institution` (
  `InstitutionId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `AwardId` varchar(10) NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `CityName` varchar(50) DEFAULT NULL,
  `ZipCode` varchar(10) DEFAULT NULL,
  `PhoneNumber` varchar(15) DEFAULT NULL,
  `StreetAddress` varchar(50) DEFAULT NULL,
  `CountryName` varchar(20) DEFAULT NULL,
  `StateName` varchar(25) DEFAULT NULL,
  `StateCode` varchar(2) DEFAULT NULL,
  `EmailAddress` varchar(50) DEFAULT NULL,
  `CountryFlag` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`InstitutionId`),
  KEY `AwardId` (`AwardId`)
) ENGINE=InnoDB AUTO_INCREMENT=486736 DEFAULT CHARSET=utf8$$

delimiter $$

CREATE TABLE `nsf_investigator` (
  `InvestigatorId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `AwardId` varchar(10) NOT NULL,
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `EmailAddress` varchar(100) DEFAULT NULL,
  `StartDate` date DEFAULT NULL,
  `EndDate` date DEFAULT NULL,
  `RoleCode` char(1) DEFAULT NULL,
  `UM_Prefix` varchar(50) DEFAULT NULL,
  `UM_GivenName` varchar(50) DEFAULT NULL,
  `UM_OtherName` varchar(50) DEFAULT NULL,
  `UM_FamilyName` varchar(50) DEFAULT NULL,
  `UM_Suffix` varchar(50) DEFAULT NULL,
  `UM_Corrected_EmailAddress` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`InvestigatorId`),
  KEY `AwardId` (`AwardId`)
) ENGINE=InnoDB AUTO_INCREMENT=562983 DEFAULT CHARSET=utf8$$

INSERT data into empty tables using LOAD DATA INFILE
------

To load data from a CSV file, you will need to use the LOAD DATA INFILE statement. 

The syntax for LOAD DATA INFILE is the following: 

LOAD DATA [LOW_PRIOITY | CONCURRENT] [LOCAL] INFILE 'file_name'
	[REPLACE | IGNORE]
	INTO TABLE tbl_name
	[CHARACTER SET charset_name]
	[{FIELDS | COLUMNS}
		[TERMINATED BY 'string']
		[[OPTIONALLY] ENCLOSED BY 'char']
		[ESCAPED BY 'char']
]

EXERCISE
------

LOAD DATA INFILE 'nsf_award.csv'
	INTO nsf_grant.nsf_award

LOAD DATA INFILE 'nsf_institution.csv'
	INTO nsf_grant.nsf_institution

LOAD DATA INFILE 'nsf_investigator.csv'
	INTO nsf_grant.nsf_investigator