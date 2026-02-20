create database	mysql_tutorial; -- creating database
use mysql_tutorial; -- using database

-- Table Creation Query
create table employees_details(
emp_id int primary key,
emp_full_name varchar(250) not null,
emp_address varchar(500) not null,
emp_salary decimal(10,2) not null,
emp_phone bigint not null
);
select * from employees_details;
desc employees_details;
show databases;
use mysql_tutorial;
show tables
desc employees_details