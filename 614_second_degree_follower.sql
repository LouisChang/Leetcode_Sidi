# Write your MySQL query statement below
select distinct b.follower as follower, count(distinct a.follower) as num
from follow a
inner join follow b
on a.followee = b.follower
group by a.followee
#order by a.followee
