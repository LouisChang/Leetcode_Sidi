# Write your MySQL query statement below
select Employee.name As name, Bonus.bonus As bonus
From
Employee
LEFT JOIN
Bonus
ON Employee.empId = Bonus.empId
Where
Bonus.bonus < 1000 or Bonus.bonus is null
