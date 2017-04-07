drop database if exists learndb;
drop database if exists test_learndb;
create database learndb CHARACTER SET utf8 COLLATE utf8_general_ci;
create database test_learndb CHARACTER SET utf8 COLLATE utf8_general_ci;
grant all on learndb.* to 'admin'@'localhost' identified by 'admin@123#';
grant all on test_learndb.* to 'admin'@'localhost' identified by 'admin@123#';
-- Remote Login uncomment to Enable
grant all on learndb.* to 'admin'@'%' identified by 'admin@123#';
grant all on test_learndb.* to 'admin'@'%' identified by 'admin@123#';
use learndb;

