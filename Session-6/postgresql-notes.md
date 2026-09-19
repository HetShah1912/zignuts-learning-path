# PostgreSQL Notes

> These notes focus on PostgreSQL-specific concepts and PostgreSQL
> features that are different from or not normally covered in MySQL
> notes. Common SQL topics such as basic `SELECT`, `WHERE`, `GROUP BY`,
> `ORDER BY`, basic joins, `INSERT`, `UPDATE`, `DELETE`, and ordinary
> constraints are intentionally not repeated.

Reference: https://neon.com/postgresql/tutorial/

## PostgreSQL vs MySQL

  ---------------------------------------------------------------------------------------------
  Topic                   PostgreSQL                     MySQL
  ----------------------- ------------------------------ --------------------------------------
  Database engine         Object-relational database     Relational database system
                          system                         

  Auto-increment          `GENERATED ... AS IDENTITY`,   `AUTO_INCREMENT`
                          `SERIAL`                       

  Boolean                 Native `BOOLEAN`               `BOOLEAN` is effectively an alias for
                                                         `TINYINT(1)`

  String type             `TEXT` is commonly used        `TEXT` family and `VARCHAR` are
                          without a length limit         commonly used

  JSON                    `JSON` and highly capable      `JSON`
                          `JSONB`                        

  Arrays                  Native array types such as     No equivalent native general-purpose
                          `TEXT[]`, `INTEGER[]`          array type

  UUID                    Native `UUID` type             Usually stored using character or
                                                         binary types

  Key/value storage       `hstore` extension             No direct equivalent

  Case-sensitive          Double quotes: `"UserName"`    Backticks: `` `UserName` ``
  identifiers                                            

  String concatenation    `||` operator                  `CONCAT()` is commonly used

  Regex                   Powerful built-in              Regex support exists but
                          regular-expression             syntax/features differ
                          operators/functions            

  Upsert                  `INSERT ... ON CONFLICT`       `INSERT ... ON DUPLICATE KEY UPDATE`

  MERGE                   Supported                      Supported in newer MySQL versions with
                                                         different syntax/behavior

  Return changed rows     `RETURNING` is available with  Traditionally requires a separate
                          many DML statements            query for this pattern

  Full outer join         Native `FULL OUTER JOIN`       No direct `FULL OUTER JOIN`

  Set difference          `EXCEPT`                       Uses alternatives such as joins or
                                                         other query techniques

  Filtering aggregates    `FILTER (WHERE ...)`           Commonly uses conditional expressions
                                                         such as `CASE`

  Conditional uniqueness  Partial indexes can enforce    No direct equivalent to PostgreSQL
                          uniqueness for only selected   partial indexes
                          rows                           

  Index types             B-tree, Hash, GiST, SP-GiST,   Different index architecture and
                          GIN, BRIN                      supported index types

  Table inheritance       Supported                      No direct equivalent

  User-defined types      `CREATE TYPE`, domains, enums, Different type system
                          composite types                

  Extensions              Rich extension ecosystem using Different plugin/component model
                          `CREATE EXTENSION`             

  Row-level security      Native `RLS` policies          No direct equivalent with the same
                                                         PostgreSQL model

  Transaction behavior    Strong MVCC-based concurrency  Uses InnoDB and its own
                          model                          transaction/concurrency implementation
  ---------------------------------------------------------------------------------------------

## PostgreSQL Data Types

### `TEXT`

PostgreSQL provides `TEXT` for variable-length strings without requiring
a maximum length.

``` sql
CREATE TABLE users (
    name TEXT
);
```

### `BOOLEAN`

PostgreSQL has a native Boolean type.

``` sql
CREATE TABLE tasks (
    completed BOOLEAN DEFAULT FALSE
);
```

Valid Boolean values include:

``` sql
TRUE
FALSE
```

### `SERIAL`

`SERIAL` creates an integer column backed by a sequence and is commonly
used for auto-generated IDs.

``` sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT
);
```

Insert without specifying the ID:

``` sql
INSERT INTO users (name)
VALUES ('Het');
```

### Identity Columns

Identity columns are the modern SQL-standard approach to generated
numeric IDs.

``` sql
CREATE TABLE users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT
);
```

You can also use:

``` sql
GENERATED BY DEFAULT AS IDENTITY
```

`GENERATED ALWAYS` normally requires PostgreSQL to generate the value,
while `BY DEFAULT` allows an explicitly supplied value when appropriate.

### `UUID`

PostgreSQL supports UUID as a native data type.

``` sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    name TEXT
);
```

UUIDs are useful when identifiers should not simply be sequential
integers.

### `ARRAY`

PostgreSQL supports arrays as a native data type.

``` sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT,
    skills TEXT[]
);
```

Insert an array:

``` sql
INSERT INTO students (name, skills)
VALUES ('Het', ARRAY['JavaScript', 'React', 'PostgreSQL']);
```

Array literal syntax:

``` sql
INSERT INTO students (name, skills)
VALUES ('Het', '{"JavaScript","React","PostgreSQL"}');
```

Access an array element:

``` sql
SELECT skills[1]
FROM students;
```

Check whether an array contains a value:

``` sql
SELECT *
FROM students
WHERE 'React' = ANY(skills);
```

### `JSON`

PostgreSQL supports JSON values.

``` sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    details JSON
);
```

Insert JSON:

``` sql
INSERT INTO products (details)
VALUES ('{"brand": "Nike", "price": 5000}');
```

### `JSONB`

`JSONB` stores JSON in a binary format designed for efficient processing
and indexing.

``` sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    details JSONB
);
```

Query a JSON field:

``` sql
SELECT details -> 'brand'
FROM products;
```

Get a JSON value as text:

``` sql
SELECT details ->> 'brand'
FROM products;
```

Nested access:

``` sql
SELECT details -> 'manufacturer' ->> 'name'
FROM products;
```

Containment:

``` sql
SELECT *
FROM products
WHERE details @> '{"brand": "Nike"}';
```

### `HSTORE`

`hstore` stores key-value pairs in a single PostgreSQL value.

Enable the extension:

``` sql
CREATE EXTENSION IF NOT EXISTS hstore;
```

Example:

``` sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    attributes HSTORE
);
```

Insert:

``` sql
INSERT INTO products (attributes)
VALUES ('"color"=>"black", "size"=>"large"');
```

### `INTERVAL`

`INTERVAL` represents a period of time.

``` sql
SELECT INTERVAL '2 days';
```

Arithmetic:

``` sql
SELECT CURRENT_DATE + INTERVAL '7 days';
```

### `TIMESTAMP WITH TIME ZONE`

PostgreSQL supports timezone-aware timestamps.

``` sql
CREATE TABLE events (
    event_time TIMESTAMPTZ
);
```

## PostgreSQL Type Casting

PostgreSQL supports explicit type conversion using `CAST()`:

``` sql
SELECT CAST('100' AS INTEGER);
```

PostgreSQL also provides the shorthand `::` operator:

``` sql
SELECT '100'::INTEGER;
```

Examples:

``` sql
SELECT '2026-09-19'::DATE;

SELECT 100::TEXT;

SELECT '12.50'::NUMERIC;
```

## PostgreSQL Sequences

A sequence generates a series of numeric values.

Create a sequence:

``` sql
CREATE SEQUENCE user_id_seq;
```

Get the next value:

``` sql
SELECT nextval('user_id_seq');
```

Get the current value:

``` sql
SELECT currval('user_id_seq');
```

Get the previous value:

``` sql
SELECT last_value
FROM user_id_seq;
```

Reset a sequence:

``` sql
ALTER SEQUENCE user_id_seq RESTART WITH 1;
```

Sequences are commonly used internally by `SERIAL` columns.

## `RETURNING`

`RETURNING` is one of the most useful PostgreSQL-specific features when
working with application backends.

It allows a DML statement to return affected rows without requiring a
separate query.

### Insert and Return the Generated ID

``` sql
INSERT INTO users (name)
VALUES ('Het')
RETURNING id;
```

### Return the Complete Inserted Row

``` sql
INSERT INTO users (name)
VALUES ('Het')
RETURNING *;
```

### Update and Return Rows

``` sql
UPDATE users
SET name = 'Het Shah'
WHERE id = 1
RETURNING *;
```

### Delete and Return Rows

``` sql
DELETE FROM users
WHERE id = 1
RETURNING *;
```

This is especially useful in Node.js/Express applications because the
application can receive the inserted or modified row immediately.

## PostgreSQL UPSERT

PostgreSQL performs upsert operations using `INSERT ... ON CONFLICT`.

### Ignore a Conflict

``` sql
INSERT INTO users (id, name)
VALUES (1, 'Het')
ON CONFLICT (id)
DO NOTHING;
```

### Update on Conflict

``` sql
INSERT INTO users (id, name)
VALUES (1, 'Het Shah')
ON CONFLICT (id)
DO UPDATE
SET name = EXCLUDED.name;
```

`EXCLUDED` refers to the row that PostgreSQL attempted to insert.

Example:

``` sql
INSERT INTO products (id, name, price)
VALUES (1, 'Keyboard', 1200)
ON CONFLICT (id)
DO UPDATE
SET
    name = EXCLUDED.name,
    price = EXCLUDED.price;
```

## `MERGE`

PostgreSQL supports `MERGE` for conditional insert, update, or delete
operations.

``` sql
MERGE INTO products AS target
USING new_products AS source
ON target.id = source.id

WHEN MATCHED THEN
    UPDATE SET
        name = source.name,
        price = source.price

WHEN NOT MATCHED THEN
    INSERT (id, name, price)
    VALUES (source.id, source.name, source.price);
```

`MERGE` is useful when synchronizing data from one source with another
table.

## `FILTER`

PostgreSQL allows an aggregate function to operate only on rows
satisfying a condition.

``` sql
SELECT
    COUNT(*) AS total,
    COUNT(*) FILTER (WHERE status = 'active') AS active_users,
    COUNT(*) FILTER (WHERE status = 'inactive') AS inactive_users
FROM users;
```

This can be cleaner than repeating conditional expressions.

## PostgreSQL Set Operations

### `EXCEPT`

`EXCEPT` returns rows from the first query that are not present in the
second query.

``` sql
SELECT email
FROM customers

EXCEPT

SELECT email
FROM subscribers;
```

### `INTERSECT`

Returns rows common to both queries.

``` sql
SELECT email
FROM customers

INTERSECT

SELECT email
FROM subscribers;
```

## PostgreSQL Full Outer Join

PostgreSQL supports `FULL OUTER JOIN` directly.

``` sql
SELECT
    customers.id,
    customers.name,
    orders.order_id
FROM customers
FULL OUTER JOIN orders
    ON customers.id = orders.customer_id;
```

This returns matching rows plus unmatched rows from both sides.

## PostgreSQL `LATERAL`

`LATERAL` allows a subquery in the `FROM` clause to reference columns
from a preceding table expression.

``` sql
SELECT
    c.id,
    c.name,
    latest_order.order_id
FROM customers AS c
LEFT JOIN LATERAL (
    SELECT order_id
    FROM orders
    WHERE orders.customer_id = c.id
    ORDER BY order_date DESC
    LIMIT 1
) AS latest_order
ON TRUE;
```

This is useful for getting a related row calculated separately for each
row of the main query.

## Common Table Expressions

PostgreSQL supports Common Table Expressions using `WITH`.

``` sql
WITH active_users AS (
    SELECT *
    FROM users
    WHERE active = TRUE
)
SELECT *
FROM active_users;
```

### Recursive CTE

PostgreSQL supports recursive queries.

``` sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 5
)
SELECT *
FROM numbers;
```

Result:

``` text
1
2
3
4
5
```

Recursive CTEs are useful for hierarchical data such as employee-manager
relationships, categories, and tree structures.

## PostgreSQL Window Functions

Window functions calculate values across related rows without collapsing
the rows into one row per group.

### `ROW_NUMBER()`

``` sql
SELECT
    name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;
```

### `RANK()`

``` sql
SELECT
    name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;
```

### `PARTITION BY`

``` sql
SELECT
    department,
    name,
    salary,
    RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS department_rank
FROM employees;
```

`PARTITION BY` divides rows into groups for the window calculation
without grouping the final result.

## PostgreSQL Table Creation Features

### `CREATE TABLE AS`

Create a new table from a query result.

``` sql
CREATE TABLE active_users AS
SELECT *
FROM users
WHERE active = TRUE;
```

### `SELECT INTO`

PostgreSQL can also create a table from a query using:

``` sql
SELECT *
INTO active_users
FROM users
WHERE active = TRUE;
```

`CREATE TABLE AS` is generally clearer for explicitly creating a table
from a query.

## Temporary Tables

Temporary tables exist only for the current session.

``` sql
CREATE TEMP TABLE temp_users (
    id INTEGER,
    name TEXT
);
```

Insert data:

``` sql
INSERT INTO temp_users
VALUES (1, 'Het');
```

Temporary tables are automatically removed when their session ends.

## `ALTER COLUMN`

### Change Data Type

``` sql
ALTER TABLE users
ALTER COLUMN age TYPE BIGINT;
```

### Set a Default

``` sql
ALTER TABLE users
ALTER COLUMN active SET DEFAULT TRUE;
```

### Remove a Default

``` sql
ALTER TABLE users
ALTER COLUMN active DROP DEFAULT;
```

### Set `NOT NULL`

``` sql
ALTER TABLE users
ALTER COLUMN name SET NOT NULL;
```

### Remove `NOT NULL`

``` sql
ALTER TABLE users
ALTER COLUMN name DROP NOT NULL;
```

## PostgreSQL-Specific Indexes

PostgreSQL supports multiple index methods for different workloads.

### B-tree

The default index type.

``` sql
CREATE INDEX idx_users_name
ON users(name);
```

Useful for equality and range queries.

### GIN

Generalized Inverted Indexes are useful for data such as arrays and
`JSONB`.

``` sql
CREATE INDEX idx_products_details
ON products
USING GIN (details);
```

### GiST

Generalized Search Tree indexes support several advanced search types
and extension-based data types.

``` sql
CREATE INDEX idx_location
ON places
USING GIST (location);
```

### BRIN

Block Range Indexes are useful for very large tables where values have a
natural physical correlation.

``` sql
CREATE INDEX idx_events_time
ON events
USING BRIN (event_time);
```

### Partial Index

A partial index contains only rows matching a condition.

``` sql
CREATE INDEX idx_active_users
ON users(email)
WHERE active = TRUE;
```

This can reduce index size and improve queries that repeatedly target a
subset of rows.

### Expression Index

An index can be created on an expression.

``` sql
CREATE INDEX idx_lower_email
ON users(LOWER(email));
```

This makes queries such as:

``` sql
SELECT *
FROM users
WHERE LOWER(email) = 'het@example.com';
```

more index-friendly.

## PostgreSQL Extensions

Extensions add functionality to PostgreSQL without modifying the core
database.

List installed extensions:

``` sql
SELECT *
FROM pg_extension;
```

Install an extension:

``` sql
CREATE EXTENSION IF NOT EXISTS extension_name;
```

Example:

``` sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

Extensions are a major part of the PostgreSQL ecosystem.

## User-Defined Types

### Enum

Create an enum:

``` sql
CREATE TYPE order_status AS ENUM (
    'pending',
    'shipped',
    'delivered',
    'cancelled'
);
```

Use it in a table:

``` sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    status order_status
);
```

### Domain

A domain creates a reusable type based on another type with constraints.

``` sql
CREATE DOMAIN positive_integer AS INTEGER
CHECK (VALUE > 0);
```

Use it:

``` sql
CREATE TABLE products (
    quantity positive_integer
);
```

### Composite Type

A composite type contains multiple fields.

``` sql
CREATE TYPE address AS (
    street TEXT,
    city TEXT,
    pincode TEXT
);
```

Use it:

``` sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    address address
);
```

## Table Inheritance

PostgreSQL supports table inheritance.

``` sql
CREATE TABLE cities (
    name TEXT,
    population INTEGER
);

CREATE TABLE capitals (
    country TEXT
) INHERITS (cities);
```

The child table inherits columns from the parent table.

## Row-Level Security

PostgreSQL provides native Row-Level Security for restricting which rows
users can access.

Enable RLS:

``` sql
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
```

Create a policy:

``` sql
CREATE POLICY user_policy
ON users
FOR SELECT
USING (id = current_user_id);
```

RLS is useful when different users should access different rows from the
same table.

## PostgreSQL Roles

PostgreSQL uses roles for authentication and authorization.

Create a role:

``` sql
CREATE ROLE app_user LOGIN PASSWORD 'password';
```

Create a role with database creation privileges:

``` sql
CREATE ROLE developer
LOGIN
CREATEDB
PASSWORD 'password';
```

Grant privileges:

``` sql
GRANT SELECT, INSERT, UPDATE
ON users
TO app_user;
```

Remove privileges:

``` sql
REVOKE UPDATE
ON users
FROM app_user;
```

## Schemas

PostgreSQL supports schemas for organizing database objects.

Create a schema:

``` sql
CREATE SCHEMA sales;
```

Create a table inside the schema:

``` sql
CREATE TABLE sales.orders (
    id SERIAL PRIMARY KEY,
    total NUMERIC(10,2)
);
```

Access the table:

``` sql
SELECT *
FROM sales.orders;
```

The `public` schema is commonly available by default.

## Search Path

PostgreSQL uses `search_path` to determine where unqualified object
names are searched.

View it:

``` sql
SHOW search_path;
```

Set it:

``` sql
SET search_path TO sales, public;
```

After setting it, you can write:

``` sql
SELECT *
FROM orders;
```

instead of:

``` sql
SELECT *
FROM sales.orders;
```

## PostgreSQL System Catalogs

PostgreSQL stores metadata about databases, tables, columns, indexes,
and other objects in system catalogs.

Examples:

``` sql
SELECT *
FROM pg_tables;
```

``` sql
SELECT *
FROM pg_indexes;
```

``` sql
SELECT *
FROM pg_database;
```

Information about columns can be queried through `information_schema`:

``` sql
SELECT
    table_name,
    column_name,
    data_type
FROM information_schema.columns
WHERE table_name = 'users';
```

## `psql` Commands

`psql` is PostgreSQL's command-line client.

Connect to PostgreSQL:

``` bash
psql -U postgres
```

Connect to a specific database:

``` bash
psql -U postgres -d mydb
```

List databases:

``` text
\l
```

Connect to a database:

``` text
\c mydb
```

List tables:

``` text
\dt
```

Describe a table:

``` text
\d users
```

Describe a table in more detail:

``` text
\d+ users
```

List schemas:

``` text
\dn
```

List roles:

``` text
\du
```

Show query history:

``` text
\s
```

Quit `psql`:

``` text
\q
```

Run a SQL file:

``` text
\i filename.sql
```

## PostgreSQL `COPY`

`COPY` is PostgreSQL's high-performance mechanism for moving table data
to and from files.

### Import CSV

``` sql
COPY users
FROM '/path/users.csv'
WITH (
    FORMAT csv,
    HEADER true
);
```

### Export CSV

``` sql
COPY users
TO '/path/users.csv'
WITH (
    FORMAT csv,
    HEADER true
);
```

For client-side file transfer through `psql`, use `\copy`:

``` text
\copy users TO 'users.csv' CSV HEADER
```

## PostgreSQL Transactions

PostgreSQL supports explicit transactions.

``` sql
BEGIN;

UPDATE accounts
SET balance = balance - 100
WHERE id = 1;

UPDATE accounts
SET balance = balance + 100
WHERE id = 2;

COMMIT;
```

Rollback:

``` sql
BEGIN;

UPDATE accounts
SET balance = balance - 100
WHERE id = 1;

ROLLBACK;
```

## Savepoints

A savepoint allows part of a transaction to be rolled back without
cancelling the entire transaction.

``` sql
BEGIN;

UPDATE accounts
SET balance = balance - 100
WHERE id = 1;

SAVEPOINT payment_step;

UPDATE accounts
SET balance = balance + 100
WHERE id = 2;

ROLLBACK TO payment_step;

COMMIT;
```

## PostgreSQL Isolation and MVCC

PostgreSQL uses Multi-Version Concurrency Control (MVCC).

MVCC allows transactions to work with row versions rather than simply
blocking every read while another transaction changes data.

PostgreSQL provides transaction isolation levels including:

``` text
READ COMMITTED
REPEATABLE READ
SERIALIZABLE
```

Check the current level:

``` sql
SHOW transaction_isolation;
```

Set it for a transaction:

``` sql
BEGIN;

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

SELECT *
FROM accounts;

COMMIT;
```

## `EXPLAIN`

`EXPLAIN` shows the query execution plan chosen by PostgreSQL.

``` sql
EXPLAIN
SELECT *
FROM users
WHERE email = 'het@example.com';
```

`EXPLAIN ANALYZE` actually executes the query and reports runtime
information.

``` sql
EXPLAIN ANALYZE
SELECT *
FROM users
WHERE email = 'het@example.com';
```

Important plan concepts include:

``` text
Seq Scan
Index Scan
Index Only Scan
Bitmap Index Scan
Nested Loop
Hash Join
Merge Join
Sort
Aggregate
```

## `ANALYZE`

`ANALYZE` collects statistics used by the PostgreSQL query planner.

Analyze one table:

``` sql
ANALYZE users;
```

Analyze the whole database:

``` sql
ANALYZE;
```

## PostgreSQL Views

Create a view:

``` sql
CREATE VIEW active_users AS
SELECT id, name, email
FROM users
WHERE active = TRUE;
```

Use it:

``` sql
SELECT *
FROM active_users;
```

Drop it:

``` sql
DROP VIEW active_users;
```

## Materialized Views

A materialized view stores the result of a query physically.

``` sql
CREATE MATERIALIZED VIEW sales_summary AS
SELECT
    product_id,
    SUM(amount) AS total_sales
FROM sales
GROUP BY product_id;
```

Refresh it:

``` sql
REFRESH MATERIALIZED VIEW sales_summary;
```

Unlike an ordinary view, a materialized view does not automatically
reflect every underlying table change.

## PostgreSQL Functions

PostgreSQL supports user-defined functions.

``` sql
CREATE FUNCTION add_numbers(a INTEGER, b INTEGER)
RETURNS INTEGER
LANGUAGE SQL
AS $$
    SELECT a + b;
$$;
```

Call it:

``` sql
SELECT add_numbers(10, 20);
```

## PL/pgSQL

PL/pgSQL is PostgreSQL's procedural language.

``` sql
CREATE OR REPLACE FUNCTION get_user_count()
RETURNS INTEGER
LANGUAGE plpgsql
AS $$
DECLARE
    total_users INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO total_users
    FROM users;

    RETURN total_users;
END;
$$;
```

Call:

``` sql
SELECT get_user_count();
```

## Stored Procedures

PostgreSQL also supports procedures.

``` sql
CREATE PROCEDURE increase_salary(
    employee_id INTEGER,
    amount NUMERIC
)
LANGUAGE SQL
AS $$
    UPDATE employees
    SET salary = salary + amount
    WHERE id = employee_id;
$$;
```

Call:

``` sql
CALL increase_salary(1, 5000);
```

## Triggers

Triggers automatically execute a function when a database event occurs.

Create a trigger function:

``` sql
CREATE OR REPLACE FUNCTION log_user_insert()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE 'New user inserted: %', NEW.name;
    RETURN NEW;
END;
$$;
```

Create the trigger:

``` sql
CREATE TRIGGER user_insert_trigger
AFTER INSERT ON users
FOR EACH ROW
EXECUTE FUNCTION log_user_insert();
```

Important trigger timing options:

``` text
BEFORE
AFTER
INSTEAD OF
```

Common events:

``` text
INSERT
UPDATE
DELETE
TRUNCATE
```

## PostgreSQL String-Specific Features

### String Concatenation with `||`

``` sql
SELECT first_name || ' ' || last_name AS full_name
FROM users;
```

### Regular Expressions

Match using a regular expression:

``` sql
SELECT *
FROM users
WHERE email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$';
```

Case-insensitive matching:

``` sql
SELECT *
FROM users
WHERE name ~* '^het';
```

PostgreSQL regex operators include:

``` text
~     case-sensitive match
~*    case-insensitive match
!~    does not match
!~*   case-insensitive does not match
```

## PostgreSQL JSON Operators

Common operators:

``` text
->      get JSON object field as JSON
->>     get JSON object field as text
#>      get nested JSON value as JSON
#>>     get nested JSON value as text
@>      contains
<@      contained by
?       key exists
?|      any key exists
?&      all keys exist
```

Example:

``` sql
SELECT details ->> 'brand'
FROM products;
```

Nested path:

``` sql
SELECT details #>> '{manufacturer,name}'
FROM products;
```

## PostgreSQL Array Operators

Check whether an array contains another array:

``` sql
SELECT ARRAY[1, 2, 3] @> ARRAY[2, 3];
```

Check overlap:

``` sql
SELECT ARRAY[1, 2, 3] && ARRAY[3, 4, 5];
```

Get array length:

``` sql
SELECT array_length(ARRAY[10, 20, 30], 1);
```

Expand an array into rows:

``` sql
SELECT unnest(ARRAY['JavaScript', 'React', 'PostgreSQL']);
```

## PostgreSQL-Specific Conditional Expressions

### `COALESCE`

Return the first non-null value:

``` sql
SELECT COALESCE(phone, 'No phone')
FROM users;
```

### `NULLIF`

Return `NULL` when two expressions are equal:

``` sql
SELECT NULLIF(10, 10);
```

### `CASE`

PostgreSQL supports standard `CASE` expressions:

``` sql
SELECT
    name,
    CASE
        WHEN salary >= 100000 THEN 'High'
        WHEN salary >= 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_level
FROM employees;
```

## PostgreSQL Random Values

Generate a random number between `0` and `1`:

``` sql
SELECT random();
```

Generate an integer in a range:

``` sql
SELECT floor(random() * 100 + 1)::INTEGER;
```

## Generate UUIDs

If the required extension is available:

``` sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

Generate a UUID:

``` sql
SELECT gen_random_uuid();
```

Example:

``` sql
CREATE TABLE users (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name TEXT NOT NULL
);
```

## PostgreSQL Practical Example

``` sql
CREATE TABLE users (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    skills TEXT[],
    metadata JSONB,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

Insert:

``` sql
INSERT INTO users (
    name,
    email,
    skills,
    metadata
)
VALUES (
    'Het Shah',
    'het@example.com',
    ARRAY['JavaScript', 'React', 'PostgreSQL'],
    '{"role": "developer", "experience": 1}'
)
RETURNING *;
```

Query JSON:

``` sql
SELECT
    name,
    metadata ->> 'role' AS role
FROM users;
```

Query arrays:

``` sql
SELECT *
FROM users
WHERE 'React' = ANY(skills);
```

Upsert:

``` sql
INSERT INTO users (
    email,
    name
)
VALUES (
    'het@example.com',
    'Het Shah'
)
ON CONFLICT (email)
DO UPDATE
SET name = EXCLUDED.name
RETURNING *;
```

## PostgreSQL Concepts to Practice

Focus on these PostgreSQL-specific areas after learning MySQL:

-   `SERIAL` and identity columns
-   Sequences
-   `RETURNING`
-   `ON CONFLICT`
-   `MERGE`
-   `JSONB`
-   JSON operators
-   Arrays
-   Array operators and `unnest()`
-   UUID
-   `hstore`
-   `INTERVAL`
-   `TIMESTAMPTZ`
-   Type casting with `::`
-   `FILTER`
-   `EXCEPT`
-   `INTERSECT`
-   `LATERAL`
-   Recursive CTEs
-   Window functions
-   Partial indexes
-   Expression indexes
-   GIN, GiST and BRIN indexes
-   Extensions
-   Enums, domains and composite types
-   Schemas and `search_path`
-   Roles
-   Row-Level Security
-   `psql` commands
-   `COPY` and `\copy`
-   `EXPLAIN ANALYZE`
-   Materialized views
-   PL/pgSQL
-   Functions and procedures
-   Triggers
-   MVCC and transaction isolation
-   PostgreSQL system catalogs

## PostgreSQL Learning Order

``` text
MySQL basics already learned
        ↓
PostgreSQL syntax differences
        ↓
PostgreSQL data types
        ↓
SERIAL / IDENTITY / SEQUENCES
        ↓
Type casting
        ↓
RETURNING
        ↓
ON CONFLICT / UPSERT
        ↓
JSON / JSONB
        ↓
Arrays
        ↓
UUID / Extensions
        ↓
CTE / Recursive CTE
        ↓
Window Functions
        ↓
FILTER / EXCEPT / INTERSECT / LATERAL
        ↓
PostgreSQL Indexes
        ↓
Schemas / Roles / RLS
        ↓
COPY / psql
        ↓
EXPLAIN ANALYZE
        ↓
Functions / PLpgSQL / Procedures
        ↓
Triggers
        ↓
Materialized Views
        ↓
MVCC / Isolation
```

## Quick PostgreSQL Cheat Sheet

``` sql
-- Identity
id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY

-- Serial
id SERIAL PRIMARY KEY

-- UUID
id UUID DEFAULT gen_random_uuid() PRIMARY KEY

-- Type casting
value::INTEGER

-- Return inserted row
INSERT ... RETURNING *

-- Upsert
INSERT ...
ON CONFLICT (...) DO UPDATE ...

-- Ignore conflict
ON CONFLICT (...) DO NOTHING

-- JSON field
data -> 'key'

-- JSON text
data ->> 'key'

-- JSON containment
data @> '{"key": "value"}'

-- Array membership
'value' = ANY(array_column)

-- Array expansion
SELECT unnest(array_column)

-- Aggregate filter
COUNT(*) FILTER (WHERE condition)

-- Full outer join
FULL OUTER JOIN

-- Set difference
EXCEPT

-- Common table expression
WITH name AS (...)

-- Recursive CTE
WITH RECURSIVE name AS (...)

-- Query plan
EXPLAIN ANALYZE ...

-- PostgreSQL command-line client
psql

-- List databases
\l

-- List tables
\dt

-- Describe table
\d table_name

-- Connect database
\c database_name

-- Quit
\q
```

## Important PostgreSQL vs MySQL Syntax to Remember

``` text
PostgreSQL                         MySQL

SERIAL                             AUTO_INCREMENT
IDENTITY                           AUTO_INCREMENT
RETURNING                          Usually separate SELECT
ON CONFLICT                        ON DUPLICATE KEY UPDATE
ILIKE                              Case-insensitive comparison patterns differ
||                                 CONCAT()
::type                             CAST(... AS type)
TEXT[]                             No equivalent native array type
JSONB                              JSON
UUID                               Usually CHAR/BINARY based
FULL OUTER JOIN                    No direct equivalent
EXCEPT                             No direct equivalent
FILTER (WHERE ...)                 Conditional aggregate patterns
TIMESTAMPTZ                        DATETIME/TIMESTAMP behavior differs
CREATE EXTENSION                   Different extension/plugin model
CREATE SCHEMA                      Schema/database terminology differs
```

## Reference

-   Neon PostgreSQL Tutorial: https://neon.com/postgresql/tutorial/
-   PostgreSQL documentation: https://www.postgresql.org/docs/
