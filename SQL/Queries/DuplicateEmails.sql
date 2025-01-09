-- Scenario - SQL query to find all duplicate emails in a table named Person
-- Solution
select count(*),Email from Person group by Email having count(*) > 1
