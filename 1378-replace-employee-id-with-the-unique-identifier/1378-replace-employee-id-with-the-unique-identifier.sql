# Write your MySQL query statement below
-- SELECT Employees.name, EmployeeUNI.unique_id
-- FROM Employees
-- INNER JOIN EmployeeUNI ON Employees.id = EmployeeUNI.unique_id


SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id;