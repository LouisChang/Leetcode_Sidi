# Write your MySQL query statement below
select a.Name
from Employee a
left join Employee b
on a.Id = b.ManagerId
group by a.Id
having count(*) >= 5
