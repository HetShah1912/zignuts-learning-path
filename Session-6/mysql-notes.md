# MySQL / SQL Notes

> **Learning Path:** Zignuts
> **Topic:** MySQL / SQL
> **Reference:** [TpointTech SQL Tutorial](https://www.tpointtech.com/sql-tutorial)
> **Database:** MySQL

---

## What is SQL?

SQL stands for **Structured Query Language**.

SQL is a language used to communicate with relational databases. It allows us to create databases, store data, retrieve data, update data, delete data, and manage database structures.

### What is MySQL?

MySQL is a relational database management system (RDBMS) that uses SQL to manage data.

```text
SQL  →  Language

MySQL  →  Database Management System
```

### SQL vs MySQL

| SQL                       | MySQL                                 |
| ------------------------- | ------------------------------------- |
| Structured Query Language | Relational Database Management System |
| Used to write queries     | Executes SQL queries                  |
| A language                | Database software                     |
| Standardized              | One implementation of SQL             |

### Example

```sql
SELECT * FROM students;
```

This SQL query retrieves all records from the `students` table.

---

## Why Learn SQL?

SQL is widely used in:

* Web development
* Backend development
* Data analytics
* Data science
* Database administration
* Business intelligence
* Software development

### Advantages of SQL

* Easy to learn for beginners.
* Uses simple English-like commands.
* Can retrieve large amounts of data.
* Supports creating and modifying databases.
* Supports data filtering and sorting.
* Supports relationships between tables.
* Works with many database systems.
* Provides security and access-control features.

### Disadvantages of SQL

* SQL syntax can vary between database systems.
* Complex queries can be difficult to understand.
* Database administration can require additional tools and knowledge.
* Poorly optimized queries can be slow.
* Database systems may have licensing or infrastructure costs.

---

# SQL Basics

## SQL Syntax

SQL statements are instructions sent to a database.

```sql
SELECT column_name
FROM table_name;
```

### Example

```sql
SELECT name
FROM students;
```

### SQL Comments

Single-line comment:

```sql
-- This is a comment
SELECT * FROM students;
```

Multi-line comment:

```sql
/*
   This is a
   multi-line comment
*/
SELECT * FROM students;
```

### Semicolon

The semicolon `;` is used to terminate SQL statements.

```sql
SELECT * FROM students;
```

---

## SQL Keywords

Keywords are reserved words that have special meaning in SQL.

Examples:

```text
SELECT
FROM
WHERE
INSERT
UPDATE
DELETE
CREATE
ALTER
DROP
JOIN
GROUP BY
ORDER BY
HAVING
```

Example:

```sql
SELECT name
FROM students
WHERE age > 18;
```

---

## SQL Data Types

Data types define the kind of data a column can store.

### Numeric Data Types

| Data Type    | Description                         | Example    |
| ------------ | ----------------------------------- | ---------- |
| INT          | Integer values                      | 25         |
| BIGINT       | Large integer values                | 1000000000 |
| SMALLINT     | Small integer values                | 100        |
| DECIMAL(p,s) | Exact decimal values                | 99.99      |
| FLOAT        | Approximate decimal values          | 12.5       |
| DOUBLE       | Double-precision approximate values | 99.999     |

Example:

```sql
CREATE TABLE products (
    id INT,
    price DECIMAL(10, 2),
    quantity INT
);
```

### String Data Types

| Data Type  | Description            |
| ---------- | ---------------------- |
| CHAR(n)    | Fixed-length string    |
| VARCHAR(n) | Variable-length string |
| TEXT       | Long text              |
| TINYTEXT   | Small text             |
| MEDIUMTEXT | Medium-sized text      |
| LONGTEXT   | Very large text        |

Example:

```sql
CREATE TABLE users (
    username VARCHAR(50),
    bio TEXT
);
```

### Date and Time Data Types

| Data Type | Example               |
| --------- | --------------------- |
| DATE      | `2026-09-16`          |
| TIME      | `14:30:00`            |
| DATETIME  | `2026-09-16 14:30:00` |
| TIMESTAMP | Timestamp value       |
| YEAR      | `2026`                |

Example:

```sql
CREATE TABLE employees (
    joining_date DATE,
    created_at DATETIME
);
```

### Boolean Data Type

MySQL supports `BOOLEAN` as a synonym for `TINYINT(1)`.

```sql
CREATE TABLE users (
    is_active BOOLEAN
);
```

Example values:

```sql
INSERT INTO users (is_active)
VALUES (TRUE);
```

---

# SQL Database

## Create Database

```sql
CREATE DATABASE company;
```

This creates a database named `company`.

## Show Databases

```sql
SHOW DATABASES;
```

## Select Database

```sql
USE company;
```

This selects the database for subsequent commands.

## Current Database

```sql
SELECT DATABASE();
```

## Create Database If Not Exists

```sql
CREATE DATABASE IF NOT EXISTS company;
```

This avoids an error if the database already exists.

## Drop Database

```sql
DROP DATABASE company;
```

**Warning:** This deletes the database and its tables.

## Drop Database If Exists

```sql
DROP DATABASE IF EXISTS company;
```

---

# SQL Table

## What is a Table?

A table stores data in rows and columns.

Example:

| id | name  | age | city      |
| -- | ----- | --- | --------- |
| 1  | Het   | 21  | Ahmedabad |
| 2  | Rahul | 22  | Surat     |
| 3  | Priya | 20  | Vadodara  |

* **Column:** A field such as `name`.
* **Row:** One complete record.
* **Table:** Collection of related data.

---

## Create Table

```sql
CREATE TABLE students (
    id INT,
    name VARCHAR(100),
    age INT,
    city VARCHAR(100)
);
```

## Create Table with Primary Key

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    city VARCHAR(100)
);
```

## Show Tables

```sql
SHOW TABLES;
```

## Describe Table

```sql
DESCRIBE students;
```

Alternative:

```sql
DESC students;
```

## Show Table Structure

```sql
SHOW CREATE TABLE students;
```

## Rename Table

```sql
RENAME TABLE students TO learners;
```

## Drop Table

```sql
DROP TABLE students;
```

## Drop Table If Exists

```sql
DROP TABLE IF EXISTS students;
```

## Truncate Table

```sql
TRUNCATE TABLE students;
```

### DELETE vs TRUNCATE vs DROP

| Command  | Purpose                       |
| -------- | ----------------------------- |
| DELETE   | Removes rows                  |
| TRUNCATE | Removes all rows from a table |
| DROP     | Removes the table itself      |

---

## ALTER TABLE

ALTER is used to modify the structure of an existing table.

### Add Column

```sql
ALTER TABLE students
ADD email VARCHAR(100);
```

### Modify Column

```sql
ALTER TABLE students
MODIFY age SMALLINT;
```

### Rename Column

```sql
ALTER TABLE students
RENAME COLUMN name TO full_name;
```

### Drop Column

```sql
ALTER TABLE students
DROP COLUMN email;
```

### Rename Table

```sql
ALTER TABLE students
RENAME TO learners;
```

---

# SQL Constraints

Constraints are rules applied to table columns.

Common constraints:

```text
PRIMARY KEY
FOREIGN KEY
NOT NULL
UNIQUE
DEFAULT
CHECK
```

## NOT NULL

A column cannot contain NULL.

```sql
CREATE TABLE students (
    id INT,
    name VARCHAR(100) NOT NULL
);
```

## UNIQUE

Ensures values in a column are unique.

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```

## PRIMARY KEY

Uniquely identifies each row.

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

## FOREIGN KEY

Creates a relationship between tables.

```sql
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);
```

## DEFAULT

Assigns a default value when no value is supplied.

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    status VARCHAR(20) DEFAULT 'active'
);
```

## CHECK

Restricts values based on a condition.

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    age INT CHECK (age >= 18)
);
```

---

# SQL SELECT Statement

SELECT is used to retrieve data from a table.

## Select All Columns

```sql
SELECT *
FROM students;
```

## Select Specific Columns

```sql
SELECT name, age
FROM students;
```

## Select Distinct Values

```sql
SELECT DISTINCT city
FROM students;
```

## Column Alias

```sql
SELECT name AS student_name
FROM students;
```

## Table Alias

```sql
SELECT s.name
FROM students AS s;
```

## SELECT with Calculation

```sql
SELECT price, quantity, price * quantity AS total
FROM products;
```

## SELECT with Expression

```sql
SELECT 10 + 20 AS result;
```

Output:

| result |
| ------ |
| 30     |

---

# SQL WHERE Clause

WHERE filters rows based on a condition.

```sql
SELECT *
FROM students
WHERE age > 18;
```

## Comparison Operators

| Operator | Meaning               |
| -------- | --------------------- |
| `=`      | Equal                 |
| `<>`     | Not equal             |
| `!=`     | Not equal             |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

### Examples

```sql
SELECT *
FROM students
WHERE age = 20;
```

```sql
SELECT *
FROM students
WHERE age <> 20;
```

```sql
SELECT *
FROM students
WHERE age >= 18;
```

---

## AND Operator

Both conditions must be true.

```sql
SELECT *
FROM students
WHERE age > 18
AND city = 'Ahmedabad';
```

## OR Operator

At least one condition must be true.

```sql
SELECT *
FROM students
WHERE city = 'Ahmedabad'
OR city = 'Surat';
```

## NOT Operator

Negates a condition.

```sql
SELECT *
FROM students
WHERE NOT city = 'Ahmedabad';
```

## BETWEEN Operator

Checks whether a value is within a range.

```sql
SELECT *
FROM students
WHERE age BETWEEN 18 AND 25;
```

## IN Operator

Checks whether a value matches any value in a list.

```sql
SELECT *
FROM students
WHERE city IN ('Ahmedabad', 'Surat');
```

## NOT IN Operator

```sql
SELECT *
FROM students
WHERE city NOT IN ('Ahmedabad', 'Surat');
```

## LIKE Operator

Used for pattern matching.

### Starts With

```sql
SELECT *
FROM students
WHERE name LIKE 'H%';
```

Names starting with `H`.

### Ends With

```sql
SELECT *
FROM students
WHERE name LIKE '%h';
```

Names ending with `h`.

### Contains

```sql
SELECT *
FROM students
WHERE name LIKE '%et%';
```

Names containing `et`.

### Single Character Wildcard

```sql
SELECT *
FROM students
WHERE name LIKE '_e%';
```

`_` matches exactly one character.

### Wildcards

| Wildcard | Meaning                 |
| -------- | ----------------------- |
| `%`      | Zero or more characters |
| `_`      | Exactly one character   |

## IS NULL

```sql
SELECT *
FROM students
WHERE email IS NULL;
```

## IS NOT NULL

```sql
SELECT *
FROM students
WHERE email IS NOT NULL;
```

---

# SQL ORDER BY

ORDER BY sorts the result.

## Ascending Order

```sql
SELECT *
FROM students
ORDER BY age ASC;
```

## Descending Order

```sql
SELECT *
FROM students
ORDER BY age DESC;
```

## Sort by Multiple Columns

```sql
SELECT *
FROM students
ORDER BY city ASC, age DESC;
```

## ORDER BY with Alias

```sql
SELECT name, age + 1 AS next_age
FROM students
ORDER BY next_age;
```

---

# SQL LIMIT

LIMIT restricts the number of rows returned.

```sql
SELECT *
FROM students
LIMIT 5;
```

## LIMIT with OFFSET

```sql
SELECT *
FROM students
LIMIT 5 OFFSET 10;
```

This skips 10 rows and returns the next 5 rows.

Alternative MySQL syntax:

```sql
SELECT *
FROM students
LIMIT 10, 5;
```

---

# SQL INSERT Statement

INSERT adds new records to a table.

## Insert One Row

```sql
INSERT INTO students (id, name, age, city)
VALUES (1, 'Het', 21, 'Ahmedabad');
```

## Insert Multiple Rows

```sql
INSERT INTO students (id, name, age, city)
VALUES
    (2, 'Rahul', 22, 'Surat'),
    (3, 'Priya', 20, 'Vadodara'),
    (4, 'Amit', 23, 'Rajkot');
```

## Insert Without Specifying Columns

```sql
INSERT INTO students
VALUES (5, 'Neha', 21, 'Ahmedabad');
```

The values must match the table's column order.

## Insert from Another Table

```sql
INSERT INTO students_backup (id, name, age, city)
SELECT id, name, age, city
FROM students;
```

---

# SQL UPDATE Statement

UPDATE modifies existing records.

## Update One Column

```sql
UPDATE students
SET age = 22
WHERE id = 1;
```

## Update Multiple Columns

```sql
UPDATE students
SET age = 23,
    city = 'Surat'
WHERE id = 2;
```

## Update All Rows

```sql
UPDATE students
SET city = 'Ahmedabad';
```

**Warning:** Without a WHERE clause, every row is updated.

---

# SQL DELETE Statement

DELETE removes records from a table.

## Delete One Row

```sql
DELETE FROM students
WHERE id = 1;
```

## Delete Multiple Rows

```sql
DELETE FROM students
WHERE age < 18;
```

## Delete All Rows

```sql
DELETE FROM students;
```

**Warning:** Without a WHERE clause, all rows are deleted.

---

# SQL Clauses

Clauses are parts of SQL statements that control filtering, grouping, sorting, and limiting.

Common clauses:

```text
FROM
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT
```

## FROM

Specifies the table.

```sql
SELECT *
FROM students;
```

## WHERE

Filters rows before grouping.

```sql
SELECT *
FROM students
WHERE age > 18;
```

## GROUP BY

Groups rows with the same values.

```sql
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city;
```

## HAVING

Filters grouped results.

```sql
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city
HAVING COUNT(*) > 2;
```

## ORDER BY

Sorts the results.

```sql
SELECT *
FROM students
ORDER BY age DESC;
```

## LIMIT

Restricts the number of returned rows.

```sql
SELECT *
FROM students
LIMIT 10;
```

---

# SQL Aggregate Functions

Aggregate functions calculate a result from multiple rows.

## COUNT()

Counts rows.

```sql
SELECT COUNT(*) AS total_students
FROM students;
```

## SUM()

Adds numeric values.

```sql
SELECT SUM(salary) AS total_salary
FROM employees;
```

## AVG()

Returns the average.

```sql
SELECT AVG(salary) AS average_salary
FROM employees;
```

## MAX()

Returns the highest value.

```sql
SELECT MAX(salary) AS highest_salary
FROM employees;
```

## MIN()

Returns the lowest value.

```sql
SELECT MIN(salary) AS lowest_salary
FROM employees;
```

## Aggregate Functions with GROUP BY

```sql
SELECT department_id,
       COUNT(*) AS total_employees,
       AVG(salary) AS average_salary
FROM employees
GROUP BY department_id;
```

---

# SQL GROUP BY

GROUP BY combines rows with the same values.

### Example Data

| id | name  | city      |
| -- | ----- | --------- |
| 1  | Het   | Ahmedabad |
| 2  | Rahul | Surat     |
| 3  | Priya | Ahmedabad |
| 4  | Amit  | Surat     |

### Query

```sql
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city;
```

### Result

| city      | total_students |
| --------- | -------------- |
| Ahmedabad | 2              |
| Surat     | 2              |

---

# SQL HAVING

HAVING filters grouped results.

### WHERE vs HAVING

| WHERE                                    | HAVING                       |
| ---------------------------------------- | ---------------------------- |
| Filters individual rows                  | Filters groups               |
| Used before grouping                     | Used after grouping          |
| Cannot directly filter aggregate results | Can filter aggregate results |

### Example

```sql
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city
HAVING COUNT(*) > 1;
```

---

# SQL Joins

A JOIN combines data from multiple tables based on a related column.

## Example Tables

### Employees

| EmployeeID | Name  | DepartmentID |
| ---------- | ----- | ------------ |
| 1          | Het   | 10           |
| 2          | Rahul | 20           |
| 3          | Priya | 10           |
| 4          | Amit  | NULL         |

### Departments

| DepartmentID | DepartmentName |
| ------------ | -------------- |
| 10           | IT             |
| 20           | HR             |
| 30           | Finance        |

---

## INNER JOIN

Returns only matching rows from both tables.

```sql
SELECT e.Name, d.DepartmentName
FROM Employees e
INNER JOIN Departments d
    ON e.DepartmentID = d.DepartmentID;
```

### Result

| Name  | DepartmentName |
| ----- | -------------- |
| Het   | IT             |
| Rahul | HR             |
| Priya | IT             |

---

## LEFT JOIN

Returns all rows from the left table and matching rows from the right table.

```sql
SELECT e.Name, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d
    ON e.DepartmentID = d.DepartmentID;
```

### Result

| Name  | DepartmentName |
| ----- | -------------- |
| Het   | IT             |
| Rahul | HR             |
| Priya | IT             |
| Amit  | NULL           |

### Important

LEFT JOIN preserves every row from the left table.

---

## RIGHT JOIN

Returns all rows from the right table and matching rows from the left table.

```sql
SELECT e.Name, d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d
    ON e.DepartmentID = d.DepartmentID;
```

### Result

| Name  | DepartmentName |
| ----- | -------------- |
| Het   | IT             |
| Priya | IT             |
| Rahul | HR             |
| NULL  | Finance        |

### Important

RIGHT JOIN preserves every row from the right table.

---

## FULL OUTER JOIN

Returns matching and non-matching rows from both tables.

MySQL does not directly support FULL OUTER JOIN.

It can be simulated using UNION:

```sql
SELECT e.Name, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d
    ON e.DepartmentID = d.DepartmentID

UNION

SELECT e.Name, d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d
    ON e.DepartmentID = d.DepartmentID;
```

---

## CROSS JOIN

Returns every possible combination of rows from both tables.

```sql
SELECT e.Name, d.DepartmentName
FROM Employees e
CROSS JOIN Departments d;
```

If one table has 4 rows and the other has 3 rows:

```text
Total rows = 4 × 3 = 12
```

---

## SELF JOIN

A table joins with itself.

### Example Employees

| EmployeeID | Name  | ManagerID |
| ---------- | ----- | --------- |
| 1          | Het   | NULL      |
| 2          | Rahul | 1         |
| 3          | Priya | 1         |

### Query

```sql
SELECT
    e.Name AS Employee,
    m.Name AS Manager
FROM Employees e
LEFT JOIN Employees m
    ON e.ManagerID = m.EmployeeID;
```

### Result

| Employee | Manager |
| -------- | ------- |
| Het      | NULL    |
| Rahul    | Het     |
| Priya    | Het     |

---

## JOIN with WHERE

```sql
SELECT e.Name, d.DepartmentName
FROM Employees e
INNER JOIN Departments d
    ON e.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = 'IT';
```

---

## JOIN with GROUP BY

```sql
SELECT d.DepartmentName,
       COUNT(e.EmployeeID) AS total_employees
FROM Departments d
LEFT JOIN Employees e
    ON d.DepartmentID = e.DepartmentID
GROUP BY d.DepartmentName;
```

---

## JOIN Summary

| Join            | Returns                             |
| --------------- | ----------------------------------- |
| INNER JOIN      | Matching rows                       |
| LEFT JOIN       | All left rows + matching right rows |
| RIGHT JOIN      | All right rows + matching left rows |
| FULL OUTER JOIN | All rows from both sides            |
| CROSS JOIN      | Every combination                   |
| SELF JOIN       | Table joined with itself            |

---

# SQL Keys

Keys identify records and create relationships between tables.

## Primary Key

Uniquely identifies each row.

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

Properties:

* Unique
* Cannot be NULL
* One primary key constraint per table
* Can contain multiple columns as a composite key

## Foreign Key

References a key in another table.

```sql
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);
```

## UNIQUE Key

Ensures values are unique.

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```

## Composite Key

A key made from multiple columns.

```sql
CREATE TABLE student_courses (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id)
);
```

## Candidate Key

A column or set of columns that can uniquely identify a row and could be selected as a primary key.

## Super Key

Any set of columns that uniquely identifies a row.

## Alternate Key

A candidate key that was not selected as the primary key.

## Surrogate Key

An artificial identifier, such as an auto-increment integer.

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);
```

## Natural Key

A real-world value used as an identifier, such as an email address or government-issued identifier where appropriate.

---

# SQL String Functions

String functions manipulate text values.

## CONCAT()

Combines strings.

```sql
SELECT CONCAT('Hello', ' ', 'World') AS message;
```

Output:

```text
Hello World
```

## CONCAT_WS()

Combines strings using a separator.

```sql
SELECT CONCAT_WS('-', '2026', '09', '16') AS date_value;
```

## UPPER()

Converts text to uppercase.

```sql
SELECT UPPER('hello') AS result;
```

## LOWER()

Converts text to lowercase.

```sql
SELECT LOWER('HELLO') AS result;
```

## LENGTH()

Returns the length in bytes.

```sql
SELECT LENGTH('Hello') AS result;
```

## CHAR_LENGTH()

Returns the number of characters.

```sql
SELECT CHAR_LENGTH('Hello') AS result;
```

## TRIM()

Removes leading and trailing spaces.

```sql
SELECT TRIM('  Hello  ') AS result;
```

## LTRIM()

Removes leading spaces.

```sql
SELECT LTRIM('  Hello') AS result;
```

## RTRIM()

Removes trailing spaces.

```sql
SELECT RTRIM('Hello  ') AS result;
```

## SUBSTRING()

Extracts part of a string.

```sql
SELECT SUBSTRING('JavaScript', 1, 4) AS result;
```

Output:

```text
Java
```

## LEFT()

Returns characters from the left.

```sql
SELECT LEFT('JavaScript', 4) AS result;
```

## RIGHT()

Returns characters from the right.

```sql
SELECT RIGHT('JavaScript', 6) AS result;
```

## REPLACE()

Replaces text.

```sql
SELECT REPLACE('Hello World', 'World', 'SQL') AS result;
```

## REVERSE()

Reverses a string.

```sql
SELECT REVERSE('Hello') AS result;
```

## LOCATE()

Finds the position of a substring.

```sql
SELECT LOCATE('SQL', 'Learn SQL') AS result;
```

## LPAD()

Pads a string on the left.

```sql
SELECT LPAD('123', 5, '0') AS result;
```

Output:

```text
00123
```

## RPAD()

Pads a string on the right.

```sql
SELECT RPAD('123', 5, '0') AS result;
```

## FORMAT()

Formats a number with commas and decimal places.

```sql
SELECT FORMAT(1234567.89, 2) AS result;
```

---

# SQL Numeric Functions

## ABS()

Returns the absolute value.

```sql
SELECT ABS(-10) AS result;
```

## ROUND()

Rounds a number.

```sql
SELECT ROUND(12.567, 2) AS result;
```

## CEIL()

Rounds up to the nearest integer.

```sql
SELECT CEIL(12.3) AS result;
```

## FLOOR()

Rounds down to the nearest integer.

```sql
SELECT FLOOR(12.9) AS result;
```

## MOD()

Returns the remainder.

```sql
SELECT MOD(10, 3) AS result;
```

## POWER()

Returns a number raised to a power.

```sql
SELECT POWER(2, 3) AS result;
```

## SQRT()

Returns the square root.

```sql
SELECT SQRT(25) AS result;
```

---

# SQL Date and Time Functions

## CURDATE()

Returns the current date.

```sql
SELECT CURDATE();
```

## CURTIME()

Returns the current time.

```sql
SELECT CURTIME();
```

## NOW()

Returns the current date and time.

```sql
SELECT NOW();
```

## YEAR()

Extracts the year.

```sql
SELECT YEAR('2026-09-16') AS result;
```

## MONTH()

Extracts the month.

```sql
SELECT MONTH('2026-09-16') AS result;
```

## DAY()

Extracts the day.

```sql
SELECT DAY('2026-09-16') AS result;
```

## DATE_FORMAT()

Formats a date.

```sql
SELECT DATE_FORMAT('2026-09-16', '%d-%m-%Y') AS result;
```

Output:

```text
16-09-2026
```

## DATEDIFF()

Returns the difference between two dates in days.

```sql
SELECT DATEDIFF('2026-09-20', '2026-09-16') AS result;
```

## DATE_ADD()

Adds a time interval.

```sql
SELECT DATE_ADD('2026-09-16', INTERVAL 5 DAY);
```

## DATE_SUB()

Subtracts a time interval.

```sql
SELECT DATE_SUB('2026-09-16', INTERVAL 2 DAY);
```

---

# SQL NULL Functions

## What is NULL?

NULL means a missing or unknown value.

It is not the same as:

```text
0
''
'NULL'
FALSE
```

## IS NULL

```sql
SELECT *
FROM students
WHERE email IS NULL;
```

## IS NOT NULL

```sql
SELECT *
FROM students
WHERE email IS NOT NULL;
```

## IFNULL()

Returns an alternative value when the first value is NULL.

```sql
SELECT IFNULL(NULL, 'Not Available') AS result;
```

## COALESCE()

Returns the first non-NULL value.

```sql
SELECT COALESCE(NULL, NULL, 'Hello') AS result;
```

## NULLIF()

Returns NULL if two expressions are equal.

```sql
SELECT NULLIF(10, 10) AS result;
```

---

# SQL CASE Statement

CASE is used for conditional logic.

## Simple CASE

```sql
SELECT name,
       CASE city
           WHEN 'Ahmedabad' THEN 'Gujarat'
           WHEN 'Surat' THEN 'Gujarat'
           ELSE 'Other'
       END AS state
FROM students;
```

## Searched CASE

```sql
SELECT name,
       age,
       CASE
           WHEN age < 18 THEN 'Minor'
           WHEN age >= 18 THEN 'Adult'
           ELSE 'Unknown'
       END AS category
FROM students;
```

---

# SQL Subqueries

A subquery is a query inside another query.

## Subquery in WHERE

Find employees earning more than the average salary:

```sql
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

## Subquery in FROM

```sql
SELECT department_id, average_salary
FROM (
    SELECT department_id,
           AVG(salary) AS average_salary
    FROM employees
    GROUP BY department_id
) AS department_summary;
```

## Subquery in SELECT

```sql
SELECT
    name,
    (SELECT COUNT(*) FROM employees) AS total_employees
FROM employees;
```

---

# SQL Set Operations

Set operations combine the results of multiple SELECT statements.

## UNION

Combines results and removes duplicate rows.

```sql
SELECT city FROM students
UNION
SELECT city FROM employees;
```

## UNION ALL

Combines results and preserves duplicates.

```sql
SELECT city FROM students
UNION ALL
SELECT city FROM employees;
```

### Requirements

* Both queries must return the same number of columns.
* Corresponding columns must have compatible data types.

---

# SQL Views

A view is a virtual table based on a SQL query.

## Create View

```sql
CREATE VIEW adult_students AS
SELECT id, name, age
FROM students
WHERE age >= 18;
```

## Select from View

```sql
SELECT *
FROM adult_students;
```

## Replace View

```sql
CREATE OR REPLACE VIEW adult_students AS
SELECT id, name, age, city
FROM students
WHERE age >= 18;
```

## Drop View

```sql
DROP VIEW adult_students;
```

### Benefits

* Simplifies complex queries.
* Can restrict access to selected columns or rows.
* Provides a reusable query interface.

---

# SQL Indexes

An index helps the database find rows more efficiently.

## Create Index

```sql
CREATE INDEX idx_student_name
ON students(name);
```

## Create Unique Index

```sql
CREATE UNIQUE INDEX idx_student_email
ON students(email);
```

## Show Indexes

```sql
SHOW INDEX FROM students;
```

## Drop Index

```sql
DROP INDEX idx_student_name
ON students;
```

### Advantages

* Can improve search performance.
* Can speed up joins and sorting.
* Unique indexes enforce uniqueness.

### Disadvantages

* Require additional storage.
* Can slow down INSERT, UPDATE, and DELETE operations.

---

# SQL Stored Procedures

A stored procedure is a group of SQL statements stored in the database.

## Create Procedure

```sql
DELIMITER //

CREATE PROCEDURE GetStudents()
BEGIN
    SELECT *
    FROM students;
END //

DELIMITER ;
```

## Call Procedure

```sql
CALL GetStudents();
```

## Procedure with Parameter

```sql
DELIMITER //

CREATE PROCEDURE GetStudentById(IN student_id INT)
BEGIN
    SELECT *
    FROM students
    WHERE id = student_id;
END //

DELIMITER ;
```

Call:

```sql
CALL GetStudentById(1);
```

## Drop Procedure

```sql
DROP PROCEDURE GetStudents;
```

---

# SQL Functions

A stored function returns a value.

## Create Function

```sql
DELIMITER //

CREATE FUNCTION DoubleValue(num INT)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN num * 2;
END //

DELIMITER ;
```

## Use Function

```sql
SELECT DoubleValue(5) AS result;
```

Output:

```text
10
```

## Drop Function

```sql
DROP FUNCTION DoubleValue;
```

---

# SQL Triggers

A trigger automatically executes when a specified event occurs on a table.

Common events:

```text
INSERT
UPDATE
DELETE
```

## Example Trigger

```sql
CREATE TABLE student_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```sql
DELIMITER //

CREATE TRIGGER after_student_insert
AFTER INSERT ON students
FOR EACH ROW
BEGIN
    INSERT INTO student_logs (message)
    VALUES ('New student inserted');
END //

DELIMITER ;
```

When a student is inserted, a log entry is created.

---

# SQL Transactions

A transaction is a group of SQL operations treated as one unit.

## START TRANSACTION

```sql
START TRANSACTION;
```

## COMMIT

Permanently saves the transaction changes.

```sql
COMMIT;
```

## ROLLBACK

Undoes uncommitted changes.

```sql
ROLLBACK;
```

## Example

```sql
START TRANSACTION;

UPDATE accounts
SET balance = balance - 500
WHERE id = 1;

UPDATE accounts
SET balance = balance + 500
WHERE id = 2;

COMMIT;
```

If something goes wrong before commit:

```sql
ROLLBACK;
```

---

# SQL ACID Properties

Transactions are commonly described using ACID properties.

| Property    | Meaning                                                               |
| ----------- | --------------------------------------------------------------------- |
| Atomicity   | All operations succeed or none are applied                            |
| Consistency | Data remains valid according to rules                                 |
| Isolation   | Concurrent transactions are isolated according to the isolation level |
| Durability  | Committed changes survive normal failures                             |

---

# SQL Injection

SQL Injection is a security vulnerability where an attacker manipulates SQL queries through untrusted input.

## Unsafe Example

Suppose an application builds a query using string concatenation:

```javascript
const username = req.body.username;

const query =
    "SELECT * FROM users WHERE username = '" +
    username +
    "'";
```

If user input is inserted directly into the query, it may change the meaning of the SQL statement.

## Safe Approach: Prepared Statements

Use parameterized queries.

### MySQL Node.js Example

```javascript
const [rows] = await connection.execute(
    "SELECT * FROM users WHERE username = ?",
    [username]
);
```

The value is supplied separately from the SQL statement.

### SQL Injection Prevention

* Use prepared statements.
* Validate input.
* Avoid SQL string concatenation.
* Use least-privilege database accounts.
* Do not expose database errors to users.
* Keep database software updated.
* Use appropriate access controls.

---

# SQL Data Control Language

DCL manages permissions.

## GRANT

Gives privileges.

```sql
GRANT SELECT
ON company.students
TO 'app_user'@'localhost';
```

## REVOKE

Removes privileges.

```sql
REVOKE SELECT
ON company.students
FROM 'app_user'@'localhost';
```

---

# SQL Data Definition Language

DDL defines database structures.

Commands:

```text
CREATE
ALTER
DROP
TRUNCATE
```

Examples:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

```sql
ALTER TABLE students
ADD email VARCHAR(100);
```

---

# SQL Data Manipulation Language

DML changes data.

Commands:

```text
INSERT
UPDATE
DELETE
```

Examples:

```sql
INSERT INTO students (id, name)
VALUES (1, 'Het');
```

```sql
UPDATE students
SET name = 'Het Shah'
WHERE id = 1;
```

```sql
DELETE FROM students
WHERE id = 1;
```

---

# SQL Data Query Language

DQL retrieves data.

```sql
SELECT *
FROM students;
```

---

# SQL TCL

Transaction Control Language manages transactions.

Commands:

```text
COMMIT
ROLLBACK
SAVEPOINT
```

## SAVEPOINT

```sql
START TRANSACTION;

UPDATE students
SET city = 'Ahmedabad'
WHERE id = 1;

SAVEPOINT student_update;

UPDATE students
SET city = 'Surat'
WHERE id = 2;

ROLLBACK TO SAVEPOINT student_update;

COMMIT;
```

---

# SQL Interview Concepts

## DELETE vs TRUNCATE

| DELETE                                                         | TRUNCATE                                                              |
| -------------------------------------------------------------- | --------------------------------------------------------------------- |
| Removes rows                                                   | Removes all rows                                                      |
| Can use WHERE                                                  | Cannot use WHERE                                                      |
| DML command                                                    | DDL command in MySQL                                                  |
| Deletes selected rows or all rows                              | Removes all rows                                                      |
| Can be rolled back in a transaction under supported conditions | Has different transactional behavior depending on the database engine |

## WHERE vs HAVING

| WHERE                   | HAVING                        |
| ----------------------- | ----------------------------- |
| Filters rows            | Filters groups                |
| Used before GROUP BY    | Used after GROUP BY           |
| Used for row conditions | Used for aggregate conditions |

## PRIMARY KEY vs UNIQUE KEY

| PRIMARY KEY                          | UNIQUE KEY                                  |
| ------------------------------------ | ------------------------------------------- |
| Uniquely identifies a row            | Enforces uniqueness                         |
| Cannot contain NULL                  | Can permit NULL depending on database rules |
| One primary key constraint per table | Multiple unique constraints allowed         |
| Used for row identity                | Used to enforce uniqueness                  |

## INNER JOIN vs LEFT JOIN

| INNER JOIN                 | LEFT JOIN                          |
| -------------------------- | ---------------------------------- |
| Returns matching rows only | Returns all left rows              |
| Unmatched rows excluded    | Unmatched right values become NULL |

## CHAR vs VARCHAR

| CHAR                           | VARCHAR                           |
| ------------------------------ | --------------------------------- |
| Fixed-length string            | Variable-length string            |
| Suitable for fixed-size values | Suitable for varying text lengths |

## UNION vs UNION ALL

| UNION                                          | UNION ALL                                 |
| ---------------------------------------------- | ----------------------------------------- |
| Removes duplicate rows                         | Keeps duplicates                          |
| May require extra work to eliminate duplicates | Usually avoids duplicate-elimination work |

---

# Common MySQL Commands

```sql
SHOW DATABASES;
```

```sql
USE company;
```

```sql
SHOW TABLES;
```

```sql
DESCRIBE students;
```

```sql
SELECT DATABASE();
```

```sql
SHOW CREATE TABLE students;
```

```sql
SELECT VERSION();
```

```sql
SHOW WARNINGS;
```

---

# Practical SQL Example

## Create Database

```sql
CREATE DATABASE college;
USE college;
```

## Create Students Table

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    city VARCHAR(100),
    marks DECIMAL(5, 2)
);
```

## Insert Data

```sql
INSERT INTO students (name, age, city, marks)
VALUES
    ('Het', 21, 'Ahmedabad', 92.50),
    ('Rahul', 22, 'Surat', 85.00),
    ('Priya', 20, 'Ahmedabad', 88.50),
    ('Amit', 23, 'Rajkot', 75.00);
```

## Select All Students

```sql
SELECT *
FROM students;
```

## Students with Marks Greater Than 80

```sql
SELECT *
FROM students
WHERE marks > 80;
```

## Sort by Marks

```sql
SELECT *
FROM students
ORDER BY marks DESC;
```

## Count Students

```sql
SELECT COUNT(*) AS total_students
FROM students;
```

## Average Marks

```sql
SELECT AVG(marks) AS average_marks
FROM students;
```

## Group by City

```sql
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city;
```

## Update Student

```sql
UPDATE students
SET marks = 95
WHERE name = 'Het';
```

## Delete Student

```sql
DELETE FROM students
WHERE name = 'Amit';
```

---

# SQL Query Execution Order

A simplified logical processing order is:

```text
FROM
JOIN
WHERE
GROUP BY
HAVING
SELECT
DISTINCT
ORDER BY
LIMIT
```

Example:

```sql
SELECT city, COUNT(*) AS total
FROM students
WHERE marks > 80
GROUP BY city
HAVING COUNT(*) > 1
ORDER BY total DESC
LIMIT 5;
```

The database logically filters rows, groups them, filters groups, selects output, sorts, and limits results.

---

# Important SQL Concepts to Remember

```text
SQL
├── Basics
│   ├── Syntax
│   ├── Data Types
│   └── Operators
│
├── Database
│   ├── CREATE DATABASE
│   ├── USE
│   └── DROP DATABASE
│
├── Tables
│   ├── CREATE TABLE
│   ├── ALTER TABLE
│   ├── DROP TABLE
│   └── TRUNCATE
│
├── Data Operations
│   ├── SELECT
│   ├── INSERT
│   ├── UPDATE
│   └── DELETE
│
├── Clauses
│   ├── WHERE
│   ├── GROUP BY
│   ├── HAVING
│   ├── ORDER BY
│   └── LIMIT
│
├── Joins
│   ├── INNER
│   ├── LEFT
│   ├── RIGHT
│   ├── CROSS
│   └── SELF
│
├── Keys
│   ├── PRIMARY KEY
│   ├── FOREIGN KEY
│   ├── UNIQUE
│   └── COMPOSITE
│
├── Functions
│   ├── Aggregate
│   ├── String
│   ├── Numeric
│   └── Date
│
├── Advanced SQL
│   ├── Subqueries
│   ├── Views
│   ├── Indexes
│   ├── Procedures
│   ├── Functions
│   ├── Triggers
│   └── Transactions
│
└── Security
    └── SQL Injection
```

---

# Quick Revision Commands

```sql
CREATE DATABASE company;
USE company;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

INSERT INTO students
VALUES (1, 'Het', 21);

SELECT * FROM students;

UPDATE students
SET age = 22
WHERE id = 1;

DELETE FROM students
WHERE id = 1;
```

# Final Takeaway

SQL is used to manage and manipulate relational databases.

The most important commands to master are:

```sql
CREATE
SELECT
INSERT
UPDATE
DELETE
ALTER
DROP
```

For practical database work, focus on:

```text
Tables
Constraints
SELECT
WHERE
JOIN
GROUP BY
HAVING
ORDER BY
Aggregate Functions
Subqueries
Transactions
```

**SQL = Querying + Managing + Organizing Data**

---

## Reference

[TpointTech SQL Tutorial](https://www.tpointtech.com/sql-tutorial)

[MySQL Documentation](https://dev.mysql.com/doc/)
