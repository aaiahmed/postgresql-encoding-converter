-- create a test database with SQL_ASCII encoding.
create database pg_sql_ascii_db
with encoding 'SQL_ASCII'
     lc_ctype 'C'
	 lc_collate 'C'
     template template0
     owner etl;

-- create a schema.
create schema if not exists raw;

-- create a test table.
create table raw.account(
    account_id bigserial,
    account_name text);

-- insert some mixed encoding data
insert into raw.account (account_name) values ('john'), ('Renée'), ('比嘉'), ('كنية‎'), ('চৌধুরী');