```mysql
create database db1;
show create database db1;
drop database antsyn;
show databases;
 drop user antsyn_dbusr@localhost;
 flush privileges;
use db1;
# view the current database
select database();

create table student(
id int,
name varchar(20),
gender varchar(10),
age int
);

show tabels;
show create table student;
desc student;

alter table student rename to stu;
alter table stu change name sname varchar(10);
alter table stu modify sname int;
alter table stu add address varchar(50);
alter table stu drop address;

drop table stu;

insert into stu (id,name,gender,age) values (1,'bob','male'.'21')
insert into stu (id,name,gender,age) values (1,'bob','male'.'21') (2,'july','female'.'20') (3,'tom','male'.'15')
update stu set age =17,id=4 where name='tom'

# update to all 
update stu set age=18;
delete from stu where name='july'

```

```mysql
DROP DATABASE IF EXISTS mydb;
CREATE DATABASE mydb;
USE mydb;

-- 创建student表
CREATE TABLE student (
    sid CHAR(6),
    sname VARCHAR(50),
    age INT,
    gender VARCHAR(50) DEFAULT 'male'
);

-- 向student表插入数据
INSERT INTO student (sid,sname,age,gender) VALUES ('S_1001', 'lili', 14, 'male');
INSERT INTO student (sid,sname,age,gender) VALUES ('S_1002', 'wang', 15, 'female');
INSERT INTO student (sid,sname,age,gender) VALUES ('S_1003', 'tywd', 16, 'male');
INSERT INTO student (sid,sname,age,gender) VALUES ('S_1004', 'hfgs', 17, 'female');
INSERT INTO student (sid,sname,age,gender) VALUES ('S_1005', 'qwer', 18, 'male');
INSERT INTO student (sid,sname,age,gender) VALUES ('S_1006', 'zxsd', 19, 'female');
INSERT INTO student (sid,sname,age,gender) VALUES ('S_1007', 'hjop', 16, 'male');
INSERT INTO student (sid,sname,age,gender) VALUES ('S_1008', 'tyop', 15, 'female');
INSERT INTO student (sid,sname,age,gender) VALUES ('S_1009', 'nhmk', 13, 'male');
INSERT INTO student (sid,sname,age,gender) VALUES ('S_1010', 'xdfv', 17, 'female');
```

```mysql
select * from student;
select sid,sname from student;
select distinct gender from student;
select count(*) from student;
select max(age) from student;
select any_value(sname),any_value(id) from student;
select any_value(sid),max(age) from student;
select * from student where age>=17;
select * from student where sid in ('S_1002','S_1003');
```

# Install mysql on rhel 7

```
rpm -Uvh https://repo.mysql.com/mysql80-community-release-el7-3.noarch.rpm
sed -i 's/enabled=1/enabled=0/' /etc/yum.repos.d/mysql-community.repo
yum -y remove mariadb-libs
yum --enablerepo=mysql57-community install mysql-community-server
systemctl start mysqld.service
```





