drop database if exists learndb;
create database learndb CHARACTER SET utf8 COLLATE utf8_general_ci;
grant all on learndb.* to 'admin'@'localhost' identified by 'admin@123#';
-- Remote Login uncomment to Enable
grant all on learndb.* to 'admin'@'%' identified by 'admin@123#';
use learndb;

