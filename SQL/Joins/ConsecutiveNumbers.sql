--Scenario -  Write a SQL query to find all numbers that appear at least three times consecutively
--Solution
select distinct l1.Num as ConsecutiveNumbers from Logs l1
Join Logs l2 on l1.Id = l2.Id-1
Join Logs l3 on l2.Id = l3.Id-1
where l1.Num = l2.Num and l2.Num = l3.Num