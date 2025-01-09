-- Scenario - SQL query that finds out employees who earn more than their managers.
-- Solution
select e.Name as Employee from Employee e
join Employee m on e.ManagerId = m.Id where e.Salary > m.Salary