# Write your MySQL query statement below
select Person.FirstName, Person.LastName, Address.City, Address.State
From Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId
