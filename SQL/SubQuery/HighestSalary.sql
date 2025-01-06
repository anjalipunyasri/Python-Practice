-- Row Number
select salary as HighestSalary from(
select salary,row_number over(order by salary desc) as rank
from employee
) as ranked_salaries
where rank = 1

-- Rank
select salary as HighestSalary from(
select salary, rank over(order by salary desc) as rank
from employee
) as ranked_salaries
where rank = 1

-- Dense Rank
select salary as HighestSalary from(
select salary, dense_rank() over(order by salary desc) as rank
from employee
) as ranked_salaries
where rank = 1