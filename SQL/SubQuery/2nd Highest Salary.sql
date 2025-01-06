--Scenario
--Write a SQL query to get the second highest salary from the Employee table.
--For example, given the above Employee table, the query should return 200 as the
--second highest salary. If there is no second highest salary, then the query
--should return null.

-- MySQL Function
select ifnull((
    select distinct Salary from employee
    order by Salary desc limit 1 offset 1),
    null) as Second Highest Salary

-- Window Functions
select salary as highestSalary from(
select salary, row_number() over (order by salary desc) as rank
from employee
) as ranked_salaries
where rank = 2