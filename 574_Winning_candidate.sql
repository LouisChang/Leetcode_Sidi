# Write your MySQL query statement below
select distinct Candidate.Name
from Candidate
Join Vote
on Candidate.id = Vote.CandidateId
where Candidate.id = 
(select CandidateId
from Vote
group by CandidateId
order by count(*) desc limit 1)
