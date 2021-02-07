# postgresql-encoding-converter

PostgreSQL supports different [encodings](https://www.postgresql.org/docs/13/multibyte.html), 
including `SQL_ASCII`, `UTF8`, `WIN1252` etc. 

However, `SQL_ASCII`, a common encoding found in earlier databases, works 
differently than the others. It does not enforce any particular encoding, 
meaning it allows to store characters from any encoding. Thus it depends on the user
it to enforce only ascii characters from the client side. 

Because `SQL_ASCII` does not enforce any encoding, converting a database from 
`SQL_ASCII` to the more ideal encoding `UTF8` can become very challenging. 
Because mixed encoding characters can get into a database or even within a single table, 
loading the data into the target database may get errors like, 
`ERROR:  invalid byte sequence for encoding "UTF8 ..."`

This program helps to convert a PostgreSQL `SQL_ASCII` encoded database, 
into `UTF-8`. It takes a list of tables as a configuration and gets a csv
dump of those tables. It then converts the csv into utf-8 with the 
configured Python [error handlers](https://docs.python.org/3/library/codecs.html#error-handlers).

It can then help create the target table and load the csv in the destination 
database. 

## Usage
Add the ENV `PGPASSWORD` containing the PostgreSQL database user password, 
and configure the rest of the settings in `config.yaml` file. 

Then simply run:
    ```
    $ python main.py
    ```
   
The converted CSV files can be found inside the `csv` folder.  