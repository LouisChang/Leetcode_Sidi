# Write your MySQL query statement below
delete b from Person a join Person b
on a.Email = b.Email
where a.Id < b.Id
