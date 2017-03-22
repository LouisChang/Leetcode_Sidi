# Write your MySQL query statement below
Select Customers.Name AS Customers
From Customers
LEFT JOIN Orders
On Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId is null

# Need left join because if the customer never orders, he will not be in the order list
#test
