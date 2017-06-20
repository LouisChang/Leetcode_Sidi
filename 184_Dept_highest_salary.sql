# Write your MySQL query statement below
/*
select b.Name as Department, a.Name as Employee, a.Salary as Salary 
from Employee a
join Department b
on a.DepartmentId = b.Id
where a.Salary >= ALL(select Salary from Employee c where a.DepartmentId = c.DepartmentId)


select Department.Name as Department, Employee.name, MAX(Employee.Salary) as Salary
from Employee
join Department 
on Employee.DepartmentId = Department.Id
group by Employee.DepartmentId



select Department.Name as Department, Employee.name, MAX(Employee.Salary) as Salary
from Employee
join Department 
on Employee.DepartmentId = Department.Id
group by Department.Name, Employee.name
*/
select Department, e.name as Employee, e.salary from employee e inner join 
 (
select Employee.DepartmentId, Department.Name as Department, MAX(Employee.Salary) as Salary
from Employee
join Department 
on Employee.DepartmentId = Department.Id
group by Employee.DepartmentId
) as a on e.salary = a.salary and a.DepartmentId = e.DepartmentId



/*
SELECT D.Name AS Department, E.Name AS Employee, E.Salary 
From Employee E, Department D 
Where E.DepartmentId = D.Id 
And (DepartmentId, Salary) in 
    (SELECT DepartmentId, max(salary) as max from Employee Group by departmentId)
*/
