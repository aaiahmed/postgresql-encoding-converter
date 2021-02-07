-- usage: select * from public.get_ddl_statement('schema', 'table');
drop function if exists public.get_ddl_statement(text, text);

create function public.get_ddl_statement(sch_name text, tbl_name text)
    returns text as $$

    declare
    _stmnt text;
	_col_name text;
	_data_type text;
	_temp text;
	_ddl text;

    begin
	_temp = 'create table if not exists ' || sch_name || '.' || tbl_name || ' (';
    for _col_name, _data_type in (select
                        column_name, data_type
                     from
                        information_schema.columns
                     where
                        table_schema = sch_name and
                        table_name = tbl_name
                     ) loop

        _temp = _temp || _col_name || ' ' || _data_type || ', ';
    end loop;
	_ddl = substring(_temp from 1 for length(_temp) - 2) || ');';

    return _ddl;
    end;
    $$ language plpgsql;