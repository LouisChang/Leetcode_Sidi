# Write your MySQL query statement below
select name
from customer
where referee_id <> (select id from customer where name = 'Jane') or referee_id is NULL
