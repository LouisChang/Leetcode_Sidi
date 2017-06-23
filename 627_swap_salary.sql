# Write your MySQL query statement below
/*
select id, name, case when sex = 'm' then 'f' else 'm' end as sex, salary
#select case when sex = 'm' then 'f' else 'm' end as temp
from salary
*/
update salary set sex = (case when sex = 'f' then 'm' else 'f' end)
