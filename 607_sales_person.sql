# Write your MySQL query statement below
select name from salesperson
where sales_id not in
(select distinct orders.sales_id as sales_id
from orders
Join company
on orders.com_id = company.com_id
where company.name = 'RED')
