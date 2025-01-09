-- Scenario -  Suppose that a website contains two tables, the Customers table and the Orders table.
--Write a SQL query to find all customers who never order anything
--Approach 1 - Left Join
select * from Customers
left Join Orders on Customer.Id = Orders.Customers_Id
where Orders.Id is null

--Approach 2 - Not In
Select c.Name from Customers c
where c.Id NOT In(
select o.Customer_Id from orders 0
)

--Approach 3 - Not Exists
Select c.Name from Customers c
where NOT EXISTS(
select o.CustomerId from Orders o where o.CustomerId = c.Id
)
