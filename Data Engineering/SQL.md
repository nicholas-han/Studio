# SQL
SQL, or Structured Query Language, is a major programming language in the database development field.

The biggest difference between SQL and other common programming languages, such as Java and Python is in the language design logic. The syntax of SQL focuses on the logic of grouping, while most other programming languages focus more on procedure, which uses linear thinking.

There are five Categories of SQL Commands

1. Data Definition Language (DDL): CREAT/DROP/ALTER/TRUNCATE
2. Data Query Language (DQL): SELECT
3. Data Manipulation Language (DML): INSERT/(SELECT)/UPDATE/DELETE/CALL LOCK
	- CRUD operations: create, read, update and delete
4. Data Control Language (DCL): GRANT/REVOKE 
5. Transaction Control Language (TCL): COMMIT/SAVEPOINT/ROLLBACK/SET TRANSACTION/SET CONSTRAINT

## Normalization

### Normalization Rules
1. First Normal Form:
	- The table has unique rows
	- The table has atomic values (each cell contain only a single value, not a list
2. Second Normal Form:
	- The table does not contain partial dependencies (one should create separate tables for different sets of values)
3. Third Normal Form: eliminate columns that don't depend on the key

Other normalization rules include Boyce-Codd Normal Form (BCNF), Fourth Normal Form and Fifth Normal Form.

In transactional systems (OLTP), where data is both read and written frequently, you typically normalize the data to 3NF. OLTP systems need to process and store transactions as well as query transactional data, and normalizing the data to 3NF helps the database to process and store individual transactions efficiently.

In analytical OLAP systems, where users primarily read data, databases prioritize read performance over write integrity. Hence, the data may have undergone some denormalization to a lower normal form before being loaded into the analytical system, such as a data warehouse. In data warehousing, data engineers focus on performance, which can benefit from having fewer tables to process.

## SQL Tips
- When practicing and using SQL, you can divide your thinking into two parts.
	1. The first part is how to write a query that meets the given conditions.
	2. The second part is how to display the generated result.
- When using conditions of Equal To, Greater Than, and Less Than, `NULL` will not be treated as an empty value or 0; instead, it will be excluded from the comparison.
- Subquery is a technique used to simplify SQL statements, and it is the first threshold for advanced SQL syntax. In the actual database system, a table often has dozens of columns. If `JOIN` is used to combine tables according to certain conditions, it may cause many redundant columns to be fetched.
	- The `WHERE` clause in SQL operates on existing columns in a table. Since the identification column is a result of concatenation performed within the SELECT statement, it doesn't exist as a standalone column in the table. Therefore, you cannot directly use WHERE to filter on dynamically created columns. This limitation is common in SQL, especially when dealing with complex queries in legacy systems. SQL provides the HAVING clause, which allows filtering on calculated or aggregated columns. 
	- However, it’s important to note that the direct use of HAVING without GROUP BY is a misuse of SQL syntax. Over-relying on HAVING can lead to performance issues as data volume grows. This is because HAVING is designed for filtering aggregate functions or the results of calculations done within the query, and its misuse can impact database efficiency.
	- The correct approach involves using a subquery or a Common Table Expression (CTE) to first define the calculated column, then applying the `WHERE` clause on that result.

```MySQL
--Using a subquery
SELECT * FROM (SELECT CONCAT(`id`, '-', `name`) AS `identification`, `age` 
  FROM `new_schema`.`users`) AS subquery WHERE `identification` LIKE '%J%';
-- Using a CTE:
WITH CTE_Users AS (SELECT CONCAT(`id`, '-', `name`) AS `identification`, `age`FROM `new_schema`.`users`)SELECT * FROM CTE_UsersWHERE `identification` LIKE '%J%';
```

## JSON
The full name of JSON is JavaScript Object Notation, which is known for its simplicity, high flexibility, and high compatibility. To learn more about JSON, please refer to MDN documentation.

The JSON has three prominent characteristics:

1. Wrap the data in curly brackets {}.
2. The text in double quotation marks can be used as the column name like "{"place": "U.S"}", followed by the value of the column.
3. The square brackets [] can wrap multiple, similar data.

In the modern age, where JSON is becoming more and more common, databases provide SQL functionalities that specifically handle the JSON format. There are even databases specially designed to handle data structures like JSON.

```JSON
{
  "orderId": 54321,
  "info": [
    {
      "productID": 34,
      "productName": "productOne",
      "quantity": 1
    },
    {
      "productID": 56,
      "productName": "productTwo",
      "quantity": 3
    },
  ],
  "orderCompleted": true
}
```

```MySQL
CREATE SCHEMA `new_schema` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE `new_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT 'This is the primary index',
  `name` VARCHAR(45) NOT NULL DEFAULT 'N/A',
  PRIMARY KEY (`id`)
);

ALTER TABLE `new_schema`.`users` ADD COLUMN `contact` JSON NULL AFTER `id`;

INSERT INTO `new_schema`.`users` (`id`, `name`, `contact`) VALUES 
  (1, 'John', JSON_OBJECT('phone', '123-456', 'address', 'New York')),
  (2, 'May', JSON_OBJECT('phone', '888-99', 'address', 'LA')),
  (3, 'Tim', JSON_OBJECT('phone', '1236')),
  (4, 'Jay', JSON_OBJECT('phone', '321-6', 'address', 'Boston'));


SELECT `id`, JSON_EXTRACT(contact, '$.phone') AS phoneFROM `new_schema`.`users`;
SELECT `id`, JSON_UNQUOTE(JSON_EXTRACT(contact, '$.phone')) AS phoneFROM `new_schema`.`users`;
SELECT `id`, JSON_UNQUOTE(JSON_EXTRACT(contact, '$.phone')) AS phoneFROM `new_schema`.`users`WHERE JSON_EXTRACT(contact, '$.phone') like '%456%';
INSERT INTO `new_schema`.`users` (`id`, `name`, `contact`) VALUES (5, 'Harry', JSON_OBJECT('phone', '1231123', 'address', 'Miami'));
UPDATE `new_schema`.`users` SET `contact` = JSON_SET(contact, '$.phone', '6666', '$.phone_2', '888') WHERE `id` = 2;
```


## Useful Links
[SQL Tutorial for Beginners | Youtube](https://www.youtube.com/watch?v=7S_tz1z_5bA)

[SQL Language Tutorial | Leetcode](https://leetcode.com/explore/featured/card/sql-language/)

[MySQL数据备份教程](https://blog.csdn.net/Aprilqxs/article/details/130816944)

