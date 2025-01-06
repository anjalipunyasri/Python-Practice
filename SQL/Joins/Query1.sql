--Question
--Write a SQL query for a report that provides the following information for each
--person in the Person table, regardless if there is an address for each of those
--people:
--FirstName, LastName, City, State

--Tables Info
select PersonId, FirstName, LastName from person
select AddressId, PersonId, City, State from address

--Solution
select FirstName,LastName, City, State from person as p left join address as a on p.PersonId = a.PersonId
