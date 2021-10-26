# Lab: 27 - Django Models
* Django has a powerful Object Relational Mapper that allows us to persist data using Python instead of SQL.

* Today you’ll build out a project with one model and wire up that model using Django Views.

* Django provides a powerful way to reason about an application's resources whether they are objects in our code or records persisted in a database.

## SQL queries:
1. create: `INSERT INTO table (col1, cool2) values ('value1', 'value2') returning id;`
2. read: `select name, email from table where condition`
3. update 
4. delete
>> [cheat sheet](https://www.sqltutorial.org/wp-content/uploads/2016/04/SQL-Cheet-Sheet-1.png)

# Object Relational Mapper (ORM):

![](https://miro.medium.com/max/700/0*CzE1_rn0FyFjRJW4.jpg)

* Object–relational mapping (ORM, O/RM, and O/R mapping tool) in computer science is a programming technique for converting data between incompatible type systems using object-oriented programming languages .
* This creates, in effect, a "virtual object database" that can be used from within the programming language
* What is an object relational mapper in Python?
* An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.

* Advantage: A lot faster.
* Disadvantage: when you want to filter some data, you have to look to all related data, or duplicate data.

![](https://miro.medium.com/max/1400/0*UkOqM_a_agYwUOoV)