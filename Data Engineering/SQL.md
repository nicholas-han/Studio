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