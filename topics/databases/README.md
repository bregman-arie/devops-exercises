# Databases

- [Databases](#databases)
  - [Exercises](#exercises)
  - [Questions](#questions)
    - [SQL](#sql)
    - [Time Series](#time-series)

## Exercises

|Name|Topic|Objective & Instructions|Solution|Comments|
|--------|--------|------|----|----|
| Message Board Tables  | Relational DB Tables | [Exercise](topics/databases/table_for_message_board_system.md) | [Solution](topics/databases/solutions/table_for_message_board_system.md)

## Questions


<details>
<summary>What type of databases are you familiar with?</summary><br><b>

Relational (SQL)
NoSQL
Time serties
</b></details>

### SQL

<details>
<summary>What is a relational database?</summary><br><b>

  * Data Storage: system to store data in tables
  * SQL: programming language to manage relational databases
  * Data Definition Language: a standard syntax to create, alter and delete tables

</b></details>

<details>
<summary>What does it mean when a database is ACID compliant?</summary><br>

ACID stands for Atomicity, Consistency, Isolation, Durability. In order to be ACID compliant, the database must meet each of the four criteria

**Atomicity** - When a change occurs to the database, it should either succeed or fail as a whole.

For example, if you were to update a table, the update should completely execute. If it only partially executes, the
update is considered failed as a whole, and will not go through - the DB will revert back to it's original
state before the update occurred. It should also be mentioned that Atomicity ensures that each
transaction is completed as it's own stand alone "unit" - if any part fails, the whole statement fails.

**Consistency** - any change made to the database should bring it from one valid state into the next.

For example, if you make a change to the DB, it shouldn't corrupt it. Consistency is upheld by checks and constraints that
are pre-defined in the DB. For example, if you tried to change a value from a string to an int when the column
should be of datatype string, a consistent DB would not allow this transaction to go through, and the action would
not be executed

**Isolation** - this ensures that a database will never be seen "mid-update" - as multiple transactions are running at
the same time, it should still leave the DB in the same state as if the transactions were being run sequentially.

For example, let's say that 20 other people were making changes to the database at the same time. At the
time you executed your query, 15 of the 20 changes had gone through, but 5 were still in progress. You should
only see the 15 changes that had completed - you wouldn't see the database mid-update as the change goes through.

**Durability** - Once a change is committed, it will remain committed regardless of what happens
(power failure, system crash, etc.). This means that all completed transactions
must be recorded in non-volatile memory.

Note that SQL is by nature ACID compliant. Certain NoSQL DB's can be ACID compliant depending on
how they operate, but as a general rule of thumb, NoSQL DB's are not considered ACID compliant
</details>

<details>
<summary>What is sharding?</summary><br><b>

Sharding is a horizontal partitioning.

Are you able to explain what is it good for?
</b></details>

<details>
<summary>You find out your database became a bottleneck and users experience issues accessing data. How can you deal with such situation?</summary><br><b>

Not much information provided as to why it became a bottleneck and what is current architecture, so one general approach could be<br>
to reduce the load on your database by moving frequently-accessed data to in-memory structure.
</b></details>

<details>
<summary>What is a connection pool?</summary><br><b>

Connection Pool is a cache of database connections and the reason it's used is to avoid an overhead of establishing a connection for every query done to a database.
</b></details>

<details>
<summary>What is a connection leak?</summary><br><b>

A connection leak is a situation where database connection isn't closed after being created and is no longer needed.
</b></details>

<details>
<summary>What is Table Lock?</summary><br><b>
</b></details>

<details>
<summary>Your database performs slowly than usual. More specifically, your queries are taking a lot of time. What would you do?</summary><br><b>

* Query for running queries and cancel the irrelevant queries
* Check for connection leaks (query for running connections and include their IP)
* Check for table locks and kill irrelevant locking sessions
</b></details>

<details>
<summary>What is a Data Warehouse?</summary><br><b>

"A data warehouse is a subject-oriented, integrated, time-variant and non-volatile collection of data in support of organisation's decision-making process"
</b></details>

<details>
<summary>Explain what is a time-series database</summary><br><b>
</b></details>

<details>
<summary>What is OLTP (Online transaction processing)?</summary><br><b>
</b></details>

<details>
<summary>What is OLAP (Online Analytical Processing)?</summary><br><b>
</b></details>

<details>
<summary>What is an index in a database?</summary><br><b>

A database index is a data structure that improves the speed of operations in a table. Indexes can be created using one or more columns, providing the basis for both rapid random lookups and efficient ordering of access to records.
</b></details>

<details>
<summary>What data types are there in relational databases?</summary><br><b>
</b></details>

<details>
<summary>Explain Normalization</summary><br><b>

Data that is used multiple times in a database should be stored once and referenced with a foreign key.<br>
This has the clear benefit of ease of maintenance where you need to change a value only in a single place to change it everywhere.
</b></details>

<details>
<summary>Explain Primary Key and Foreign Key</summary><br><b>

Primary Key: each row in every table should a unique identifier that represents the row.<br>
Foreign Key: a reference to another table's primary key. This allows you to join table together to retrieve all the information you need without duplicating data.
</b></details>

<details>
<summary>What types of data tables have you used?</summary><br><b>

  * Primary data table: main data you care about
  * Details table: includes a foreign key and has one to many relationship
  * Lookup values table: can be one table per lookup or a table containing all the lookups and has one to many relationship
  * Multi reference table
</b></details>

<details>
<summary>What is ORM? What benefits it provides in regards to relational databases usage?</summary><br><b>

[Wikipedia](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping): "is a programming technique for converting data between incompatible type systems using object-oriented programming languages"

In regards to the relational databases:

  * Database as code
  * Database abstraction
  * Encapsulates SQL complexity
  * Enables code review process
  * Enables usage as a native OOP structure
</b></details>

<details>
<summary>What is DDL?</summary><br><b>

[Wikipedia](https://en.wikipedia.org/wiki/Data_definition_language): "In the context of SQL, data definition or data description language (DDL) is a syntax for creating and modifying database objects such as tables, indices, and users."
</b></details>

### Time Series

<details>
<summary>What is Time Series database?</summary><br><b>

A database designed specifically for time series based data.

It comes with multiple optimizations:

<TODO>: complete this :)
</b></details>