CREATE DATABASE DataDigger;
USE DataDigger;

-- 2 Customers Table --

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Address VARCHAR(255)
);

INSERT INTO Customers (Name, Email, Address) VALUES
('Alice', 'alice@gmail.com', 'Delhi'),
('Bob', 'bob@gmail.com', 'Mumbai'),
('Charlie', 'charlie@gmail.com', 'Pune'),
('David', 'david@gmail.com', 'Bangalore'),
('Eva', 'eva@gmail.com', 'Chennai');


----sql----

-- -- Retrieve all customers
-- SELECT * FROM Customers;

-- -- Update customer address
-- UPDATE Customers SET Address = 'Noida' WHERE CustomerID = 1;

-- -- Delete a customer
-- DELETE FROM Customers WHERE CustomerID = 5;

-- -- Display customers named 'Alice'
-- SELECT * FROM Customers WHERE Name = 'Alice';

-- 3 Orders Table --

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES
(1, '2025-01-01', 2500),
(2, '2025-01-05', 1500),
(3, '2025-01-10', 3200),
(1, '2025-01-15', 1800),
(4, '2025-01-20', 4000);


----sql----

-- -- Orders by specific customer
-- SELECT * FROM Orders WHERE CustomerID = 1;

-- -- Update order total amount
-- UPDATE Orders SET TotalAmount = 2000 WHERE OrderID = 2;

-- -- Delete order by OrderID
-- DELETE FROM Orders WHERE OrderID = 3;

-- -- Orders in last 30 days
-- SELECT * FROM Orders
-- WHERE OrderDate >= CURDATE() - INTERVAL 30 DAY;

-- -- Highest, Lowest, Average order amount
-- SELECT 
--     MAX(TotalAmount) AS Highest,
--     MIN(TotalAmount) AS Lowest,
--     AVG(TotalAmount) AS Average
-- FROM Orders;

-- 4 Create Table --
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(100),
    Price DECIMAL(10,2),
    Stock INT
);

INSERT INTO Products (ProductName, Price, Stock) VALUES
('Laptop', 60000, 10),
('Mobile', 20000, 15),
('Headphones', 1500, 0),
('Keyboard', 800, 20),
('Monitor', 12000, 5);


----sql----

-- -- Products sorted by price (DESC)
-- SELECT * FROM Products ORDER BY Price DESC;

-- -- Update product price
-- UPDATE Products SET Price = 18000 WHERE ProductID = 2;

-- -- Delete product if out of stock
-- DELETE FROM Products WHERE Stock = 0;

-- -- Products between ₹500 and ₹2000
-- SELECT * FROM Products WHERE Price BETWEEN 500 AND 2000;

-- -- Most expensive & cheapest product
-- SELECT 
--     MAX(Price) AS MostExpensive,
--     MIN(Price) AS Cheapest
-- FROM Products;

-- 5 Order Details Table

CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    SubTotal DECIMAL(10,2),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO OrderDetails (OrderID, ProductID, Quantity, SubTotal) VALUES
(1, 1, 1, 60000),
(1, 4, 2, 1600),
(2, 2, 1, 20000),
(4, 5, 1, 12000),
(5, 1, 1, 60000);


----sql----

-- -- Order details for a specific order
-- SELECT * FROM OrderDetails WHERE OrderID = 1;

-- -- Total revenue from all orders
-- SELECT SUM(SubTotal) AS TotalRevenue FROM OrderDetails;

-- -- Top 3 most ordered products
-- SELECT ProductID, SUM(Quantity) AS TotalSold
-- FROM OrderDetails
-- GROUP BY ProductID
-- ORDER BY TotalSold DESC
-- LIMIT 3;

-- -- Count how many times a product sold
-- SELECT COUNT(*) AS TimesSold
-- FROM OrderDetails
-- WHERE ProductID = 1;
