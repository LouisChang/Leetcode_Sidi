# Write your MySQL query statement below
Select Score, (Select count(distinct Score) From Scores WHERE Score >= s.Score) As Rank
From Scores s
Order By Score desc
