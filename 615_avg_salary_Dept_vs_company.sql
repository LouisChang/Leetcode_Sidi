# Write your MySQL query statement below
select A.pay_month as pay_month, A.department_id as department_id, 
(case when A.pay > B.pay then 'higher'
when A.pay < B.pay then 'lower'
else 'same' end
) as comparison
from 
(select LEFT(s.pay_date,7) as pay_month, e.department_id as department_id, AVG(s.amount) as pay
from salary s
join employee e
on s.employee_id = e.employee_id
group by e.department_id, LEFT(s.pay_date,7)) A
Join
(select AVG(amount) as pay,LEFT(pay_date,7) as pay_month from salary group by LEFT(pay_date,7)
) B
on A.pay_month = B.pay_month


