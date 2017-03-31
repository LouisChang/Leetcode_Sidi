# Write your MySQL query statement below
#optimal solution
#select (select distinct Salary from Employee order by Salary Desc limit 1 offset 1) AS SecondHighestSalary

SELECT max(Salary) as SecondHighestSalary
From Employee
Where Salary < (select MAX(Salary) from Employee)
