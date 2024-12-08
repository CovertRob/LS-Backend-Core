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

- With constraints, instead of changing them, we usually add them to or remove them from the column definition
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


- Shorthand for adding `CHECK` constraints:
  - Must include the parentheses around the `CHECK` clause otherwise you get a syntax error

~~~SQL
ALTER TABLE birds ADD CONSTRAINT check_age CHECK (age > 0);
ALTER TABLE birds ADD CHECK (age > 0);
~~~

- For adding to a specific column you can also use `ALTER COLUMN`:
  - The `SET CONSTRAINT` syntax is used to modify as existing constraint, not to add a new one. Cannot use this syntax to add for example a `UNIQUE` constraint to a column

~~~SQL
ALTER TABLE table_name
ALTER COLUMN column_name SET CONSTRAINT constraint_definition;
~~~

- To add any other constraint to an EXISTING table, must use this syntax:

~~~SQL
ALTER TABLE table_name
      ADD [ CONSTRAINT constraint_name ]
      constraint_clause;

ALTER TABLE films ADD CONSTRAINT director_name
    CHECK (length(director) >= 3 AND position(' ' in director) > 0);
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

- Can also do this to avoid an error:

~~~SQL
DROP TABLE IF EXISTS birds;
~~~

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

### Limit and Offset

- `LIMIT` and `OFFSET` are the base on which pagination is built

~~~SQL
SELECT * FROM users LIMIT 1 OFFSET 1;
~~~

- The above limits the return to 1 row and will skip the first row

- Commonly used in development when testing queries as well

### Distinct Clause

`SELECT DISTINCT full_name FROM users;`

- Use the above to filter out duplicates when selecting

- Using `DISTINCT in conjunction with functions is helpful

`SELECT count(DISTINCT full_name) FROM users;`

### Functions

- Common groups - String, date/time, aggregate
- Examples:

~~~SQL
SELECT length(full_name) FROM users;

SELECT trim(leading ' ' from full_name) FROM users;

SELECT full_name, date_part('year', last_login) FROM users;

SELECT full_name, age(last_login) FROM users;
~~~

- Aggregate functions perform aggregation - compute a single result from a set of input values
- Examples:

~~~SQL
SELECT count(id) FROM users;

SELECT sum(id) FROM users;

SELECT min(last_login) FROM users;

SELECT max(last_login) FROM users;

SELECT avg(id) FROM users;
~~~

- `GROUP BY` allows us to split up groups when using functions
  - When using aggregate function, if you include columns in the column list alongside the function, those those columns must also be included in a `GROUP BY` clause

~~~SQL
SELECT enabled, count(id) FROM users GROUP BY enabled;
~~~

### Updating Data

- `UPDATE` statement syntax
  - The `WHERE` clause is optional, wihtout it postgres will update every row inthe table
  - Best to test target rows using the clause in a `SELECT` statement first

~~~SQL
UPDATE table_name
SET column_name = value, ...
WHERE expression;
~~~

- `DELETE` statement syntax

~~~SQL
DELETE FROM table_name WHERE expression;
~~~

- With update, you can update one or more columns within one or more rows using a set clause, but with delete you can only delete one or more entire rows and not particular pieces of data

- Can set things to null with an `UPDATE` statement to achieve the same thing:

~~~SQL
UPDATE table_name SET column_name1 = NULL
WHERE expression;
~~~

- Note that although in PostgreSQL boolean values display as t or f in the results of a SELECT query, t and f are not valid literal boolean values unless used in single quote marks: 't', 'f'. Other acceptable literals are true or false without quote marks; or 't', 'true', 'y', 'yes', 'on', '1' with quote marks for true, and 'f', 'false', 'n', 'no', 'off', '0' with quote marks for false.

### Normalization

- The process of splitting up data to remove duplication and improve data integrity is known as normalization
  - The mechanism for carrying out normalization is arranging data in multiple tables and defining relationships between them
  - Zooming out and looking at these possible relationships is where database design comes into play

- Database design involves defining **entities** to represent different sorts of data and designing **relationships** between those entities
  - Entities represent real word objects or a set of data that we want to model within our database
  - Create Entity Relationship Diagram (ERD)

### Keys

- Keys are a special type of constraint used to establish realtionships and uniqueness - used to identify a specific row in the current table or refer to a specific row in another table
  - Primary Keys and Foreign Keys

- Primary key: a unique identifier for a row of data
  - Setting a column as `NOT NULL` and `UNIQUE` such as ID basically makes it a primary key, just not officially set yet
  - Each table can only have one primary key - using `ID` is common practice
- Foreign Key: associates a row in one table to a row in another table - you set a column in one table as a Foreign Key and have that column reference another table's Primary Key column

~~~SQL
FOREIGN KEY (fk_col_name)
REFERENCES target_table_name (pk_col_name);
~~~

- Referential Integrity guarantees that a given foreign key value references an existing record in the target table, if it doesn't, an error occurs

### Relationship Types

- One-to-One: exists when a particular entity instance exists in one table and it can have only one associated entity instance in another table

~~~SQL
/*
one-to-one: User has one address
*/

CREATE TABLE addresses (
  user_id int, -- Both a primary and foreign key
  street varchar(30) NOT NULL,
  city varchar(30) NOT NULL,
  state varchar(30) NOT NULL,
  PRIMARY KEY (user_id),
  FOREIGN KEY (user_id)
      REFERENCES users (id)
      ON DELETE CASCADE
);
~~~

- Modality of the relationship determines whether you can or cannot add data without a relationship being present

- Must set `ON DELETE` clauses to delete associated rows when you delete another row otherwise postgres throws an error
  - Various options include `SET NULL`, `CASCADE`, and `SET DEFAULT`

- One-to-Many

~~~SQL
CREATE TABLE books (
  id serial,
  title varchar(100) NOT NULL,
  author varchar(100) NOT NULL,
  published_date timestamp NOT NULL,
  isbn char(12),
  PRIMARY KEY (id),
  UNIQUE (isbn)
);

/*
 one-to-many: Book has many reviews
*/

CREATE TABLE reviews (
  id serial,
  book_id integer NOT NULL,
  reviewer_name varchar(255),
  content varchar(255),
  rating integer,
  published_date timestamp DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (book_id)
      REFERENCES books(id)
      ON DELETE CASCADE
);
~~~

- Note that the foreign key book_id has a NOT NULL constraint. In general, foreign keys in one-to-many relationships should not allow NULL. In this case, it makes no sense to have a review that isn't tied to a book.

- Many-to-Many

- There isn't a way to implement a many-to-many relationship between two tables directly. Instead, we break apart this many-to-many relationship into two one-to-many relationships using a third, cross-reference, table (also known as a join table). This table holds the relationship between the two entities, by having two FOREIGN KEYs, each of which references the PRIMARY KEY of one of the tables for which we want to create this relationship.

~~~SQL
CREATE TABLE checkouts (
  id serial,
  user_id int NOT NULL,
  book_id int NOT NULL,
  checkout_date timestamp,
  return_date timestamp,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
                        ON DELETE CASCADE,
  FOREIGN KEY (book_id) REFERENCES books(id)
                        ON DELETE CASCADE
);
~~~

- Should not allow `NULL` values in many-to-many relationships as well

- Think of many-to-many as combining two one-to-many relationships

- Adding foreign key syntax

~~~SQL
ALTER TABLE table_name
      ADD FOREIGN KEY (column_name)
      REFERENCES other_table(other_table_primary_key);
~~~

- Only use the `ON DELETE CASCADE` statement in one-to-one relationships

- Refer to LS burger example in book for creating a many-to-many setup

### Joins

- JOINs are clauses in SQL statements that link two tables together

- Syntax:
  - Statement after `ON` is the *join condition* - defines logic by which a row in one table is joined to a row in another table
    - Commonly done by using primary key of one table and foreign key of the table we want to join it with

~~~SQL
SELECT table_nameN.column_name, ...
       FROM table_name1
       join_type JOIN table_name2
                 ON join_condition;
~~~

- To join one table to another need following info:
  - Name of the first table to join
  - Type of join to use
  - Name of second table to join
  - Join condition

- The join statement produces what is known as a transient join table - the `SELECT column_list FROM` statement is then executed for this transient table
  - Note that this idea of transient tables is only a mental model

- Types of Joins
  - `INNER` - returns a result set that contains the common elements of the tables (an intersection where they match on the joined condition)
  - `LEFT` - AKA LEFT OUTER JOIN takes all rows from left table and joins it with a second table. Null values are used to represent missing values from the second table
  - `RIGHT` - AKA RIGHT OUTER JOIN, same thing as above but with the table roles switched
  - `FULL` - combination of right and left joins
  - `CROSS` - AKA cartesian join, contains every possible combination of rows from the tables that have been joined - has no ON clause becuase of this - mathematically this is the cross product of a set
  - To join multiple tables together there must be a logical relationship between the tables involved
  - Multiple joins act on the transient table created by the join before it

- Can use aliasing to reduce syntax length:
  - We can even use a shorthand for aliasing by leaving out the AS keyword entirely. FROM users u and FROM users AS u are equivalent SQL clauses.

~~~SQL
SELECT u.full_name, b.title, c.checkout_date
       FROM users AS u
       INNER JOIN checkouts AS c
           ON u.id = c.user_id
       INNER JOIN books AS b
           ON b.id = c.book_id;
~~~

- Can use aliasing for greater context:

~~~SQL
SELECT count(id) AS "Number of Books Checked Out"
       FROM checkouts;
~~~

### Subqueries

- Nesting `SELECT` statements and using them in other `SELECT` statements is known as a subquery

~~~SQL
SELECT u.full_name FROM users u
       WHERE u.id NOT IN (
           SELECT c.user_id FROM checkouts c
       );
~~~

- General rule of thumb, JOINs are faster to run than subqueries


### More Examples

~~~SQL

CREATE TABLE airlines (
  id serial PRIMARY KEY,
  airline_name varchar(30),
  country varchar(50),
  iata_code char(2),
  icao_code char(3),
  website varchar(40),
  CHECK (length(iata_code) = 2),
  CHECK (length(icao_code) = 3)
);
ALTER TABLE airlines
  ALTER COLUMN airline_name SET NOT NULL;
~~~

~~~SQL
  CREATE TABLE airlines (
  id serial PRIMARY KEY,
  airline_name varchar(30) NOT NULL,
  country varchar(50),
  iata_code varchar(2) CHECK (length(iata_code) = 2),
  icao_code varchar(3) CHECK (length(icao_code) = 3),
  website varchar(40)
);
~~~

~~~SQL
CREATE TABLE airlines (
  id serial PRIMARY KEY,
  airline_name varchar(30) NOT NULL,
  country varchar(50),
  iata_code char(2),
  icao_code char(3),
  website varchar(40)
);
ALTER TABLE airlines
  ADD CHECK (length(iata_code) = 2),
  ADD CHECK (length(icao_code) = 3);
~~~

~~~SQL
CREATE TABLE airlines (
  id serial PRIMARY KEY,
  airline_name varchar(30) NOT NULL,
  country varchar(50)
);
ALTER TABLE airlines
  ADD COLUMN iata_code char(2),
  ADD COLUMN icao_code char(3),
  ADD COLUMN website varchar(40),
  ADD CHECK (length(iata_code) = 2),
  ADD CHECK (length(icao_code) = 3);
~~~

- All 4 of the above accomplish the same thing

## Scheme, Data, and SQL

### SQL

- SQL is a special purpose language since it is typically only used to interact with relational databases

- The three sublanguages of SQL are DDL, DML, DCL - Data definition language, data manipulation language, data control language

- Various string escaping:
  - 'canoe'
  - 'a long road'
  - 'weren''t'
  - '"No way!"'

- The `||` operator is used to conatenate strings

- You can do math in SQL
  - `trunc()` truncates a value to a default decimal place of 0 or a specified precision

~~~SQL
sql-course=# SELECT trunc(4 * pi() * 26.3 ^ 2);
 trunc
-------
  8692
(1 row)
~~~

- SQL consists of 3 different sublanguages. One of these sublanguges is called the Data Control Language (DCL) component of SQL. It is used to control access to a database, it is responsible for defining the rights and roles to indvidual users. Common statements include `GRANT` and `REVOKE`
- Another sublanguage is called the Data Manipulation Language (DML). It is used to manipulate the data that is present inside of the database to do things like create, read, update, and delete data. Such actiions include working with statements like `INSERT`, `UPDATE`, `SELECT`, `DELETE`. 
- Another sublanguge is called the Data Definition Language (DDL). This sub-language is used to define the schema and relations of the tables present in the database. This includes creating, modifying, and deleting databases and tables. Put together, this describes how the data is structured. Common statements include `CREATE`, `ALTER`, and `DROP`.

- `SELECT` statements query (read) data in a database. Since it manipulates the data and not the structure of the data, it is part of the DML sublanguage.

- `CREATE TABLE` statements create and define the structure of new tables in the database. This structure defines how the data is stored. It describes the data and its attributes through data definitions. Since this involves the creation of a table structure, this is part of the DDL.

- `ALTER TABLE` statements change the definitions of the table that define what kinds of data is stored and its attributes. THerefore, it is a part of the DDL. Modifies the characteristics and attributes of a table. No manipulation of data takes place.

- `INSERT INTO` statements write data to tables for storage. Since they directly interact with data manipulation, this is part of the DML. Adds new rows of data in a database. Manipulates data and not the structure of it.

- `\d things` is a `psql` meta-command and is therefore not a part of any SQL sub-language

- `DELETE FROM` is part of the DML becuase it deletes specific rows of data in a database, manipulating the data and not the structure of the data.

- `DROP DATABASE` is considered a part of the DDL because its main purpose is to operate on data definitions. The deletion of data is merely a side effect.

- `CREATE SEQUENCE` statements modify the characteristics and attributes of a database by adding a sequence object to the database structure. It therefore manipulates the data definitions and not data directly, therefore it is a part of the DDL. (Sequence is a special kind of database object that generates a series of unique numbers)

### Null

- `Null` in Postgres cannot be evaluated to a truthy value when comparing two `Null` values as you can in other programming languages
  - When a `Null` value appears to either side of any ordinary comparison operator, the operator will return `NULL` instead of true or false. 
  - Postgres displays `NULL` values as empty
  - **Must use the `IS NULL` or `IS NOT NULL` constructs in postgres**

### Data Types

[text](https://www.postgresql.org/docs/current/datatype.html)

- `varchar(n)` stores up to `n` characters while `text` can store an unlimited number of characters (up to Postgres max)

- `integer` vs `decimal` vs `real` - integer values are non-fractional numbers. Real are floating point numbers that can include fractional values. Decimal values can contain non-floating point fractional values with a limited precision

- 2147483647 is the max for an `integer` value

- `timestamp` includes a date and time of day, while `date` only includes the date (no time)

- You cannot store a timezone in `timestamp`, must use `timestamp with time zone` (`timestamptz`)

- **If both values are integers, postgres defaults to integer division which truncates the decimal** - remember when dealing with fraction and division

### Loading Database Dumps

- `$ psql -d my_database < file_to_import.sql` to pipe

- Or you can import a SQL file using the `\i` meta-command

### Select stuff

~~~SQL
SELECT title, extract("year" from current_date) - "year" AS age
  FROM films
  ORDER BY age ASC;

EXTRACT(field FROM source)
~~~

- The PostgreSQL EXTRACT function retrieves specific components of a date, time, or interval value. It is a versatile function useful for breaking down timestamps into meaningful parts, such as year, month, day, hour, or even epoch seconds.

- Keep this example in mind for using `GROUP BY`

~~~SQL
SELECT state, COUNT(id) FROM people GROUP BY state ORDER BY count DESC LIMIT 10;
~~~

~~~SQL
SELECT substr(email, strpos(email, '@') + 1) as domain,
         COUNT(id)
  FROM people
  GROUP BY domain
  ORDER BY count DESC;
~~~

~~~SQL
SELECT date, ROUND((low + high) / 2, 1) AS average FROM temperatures 
WHERE extract(day from date) >= 2 AND extract(day from date) <= 8;

/* OR */

SELECT date, ROUND((high + low) / 2.0, 1) as average
  FROM temperatures
 WHERE date BETWEEN '2016-03-02' AND '2016-03-08';
-- Can also cast here
((high + low) / 2.0)::decimal(3,1).
~~~

- Use the below command to produce a SQL dump file

~~~bash
pg_dump -d sql-course -t weather --inserts > dump.sql
~~~

- If you leave off the `--inserts` flag it will default to using a `COPY FROM stdin` statement istead of multiple insert statements
  - Data will be in tab deliminated rows instead
  - It is more efficient on large data sets

~~~SQL
COPY weather (date, low, high, rainfall) FROM stdin;
2016-03-07  29  32  0.000
2016-03-08  23  31  0.000
2016-03-09  17  28  0.000
2016-03-01  34  43  0.117
2016-03-02  32  44  0.117
2016-03-03  31  47  0.156
2016-03-04  33  42  0.078
2016-03-05  39  46  0.273
2016-03-06  32  43  0.078
\.
~~~

- Weird example for retrieving data based on films decades. Uses integer division to get the decades

~~~SQL
SELECT year / 10 * 10 as decade, ROUND(AVG(duration)) as average_duration
  FROM films GROUP BY decade ORDER BY decade;
~~~

- Funky example for grouping by multiple different things at once:

~~~SQL
SELECT year / 10 * 10 AS decade, genre, string_agg(title, ', ') AS films
  FROM films GROUP BY decade, genre ORDER BY decade, genre;
~~~

- **If you have a default value that violates a constraint you add you will still get an error**

- **PostgreSQL uses 1-based indexing for string functions, so the first character in the string is at position 1.**

### Keys

- SQL databases provide keys that uniquely identify a single row in a database table: Natura Keys and Surrogate Keys

- Natural Key - an existing value in a dataset that can be used to uniquely identify each row of data in that dataset
  - Most values are not good canidates (phone numbers and email addresses change for example)
  - Can use more than one existing value together as a **composite key**

- Surrogate Keys - value that is created solely for the purpose of identifying a row of data in a database table
  - Common one is an auto-incrementing integer
  - Common nomenclature is id (short for identifier)

- The actual interpretation of `SERIAL`

~~~SQL
-- This statement:
CREATE TABLE colors (id serial, name text);

-- is actually interpreted as if it were this one:
CREATE SEQUENCE colors_id_seq;
CREATE TABLE colors (
    id integer NOT NULL DEFAULT nextval('colors_id_seq'),
    name text
);
~~~

- Sequence - special kind of relation that generates a series of numbers
  - Remembers the last number it generated so it generates numbers in a predetermined sequence automatically
  - The next value of a sequence is accessed using `nextval` - kind of like `next` with generators in python
  - Once a number is returned by `nextval` for a standard sequence, it will not be returned again, regardless of whether the value was stored in a row or not
    - For example, if we run `SELECT nextval('colors_id_seq');` separately, it will skip that number next time we go to submit data into the table

- Database development conventions:
  - All tables should have a primary key column called `id`
  - The `id` column should automatically be set to a unique values as new rows are inserted into the table
  - The `id` column will often be an integer, but there are other data types (such as UUIDs) that can provide specific benefits
    - UUID's are universally unique identifiers and are usually large hexadecimal strings representing large numbers

- You can customize your sequences such as even only like below

~~~SQL
CREATE SEQUENCE even_counter INCREMENT BY 2 MINVALUE 2;
~~~

- You cannot add multiple primary keys to a table
- You can still drop the primary key later on:

~~~SQL
ALTER TABLE films DROP CONSTRAINT films_pkey;
~~~

### Query Execution

1. Rows are collected into a virtual table. Creates new temporary tables using data from all the tables listed in the query's `FROM` clause. Different from the transient tables in joins.

2. Rows are filtered using WHERE conditions

3. Rows are divided into groups

4. Groups are filtered using HAVING conditions. Similar to `WHERE` conditions but are applied to the values that are used to create groups and not individual rows. A column that is mentioned in a `HAVING` clause should appear in a `GROUP BY` cclause and/or an aggregate function. Both `GROUP BY` and aggregate functions perform grouping, and the `HAVING` clause is used to filter that aggregated/grouped data

5. Computer values to return using select list

6. Sort results as defined in an `ORDER BY` clause otherwise defualt is the order of rows in the tables

7. Limit results based on `LIMIT` or `OFFSET` clauses to adjust which rows in the result set are returned

### Aliasing

- Use aliases for columns that would otherwise create collisions when conducting joins and to clarify data

- If you alias a table, postgres expects you to use that alias everywhere in the query, even if its before the alias definition
  - You don't want to alias table names unless required

### Enumeration

- Enumerated (enum) types are data types that comprise a static, ordered set of values. They are equivalent to the enum types supported in a number of programming languages. An example of an enum type might be the days of the week, or a set of status values for a piece of data.

- Existing values cannot be removed from an enum type, nor can the sort ordering of such values be changed, short of dropping and re-creating the enum type.

- Enums are also case and space sensitive

- Syntax is as follows:

~~~SQL
ALTER TABLE stars
DROP CONSTRAINT stars_spectral_type_check;

CREATE TYPE spectral_type_enum AS ENUM ('O', 'B', 'A', 'F', 'G', 'K', 'M');

ALTER TABLE stars
ALTER COLUMN spectral_type TYPE spectral_type_enum
                           USING spectral_type::spectral_type_enum;
~~~

### Schema Diagrams

- conceptual scheme are high level desings focused on identifying entities and their relationships

- physical schema are low level database-specific design focused on implementation

### Database diagrams

- Cardinality - the number of objects on each side of the relationship

- Modality - indicates if the relationship is required or optional
  - if required there must be an instance of the relationship
  - usually 1 for required and 0 for optional
  - Not usually seen in the schema of a database but probably certain constraints in the table to enforce the relationships

- Most common notation is crows foot notation

- **one to one relationships are very rare and usually indicates that those entities should be in the same table together**

### Practice

- More complex joins:

~~~SQL
SELECT e.name, COUNT(t.id) AS popularity
  FROM events AS e
  LEFT OUTER JOIN tickets AS t
    ON t.event_id = e.id
  GROUP BY e.id
  ORDER BY popularity DESC;
~~~