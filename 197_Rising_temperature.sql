# Write your MySQL query statement below
select W1.Id
From
Weather W1
JOIN Weather W2
On TO_DAYS(W1.Date)  = TO_DAYS(W2.Date) + 1
Where W1.Temperature > W2.Temperature
