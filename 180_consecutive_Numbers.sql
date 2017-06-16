# Write your MySQL query statement below
select distinct a.Num as ConsecutiveNums
from Logs a join Logs b join Logs c
on a.Id + 1 = b.Id and b.Id + 1 = c.Id
where a.Num = b.Num and b.Num = c.Num
