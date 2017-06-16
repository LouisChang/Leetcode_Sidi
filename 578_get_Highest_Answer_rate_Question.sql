# Write your MySQL query statement below
# Case evaluation
select temp.question_id as survey_log
from (select a.question_id,SUM(case when a.action = 'show' then 1 else 0 end) as col1,SUM(case when a.action = 'answer' then 1 else 0 end) as col2 from survey_log a group by a.question_id) temp
order by temp.col2/temp.col1 desc limit 1
