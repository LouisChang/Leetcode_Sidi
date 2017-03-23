# Write your MySQL query statement below
Select E1.Name AS Employee
FROM Employee E1
JOIN Employee E2
ON E1.ManagerId = E2.Id
Where E1.Salary > E2.Salary
