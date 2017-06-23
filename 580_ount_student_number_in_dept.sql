# Write your MySQL query statement below
select department.dept_name as dept_name, count(distinct student.student_id) as student_number
from student
right join department
on student.dept_id = department.dept_id
group by department.dept_id
order by count(distinct student.student_id) desc, department.dept_name asc
