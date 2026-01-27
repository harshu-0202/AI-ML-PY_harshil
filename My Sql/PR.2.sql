-- Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    RegistrationDate DATE
);

-- Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Employees Table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    HireDate DATE,
    Salary DECIMAL(10,2)
);


-- Customers
INSERT INTO Customers VALUES
(1, 'John', 'Doe', '  john.doe@email.com  ', '2022-03-15'),
(2, 'Jane', 'Smith', 'jane.smith@email.com', '2021-11-02');

-- Orders
INSERT INTO Orders VALUES
(101, 1, '2023-07-01', 150.50),
(102, 2, '2023-07-03', 200.75);

-- Employees
INSERT INTO Employees VALUES
(1, 'Mark', 'Johnson', 'Sales', '2020-01-15', 50000),
(2, 'Susan', 'Lee', 'HR', '2021-03-20', 55000);


-- 1. INNER JOIN – orders with customer details

SELECT o.OrderID, c.FirstName, c.LastName, o.TotalAmount
FROM Orders o
INNER JOIN Customers c ON o.CustomerID = c.CustomerID;

-- 2. LEFT JOIN – all customers and orders (if any)

SELECT c.FirstName, c.LastName, o.OrderID
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID;

-- 3. RIGHT JOIN – all orders and customers (if any)

SELECT c.FirstName, c.LastName, o.OrderID
FROM Customers c
RIGHT JOIN Orders o ON c.CustomerID = o.CustomerID;

-- 4. FULL OUTER JOIN (MySQL workaround)

SELECT c.FirstName, c.LastName, o.OrderID
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
UNION
SELECT c.FirstName, c.LastName, o.OrderID
FROM Customers c
RIGHT JOIN Orders o ON c.CustomerID = o.CustomerID;

-- 5. Customers with orders above average amount

SELECT DISTINCT CustomerID
FROM Orders
WHERE TotalAmount > (SELECT AVG(TotalAmount) FROM Orders);

-- 6. Employees with salary above average

SELECT *
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);

-- 7. Extract year & month from OrderDate

SELECT OrderID,
       YEAR(OrderDate) AS OrderYear,
       MONTH(OrderDate) AS OrderMonth
FROM Orders;

-- 8. Difference in days (OrderDate vs current date)

SELECT OrderID,
       DATEDIFF(CURRENT_DATE, OrderDate) AS DaysDifference
FROM Orders;

-- 9. Format OrderDate (DD-MMM-YYYY)

SELECT OrderID,
       DATE_FORMAT(OrderDate, '%d-%b-%Y') AS FormattedDate
FROM Orders;

-- 10. Concatenate FirstName & LastName

SELECT CONCAT(FirstName, ' ', LastName) AS FullName
FROM Customers;

-- 11. Replace 'John' with 'Jonathan'

SELECT REPLACE(FirstName, 'John', 'Jonathan') AS UpdatedName
FROM Customers;

-- 12. Uppercase FirstName & lowercase LastName

SELECT UPPER(FirstName) AS FirstName_Upper,
       LOWER(LastName) AS LastName_Lower
FROM Customers;

-- 13. Trim extra spaces from Email

SELECT TRIM(Email) AS CleanEmail
FROM Customers;

-- 14. Running total of TotalAmount

SELECT OrderID,
       TotalAmount,
       SUM(TotalAmount) OVER (ORDER BY OrderDate) AS RunningTotal
FROM Orders;

-- 15. Rank orders by TotalAmount

SELECT OrderID,
       TotalAmount,
       RANK() OVER (ORDER BY TotalAmount DESC) AS AmountRank
FROM Orders;

-- 16. Assign discount using CASE

SELECT OrderID,
       TotalAmount,
       CASE
           WHEN TotalAmount > 1000 THEN '10% Discount'
           WHEN TotalAmount > 500 THEN '5% Discount'
           ELSE 'No Discount'
       END AS Discount
FROM Orders;

-- 17. Categorize employee salaries

SELECT EmployeeID,
       Salary,
       CASE
           WHEN Salary >= 60000 THEN 'High'
           WHEN Salary BETWEEN 50000 AND 59999 THEN 'Medium'
           ELSE 'Low'
       END AS SalaryCategory
FROM Employees;

 