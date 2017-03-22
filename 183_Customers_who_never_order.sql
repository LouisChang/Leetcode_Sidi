# Write your MySQL query statement below
Select Customers.Name AS Customers
From Customers
LEFT JOIN Orders
On Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId is null
