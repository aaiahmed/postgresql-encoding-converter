----------------------------------------------------------
-- source database with SQL_ASCII encoding
----------------------------------------------------------
create database pg_sql_ascii_db
with encoding 'SQL_ASCII'
     lc_ctype 'C'
	 lc_collate 'C'
     template template0
     owner etl;

-- create a schema
create schema if not exists raw;

-- create a table to load some test data
create table if not exists raw.account(
    account_id bigserial,
    account_name text);

-- insert some rows with mixed encoding
insert into raw.account (account_name) values ('greg'), ('Renée'), ('比嘉'), ('كنية‎'), ('চৌধুরী');

----------------------------------------------------------
-- target database with SQL_ASCII encoding
----------------------------------------------------------
create database pg_utf8_db
with encoding 'UTF8'
     lc_ctype 'en_US.UTF-8'
	 lc_collate 'en_US.UTF-8'
     template template0
     owner etl;

-- create a schema
create schema if not exists raw;

-- create a table to load some test data
create table if not exists raw.account(
    account_id bigserial,
    account_name text);
