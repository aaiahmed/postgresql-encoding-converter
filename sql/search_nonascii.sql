-- usage: select * from public.search_nonscii_characters('schema', 'table');

drop function if exists public.search_nonscii_characters(text,text);

create function public.search_nonscii_characters(sch_name text, tbl_name text)
    returns table(_sch_name text, _tbl_name text, _col_name text, _col_content text)
    as $$

    declare
    _stmnt text;

    begin

    create temp table temp_non_ascii_content (
        _sch_name text,
        _tbl_name text,
        _col_name text,
        _col_content text);

    for _col_name in (select
                        column_name
                     from
                        information_schema.columns
                     where
                        table_schema = sch_name and
                        table_name = tbl_name and
                        data_type in ('character', 'character varying', 'text')
                     ) loop

        _stmnt = 'select '|| _col_name ||'::text from '|| sch_name || '.' || tbl_name ||' where '|| _col_name ||' ~ ''[^[:ascii:]]''';

        for _col_content in execute (_stmnt) loop
            insert into temp_non_ascii_content values (sch_name, tbl_name, _col_name, _col_content);
        end loop;

    end loop;

    return query select * from temp_non_ascii_content;
    end;
    $$ language plpgsql;