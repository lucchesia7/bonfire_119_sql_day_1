-- SELECT keyword is how we access information from a SQL table
-- * returns all columns and rows from the specified tables
SELECT * 
FROM customer;

-- SELECT can be used to grab certain columns as well
SELECT upc 
FROM inventory;

-- SELECT to gather information from multiple tables

SELECT * 
FROM inventory, customer;

-- WHERE clause
SELECT *
FROM customer
WHERE customer.customer_id = 1;

-- We can aggregate functions in our select statements
SELECT COUNT(first_name)
FROM customer;

SELECT SUM(total_cost)
FROM orders;

-- We can also do groupby statements
SELECT first_name, last_name
FROM customer
GROUP BY first_name
LIMIT 1