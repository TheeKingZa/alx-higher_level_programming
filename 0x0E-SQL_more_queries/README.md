# Object Relational Mapping
[<](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x0D-SQL_introduction/README.md) 0x0E [>](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x0F-python-object_relational_mapping/README.md)

NEED TO KNOW?
-------------
How to create a new MySQL user
How to manage privileges for a user to a database or table
What’s a PRIMARY KEY
What’s a FOREIGN KEY
How to use NOT NULL and UNIQUE constraints
How to retrieve datas from multiple tables in one request
What are subqueries
What are JOIN and UNION?
----------------------------------------------

1.
Create a New MySQL User:
To create a new MySQL user, you can use the CREATE USER statement. Here's an example:

==CODE==

CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';

-----------------------------------

2.
Manage Privileges for a User:
You can manage privileges using the GRANT statement. For example, to grant all privileges on a specific database to a user:

==CODE==
GRANT ALL PRIVILEGES ON database_name.* TO 'user'@'localhost';

------------------------------------

3.
PRIMARY KEY:
A PRIMARY KEY is a column or a set of columns in a database table that uniquely identifies each row. It enforces the uniqueness constraint and ensures data integrity.

------------------------------------

4.
FOREIGN KEY:
A FOREIGN KEY is a column or a set of columns in a table that is used to establish a link between data in two tables. It creates a relationship between tables, typically referring to the primary key of another table.
-------------------------------------

5.
NOT NULL and UNIQUE Constraints:
* 'NOT NULL' ensures that a column cannot have a NULL (empty) value.
* 'UNIQUE' ensures that all values in a column are unique.

--------------------------------------

6.
Retrieve Data from Multiple Tables:
You can use SQL JOINs to retrieve data from multiple tables in a single query. Common types include INNER JOIN, LEFT JOIN, and RIGHT JOIN.

--------------------------------------

7.
Subqueries:
Subqueries are queries embedded within another query. They are used to retrieve data that will be used in the main query. For example, to find all customers who made a purchase:

==CODE==
SELECT * FROM customers WHERE customer_id IN (SELECT customer_id FROM orders);

------------------------------------------

8.
JOIN and UNION:
* 'JOIN' combines rows from two or more tables based on a related column.
* 'UNION' combines the result sets of two or more SELECT statements into a single result set.

======================================================================================
