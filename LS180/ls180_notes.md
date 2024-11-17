# Notes from Database Foundations

## Book Notes

### Getting Started

- sudo service postgresql status for checking the status of your database.
- sudo service postgresql start to start running your database.
- sudo service postgresql stop to stop running your database.
- Had to create a user named robert_feconda to connect to any database because postgres uses peer validation with my ubuntu system as a form of login
- The terminal won't run a SQL command until it reaches an `;`


### Basics 

- In the `WHERE`clause of SQL queries, `=` is treated as an 'equality' operator, in that it compares things. In most programming languages, a single `=` operator is used solely for assignment, but not so in SQL.

- PostgreSQL is a client-server database architecture

- SQL sub-languages
  - **DDL: data defintion language** - used to define the structure of a database and the tables and columns with it
  - **DML: data manipulation language** - used to retreive or modify data stored in a database. (SELECT queries are part of DML)
  - **DCL: data control language** - used to determien what various users are allowed to do when interacting with a database

- Basic querie on the `ls_burger` database: `SELECT customer_name FROM orders WHERE side = 'Fries';`
- Schema: concerned with the structure of a database - names of tables, table columns, data types and constraints
- Data: concerned with the contents of a database - actual values associated with specific rows and columns in a table
- Combining schema and data si what provides us with structured data we can interact with
  - We can create, read, update, and delete schema and data - both have different syntax though

- PSQL Meta-commands
  - `\l` or `\list` : displays all databases
  - `\c sql_book` connects to the `sql_book` database
  - `\q` exits the psql session

- CLI commands
  - `psql -d sql_book` : starts a psql session and connect to the `sql_book` database
  - `createdb sql_book` : creates a new database called `sql_book` using a psql utility
  - `dropdb my_database` : permanently deletes the database named `my_database` and all of its data
  - `createdb` and `dropdb` are wrapper functions for actual SQL statements: `CREATE DATABASE` and `DROP DATABASE`

### Create and View Tables

- Format of `CREATE TABLE` statement below

~~~SQL
CREATE TABLE table_name (
    column_1_name column_1_data_type [constraints, ...],
    column_2_name column_2_data_type [constraints, ...],
    .
    .
    .
    constraints
);
~~~

- Column names and data types are a required part of each column definition, constraints are optional
  - Constraints can be defined at the table or column level

- Breakdown the below create table statement:
- Use `\dt` to view a list of tables in the database
  - Use `\d table_name` to view details on one of the tables

~~~SQL
CREATE TABLE users (
       id serial UNIQUE NOT NULL,
       username char(25),
       enabled boolean DEFAULT TRUE
);
~~~

- CREATE TABLE: Firstly, CREATE TABLE users is the primary command.
- users: The name of the table that will be created.
- (): The information in the parentheses is related to the columns in the table.
- id, username, enabled: These are the three columns of the table.
- serial, char(25), boolean: These are the data types of the columns. We will look at data types shortly.
- UNIQUE, NOT NULL: These are constraints. We'll talk about these later in this chapter.
- DEFAULT TRUE: Specifies a default value for the column. We'll revisit this later.
- Notice that each column definition is comma separated; this is the standard in any SQL database management system.

- Data types classify particular values that are allowed for that column
- DDL and DCL make up a tables schema - DCL is the owner column, for security purposes such as access and permissions

### Altering Tables

- Format of an `ALTER TABLE` statement for various alterations:

~~~SQL
ALTER TABLE table_to_change
    stuff_to_change_goes_here
    additional_arguments;

ALTER TABLE users
      RENAME TO all_users;

ALTER TABLE all_users
    RENAME COLUMN username TO full_name;

ALTER TABLE all_users
    ALTER COLUMN full_name TYPE varchar(25);
~~~

- With constraints, instead of changing them, we usually add them to or remove th em from the column definition
  - There is an `ALTER CONSTRAINT` clause used to change certain aspects of Foreign Key constraints but usually just adding/removing
- There are table and column restraints: syntax in commands differs but function the same
  - `NOT NULL` column constraint
  - `PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK` either table or column constraint
- Special command for `NOT NULL` since it's always a column constraint:

~~~SQL
ALTER TABLE table_name
      ALTER COLUMN column_name
      SET NOT NULL;
~~~

- To add any other constraint to an EXISTING table, must use this syntax:

~~~SQL
ALTER TABLE table_name
      ADD [ CONSTRAINT constraint_name ]
      constraint_clause;
~~~

- To remove a constraint:

~~~SQL
ALTER TABLE table_name
      DROP CONSTRAINT constraint_name;
~~~

- If we wanted to remove the default clause that appears when we set the `id serial` column:

~~~SQL
ALTER TABLE all_users
      ALTER COLUMN id
      DROP DEFAULT;
~~~

- Adding a column for last login example:
  - `NOW` is a SQL function, it provides the current date and time when it is called. There are many such functions in postgres

~~~SQL
ALTER TABLE all_users
      ADD COLUMN last_login timestamp
                 NOT NULL
                 DEFAULT NOW();
~~~

- Removing a column:

~~~SQL
ALTER TABLE all_users DROP COLUMN enabled;
~~~

- Deleting a table is much the same as dropping a database:
  - `DROP TABLE all_users;`
  - Both `DROP COLUMN` and `DROP TABLE` are not reversible

### Data and DML

- DML (data minipulation language) is a sub-language of SQL which incorporates the various key words, claues and syntax used to write Data Minupulation Statements.
  - Used for accessing and manipulating data in the database
  - `INSERT, SELECT, UPDATE, DELETE`
- *CRUD* - create, read, update, delete, analogous to the above operations

- General `INSERT` statement:
  - Required: table name, names of columns, values we are storing
  - Must specifcy a value for each column we name, if no column specified for data insertion then a null or default value will be added to the record you wish to store instead

~~~SQL
INSERT INTO table_name
            (column1_name, column2_name,...)
     VALUES (data_for_column1, data_for_column2, ...);

INSERT INTO users (full_name)
           VALUES ('Jane Smith'), ('Harry Potter');
~~~

- Return value: `INSERT 0 1` - 0 is the `oid` tag and `1` is the count of rows inserted
- Often rely on the `DEFAULT` constraint when inserting data for certain columns
- Remember that database indexes come into play when `UNIQUE` constraint is applied

- Can add `CHECK` constraints to ensure values are not something when insertin data:
- `ALTER TABLE users ADD CHECK (full_name <> '');`
  - `<>` is an operator is SQL representing 'not equal'
  - If no name specified for our check constraint, it's fine to leave the naming up to postgres
  - NOTE: must escape quote marks with another quote mark, strings are marked by single `''` in postgres

- More examples:

~~~SQL
INSERT INTO celebrities (first_name, last_name, occupation, date_of_birth, deceased)
              VALUES ('Bruce', 'Springsteen', 'Singer, Songwriter', '1949-09-23', false);

INSERT INTO countries (name, capital, population)
             VALUES ('USA', 'Washington D.C.', 325365189),
                    ('Germany', 'Berlin', 82349400),
                    ('Japan', 'Tokyo', 126672000);

ALTER TABLE celebrities
  ALTER COLUMN last_name DROP NOT NULL;

INSERT INTO orders (customer_name, customer_email, customer_loyalty_points, burger, side, drink, burger_cost, side_cost, drink_cost)
            VALUES ('James Bergman', 'james1998@email.com', 28, 'LS Chicken Burger', 'Fries', 'Cola', 4.50, 0.99, 1.50),
                   ('Natasha O''Shea', 'natasha@osheafamily.com', 18, 'LS Cheeseburger', 'Fries', NULL, 3.50, 0.99, DEFAULT),
                   ('Natasha O''Shea', 'natasha@osheafamily.com', 42, 'LS Double Deluxe Burger', 'Onion Rings', 'Chocolate Shake', 6.00, 1.50, 2.00),
                   ('Aaron Muller', NULL, 10, 'LS Burger', NULL, NULL, 3.00, DEFAULT, DEFAULT);
~~~

- Generally want to avoid boolean columns from having `null` values because it creates three possible states
  - If default set for boolean column and there is not a null constraint set, postgres will still allow null to be inserted

### Select Query Syntax

- `SELECT` statement syntax:

~~~SQL
SELECT column_name, ...
  FROM table_name
  WHERE condition;
~~~

- In a query response:
  - The order of columns in the response is the order that the column names are specified in our query, rather than the 'natural' order of the table columns
  - The number of rows returned are the rows that match the WHERE condition
- Statements consist of identifiers and keywords
  - Identifiers: identify tables or columns within a table
  - Keywords: such as `SELECT` and `FROM` tell postgres to do something specific
  - Can double quote "" identifiers to escape them if they are the same as identifiers, such as `year`

- SQL allows returning sorted data by adding the `ORDER BY column_name` clause to a query

~~~SQL
SELECT column_name, ...
       FROM table_name
       WHERE condition
       ORDER BY column_name;
~~~

- When using `ORDER BY`
  - `False` comes before `True` in ascending order
  - Use keywords `ASC` or `DESC` to specify sort direction, default is `ASC`
  - Can fine tune by having comma-separated expression in the `ORDER BY` clause

~~~SQL
SELECT full_name, enabled FROM users
ORDER BY enabled DESC, id DESC;
~~~

### Operators

- Comparison, Logical, and String matching
  - Not all, just common ones in postgres
- `<, >, <=, >=, =, <>`

- Comparison predicates - behave like operators but with special syntax
  - `BETWEEN`, `NOT BETWEEN`, `IS DISTINCT FROM`, `IS NOT DISTINCT FROM`
  - `IS NULL`, `IS NOT NULL`
  - When identifying `NULL` values we must use the `IS NULL` comparison predicate

`SELECT * FROM my_table WHERE my_column IS NULL;`

- Three logical operators are `AND` `OR`, `NOT`

~~~SQL
SELECT * FROM users
         WHERE full_name = 'Harry Potter'
            OR enabled = 'false';
~~~

- Substring matching usually done using `LIKE` or case-insensitive `ILIKE` operator
  - In our example, trying to find only last names when we only have a full_name column
  - Below, `%` is a wildcard character for string matching
  - Underscore, `_` is also a string wildcard but only for ONE character
  - Can only use `SIMILAR TO` which compares the target column to a Regex pattern
~~~SQL
SELECT * FROM users WHERE full_name LIKE '%Smith';
SELECT * FROM users WHERE full_name LIKE '%SMITH';
SELECT * FROM users WHERE full_name ILIKE '%SMITH';
~~~

- Having multiple `ORDER BY` clauses doesn't affect every row, only if rows are equal does it move onto the next clause

- Remember to include matching for `NULL` if it is allowed
  - Good example for why you should always attach a `NOT NULL` constaint to boolean columns

~~~SQL
SELECT first_name, last_name
FROM celebrities
WHERE deceased != true
OR deceased IS NULL;

SELECT first_name, last_name
FROM celebrities
WHERE occupation LIKE '%Singer%';

SELECT first_name, last_name
FROM celebrities
WHERE (occupation LIKE '%Actor%' OR occupation LIKE '%Actress%')
AND occupation LIKE '%Singer%';
~~~

- Note in the above that `AND` has a higher operator precedence in SQL than `OR`